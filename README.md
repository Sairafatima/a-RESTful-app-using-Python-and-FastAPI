# a-RESTful-app-using-Python-and-FastAPI
<html>
<h1>Endpoints Implemented</h1>

<ul>
  <li>User Registration</li>
  <li>User Login</li>
  <li>Search items</li>
  <li>Remove items</li>
  <li>Update items</li>
</ul>

<h1>Technologies Used</h1>
<ul>
  <li>Python</li>
  <li>Fast Api</li>
  <li>Git Conrol(Optional)</li>
  <li>MySql</li>
</ul>

<h1> Important Installations</h1>
<ul>
  <li>Python3.9</li>
  <li>Fast API</li>
  <li>Git Control (Optional)</li>
  <li>Xamp: to run MySQL server</li>
</ul>
<h1>Steps to follow</h1>
<ul>
  <li>Install python 3 on your pc and make sure it is added in Environment Variables</li>
  <li>Run command to upgrade pip version:<b> python -m pip install --upgrade pip </b></li>
  <li>Install Virtual environment:<b> pip install pipenv </b></li>
</ul>
<h>Git Control(Optional)</h1>
<ul>
  <li>Install GitHub on your pc. Make sure to add Git in you path Variable</li>
  <li>Install Git extension in VSCode</li>
  <li>Connect your GitHub account by running command in VSCode terminal </li>
  <b> git config --global user.name <"username">  </b><br>
   <b>git config --global user.email <"email account"> </b>
  <li>Install Virtual environment:<b> pip install pipenv </b> </li>
  <li>Activate python scripts in Virtual environment: <b> source venv/Scripts/activate  </b> </li>
  <li>Create main file in this case it is index.py: <b> type > index.py</b></li>
  <li>Create configuration file for database connection in this case it is config/db.py</li>
  <b>Make sure to use correct database URL in configuration file</b>
  <li>Create Models folder and create user.py, items.py and index.py</li>
  <b>These files implement table structures of our database</b>
  <li>Create Schema folder and create user.py, items.py and index.py</li>
  <b>These files implement objects having same fields/attributes/datatypes as tables</b>
  <li>Create Routes folder and create user.py, items.py and index.py</li>
  <b>These files implement end points</b>
  <li>Run following commands to install necessary libraries</li>
  <b>pip install fastapi sqlalchemy uvicorn pydantic fastapi-pagination fastapi-login pyjwt  passlib bcrypt tortoise-orm python-multipart pandas</b><br>
  <li>Setup Xamp and run MySQL server on local host</li>
  <li>Create Tables on MySQL server according to models defined in your files</li>
  <li> Run command to start API on http://127.0.0.1:8000/docs :<b> uvicorn index:app --reload</b></li>
</ul>
</html>
