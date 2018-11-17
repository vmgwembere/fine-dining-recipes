
 # datacentric project
Python, MongoDb, mLab, Flask, Materialize

Developer: vmgwembere

App available at: https://fine-dine-app-new.herokuapp.com/


# ux 

Navbar

Home
New task
Manage categories
Home page

List of tasks (each with a task name, due date, description)
Title: Tasks
Buttons: edit, mark complete, add new task
Add Task page

Inputs: category, name, description, due date (calendar), is urgent
Submit: add task
Edit Task page

Title: Edit Task
Inputs: category, name, description, due date (calendar), is urgent
Submit: update task
Categories page

Title: Categories
List of categories (each with category name)
Buttons: delete, edit, new category
Edit Category page

Title: Edit Category
Inputs: name
Buttons: update category
New Category page

Title: New Category
Inputs: name
Buttons: add category


## Technologies and Dependencies
HTML5
CSS3
Materialize
Python3
pip3
Flask
flask-pymongo
MongoDB
mLab
Heroku
4 Workflow
Create new database on mlab.com

## Heroku Deployment
Create a new app on heroku.com

Login to heroku with email and password

$ heroku login
Add heroku remote

$ heroku git:remote 
Add requirements.txt

$ sudo pip3 freeze --local > requirements.txt
Add Procfile (this tells heroku what to do with the project)

$ echo web: python run.py > Procfile
Git commit and push to heroku remote

$ git add Procfile
$ git ci -m 'Add requirements.txt and Procfile'
$ git push -u heroku master
Set up dynos

$ heroku ps:scale web=1
Setup config variables on heroku dashboard
