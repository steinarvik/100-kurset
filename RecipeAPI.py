from flask import Flask
import json

recipes = {
    1: {'id': 1, 'title': 'Spaghetti Carbonara', 'ingredients': ['spaghetti', 'eggs', 'pecorino cheese', 'guanciale'], 'instructions': 'Cook pasta, fry guanciale, mix with eggs and cheese, and combine with pasta.'},
    2: {'id': 2, 'title': 'Tomato Soup', 'ingredients': ['tomato', 'water', 'salt'], 'instructions': 'Boil all together until mushy, blend, and serve.'},
    3: {'id': 3, 'title': 'Grilled Cheese Sandwich', 'ingredients': ['bread', 'cheese', 'butter'], 'instructions': 'Butter bread, place cheese between slices, grill until golden.'}
}
# print(recipes)

app = Flask(__name__)

@app.route('/recipies/<res_id>')
def get_res(res_id):
    res_id_num = int(res_id)
    resept = recipes.get(res_id_num)
    return resept




@app.route('/')
def index():
    return "Hjemmesiden"

app.run(debug=True)
