alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encode(plain_text, plain_shift):
    encode_message = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + plain_shift
        new_letter = alphabet[new_position]
        encode_message += new_letter
    return encode_message


def decode(plain_text, plain_shift):
    decode_message = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position - plain_shift
        new_letter = alphabet[new_position]
        decode_message += new_letter
    return decode_message


if direction  == "encode":
    print(f" The encoded message is : {encode(plain_text=text, plain_shift=shift)}")

elif direction == "decode":
    print(f"The decoded message is : {decode(plain_text=text, plain_shift=shift)}")

else:
    print("Try again! ERROR!!")

