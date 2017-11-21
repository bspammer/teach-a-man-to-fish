from teachamantofish import app, api, shopping_project_id
from flask import render_template, send_from_directory, request

@app.route("/img/<path:path>")
def img(path):
    return send_from_directory("static/img", path)

@app.route("/css/<path:path>")
def css(path):
    return send_from_directory("static/css", path)

@app.route("/fonts/<path:path>")
def fonts(path):
    return send_from_directory("static/fonts", path)

@app.route("/")
def root():
    return render_template("home.html", recipes=RECIPES*30)

@app.route("/add")
def add():
    recipe_id = int(request.args["recipeid"])
    recipe = RECIPES[recipe_id]
    add_recipe(recipe["title"], recipe["ingredients"])
    return "Successfully added recipe"


def add_recipe(recipe_name, ingredients):
    # api.add_item(recipe_name, project_id=shopping_project_id, indent=1)
    # for ingredient in ingredients:
        # api.add_item(ingredient, project_id=shopping_project_id, indent=2)
    # api.commit()
    return True

RECIPES = [
        {
            "title": "Crispy Garlicky Chicken p108",
            "nice_title": "Crispy Garlicky Chicken",
            "img_url": "/img/crispygarlickychicken.jpg",
            "recipe_id": 0,
            "ingredients": [
                "2 skinless chicken breasts",
                "Seeded wholemeal bread",
                "Garlic clove",
                "Lemon",
                "50g rocket",
                ]
        },
        {
            "title": "Flaky Pastry Pesto Chicken p114",
            "nice_title": "Flaky Pastry Pesto Chicken",
            "img_url": "/img/flakypastrypestochicken.jpg",
            "recipe_id": 1,
            "ingredients": [
                "320 sheet puff pastry",
                "4 chicken breasts",
                "Green pesto",
                "400g cherry tomatoes",
                "400g green beans",
                ]
        },
        {
            "title": "Speedy Spinach Curry p162",
            "nice_title": "Speedy Spinach Curry",
            "img_url": "/img/speedyspinachcurry.jpg",
            "recipe_id": 2,
            "ingredients": [
                "20g unsalted cashew nuts",
                "1 Onion",
                "2 tsps rogan josh curry paste",
                "100g paneer cheese",
                "200g baby spinach",
                ]
        },
        {
            "title": "Ham & Egg Curried Noodles p259",
            "nice_title": "Ham & Egg Curried Noodles",
            "img_url": "/img/hamandeggcurriednoodles.jpg",
            "recipe_id": 3,
            "ingredients": [
                "150g egg noodles",
                "4 spring onions",
                "100g roast ham",
                "2 teaspoons curry powder",
                "2 large eggs",
                ]
        },
    ]
