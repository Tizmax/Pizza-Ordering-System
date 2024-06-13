from flask import Flask, render_template, request, redirect, url_for, jsonify, json
from datetime import datetime

app = Flask(__name__)

tailles = ['P','M','G']

sauces = {
    "Rouge": "rouge.jpg",
    "Blanche": "blanche.jpg",
    "Rose": "rouge.jpg",
}

supplement_classique = {
        "P": 1,
        "M": 1.5,
        "G": 2
    }
supplement_fixe = {
        "P": 1.5,
        "M": 1.5,
        "G": 1.5
    }


# Dictionary of ingredients
ingredients = {
    "Gruyère": {
        "image": "cheese.jpg",
        "description": "Gruyère rapé",
        "prix": supplement_classique
    },
    "Mozzarella": {
        "image": "cheese.jpg",
        "description": "Mozzarella rapée",
        "prix": supplement_classique
    },
    "Olives": {
        "image": "olives.jpg",
        "description": "Olives noires",
        "prix": supplement_fixe

    },
    "Anchois": {
        "image": "anchois.jpg",
        "description": "Anchois",
        "prix": supplement_classique
    },
    "Jambon": {
        "image": "jambon.jpg",
        "description": "Cubes de jambon",
        "prix": supplement_classique
    },
    "Champignons": {
        "image": "champignons.jpg",
        "description": "Champignons hachés",
        "prix": supplement_classique
    },
    "Oignons": {
        "image": "oignons.jpg",
        "description": "Oignons hachés",
        "prix": supplement_classique
    },
    "Knacky": {
        "image": "chorizo.jpg",
        "description": "Saucisses knacky",
        "prix": supplement_classique
    },
    "Chorizo": {
        "image": "chorizo.jpg",
        "description": "Tranches de chorizo",
        "prix": supplement_classique
    },
    "Thon": {
        "image": "thon.jpg",
        "description": "Miettes de thon",
        "prix": supplement_classique
    },
    "Câpres": {
        "image": "câpres.jpg",
        "description": "Câpres",
        "prix": supplement_classique
    },
    "Bolognaise": {
        "image": "cheese.jpg",
        "description": "Sauce Bolognaise",
        "prix": supplement_classique
    },
    "Lardons": {
        "image": "lardons.jpg",
        "description": "Lardons fumés",
        "prix": supplement_classique
    },
    "Oeuf": {
        "image": "oeuf.jpg",
        "description": "Oeuf",
        "prix": supplement_fixe
    },
    "Figatellu": {
        "image": "figatellu.jpg",
        "description": "Figatellu corse",
        "prix": supplement_classique
    },
    "Fruits de mer": {
        "image": "fruits de mer.jpg",
        "description": "Salade de fruits de mer",
        "prix": supplement_classique
    },
    "Kebab": {
        "image": "kebab.jpg",
        "description": "Mix de volailles épicé",
        "prix": supplement_classique
    },
    "Roquefort": {
        "image": "roquefort.jpg",
        "description": "Roquefort",
        "prix": supplement_classique
    },
    "Chèvre": {
        "image": "chèvre.jpg",
        "description": "Buche de chèvre",
        "prix": supplement_classique
    },
    "Poivrons": {
        "image": "poivrons.jpg",
        "description": "Poivrons",
        "prix": supplement_classique
    },
    "Coeurs d'artichaut": {
        "image": "artichaut.jpg",
        "description": "Artichauts",
        "prix": supplement_classique
    },
    "Aubergine": {
        "image": "aubergine.jpg",
        "description": "Aubergines",
        "prix": supplement_classique
    },
    "Miel": {
        "image": "miel.jpg",
        "description": "Miel AOP de Corse",
        "prix": supplement_classique
    },
    "Pignons": {
        "image": "pignons.jpg",
        "description": "Pignons de pin",
        "prix": supplement_classique
    }
}

prix_pizza_1 = {
    "P": 6.5,
    "M": 8.5,
    "G": 11.5
}
prix_pizza_2 = {
    "P": 7,
    "M": 9,
    "G": 12
}
prix_pizza_3 = {
    "P": 7.5,
    "M": 10,
    "G": 13
}

