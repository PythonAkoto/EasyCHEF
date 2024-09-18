"""Quick teat to check the api calls and what data i get back"""

# search recipe
import requests

url = (
    "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/complexSearch"
)

querystring = {
    "query": "pasta",
    "cuisine": "italian",
    "excludeCuisine": "greek",
    "diet": "vegetarian",
    "intolerances": "gluten",
    "equipment": "pan",
    "includeIngredients": "tomato,cheese",
    "excludeIngredients": "eggs",
    "type": "main course",
    "instructionsRequired": "true",
    "fillIngredients": "false",
    "addRecipeInformation": "false",
    "titleMatch": "Crock Pot",
    "maxReadyTime": "20",
    "ignorePantry": "true",
    "sort": "calories",
    "sortDirection": "asc",
    "minCarbs": "10",
    "maxCarbs": "100",
    "minProtein": "10",
    "maxProtein": "100",
    "minCalories": "50",
    "maxCalories": "800",
    "minFat": "10",
    "maxFat": "100",
    "minAlcohol": "0",
    "maxAlcohol": "100",
    "minCaffeine": "0",
    "maxCaffeine": "100",
    "minCopper": "0",
    "maxCopper": "100",
    "minCalcium": "0",
    "maxCalcium": "100",
    "minCholine": "0",
    "maxCholine": "100",
    "minCholesterol": "0",
    "maxCholesterol": "100",
    "minFluoride": "0",
    "maxFluoride": "100",
    "minSaturatedFat": "0",
    "maxSaturatedFat": "100",
    "minVitaminA": "0",
    "maxVitaminA": "100",
    "minVitaminC": "0",
    "maxVitaminC": "100",
    "minVitaminD": "0",
    "maxVitaminD": "100",
    "minVitaminE": "0",
    "maxVitaminE": "100",
    "minVitaminK": "0",
    "maxVitaminK": "100",
    "minVitaminB1": "0",
    "maxVitaminB1": "100",
    "minVitaminB2": "0",
    "maxVitaminB2": "100",
    "minVitaminB5": "0",
    "maxVitaminB5": "100",
    "minVitaminB3": "0",
    "maxVitaminB3": "100",
    "minVitaminB6": "0",
    "maxVitaminB6": "100",
    "minVitaminB12": "0",
    "maxVitaminB12": "100",
    "minFiber": "0",
    "maxFiber": "100",
    "minFolate": "0",
    "maxFolate": "100",
    "minFolicAcid": "0",
    "maxFolicAcid": "100",
    "minIodine": "0",
    "maxIodine": "100",
    "minIron": "0",
    "maxIron": "100",
    "minMagnesium": "0",
    "maxMagnesium": "100",
    "minManganese": "0",
    "maxManganese": "100",
    "minPhosphorus": "0",
    "maxPhosphorus": "100",
    "minPotassium": "0",
    "maxPotassium": "100",
    "minSelenium": "0",
    "maxSelenium": "100",
    "minSodium": "0",
    "maxSodium": "100",
    "minSugar": "0",
    "maxSugar": "100",
    "minZinc": "0",
    "maxZinc": "100",
    "offset": "10",
    "number": "10",
    "limitLicense": "false",
    "ranking": "2",
}

headers = {
    "X-RapidAPI-Key": "670505dc3fmsh9cd923658f74705p10c323jsnc8539188f679",
    "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
}

response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)

# search recipe by ingredients
import requests

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"

querystring = {
    "ingredients": "apples,flour,sugar",
    "number": "2",
    "ignorePantry": "true",
    "ranking": "1",
}

headers = {
    "X-RapidAPI-Key": "670505dc3fmsh9cd923658f74705p10c323jsnc8539188f679",
    "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

# get random recipe
import requests

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random"

querystring = {
    "tags": "breakfast",
    "number": "1",
}  # dessert, main course, starter, breakfast, brunch, (options)

headers = {
    "X-RapidAPI-Key": "670505dc3fmsh9cd923658f74705p10c323jsnc8539188f679",
    "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.json()
data = data["recipes"][0]

title = data["title"]
img = data["image"]
servings = data["servings"]
prepare_time = data["preparationMinutes"]
cook_time = data["cookingMinutes"]
ready_in = data["readyInMinutes"]
instructions = data["instructions"]


# print(title, img, servings, prepare_time, cook_time, ready_in, instructions)

# generate meal plan
import requests

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/mealplans/generate"

querystring = {
    "timeFrame": "day",
    "targetCalories": "2000",
    "diet": "vegetarian",
    "exclude": "shellfish, olives",
}

headers = {
    "X-RapidAPI-Key": "670505dc3fmsh9cd923658f74705p10c323jsnc8539188f679",
    "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
}

response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)

# get meal plan for the week
import requests

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/mealplanner/dsky/week/2020-06-01"

querystring = {"hash": "4b5v4398573406"}

headers = {
    "X-RapidAPI-Key": "670505dc3fmsh9cd923658f74705p10c323jsnc8539188f679",
    "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
}

response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)
