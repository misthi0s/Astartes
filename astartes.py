import random
import os
import argparse
import sys


def encode(byte_array, seed):
    encoded_list = []

    try:
        with open(os.path.normpath("wordlists/ASTARTES.txt"), "r") as wordlist_f:
            astartes_list = wordlist_f.read().splitlines()
    except Exception as wordlist_e:
        print("[-] Error reading master wordlist. Please make sure default wordlist exists at 'wordlists/ASTARTES.txt'")
        print("[-] Error message: {}".format(wordlist_e))
        sys.exit(5)

    print("[+] Randomizing wordlist using seed '{}'".format(seed))
    random.seed(seed)
    random.shuffle(astartes_list)
    bytes_astartes = astartes_list[0:256]

    if not os.path.isdir(os.path.normpath("wordlists/seeds")):
        os.makedirs(os.path.normpath("wordlists/seeds"))

    print("[+] Writing seeded wordlist to output file.")
    with open(os.path.normpath("wordlists/seeds/{}.list".format(seed)), "w+") as seedlist:
        seedlist.write('\n'.join(bytes_astartes))

    print("[+] Encoding input with Astartes seeded wordlist.")
    for value in byte_array:
        encoded_list.append(bytes_astartes[value])

    return encoded_list


def main():
    output_list = []
    parser = argparse.ArgumentParser(description="Astartes - byte encoder")
    parser.add_argument("--file", help="File to encode")
    parser.add_argument("--hex", help="Hex string to encode. Use escaped hex notation. Example: '\\x00\\x01\\xab\\xcd'")
    parser.add_argument("--string", help="ASCII string to encode")
    parser.add_argument("--seed", help="Seed to use to randomize encoder (default: ForTheEmperor!)", default="ForTheEmperor!")
    parser.add_argument("--output", help="Output file to write encoded payload to (default: astartes_encoded.txt)", default="astartes_encoded.txt")
    args = parser.parse_args()

    arguments_passed = 0
    if args.file:
        arguments_passed += 1
    if args.hex:
        arguments_passed += 1
    if args.string:
        arguments_passed += 1

    if arguments_passed > 1:
        print("[-] More than one encoding argument specified! Please only specify one (--file, --hex, or --string).")
        sys.exit(1)
    elif arguments_passed < 1:
        print("[-] No encoding argument specified! Please specify one input (--file, --hex, or --string).")
        sys.exit(1)

    if args.file:
        print("[+] File chosen as input. Encoding file contents with Astartes.")
        if not os.path.exists(args.file):
            print("[-] File specified does not exist! Please enter valid path to a file to encode.")
            sys.exit(2)
        try:
            with open(args.file, "rb") as encode_f:
                bytes_f = encode_f.read()
        except Exception as file_e:
            print("[-] Error opening file. Error message encountered: {}".format(file_e))
            sys.exit(3)
        output_list = encode(bytes_f, args.seed)

    if args.string:
        print("[+] String chosen as input. Encoding string with Astartes.")
        bytes_s = args.string.encode()
        output_list = encode(bytes_s, args.seed)

    if args.hex:
        print("[+] Hex chosen as input. Encoding string with Astartes.")
        try:
            unescaped_hex = args.hex.replace("\\x", "")
            bytes_s = bytes.fromhex(unescaped_hex)
        except Exception as hex_e:
            print("[-] Error converting hex to bytes. Please make sure hex is properly formatted.")
            print("[-] Error message: {}".format(hex_e))
            sys.exit(3)
        output_list = encode(bytes_s, args.seed)

    try:
        with open(args.output, "w+") as output_f:
            output_f.write(','.join(output_list))
    except Exception as output_e:
        print("[-] Error writing output to file. Please verify write permissions are correct.")
        print("[-] Error message: {}".format(output_e))
        sys.exit(4)
    print("[+] Encoded payload written to {} successfully.".format(args.output))


if __name__ == '__main__':
    header = """
  ___      _             _            
 / _ \    | |           | |           
/ /_\ \___| |_ __ _ _ __| |_ ___  ___ 
|  _  / __| __/ _` | '__| __/ _ \/ __|
| | | \__ \ || (_| | |  | ||  __/\__ \\
\_| |_/___/\__\__,_|_|   \__\___||___/    

"""
    print(header)
    main()
