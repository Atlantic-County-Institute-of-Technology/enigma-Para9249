# enigma.py
# description: a simple rotational ciphertext program that can create1
# custom encoded messages, as well as encode and decode from file.
# author: Christopher Parada
# created: 11/18/2024
# last update:  11/18/24

import random

alphabet = "abcdefghijklmnopqrstuvwxyz"

# user inputs a message and selects a key, the message is then translated 
def encode_message():
    message = (input("Please input the message you would like to decode"))
    key = int(input("Please input the key"))
    if key == "":
        key = random.randint(0,26)
    print(key)
    for x in range(len(message)):
        ordmessage = ord(message[x])
        ordmessage = ordmessage + key
        print(chr(ordmessage))
    # encodes a  file, similarly to encode_message, except now targeting a filename
def encode_file():
    pass

# decodes file using a user-specified key. If key is unknown, a keypress should  call decode_unknown_key()
def decode_file():
    pass

# runs if the key is unknown. Prints out all possible combinations.
def decode_unknown_key(filename):
   pass


# main method declaration
def main():
    while True:
        print(f"welcome to the machine that encodes stuff\n"
              f"Please select an option:\n"
              f"[1]: Encode a custom message.\n"
              f"[2]: Encode a file.\n"
              f"[3]: Decode a file.\n"
              f"[4]: Exit.")

        selection = input("Choose an option:")

        if selection == "1":
            encode_message()
        elif selection == "2":
            encode_file()
        elif selection == "3":
            decode_file()
        elif selection == "4":
            print("Goodbye.")
            exit()
        else:
            print("Invalid choice. Please try again.")

# runs on program start
if __name__ == "__main__":
    main()