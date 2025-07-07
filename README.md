# 📁 Directory Size Calculator

A command-line application that simulates a virtual file system with a hierarchical structure of directories and files. Built for navigating, listing, and calculating directory sizes — without touching the actual filesystem.

Created by **Nyx Zhao** | [zhaolili918@gmail.com](mailto:zhaolili918@gmail.com)

---

## 🧠 Overview

This project provides a simulated file system in memory. Users can:
- Navigate through virtual folders with `cd`
- List directory contents with `ls`
- Calculate total directory size recursively with `size`

---

## ⚙️ Features

- ✅ CLI interface with Unix-style commands
- ✅ Support for `cd ..`, `cd ./folder1/folder2`
- ✅ Recursively calculates size across nested directories
- ✅ Includes unit tests and an example file system
- ✅ Clean, extensible code structure using OOP

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/directory-size-calculator.git
cd directory-size-calculator
```

### 2. Run the application

```bash
python3 src/main.py
```

If python3 doesn't work try

```bash
python src/main.py
```

---
## 💻 Test Data

Run unit tests from the root directory:
```bash
python3 test/test_file_system.py
```
Or if you're using an IDE like PyCharm, just run the test file directly.

Tests cover:
- ✅ Valid and invalid cd usage
- ✅ Deeply nested directory traversal
- ✅ Empty directory behavior
- ✅ Correct recursive size calculation

---
## 🌱 Seed Data

An example file system is preloaded via example.py, containing directories like:

```arduino
root/
├── docs/
├── desktop/
│   └── screenshots/
│   └── text/
├── media/
│   └── music/
│   └── images/
```
Each folder contains multiple files with varying sizes to simulate real-world behavior.

---
## 🙏 Acknowledgments

This project was created as part of a CLI simulation coding exercise. Big thanks to the reviewers for their time and attention.

