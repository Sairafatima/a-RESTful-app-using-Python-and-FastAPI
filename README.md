# a-RESTful-app-using-Python-and-FastAPI
<html>
<h1>Endpoints Implemented</h1>

<ul>
  <li>User Registrations</li>
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
  <li>Fast Api</li>
  <li>Git Control(Optional)</li>
  <li>Xamp: to run mySql server</li>
</ul>
<h1>Steps to follow</h1>
<ul>
  <li>Install python 3 on your pc and make sure it is added in Environment Variables</li>
  <li>Run command to upgrade pip version: -m pip install --upgrade pip   </li>
  <li>Install Virtual environment: pip install pipenv  </li>
</ul>
<h>Git Control(Optional)</h1>
<ul>
  <li>Install Github on ur pc. Make sure to add Git in ur path</li>
  <li>Install Git extension in VSCode</li>
  <li>Connect your GitHub account by running this command in  VSCode terminal </li>
  <b> git config --global user.name <"username">  </b><br>
   <b>git config --global user.name <"email account"> </b>
  <li>Install Virtual environment:<b> pip install pipenv </b> </li>
  <li>Activate python scripts in Virtual environment: <b> source venv/Scripts/activate  </b> </li>
  <li>Create main file in this case it is index.py: <b> type > index.py</b></li>
  <li>Create configration file for database connection in this case it is config/db.py</li>
  <b>Make sure to use corrent database URL in configration file</b>
  <li>Create Models folder and create user.py,items.py and index.py</li>
  <b>These files implements table structures of our databse</b>
  <li>Create Schema folder and create user.py,items.py and index.py</li>
  <b>These files implements objects having same feilds as tables</b>
  <li>Create Routes folder and create user.py,items.py and index.py</li>
  <b>These files implements end points</b>
  <li>Run following commands to install necassry libraries</li>
  <b>pip install fastapi sqlalchemy uvicorn pydantic fastapi-pagination fastapi-login pyjwt  passlib bcrypt tortoise-orm python-multipart pandas</b><br>
  <li>Setup Xamp and run MyqSql server on local host</li>
  <li>Create Tables on MySql server according to models defined in your files</li>
  <li> Run command to start API on http://127.0.0.1:8000/docs :<b> uvicorn index:app --reload</b></li>



</ul>






</html>