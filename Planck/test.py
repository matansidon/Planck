import requests

BASE = "http://127.0.0.1:5000/"
# response=requests.put(BASE+"video/1", {"likes": 10})

response = requests.get(
    "https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup")
data = response.json()
pizzas = data['Data']["categoriesList"][3]["dishList"]
drinks=data['Data']["categoriesList"]
{"categoryName":"Drinks"}["dishList"]
print(len(data['Data']["categoriesList"][5]["dishList"]))
'''
class Dish:
    def __init__(self,id,name,desc,price,category_id,choices,image,popular,score,enable_comment):
        self.id=id
        self.name=name
        self.desc=desc
        self.price=price
        self.category_id=category_id
        self.choices=choices
        self.image=image
        self.popular=popular
        self.score=score
        self.enable_comment=enable_comment


class Pizza(Dish):
    def get(self):

'''

def get_drinks():
    from main import Dish

    d=[]
    for drink in drinks:
        id = drink['dishId']
        name = drink['dishName']
        desc = drink['dishDescription']
        price = drink['dishPrice']
        category_id = drink['categoryID']
        choices = drink['choices']
        image = drink['dishImageUrl']
        popular = drink['isPopularDish']
        score = drink['dishPopularityScore']
        enable_comment = drink['enableComment']
        d.append(Dish(id, name, desc, price, category_id, choices, image, popular, score, enable_comment))
    return d

def get_pizzas():
    from main import Dish
    l = []
    for pizza in pizzas:
        id = pizza['dishId']
        name = pizza['dishName']
        desc = pizza['dishDescription']
        price = pizza['dishPrice']
        category_id = pizza['categoryID']
        choices = pizza['choices']
        image = pizza['dishImageUrl']
        popular = pizza['isPopularDish']
        score = pizza['dishPopularityScore']
        enable_comment = pizza['enableComment']
        print(id)
        print(name)

        l.append(Dish(id, name, desc, price, category_id, choices, image, popular, score, enable_comment))

    # print(l)

    return l
