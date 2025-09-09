💬 Enter into that project directory
cd fastAPI
Create a Virtual Environment
python -m venv .venv
Activate the Virtual Environment
source .venv/bin/activate
Check the Virtual Environment is Active
which python

/home/user/fastAPI/.venv/bin/python
Upgrade pip
python -m pip install --upgrade pip
Add .gitignore
If you are using Git (you should), add a .gitignore file to exclude everything in your .venv from Git.
echo "*" > .venv/.gitignore

Install Packages
Install from requirements.txt
pip install -r requirements.txt
Run Your Program
