import random
import math


# =====================================
# PRIME NUMBER FUNCTIONS
# =====================================

def is_prime(number):
    """
    Checks whether a number is prime.
    Returns True if prime, otherwise False.
    """
    if number < 2:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True


def generate_prime():
    """
    Generates a random prime number.
    """
    while True:
        number = random.randint(10000, 50000)

        if is_prime(number):
            return number


# =====================================
# MATHEMATICAL FUNCTIONS
# =====================================

def gcd(a, b):
    """
    Finds the Greatest Common Divisor.
    """
    while b != 0:
        a, b = b, a % b

    return a


def extended_gcd(a, b):
    """
    Extended Euclidean Algorithm.
    Used for finding modular inverse.
    """
    if a == 0:
        return b, 0, 1

    gcd_value, x1, y1 = extended_gcd(b % a, a)

    x = y1 - (b // a) * x1
    y = x1

    return gcd_value, x, y


def mod_inverse(e, phi):
    """
    Calculates d such that:
    (d × e) mod phi = 1
    """
    gcd_value, x, y = extended_gcd(e, phi)

    if gcd_value != 1:
        raise Exception("Modular inverse does not exist.")

    return x % phi


# =====================================
# RSA KEY GENERATION
# =====================================

def generate_keys():
    """
    Generates RSA public and private keys.
    """

    p = generate_prime()

    q = generate_prime()

    while p == q:
        q = generate_prime()

    n = p * q

    phi = (p - 1) * (q - 1)

    # Standard RSA public exponent
    e = 65537

    # Rare fallback if gcd != 1
    if gcd(e, phi) != 1:

        while True:
            e = random.randint(2, phi - 1)

            if gcd(e, phi) == 1:
                break

    d = mod_inverse(e, phi)

    return p, q, n, phi, e, d


# =====================================
# RSA ENCRYPTION
# =====================================

def encrypt(message, e, n):
    """
    Encrypts a plaintext message.
    """

    encrypted_message = []

    for character in message:
        encrypted_value = pow(ord(character), e, n)
        encrypted_message.append(encrypted_value)

    return encrypted_message


# =====================================
# RSA DECRYPTION
# =====================================

def decrypt(ciphertext, d, n):
    """
    Decrypts an encrypted message.
    """

    decrypted_message = ""

    for value in ciphertext:
        character = chr(pow(value, d, n))
        decrypted_message += character

    return decrypted_message


# =====================================
# DISPLAY FUNCTIONS
# =====================================

def display_keys(e, d, n):
    """
    Displays public and private keys.
    """

    print("\n" + "=" * 50)
    print("RSA KEYS")
    print("=" * 50)

    print("\nPUBLIC KEY")
    print(f"e = {e}")
    print(f"n = {n}")

    print("\nPRIVATE KEY")
    print(f"d = {d}")
    print(f"n = {n}")

    print("=" * 50)


def display_parameters(p, q, phi):
    """
    Displays RSA parameters.
    """

    print("\nRSA PARAMETERS")
    print("-" * 50)
    print(f"Prime p = {p}")
    print(f"Prime q = {q}")
    print(f"Phi(n)  = {phi}")
    print("-" * 50)


# =====================================
# MENU
# =====================================

def menu():
    print("\n")
    print("=" * 50)
    print("RSA ALGORITHM MENU")
    print("=" * 50)
    print("1. Encrypt Message")
    print("2. Decrypt Last Message")
    print("3. Display Keys")
    print("4. Generate New Keys")
    print("5. Exit")
    print("=" * 50)


# =====================================
# MAIN PROGRAM
# =====================================

def main():

    print("=" * 60)
    print("      RSA CRYPTOGRAPHY SYSTEM")
    print("      Developed in Python")
    print("=" * 60)

    p, q, n, phi, e, d = generate_keys()

    print("\nRSA Keys Generated Successfully!")

    display_parameters(p, q, phi)

    last_ciphertext = None

    while True:

        menu()

        choice = input("Enter your choice (1-5): ").strip()

        # -------------------------
        # OPTION 1
        # -------------------------
        if choice == "1":

            message = input("\nEnter message to encrypt: ").strip()

            if not message:
                print("Message cannot be empty.")
                continue

            last_ciphertext = encrypt(message, e, n)

            print("\nEncrypted Message:")
            print(last_ciphertext)

        # -------------------------
        # OPTION 2
        # -------------------------
        elif choice == "2":

            if last_ciphertext is None:
                print("\nNo encrypted message available.")
                continue

            decrypted_message = decrypt(
                last_ciphertext,
                d,
                n
            )

            print("\nDecrypted Message:")
            print(decrypted_message)

        # -------------------------
        # OPTION 3
        # -------------------------
        elif choice == "3":

            display_keys(e, d, n)

        # -------------------------
        # OPTION 4
        # -------------------------
        elif choice == "4":

            print("\nGenerating new RSA keys...\n")

            p, q, n, phi, e, d = generate_keys()

            display_parameters(p, q, phi)

            last_ciphertext = None

            print("New keys generated successfully!")

        # -------------------------
        # OPTION 5
        # -------------------------
        elif choice == "5":

            print("\nThank you for using the RSA Cryptography System.")
            print("Program terminated successfully.")

            break

        # -------------------------
        # INVALID CHOICE
        # -------------------------
        else:

            print("\nInvalid choice.")
            print("Please enter a number from 1 to 5.")


# =====================================
# PROGRAM ENTRY POINT
# =====================================

if __name__ == "__main__":
    main()