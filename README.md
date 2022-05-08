# MealFilteringMicroservice

## Prerequisites
* python 3 & pip 3 installed
* Clone the project repository
* (Optional, but recommended) Navigate to repository root, and create and activate python virtual environment (see https://docs.python.org/3/library/venv.html for details)
  * For example, in bash run `python -m venv ./venv` to create and then `source ./venv/Scripts/activate` to activate
* Run `pip install -e .` to set up the project and the dependencies (flask)

## How to start the microservice
* In bash within the repository root, run `FLASK_APP=./mealfilteringservice/app.py flask run`
* To use a different port than the default (5000), use the `-p <PORT>` option