# Dictionary of pizzas
pizzas = {
    "Marguerite": {
        "image": "margherita.jpg",
        "description": "Classic cheese and tomato pizza",
        "sauce": "Rouge",
        "ingredients": ["Gruyère", "Olives"],
        "prix": prix_pizza_1
    },
    "Anchois": {
        "image": "margherita.jpg",
        "description": "Classic cheese and tomato pizza",
        "sauce": "Rouge",
        "ingredients": ["Anchois", "Olives"],
        "prix": prix_pizza_1
    },
    "Napolitaine": {
        "image": "margherita.jpg",
        "description": "Classic cheese and tomato pizza",
        "sauce": "Rouge",
        "ingredients": ["Anchois", "Gruyère", "Olives"],
        "prix": prix_pizza_1
    },
    "Jambonnière": {
        "image": "margherita.jpg",
        "description": "Classic cheese and tomato pizza",
        "sauce": "Rouge",
        "ingredients": ["Jambon", "Gruyère"],
        "prix": prix_pizza_1
    },
    "Forestière": {
        "image": "margherita.jpg",
        "description": "Classic cheese and tomato pizza",
        "sauce": "Rouge",
        "ingredients": ["Champignons", "Gruyère"],
        "prix": prix_pizza_1
    },
    "Reine": {
        "image": "margherita.jpg",
        "description": "Classic cheese and tomato pizza",
        "sauce": "Rouge",
        "ingredients": ["Jambon", "Champignons", "Gruyère"],
        "prix": prix_pizza_1
    },
    "Oignons": {
        "image": "margherita.jpg",
        "description": "Classic cheese and tomato pizza",
        "sauce": "Rouge",
        "ingredients": ["Oignons", "Gruyère"],
        "prix": prix_pizza_1
    },
    "Knacky": {
        "image": "margherita.jpg",
        "description": "Classic cheese and tomato pizza",
        "sauce": "Rouge",
        "ingredients": ["Knacky", "Gruyère"],
        "prix": prix_pizza_1
    },
    "Chorizo": {
        "image": "margherita.jpg",
        "description": "Classic cheese and tomato pizza",
        "sauce": "Rouge",
        "ingredients": ["Chorizo", "Champignons", "Gruyère"],
        "prix": prix_pizza_2
    },
    "Thon et Câpres": {
        "image": "margherita.jpg",
        "description": "Classic cheese and tomato pizza",
        "sauce": "Rouge",
        "ingredients": ["Thon", "Câpres", "Gruyère"],
        "prix": prix_pizza_2
    },
    "Bolognaise": {
        "image": "margherita.jpg",
        "description": "Classic cheese and tomato pizza",
        "sauce": "Rouge",
        "ingredients": ["Bolognaise", "Gruyère"],
        "prix": prix_pizza_2
    },
    "Carbonara": {
        "image": "margherita.jpg",
        "description": "Classic cheese and tomato pizza",
        "sauce": "Blanche",
        "ingredients": ["Lardons", "Oignons", "Gruyère"],
        "prix": prix_pizza_2
    },
    "Chausson": {
        "image": "margherita.jpg",
        "description": "Classic cheese and tomato pizza",
        "sauce": "Rouge",
        "ingredients": ["Jambon", "Champignons", "Gruyère", "Oeuf"],
        "prix": prix_pizza_2
    },
    "Figatellu": {
        "image": "margherita.jpg",
        "description": "Classic cheese and tomato pizza",
        "sauce": "Rouge",
        "ingredients": ["Figatellu", "Champignons", "Gruyère"],
        "prix": prix_pizza_3
    },
    "Fruits de mer": {
        "image": "margherita.jpg",
        "description": "Classic cheese and tomato pizza",
        "sauce": "Rouge",
        "ingredients": ["Fruits de mer", "Gruyère"],
        "prix": prix_pizza_3
    },
    "Kebab": {
        "image": "margherita.jpg",
        "description": "Classic cheese and tomato pizza",
        "sauce": "Blanche",
        "ingredients": ["Kebab", "Gruyère"],
        "prix": prix_pizza_3
    },
    "Roquefort": {
        "image": "margherita.jpg",
        "description": "Classic cheese and tomato pizza",
        "sauce": "Blanche",
        "ingredients": ["Jambon", "Roquefort", "Gruyère"],
        "prix": prix_pizza_3
    },
    "3 Fromages": {
        "image": "pepperoni.jpg",
        "description": "Pepperoni and cheese",
        "sauce": "Blanche",
        "ingredients": ["Roquefort", "Gruyère", "Chèvre"],
        "prix": prix_pizza_3
    },
    "Poivrons et Lardons": {
        "image": "veggie.jpg",
        "description": "Mixed vegetables and cheese",
        "sauce": "Rouge",
        "ingredients": ["Poivrons", "Lardons", "Gruyère"],
        "prix": prix_pizza_3
    },
    "4 Saisons": {
        "image": "veggie.jpg",
        "description": "Mixed vegetables and cheese",
        "sauce": "Rouge",
        "ingredients": ["Coeurs d'artichaut", "Poivrons", "Aubergine", "Gruyère"],
        "prix": prix_pizza_3
    },
    "Pizza du chef": {
        "image": "veggie.jpg",
        "description": "Mixed vegetables and cheese",
        "sauce": "Rouge",
        "ingredients": ["Poivrons", "Aubergine", "Gruyère", "Chèvre"],
        "prix": prix_pizza_3
    },
    "Pizza de Sophie": {
        "image": "hawaiian.jpg",
        "description": "Ham, pineapple, and cheese",
        "sauce": "Blanche",
        "ingredients": ["Gruyère", "Chèvre", "Miel", "Pignons"],
        "prix": prix_pizza_3
    }
}


planning = {}
order = []
pizza = {
    "name": "",
    "half": "",
    "size": "M",
    "sauce": "",
    "supplements": [],
    "deplements": [],
    "quantity" : 1,
    "price": 0
}
clientName = ""
hour = ""
details = ""

