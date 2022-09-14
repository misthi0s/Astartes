def decode(encoded, seed, type):
    decoded_value = []
    with open("{}.list".format(seed), "r") as seedlist_f:
        bytes_encoded = seedlist_f.read().splitlines()
    for value in encoded:
        decoded_value.append((bytes_encoded.index(value).to_bytes(1, 'big')))
    if type == "string":
        print("decoded string value: {}".format((b''.join(decoded_value).decode("utf-8"))))
    elif type == "file":
        with open("file_decoded.gif", "wb") as output_f:
            output_f.write(b''.join(decoded_value))


if __name__ == '__main__':
    seed = "RogalDorn"
    with open("string_encoded.txt", "r") as s_encoded_h:
        string_contents = s_encoded_h.read()
    print("string_encoded.txt contents: {}".format(string_contents))
    s_byte_array = string_contents.split(",")
    decode(s_byte_array, seed, "string")
    with open("file_encoded.txt", "r") as f_encoded_h:
        file_contents = f_encoded_h.read()
    f_byte_array = file_contents.split(",")
    print("\nWriting decoded 'file_encoded.txt' to output 'file_decoded.gif' file!")
    decode(f_byte_array, seed, "file")


