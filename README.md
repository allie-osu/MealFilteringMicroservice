# MealFilteringMicroservice

## Prerequisites
* python 3 & pip 3 installed
* Clone the project repository
* (Optional, but recommended) Navigate to repository root, and create and activate python virtual environment (see https://docs.python.org/3/library/venv.html for details)
  * For example, in a terminal run `python3 -m venv ./venv` to create and then `source ./venv/bin/activate` to activate
* Run `pip install -e .` to set up the project and the dependencies (flask)

## How to start the microservice
* In a terminal within the repository root, run `FLASK_APP=./mealfilteringservice/app.py flask run -h localhost -p <PORT>`
* I noticed issues with flask's default port of 5000 on Mac, so something like 8000 may work better.

## Example Request

```
cd <project root>

curl --location --request GET 'http://localhost:8000/filtered_meals' \
--form 'filters=@"./mealfilteringservice/static/example_filters.json"' \
--form 'meals=@"./mealfilteringservice/static/example_meals.json"'
```

## Example Response
```
[
  {
    "id": 3,
    "name": "Steak Quesadilla",
    "category": "Dinner",
    "ingredients": ["Steak", "Tortillas", "Salt", "Pepper", "Vegetable Oil", "Jack Cheese"]
  }
]
```