def totalSoiree():
    totals = {
        "P": 0,
        "M": 0,
        "G": 0
    }
    counts = {
        "P": 0,
        "M": 0,
        "G": 0
    }
    total = 0
    for time, orders in planning.items():
        for order in orders:
            total += order["price"]
            for pizza in order["pizzas"]:
                totals[pizza["size"]] += 0
                counts[pizza["size"]] += 1
    return counts, total



def pricing(order):
    price = 0
    for pizza in order:
        price += pizzas[pizza["name"]]["prix"][pizza["size"]]
        for supplement in pizza["supplements"]:
            price += ingredients[supplement]["prix"][pizza["size"]]
    return price

def save():
    json.dump(planning, open("planning.txt",'w'))
    

@app.route('/modif_order', methods=['POST'])
def modif_order():
    req = request.json

    time = req["time"]
    index = int(req["index"])
    global order
    order = planning[time][index]["pizzas"]
    global clientName
    clientName = planning[time][index]["name"]
    global hour
    hour = time
    if len(planning[time]) > 1:
        planning[time].pop(index)
    else:
        planning.pop(time)
    
    save()

    return jsonify({'status': 'success'}) 

@app.route('/dec_quantity', methods=['POST'])
def dec_quantity():
    index = int(request.json)

    if order[index]["quantity"] == 1:
        order.pop(index)

    order[index]["quantity"] -= 1


    return jsonify({'status': 'success'}) 

@app.route('/inc_quantity', methods=['POST'])
def inc_quantity():
    index = int(request.json)

    order[index]["quantity"] += 1
    
    return jsonify({'status': 'success'})    

@app.route('/update_taille', methods=['POST'])
def update_taille():
    global pizza
    data = request.json

    pizza["size"] = data
    
    return jsonify({'status': 'success'})

@app.route('/update_sauce', methods=['POST'])
def update_sauce():
    global pizza
    data = request.json

    if data == pizzas[pizza["name"]]["sauce"]:
        pizza["sauce"] = ""
    else:
        pizza["sauce"] = data
    
    return jsonify({'status': 'success'})

@app.route('/update_pizza', methods=['POST'])
def update_pizza():
    global pizza
    data = request.json
    pizza["name"] = data
    pizza["supplements"] = []
    pizza["deplements"] = []
    pizza["sauce"] = ""
    pizza["size"] = "M"
    
    return jsonify({'status': 'success'})

@app.route('/add_supplement', methods=['POST'])
def add_supplement():
    global order
    data = request.json
    pizza["supplements"].append(data)
    
    return jsonify({'status': 'success'})

@app.route('/remove_supplement', methods=['POST'])
def remove_supplement():
    global pizza
    data = int(request.json)
    pizza["supplements"].pop(data)
    
    return jsonify({'status': 'success'})

@app.route('/remove_order', methods=['POST'])
def remove_order():
    order = request.json
    time = order["time"]
    index = int(order["index"])
    if len(planning[time]) > 1:
        planning[time].pop(index)
    else:
        planning.pop(time)

    
    save()

    return jsonify({'status': 'success'})

@app.route('/add_deplement', methods=['POST'])
def add_deplement():
    global order
    data = request.json
    pizza["deplements"].append(data)
    
    return jsonify({'status': 'success'})


@app.route('/reset_order', methods=['POST'])
def reset_order():
    global order
    global clientName
    global details
    global hour
    order = []
    clientName = ""
    details = ""
    hour = ""
    
    return jsonify({'status': 'success'})

@app.route('/add_pizza_to_order', methods=['POST'])
def add_pizza_to_order():
    global order
    order.append(pizza.copy())
    
    return jsonify({'status': 'success'})

@app.route('/')
def index():
    return redirect(url_for('planning'))


@app.route('/order_display')
def order_display():
    sorted_planning = dict(sorted(planning.items()))
    return render_template('order_display.html', planning=sorted_planning)


@app.route('/choose_pizza')
def choose_pizza():
    return render_template('choose_pizza.html', pizzas=pizzas)

@app.route('/choose_supplements')
def choose_supplements():
    pizza = request.args.get('pizza', '')
    return render_template('choose_supplements.html', pizza=pizza, pizzas=pizzas, supplements=ingredients, sauces=sauces, tailles=tailles)

@app.route('/recap', methods=['GET', 'POST'])
def recap():
    if request.method == 'POST':
        name = request.form['name']
        time_str = request.form['time']
        price = pricing(order)

        try:
            if time_str in planning:
                planning[time_str].append({"name": name, "pizzas": order.copy(), "price" : price})
                
            else:
                planning[time_str] = [{"name": name, "pizzas": order.copy(),"price" : price}]
            
            
            save()
            return redirect(url_for('order_display'))
        except ValueError:
            return "Invalid time format. Please use HH:MM format.", 400
    return render_template('recap.html', order=order, pizzas = pizzas, name=clientName, hour=hour)


@app.route('/totals')
def totals():
    return render_template('totals.html', totals=totalSoiree())


if __name__ == "__main__":
    planning = json.load(open("planning.txt"))
    app.run(host='0.0.0.0', port=5000, debug=True)

