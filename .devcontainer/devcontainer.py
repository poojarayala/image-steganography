def main():
    a = int(input(":: Welcome to Steganography ::\n1. Encode\n2. Decode\n"))
    if (a == 1):
        encode()
    elif (a == 2):
        decoded_data = decode()
        print("Decoded Word : " + decoded_data)
    else:
        raise Exception("Enter correct input")

if __name__ == '__main__':
    main()
