FastAPI Project
This is a simple FastAPI project. Follow the steps below to set up and run the application.

Prerequisites
Before you begin, ensure you have the following installed on your system:

Python 3.x

pip (Python's package installer)

Installation and Setup
Follow these steps to set up the project environment and install the necessary dependencies.

1. Navigate to the Project Directory
Open your terminal and change your current directory to the project folder.

cd fastAPI

2. Create a Virtual Environment
It is a best practice to use a virtual environment to manage project dependencies. This keeps the packages isolated from your system-wide Python installation.

python -m venv .venv

3. Activate the Virtual Environment
Activate the virtual environment to ensure all subsequent packages are installed within it.

source .venv/bin/activate

You can verify that the virtual environment is active by checking the path of the python executable.

which python

The output should be similar to:

/home/user/fastAPI/.venv/bin/python

4. Upgrade pip
It's a good practice to ensure your pip installer is up to date.

python -m pip install --upgrade pip

5. Add .gitignore
To prevent the virtual environment folder (.venv) from being tracked by Git, create a .gitignore file.

echo ".venv" > .gitignore

Note: The original instruction used echo "*" which is too broad and can cause issues. It's better to explicitly ignore the .venv folder.

6. Install Dependencies
Install all the required packages from the requirements.txt file.

pip install -r requirements.txt

Running the Application
Once the dependencies are installed, you can start the application.

python main.py

Example Output
When the application runs successfully, you will see a "Hello World" message.

Hello World
