import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

<<<<<<< HEAD


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = 'mongodb://admin:1veronica@ds235352.mlab.com:35352/cookbook'
=======
app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = 'mongodb://admin:admin@ds123926.mlab.com:23926/task_manager'
>>>>>>> fb6dcd016d73d815a8b579b874e07680df2cd7c1

mongo = PyMongo(app)

@app.route('/')
<<<<<<< HEAD
@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
    categories=mongo.db.categories.find())
    
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", 
    recipes=mongo.db.recipes.find())    
    

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes =  mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))
        
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('editrecipe.html', recipe=the_recipe, categories=all_categories)        
            
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get['recipe_name'],
        'category_name':request.form.get['category_name'],
        'recipe_description': request.form.get['recipe_description'],
        'sub_date': request.form.get['sub_date'],
        'has_allergens':request.form.get['has_allergens']
    })
    return redirect(url_for('get_recipes'))            
    
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))    
    
@app.route('/get_categories')
def get_categories():
    return render_template('categories.html',
    categories=mongo.db.categories.find())
    

@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
    category=mongo.db.categories.find_one({'_id': ObjectId(category_id)}))


@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    mongo.db.categories.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form['category_name']})
    return redirect(url_for('get_categories'))


  

@app.route('/delete_category/<category_id>')  
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for("get_categories"))
    

@app.route('/insert_category', methods=['POST'])
def insert_category():
    categories = mongo.db.categories
    category_doc = {'category_name': request.form['category_name']}
    categories.insert_one(category_doc)
    return redirect(url_for('get_categories'))
    

@app.route('/new_category')
def new_category():
    return render_template('addcategory.html')

       

if __name__ == '__main__':
    app.run(host='0.0.0.0',
        port=int(os.environ.get('PORT',5000 )),
        debug=False)
=======
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", 
    tasks=mongo.db.tasks.find())
    



# @app.route('/')
# def hello():
#     return "Hello World ...again"
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
>>>>>>> fb6dcd016d73d815a8b579b874e07680df2cd7c1
