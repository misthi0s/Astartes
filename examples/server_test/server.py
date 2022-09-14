import os
import random
from flask import Flask, request

app = Flask(__name__)


def calculate_encoder(seed):
    with open(os.path.normpath("../../wordlists/ASTARTES.txt"), "r") as wordlist_f:
        astartes_list = wordlist_f.read().splitlines()

        random.seed(seed)
        random.shuffle(astartes_list)
        bytes_astartes = astartes_list[0:256]
        return bytes_astartes


@app.route('/')
def main():
    if request.headers.get('Authorization'):
        seed = request.headers.get('Authorization')
        encoder = calculate_encoder(seed)
        return encoder
    elif request.args.get('_'):
        seed = request.args.get('_')
        encoder = calculate_encoder(seed)
        return encoder
    else:
        return ''


app.run(debug=False)
