from cracker import crack
from cypher import decrypt, encrypt
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    while True:
        print(f"""
1. Encrypt
2. Decrypt
3. Crack
0. Exit
        """)

        try:
            choice = int(input("> "))
            if choice == 1:
                message = input("Enter message: ")
                shift = int(input("Position shift: "))

                clear_screen()
                results = encrypt(message, shift)
                print(f"\nEncrypted: \033[32m{results}\033[0m\nShifted: \033[32m{shift % 26}\033[0m")

            elif choice == 2:
                message = input("Enter message: ")
                shift = int(input("Position shift: "))
                
                clear_screen()
                results = decrypt(message, shift)
                print(f"\nDecrypted: \033[32m{results}\033[0m")

            elif choice == 3:
                message = input("Enter message: ")

                clear_screen()
                results = crack(message)

                print("\nCAESAR CIPHER CRACK RESULTS\n")

                for shift, decrypted in results:
                    print(f"Shift {shift:2}: {decrypted}")

            elif choice == 0:
                break

            else:
                print("Invalid option.")
                continue

        except ValueError:
            print("")

if __name__ == "__main__":
    main()
