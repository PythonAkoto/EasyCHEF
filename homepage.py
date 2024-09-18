import os
import typing
from flask import Flask, Blueprint, render_template, request, url_for
import requests
from dotenv import load_dotenv
load_dotenv()


home: Blueprint = Blueprint("home", __name__)


@home.route("/")
@home.route("/home", methods=["GET", "POST"])
def homepage():
    if request.method == "GET":
        return render_template("home.html")
    else:
        ing = request.form.get("ingredients")
        url = os.environ['API_URL']
        querystring = {
            "ingredients": f"{ing}",
            "number": "3",  # number of recipes
            "ignorePantry": "false",
            "ranking": "1",
        }

        headers = {
            "X-RapidAPI-Key": os.environ['X-RapidAPI-Key'],
            "X-RapidAPI-Host": os.environ['X-RapidAPI-Host'],
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()
        try:
            # accessing the recipe dictionary
            # chnage to then repeat process for all three:
            # recipe1 = data[0], recipe2 = data[1], recipe3 = data[2]
            recipe1 = data[0]
            recipe2 = data[1]
            recipe3 = data[2]

            # recipe 1
            recipe1_title = recipe1["title"]
            recipe1_img = recipe1["image"]

            # recipe 2
            recipe2_title = recipe2["title"]
            recipe2_img = recipe2["image"]

            # recipe 3
            recipe3_title = recipe3["title"]
            recipe3_img = recipe3["image"]

            return (
                render_template(
                    "home.html",
                    recipe1=recipe1,
                    recipe1_title=recipe1_title,
                    recipe1_img=recipe1_img,
                    recipe2=recipe2,
                    recipe2_title=recipe2_title,
                    recipe2_img=recipe2_img,
                    recipe3=recipe3,
                    recipe3_title=recipe3_title,
                    recipe3_img=recipe3_img,
                ),
                200,
            )
        except:
            void = "No results"
            return render_template("home.html", void=void), 400


@home.route("/", methods=["POST"])
def random_recipe():
    meal_options = request.form.get("meal_options")
    breakfast = request.form.get("breakfast")
    brunch = request.form.get("brunch")
    starter = request.form.get("starter")
    main_course = request.form.get("main_course")
    dessert = request.form.get("dessert")
    vege = request.form.get("vege")
    vegan = request.form.get("vegan")

    url = os.environ['API_URL']

    querystring = {"tags": "", "number": "1"}

    headers = {
        "X-RapidAPI-Key": os.environ['X-RapidAPI-Key'],
        "X-RapidAPI-Host": os.environ['X-RapidAPI-Host'],
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()

    try:
        # data = response.json()
        data1 = data["recipes"][0]

        title = data1["title"]
        img = data1["image"]
        servings = data1["servings"]
        prepare_time = data1["preparationMinutes"]
        cook_time = data1["cookingMinutes"]
        ready_in = data1["readyInMinutes"]
        instructions = data1["instructions"]
        return render_template(
            "home.html",
            data=data,
            title=title,
            img=img,
            servings=servings,
            prepare_time=prepare_time,
            cook_time=cook_time,
            ready_in=ready_in,
            instructions=instructions,
        )
    except:
        void = "No Results"
        return render_template("home.html", void=void)
