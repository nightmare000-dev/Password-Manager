# Password-Manager
This tool can generate a complicated password for you consisting of 16 random symbols. You're able to **delete and edit** a list of your passwords on the `View List` page. The script will create a `db.json` file and there you will find all your passwords.

# Usage


### Linux
**Clone the repository and change your directory**
```bash
git clone --depth=1 https://github.com/nightmare000-dev/Password-Manager.git
cd ~/Password-Manager
```

**Create .venv, activate it and install requirements**
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

**Use `chmod +x main.py` if it's neccessary**

**Now you can run `./main.py` file**
