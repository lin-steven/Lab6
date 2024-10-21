# Lab 6 Project

def encode(password): # By: Steven Lin
    encoded = ""
    for digit in password:
        encoded += str((int(digit) + 3) % 10)
    return encoded

def decode(code): #By: Daniel Pool
	decoded = ""
	for i in code:
		decoded += str((int(i) - 3) % 10)
	return decoded

if __name__ == '__main__':  # Main method made by Steven Lin
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        option = int(input("Please enter an option:"))
        if option == 1:
            password = input("Please enter your password to encode:")
            encoded_pass = encode(password)
            print("Your password has been encoded and stored!")
        if option == 2:
            print(f"The encoded password is {encoded_pass}, and the original password is {decode(encoded_pass)}.")
        if option == 3:
            break
