# 📖 **Password Manager — User Guide**

#### About the Program
**Password Manager** is a simple, fast, and user-friendly console-based password manager written in Python.

**Features:**
- Generate strong random passwords
- Save passwords for websites, apps, or services
- View all saved passwords
- Edit or delete existing entries
- Copy passwords to clipboard
- Clean and nice-looking interface (using Rich and PyFiglet)

---

### 🚀 How to Run the Program

#### 1. Clone the repository
```bash
git clone https://github.com/nightmare000-dev/Password-Manager.git
cd Password-Manager
```

#### 2. Create virtual environment and install dependencies

**Windows:**
```cmd
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

**Linux / macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

#### 3. Run the program
```bash
python main.py
```

---

### Main Menu

After launching, you will see the main menu:

```
1. Password Generator
2. View list of passwords
3. Help
4. Exit
```
---

### Features

#### 1. Password Generator
- Generates a strong 16-character password (uppercase, lowercase, numbers, special symbols)
- After generation, you can immediately save it with a service name and login

#### 2. Password List
In this section you can:
- View all saved passwords
- Copy a password to clipboard (`copy`)
- Edit an entry (`edit`)
- Delete an entry (`delete`)

#### 3. Help
Shows this help information.

---

### Project Structure

| File / Folder       | Purpose                              |
|---------------------|--------------------------------------|
| `main.py`           | Main file - program entry point      |
| `functions.py`      | Core functions and menu logic        |
| `options.py`        | Menu display functions               |
| `vocabulary.py`     | All text and menu strings            |
| `pages/`            | Folder with separate menu pages      |
| `requirements.txt`  | List of required Python packages     |

---

### How to Use (Quick Start)

1. Run the program → `python main.py`
2. Choose **1** to generate a new password
3. Choose **2** to see your saved passwords
4. Use numbers to navigate through menus

---
