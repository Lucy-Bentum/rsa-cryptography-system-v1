# RSA Cryptography System in Python

## Overview

This project is a Python implementation of the RSA (Rivest–Shamir–Adleman) public-key cryptography algorithm. It demonstrates the fundamental concepts of asymmetric encryption by generating RSA key pairs, encrypting plaintext messages, and decrypting ciphertext using the corresponding private key.

The project was developed as part of an Information and Cybersecurity course to provide a practical understanding of how RSA works.

---

## Features

* Generate two random prime numbers
* Generate RSA public and private keys
* Encrypt plaintext messages
* Decrypt encrypted messages
* Display generated RSA keys
* Generate a new RSA key pair
* Menu-driven interface
* Input validation and error handling

---

## Technologies Used

* Python 3
* Built-in Python modules:

  * `random`
  * `math`

No external libraries are required.

---

## Project Structure

```text
RSA_Project/
│
├── rsa.py          # Main Python program
├── README.md       # Project documentation
└── .gitignore      # Git ignore file (optional)
```

---

## How the Program Works

1. The program generates two random prime numbers (**p** and **q**).
2. It computes:

   * **n = p × q**
   * **φ(n) = (p − 1)(q − 1)**
3. The public exponent (**e**) is selected.
4. The private exponent (**d**) is calculated using the Extended Euclidean Algorithm.
5. The program generates:

   * Public Key: **(e, n)**
   * Private Key: **(d, n)**
6. Users can encrypt and decrypt messages through a simple menu-driven interface.

---

## Running the Project

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/rsa-cryptography-system.git
```

Navigate into the project directory:

```bash
cd rsa-cryptography-system
```

Run the program:

```bash
python rsa.py
```

---

## Example

```text
========== RSA CRYPTOGRAPHY SYSTEM ==========

1. Encrypt Message
2. Decrypt Last Message
3. Display Keys
4. Generate New Keys
5. Exit

Enter your choice:
```

---

## Learning Objectives

This project demonstrates:

* Prime number generation
* Greatest Common Divisor (GCD)
* Euler's Totient Function
* Modular arithmetic
* Public-key cryptography
* RSA key generation
* Encryption and decryption processes

---

## Author

**Lucy Bentum**

Computer Science and Engineering

University of Mines and Technology (UMaT)

---

## License

This project is intended for educational and academic purposes.
