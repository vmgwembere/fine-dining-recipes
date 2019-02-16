# Fine Dining Recipes

A web application that allows users to store and easily access cooking recipes.

<<<<<<< HEAD
The backend code and frontend form to allowS users to add new recipes to the site.

The backend code  groupS and summariseS the recipes on the site, based on their attributes such as cuisine, country of origin, allergens, ingredients, etc. and a frontend page to show this summary, and make the categories clickable to drill down into a filtered view based on that category. This frontend page can be as simple or as complex as you’d like; you can use a Python library such as matplotlib, or a JS library such as d3/dc (that you learned about if you took the frontend modules) for visualisation.
=======
The backend code and frontend form to allows users to add new recipes to the site.

The backend code  groups and summarises the recipes on the site, based on their attributes such as cuisine, country of origin, allergens, ingredients, etc. and a frontend page to show this summary, and make the categories clickable to drill down into a filtered view based on that category. 
>>>>>>> fb6dcd016d73d815a8b579b874e07680df2cd7c1

The backend code is used to retrieve a list of recipes, filtered based on various criteria.

There is a detailed view for each recipes, that would just show all attributes for that recipe, and the full preparation instructions.
 
## UX


<<<<<<< HEAD
Bright and bold colours 
=======
Bright and bold colours aim is to standout and be inviting to website users like the recipes.
>>>>>>> fb6dcd016d73d815a8b579b874e07680df2cd7c1

## Features
Navbar

<<<<<<< HEAD
Home New task Manage categories Home page
=======
Home Newtask Managecategories Home 
>>>>>>> fb6dcd016d73d815a8b579b874e07680df2cd7c1

List of tasks (each with a task name, due date, description) Title: Tasks Buttons: edit, mark complete, add new task Add Task page

Inputs: category, name, description, due date (calendar), is urgent Submit: add task Edit Task page

Title: Edit Task Inputs: category, name, description, due date (calendar), has allergens Submit: update task Categories page

Title: Categories List of categories (each with category name) Buttons: delete, edit, new category Edit Category page

Title: Edit Category Inputs: name Buttons: update category New Category page

Title: New Category Inputs: name Buttons: add category 
 

- 
## Technologies Used
<<<<<<< HEAD
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
Create new database on mlab.com


## Testing


=======
1.HTML5 

2.CSS3 

3.Materialize

4.Python3

5.Flask

6.flask-pymongo

7.MongoDB

8.mLab

9.Heroku



## Testing

Manual testing to see if database was correctly connected by creating and deleting categories on the backend and through the site.
>>>>>>> fb6dcd016d73d815a8b579b874e07680df2cd7c1


## Deployment

Create a new app on heroku.com

Login to heroku with email and password

heroku login Add heroku remote

heroku git:remote Add requirements.txt

sudo pip3 freeze --local > requirements.txt Add Procfile (this tells heroku what to do with the project)

echo web: python run.py > Procfile Git commit and push to heroku remote

git add Procfile $ git ci -m 'Add requirements.txt and Procfile' $ git push -u heroku master Set up dynos

heroku ps:scale web=1 Setup config variables on heroku dashboard

## Credits

Code-Institute-Solutions/flask-mongo-task-manager 

<<<<<<< HEAD
### Content
- 
=======
>>>>>>> fb6dcd016d73d815a8b579b874e07680df2cd7c1

### Media
- The photos used in this site were obtained from pixabay

### Acknowledgements

- I received inspiration for this project from code institute mini project
<<<<<<< HEAD
=======


>>>>>>> fb6dcd016d73d815a8b579b874e07680df2cd7c1
