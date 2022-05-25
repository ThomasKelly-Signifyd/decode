import base64
from os import system
import subprocess
import json


def decode(encoded_string):
    return base64.b64decode(encoded_string)


def copy_to_clipboard(output):
    process = subprocess.Popen(
        "pbcopy", env={"LANG": "en_US.UTF-8"}, stdin=subprocess.PIPE
    )
    process.communicate(output)


def decode_string(input):
        if input == "q":
            print("Exiting...")
            exit()

        return(decode(input))


def decode_json(input):
    if input == "q":
        print("Exiting...")
        exit()

    input = decode(input)

    parsed = json.loads(input)
    return json.dumps(parsed, indent=4, sort_keys=True).encode()


def get_data_field_from_sqs_json(input):
    parsed = json.loads(input)

    return parsed['data']


def main():
    execution_type = input("Pick one of these 3 options:\n1. Decode String\n2. Decode JSON\n3. Decode SQS Message\n----------\n")

    while True:
        output_string = ""

        if execution_type == "1":
            input_string = input("Paste base64 encoded string here and hit Enter:\n")
            output_string = decode_string(input_string)  
        elif execution_type == "2":
            input_string = input("Paste base64 encoded JSON here and hit Enter:\n")
            output_string = decode_json(input_string)
        elif execution_type == "3":
            input_string = input("Paste AWS SQS Message here and hit Enter:\n")
            output_string = decode_json(get_data_field_from_sqs_json(input_string))
        else:
            SystemExit()

        print(f"{'-'*20}-----\nDecoded Data:\n")
        print(output_string.decode("utf-8"))

        copy_to_clipboard(output_string)

        print(f"\nDecoded Data copied to Clipboard\n{'-'*20}")


if __name__ == "__main__":
    main()
