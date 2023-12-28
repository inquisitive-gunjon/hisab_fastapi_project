
# Hishab - Daily Expense Project

Hishab is a daily expense project, and its backend is created using the FastAPI Python framework.

## Command Lines

Follow these steps to set up and run the project:

### Step 1: Install Virtual Environment 
```bash
$ pip install virtualenv

### Step 2: Set Up Virtual Environment
```bash
$ virtualenv venv
### Step 3: Activate Virtual Environment
```bash
$ source venv/bin/activate
### Step 4: Create index.py File
```bash
$ touch index.py
### Step 5: Install XAMPP
```bash
Download and install XAMPP from https://www.apachefriends.org/

For Mac Users
If your Mac does not support XAMPP, use the following command, then try again. Otherwise, skip this step:


$ xattr -dr com.apple.quarantine /Users/mac-m2/Downloads/xampp-osx-8.2.4-0-installer.app
### Step 6: Install Dependencies
```bash
$pip install fastapi sqlalchemy pymysql uvicorn
### Step 7: Install JWT Authentication Dependencies

$ pip install python-jose pyjwt passlib
Project Configuration
Make sure to configure your project settings appropriately before running. Check and update the configuration files accordingly.

Running the Project
Once everything is set up and configured, run the project using the following command:

$ uvicorn index:app --reload
Visit http://127.0.0.1:8000/ in your browser to access the Hishab project.

Feel free to explore and manage your daily expenses with Hishab!
