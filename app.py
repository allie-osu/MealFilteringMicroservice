import json

from flask import Flask, request

app = Flask(__name__)


def _load_json_file(file_key):
    file = request.files[file_key]
    data = json.loads(file.read())
    file.close()
    return data


def _do_filters_apply(meal, filters):
    for filter in filters:
        if "attribute" not in filter or "value" not in filter:
            print(f"Skipping filter [{filter}], because it is missing the attribute or value.")
            continue

        if meal[filter["attribute"]] != filter["value"]:
            return False

    return True


@app.route("/filtered_meals", methods=["GET"])
def filtered_meals():
    if "meals" not in request.files:
        return "No meals file provided."

    if "filters" not in request.files:
        return "No filters file provided."

    meals = _load_json_file("meals")
    filters = _load_json_file("filters")

    results = []

    for meal in meals:
        if _do_filters_apply(meal, filters):
            results.append(meal)

    return json.dumps(results)

