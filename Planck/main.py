from flask import Flask, request
from flask_restful import Api, Resource
app = Flask(__name__)
api = Api(app)

videos = {}
image = {}
data = {}
resturant = {}
dishes = {}
drinks={}


class Data(Resource):
    def get(self, data_id):
        return data[data_id]

    def put(self, video_id):
        print(request.form)
        return {}


class Video(Resource):
    def get(self, video_id):
        return videos[video_id]

    def put(self, video_id):
        print(request.form)
        return {}


class Image(Resource):
    @app.route('/GET/pizzas', methods=['GET'])
    def get(self, image_id):
        return image[image_id]

    def put(self, image_id):
        print(request.form)
        return {}


'''
class Product(Resource):
    def get(self):
        return 1
        '''


class Dish(Resource):
    def __init__(self, id, name, desc, price, category_id, choices, image, popular, score, enable_comment):
        self.id = id
        self.name = name
        self.desc = desc
        self.price = price
        self.category_id = category_id
        self.choices = choices
        self.image = image
        self.popular = popular
        self.score = score
        self.enable_comment = enable_comment

    def __str__(self):
        return f"{self.id}, {self.name}, {self.price}"

    def get(self):
        return dishes['dish_id']


class Drink(Resource):
    def __init__(self, id, name, desc, price, category_id, choices, image, popular, score, enable_comment):
        self.id = id
        self.name = name
        self.desc = desc
        self.price = price
        self.category_id = category_id
        self.choices = choices
        self.image = image
        self.popular = popular
        self.score = score
        self.enable_comment = enable_comment
    def __str__(self):
            return f"{self.id}, {self.name}, {self.desc},{self.price}"
    def get(self):
        return drinks['drink_id']
'''
class Pizza(Dish):
    @app.route('/GET/pizzas', methods=['GET'])
    def get(self):
        return{}
'''

# api.add_resource(Video,"/video/<int:video_id>")
api.add_resource(Image, "/image/<int:image_id>")
# api.add_resource(Data,"/data/<int:data>")
api.add_resource(Dish, "/dishes/<int:dish_id>")
api.add_resource(Drink,  "/dishes/<int:dish_id>")



# print(data['Data'])
@app.route("/pizza", methods=['GET'])
def pizza():
    from test import get_pizzas
    result = [str(pizza)for pizza in get_pizzas()]
    return {"data": result}

@app.route("/drinkk", methods=['GET'])
def drinkk():
    from test import get_drinks
    result = [str(drink)for drink in get_drinks()]
    return {"drink": result}


if __name__ == "__main__":
    app.run(debug=True)
