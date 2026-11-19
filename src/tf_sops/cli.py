#!/usr/bin/python
import argparse
import base64
import json
import subprocess
import sys

SOPS_ENC_CMD = ["sops", "encrypt", "--input-type", "binary", "--output-type", "binary", "--filename-override", "tofu.tfstate"]
SOPS_DEC_CMD = ["sops", "decrypt", "--input-type", "binary", "--output-type", "binary", "--filename-override", "tofu.tfstate"]

def app():
    parser = argparse.ArgumentParser(prog='My External Encryption Method')
    parser.add_argument('--encrypt', action='store_true')
    parser.add_argument('--decrypt', action='store_true')
    parser.add_argument('--test', action='store_true')
    args = parser.parse_args()
    # Make sure that this program isn't running interactively:
    if sys.stdout.isatty() and not args.test:
        sys.stderr.write("This is an OpenTofu encryption method and is not meant to be run interactively. "
                         "Please configure this program in your OpenTofu encryption block to use it.\n")
        sys.exit(1)

    # Write the header:
    sys.stdout.write((json.dumps({"magic": "OpenTofu-External-Encryption-Method", "version": 1}) + "\n"))
    sys.stdout.flush()

    # Read the input:
    inputData = sys.stdin.read()
    if not args.test:
        data = json.loads(inputData)
        payload = base64.b64decode(data["payload"])
    else:
        payload = base64.b64decode(inputData)

    # Produce the output payload here.
    if args.encrypt:
        outputPayload = subprocess.run(SOPS_ENC_CMD, input=payload, capture_output=True).stdout
    elif args.decrypt:
        outputPayload = subprocess.run(SOPS_DEC_CMD, input=payload, capture_output=True).stdout
    else:
        raise "Expected --encrypt or --decrypt."

    # Write the output:
    sys.stdout.write(json.dumps({
        "payload": base64.b64encode(outputPayload).decode('ascii'),
    }))
