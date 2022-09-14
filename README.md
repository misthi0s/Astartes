<head>
<h1 align=center>Astartes - Byte Encoder</h1>
</head>

<p align="center">
  <img src="images/astartes.jpg" alt="Astartes"/>
</p>

Astartes is an encoding tool, converting each byte in an input dataset into the name of an Astartes chapter. A seed is used to randomize the list of over 400 Chapters into the appropriate set of 256 values, allowing for a level of unique encoding depending on the input seed.

---

## Features

* Seeded randomization allowing for encoding variation on the same payload
* Supports encoding a string, hex value, or entire file
* Outputs the seeded wordlist for easier usage in decoding
* Unlimited possibility to praise the Emperor
---
## Installation

Clone the repository:<br>
```git clone https://github.com/misthi0s/Astartes```

(Optional) Install Flask for the server_test.py example:<br>
```pip3 install Flask```

Help information can be accessed by running the `-h` switch:<br>
```python3 astartes.py -h```

---
## Usage

Astartes supports the following switches:
<table>
<tr>
<th>Switch</th>
<th>Description</th>
<th>Mandatory?</th>
</tr>
<tr>
<td>--file</td>
<td>Input file to encode</td>
<td>Yes (If no --hex or --string)</td>
</tr>
<tr>
<td>--hex</td>
<td>Input hex to encode; use escaped notation (IE, "\x01\xab")</td>
<td>Yes (If no --file or --string)</td>
</tr>
<tr>
<td>--string</td>
<td>Input string to encode</td>
<td>Yes (If no --hex or --file)</td>
</tr>
<tr>
<td>--seed</td>
<td>Seed to use to randomize Chapter wordlist (Default: ForTheEmperor!)</td>
<td>No</td>
</tr>
<tr>
<td>--output</td>
<td>File to write encoded payload to (default: astartes_encoded.txt)</td>
<td>No</td>
</tr>
</table>

---
## Examples

Encode string value of "Imperium of Man":<br>
```python3 astartes.py --string "Imperium of Man"```

Encode file "heresy.txt" with seed of "Thousand Suns":<br>
```python3 astartes.py --file heresy.txt --seed "Thousand Suns"```

Encode hex value "\x45\x6d\x70\x65\x72\x6f\x72" with seed of "Custodes" and save to file "Terra.txt":<br>
```python3 astartes.py --hex "\x45\x6d\x70\x65\x72\x6f\x72" --seed "Custodes" --output Terra.txt```

---
## Decoding

To decode an Astartes payload, you will need the following items:

1). The encoded payload value (obviously)

2). The seed used during the encoding process **-OR-** the output wordlist generated during the encoding process corresponding to the seed used

---
## Decoding Example

To give an idea how an Astartes payload can be generated, an example has been included in this repository in the `examples/decoder_test` directory.
The files `string_encoded.txt` and `file_encoded.txt` represent the encoded payloads and the `RogalDorn.list` file represents the seeded wordlist used during the encoding process (seed value used was `RogalDorn`).
The `decode.py` file uses these files to decode the Astartes payload and print the result to the screen. The `--string` and `--file` parameters, respectively, were used during the encoding processes.

To see how this works, simply move to the `examples/decoder_test` and run:<br>
>python3 decode.py

The encoded string and the subsequent decoded string should print to the screen followed by the decoded file payload being saved to an output file. To see how this was done, simply review the `decode` function in the script.
This is a simple example of how an encoded payload can be decoded via Python, but this same methodology can be applied to other programming languages as well.

---
## Remote Wordlist Example

This repository also contains an example on how to remotely access the seeded wordlist to decode a payload. This can be useful in cases
where you do not want the encoder map to be within the same payload as the actual encoded value.

This example spins up a Flask-based web server which can be queried with the seed to return the randomized encoder map. **NOTE:** This example
should NOT be exposed to any sort of potentially hostile network, as it is a very basic example simply meant to show one way of 
remotely hosting the wordlist. It should not be considered secure or production-ready AT ALL.

To spin up the web server, move to the `examples/server_test` directory and run:<br>
>python3 server.py

This will spin up a web server hosted locally at `http://127.0.0.1:5000`. This web server supports two methods of querying the wordlist:

* **Query Parameter**: Passing a query parameter of `_=` followed by the seed will return the seeded wordlist in a Python list format.
    * Example: `curl http://127.0.0.1:5000/?_=LemanRuss`
* **Request Header**: Passing an HTTP request header of `Authorization` with the seed as the value will return the seeded wordlist in a Python list format.
    * Example: `curl -H "Authorization: Sanguinius" http://127.0.0.1:5000`

The returned list can then be used as the encoder map to decode the payload in a program.

---
## Additional Notes

* Unless you want to view the decoding / remote wordlist examples, the only directory in this repository required to encode payloads is the `wordlists` one.
This directory contains the master wordlist as well as the directory structure for the seeded wordlists. The main
`astartes.py` file MUST be in the same parent directory as this `wordlists` directory, otherwise the script will break.
* The Astartes Chapters wordlist was derived from the [Warhammer 40k Wiki](https://warhammer40k.fandom.com/wiki/List_of_Space_Marine_Chapters).

---
## Issues

If you run into any issues with Astartes, feel free to open an issue. For the Emperor!