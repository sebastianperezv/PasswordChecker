# 🔒 Pwned Password Checker (CLI)

This Python script checks if one or more passwords have been **compromised in known data breaches**, using the [Have I Been Pwned API](https://haveibeenpwned.com/API/v3#PwnedPasswords).
It uses **SHA-1 hashing + k-anonymity** to protect your passwords while querying the API.

---

## 🛠️ Features

* Uses the **Pwned Passwords API** securely
* Protects privacy: only the first 5 characters of the hash are sent
* Tells you how many times each password was leaked
* Simple CLI usage – pass multiple passwords as arguments

---

## 📦 Requirements

* Python 3.x
* `requests` library

Install the required package:

```bash
pip install requests
```

---

## 🚀 Usage

Run the script from the command line:

```bash
python pwned_password_checker.py <password1> <password2> ...
```

### Example:

```bash
python pwned_password_checker.py 123456 password qwerty
```

### Output:

```
123456 was found 2389473 times...you should change your password
password was found 3452891 times...you should change your password
qwerty was found 982374 times...you should change your password
```

If a password is not found:

```
myS3cretPass was NOT found. Carry on!
```

---

## 🔐 How It Works

1. The password is hashed using SHA-1.
2. Only the **first 5 characters** of the hash are sent to the API.
3. The API returns a list of matching hashes and breach counts.
4. Your script checks if the **tail of your hash** is in the list.
5. If found, it tells you how many times that password has appeared in breaches.

---

## ⚠️ Disclaimer

This script is for **educational and security-awareness purposes only**.
Avoid running it with real passwords on untrusted systems.

---

## 📄 License

MIT License – [See LICENSE](LICENSE)

---

Let me know if you'd like:

* A `.gitignore` file
* A `requirements.txt`
* Instructions for packaging it as a CLI tool (`setup.py`)
