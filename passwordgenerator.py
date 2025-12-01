import random
import string


def generate_password(length, use_letters=True, use_digits=True, use_symbols=True):
    alphabet = ""

    if use_letters:
        alphabet += string.ascii_letters
    if use_digits:
        alphabet += string.digits
    if use_symbols:
        alphabet += string.punctuation

    if not alphabet:
        print("Error: Characters types unselected")
        return

    return "".join(random.choice(alphabet) for _ in range(length))

def main():
    print("!===========================!")
    print("Welcome to Password Generator")
    print("!===========================!")


    print("\nSELECT AN OPTION:")
    print("1) STRONG PASSWORD ")
    print("2) MEDIUM PASSWORD ")
    print("3) WEAK PASSWORD ")
    print("4) I WANT 2 B HACKED ")

    choice = int(input("\nSelect an option(1-4): ").strip())

    if choice == 1:
        password = generate_password(32, use_letters=True, use_digits=True, use_symbols=True)
        print("\n STRONG PASSWORD: ", password)

    elif choice == 2:
        password = generate_password(16, use_letters=True, use_digits=True, use_symbols=True)
        print("\n MEDIUM PASSWORD: ", password)

    elif choice == 3:
        password = generate_password(16, use_letters=True, use_digits=True, use_symbols=False)
        print("\n WEAK PASSWORD: ", password)

    elif choice == 4:
        password = generate_password(8, use_letters=True, use_digits=False, use_symbols=False)
        print("\n I WANT 2 B HACKED PASSWORD: ", password)

    else:
        print("\nI said choose options 1-4 -_-")
        return


if __name__ == "__main__":
    main()



