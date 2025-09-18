# FastAPI Project Setup Guide

This guide will help you set up and run the FastAPI project in this directory.

## 💬 Getting Started

### 1. Enter into the Project Directory

```bash
cd fastAPI
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

- **On Linux/MacOS:**
    ```bash
    source .venv/bin/activate
    ```
- **On Windows:**
    ```bash
    .venv\Scripts\activate
    ```

### 4. Check if the Virtual Environment is Active

```bash
which python
```
You should see a path similar to:
```
/home/user/fastAPI/.venv/bin/python
```

### 5. Upgrade pip

```bash
python -m pip install --upgrade pip
```

### 6. Add .gitignore (Recommended if Using Git)

To ensure your virtual environment is not tracked by git, add a `.gitignore` file inside `.venv`:

```bash
echo "*" > .venv/.gitignore
```

Alternatively, add `.venv/` to your project's main `.gitignore` file to ignore the whole environment.

### 7. Install Required Packages

Install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 8. Run Your Program

Now you can run your FastAPI application as needed.

```bash
uvicorn app.main:app --reload
```
---

**Happy coding! 🚀**
