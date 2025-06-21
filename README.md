# 🔒 Pwned Password Checker (`checkmypass.py`)

This Python script checks if your password(s) have appeared in known data breaches, using the [Have I Been Pwned](https://haveibeenpwned.com/) API.
It follows the **k-anonymity** model, sending only part of your hashed password to keep your data secure.

---

## 🛠️ Features

* Queries the Pwned Passwords API using SHA-1 and k-anonymity
* Checks multiple passwords via command line
* Reports how many times each password was leaked
* Privacy-respecting: your full password or full hash is **never sent**

---

## 📦 Requirements

* Python 3.x
* `requests` library

Install the dependency:

```bash
pip install requests
```

---

## 🚀 Usage

Run the script from the command line:

```bash
python checkmypass.py <password1> <password2> ...
```

### Example:

```bash
python checkmypass.py 123456 password myS3cret
```

### Output:

```
123456 was found 2389473 times...you should change your password
password was found 3452891 times...you should change your password
myS3cret was NOT found. Carry on!
```

---

## 🔍 How It Works

1. Each password is hashed using **SHA-1**.
2. The first 5 characters of the hash are sent to the API.
3. The API responds with all hashes starting with those 5 characters.
4. The script checks if the full hash (via its tail) is in the response.
5. If matched, it reports how many times that password was exposed.

---

## ⚠️ Security Notice

This script is **for learning and personal use**.
Do **not use real passwords** on shared or public machines.

