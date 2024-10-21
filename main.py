# Lab 6 Project

def decode(code): #By: Daniel Pool
	decoded = ""
	for i in code:
		decoded += str((int(i) - 3) % 10)
	return decoded

print("This is Lab 6.")
