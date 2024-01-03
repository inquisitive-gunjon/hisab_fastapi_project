
# Hishab - Daily Expense Project

Hishab is a daily expense project, and its backend is created using the FastAPI Python framework.

## Command Lines

Follow these steps to set up and run the project:

### Step 1: Install Virtual Environment 
```bash
$ pip install virtualenv
```

### Step 2: Set Up Virtual Environment
```bash
$ virtualenv venv
```
### Step 3: Activate Virtual Environment
```bash
$ source venv/bin/activate
```
### Step 4: Create index.py File
```bash
$ touch index.py
```
### Step 5: Install XAMPP

Download and install XAMPP from https://www.apachefriends.org/

For Mac Users
If your Mac does not support XAMPP, use the following command, then try again. Otherwise, skip this step:


$ xattr -dr com.apple.quarantine /Users/mac-m2/Downloads/xampp-osx-8.2.4-0-installer.app
### Step 6: Install Dependencies
```bash
$pip install fastapi sqlalchemy pymysql uvicorn
```
### Step 7: Install JWT Authentication Dependencies
```bash
$ pip install python-jose pyjwt passlib
```
```bash
$ pip install bcrypt
```
Project Configuration
Make sure to configure your project settings appropriately before running. Check and update the configuration files accordingly.

In FastAPI, you can store sensitive information like the `SECRET_KEY` in environment variables to keep them secure. Here's a step-by-step guide on how to hide the `SECRET_KEY` using environment variables:

1. **Install python-dotenv:**

   You can use the `python-dotenv` package to load environment variables from a `.env` file. Install it using:

   ```bash
   pip install python-dotenv
   ```

2. **Create a .env file:**

   Create a file named `.env` in your project directory and add your `SECRET_KEY` to it:

   ```env
   SECRET_KEY=my_secret_key_here
   ```

   Replace `my_secret_key_here` with your actual secret key.

3. **Load environment variables in your FastAPI app:**

   In your FastAPI app, use `load_dotenv` from `python-dotenv` to load the environment variables from the `.env` file. Modify your main FastAPI script (`main.py` or similar) as follows:

   ```python
   from fastapi import FastAPI
   from dotenv import load_dotenv

   load_dotenv()  # Load environment variables from .env file

   app = FastAPI()

   # Access your secret key using os.getenv
   SECRET_KEY = os.getenv("SECRET_KEY")

   @app.get("/")
   def read_root():
       return {"Hello": "World"}
   ```

   Now, `SECRET_KEY` will be populated with the value from the `.env` file.

4. **Add .env to .gitignore:**

   To ensure that your `.env` file is not shared in version control systems, add it to your `.gitignore` file. Create a `.gitignore` file if you don't have one and add the following line:

   ```
   .env
   ```

   This prevents the `.env` file from being included in your Git repository.

By following these steps, you keep sensitive information like the `SECRET_KEY` separate from your codebase, making it easier to manage and more secure. Always remember not to share your secret keys or sensitive information publicly.


Make sure you also have the .env file in your project directory with the SECRET_KEY specified.

If the problem persists, ensure that your virtual environment is activated or that you are installing the package in the correct Python environment where your FastAPI application is running.

Running the Project
Once everything is set up and configured, run the project using the following command:
```bash
$ uvicorn index:app --reload
```
Visit http://127.0.0.1:8000/ in your browser to access the Hishab project.

Feel free to explore and manage your daily expenses with Hishab!
