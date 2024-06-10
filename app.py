from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime

app = Flask(__name__)

sauces = {
    "rouge": {
        "image": "cheese.jpg",
        "description": "Sauce tomate"
    },
    "blanche": {
        "image": "cheese.jpg",
        "description": "Crème Fraiche"
    },
    "rose": {
        "image": "cheese.jpg",
        "description": "Tomate et Crème"
    }
}

# Dictionary of ingredients
ingredients = {
    "Gruyère": {
        "image": "cheese.jpg",
        "description": "Gruyère rapé"
    },
    "Mozzarella": {
        "image": "cheese.jpg",
        "description": "Mozzarella rapée"
    },
    "Olives": {
        "image": "cheese.jpg",
        "description": "Olives noires"
    },
    "Anchois": {
        "image": "cheese.jpg",
        "description": "Anchois"
    },
    "Jambon": {
        "image": "cheese.jpg",
        "description": "Cubes de jambon"
    },
    "Champignons": {
        "image": "cheese.jpg",
        "description": "Champignons hachés"
    },
    "Oignons": {
        "image": "cheese.jpg",
        "description": "Oignons hachés"
    },
    "Chorizo": {
        "image": "cheese.jpg",
        "description": "Tranches de chorizo"
    },
    "Thon": {
        "image": "cheese.jpg",
        "description": "Miettes de thon"
    },
    "Câpres": {
        "image": "cheese.jpg",
        "description": "Câpres"
    },
    "Bolognaise": {
        "image": "cheese.jpg",
        "description": "Sauce Bolognaise"
    },
    "Lardons": {
        "image": "cheese.jpg",
        "description": "Lardons fumés"
    },
    "Oeuf": {
        "image": "cheese.jpg",
        "description": "Oeuf"
    },
    "Figatellu": {
        "image": "cheese.jpg",
        "description": "Figatellu corse"
    },
    "Fruits de mer": {
        "image": "cheese.jpg",
        "description": "Salade de fruits de mer"
    },
    "Kebab": {
        "image": "cheese.jpg",
        "description": "Mix de volailles épicé"
    },
    "Roquefort": {
        "image": "cheese.jpg",
        "description": "Roquefort"
    },
    "Chèvre": {
        "image": "cheese.jpg",
        "description": "Buche de chèvre"
    },
    "Poivrons": {
        "image": "cheese.jpg",
        "description": "Poivrons"
    },
    "Coeurs d'artichaut": {
        "image": "cheese.jpg",
        "description": "Artichauts"
    },
    "Aubergine": {
        "image": "cheese.jpg",
        "description": "Aubergines"
    },
    "Miel": {
        "image": "cheese.jpg",
        "description": "Miel AOP de Corse"
    },
    "Pignons": {
        "image": "cheese.jpg",
        "description": "Pignons de pin"
    }
}

# Dictionary of pizzas
pizzas = {
    "Marguerite": {
        "image": "margherita.jpg",
        "description": "Classic cheese and tomato pizza",
        "sauce": sauces["rouge"],
        "ingredients": [ingredients["Gruyère"], ingredients["Olives"]]
    },
    "Anchois": {
        "image": "margherita.jpg",
        "description": "Classic cheese and tomato pizza",
        "sauce": sauces["rouge"],
        "ingredients": [ingredients["Anchois"], ingredients["Olives"]]
    },
    "Napolitaine": {
        "image": "margherita.jpg",
        "description": "Classic cheese and tomato pizza",
        "sauce": sauces["rouge"],
        "ingredients": [ingredients["Gruyère"], ingredients["Anchois"], ingredients["Olives"]]
    },
    "Jambonnière": {
        "image": "margherita.jpg",
        "description": "Classic cheese and tomato pizza",
        "sauce": sauces["rouge"],
        "ingredients": [ingredients["Gruyère"], ingredients["Jambon"]]
    },
    "Forestière": {
        "image": "margherita.jpg",
        "description": "Classic cheese and tomato pizza",
        "sauce": sauces["rouge"],
        "ingredients": [ingredients["Gruyère"], ingredients["Olives"]]
    },
    "Reine": {
        "image": "margherita.jpg",
        "description": "Classic cheese and tomato pizza",
        "sauce": sauces["rouge"],
        "ingredients": [ingredients["Gruyère"], ingredients["Olives"]]
    },
    "Oignons": {
        "image": "margherita.jpg",
        "description": "Classic cheese and tomato pizza",
        "sauce": sauces["rouge"],
        "ingredients": [ingredients["Gruyère"], ingredients["Olives"]]
    },
    "Knacky": {
        "image": "margherita.jpg",
        "description": "Classic cheese and tomato pizza",
        "sauce": sauces["rouge"],
        "ingredients": [ingredients["Gruyère"], ingredients["Olives"]]
    },
    "Chorizo": {
        "image": "margherita.jpg",
        "description": "Classic cheese and tomato pizza",
        "sauce": sauces["rouge"],
        "ingredients": [ingredients["Gruyère"], ingredients["Olives"]]
    },
    "Thon et Câpres": {
        "image": "margherita.jpg",
        "description": "Classic cheese and tomato pizza",
        "sauce": sauces["rouge"],
        "ingredients": [ingredients["Gruyère"], ingredients["Olives"]]
    },
    "Bolognaise": {
        "image": "margherita.jpg",
        "description": "Classic cheese and tomato pizza",
        "sauce": sauces["rouge"],
        "ingredients": [ingredients["Gruyère"], ingredients["Olives"]]
    },
    "Carbonara": {
        "image": "margherita.jpg",
        "description": "Classic cheese and tomato pizza",
        "sauce": sauces["rouge"],
        "ingredients": [ingredients["Gruyère"], ingredients["Olives"]]
    },
    "Chausson": {
        "image": "margherita.jpg",
        "description": "Classic cheese and tomato pizza",
        "sauce": sauces["rouge"],
        "ingredients": [ingredients["Gruyère"], ingredients["Olives"]]
    },
    "Figatellu": {
        "image": "margherita.jpg",
        "description": "Classic cheese and tomato pizza",
        "sauce": sauces["rouge"],
        "ingredients": [ingredients["Gruyère"], ingredients["Olives"]]
    },
    "Fruits de mer": {
        "image": "margherita.jpg",
        "description": "Classic cheese and tomato pizza",
        "sauce": sauces["rouge"],
        "ingredients": [ingredients["Gruyère"], ingredients["Olives"]]
    },
    "Kebab": {
        "image": "margherita.jpg",
        "description": "Classic cheese and tomato pizza",
        "sauce": sauces["rouge"],
        "ingredients": [ingredients["Gruyère"], ingredients["Olives"]]
    },
    "Roquefort": {
        "image": "margherita.jpg",
        "description": "Classic cheese and tomato pizza",
        "sauce": sauces["rouge"],
        "ingredients": [ingredients["Gruyère"], ingredients["Olives"]]
    },
    "3 Fromages": {
        "image": "pepperoni.jpg",
        "description": "Pepperoni and cheese",
        "sauce": sauces["rouge"],
        "ingredients": [ingredients["Gruyère"], ingredients["Olives"]]
    },
    "Poivrons et Lardons": {
        "image": "veggie.jpg",
        "description": "Mixed vegetables and cheese",
        "sauce": sauces["rouge"],
        "ingredients": [ingredients["Gruyère"], ingredients["Olives"]]
    },
    "4 Saisons": {
        "image": "veggie.jpg",
        "description": "Mixed vegetables and cheese",
        "sauce": sauces["rouge"],
        "ingredients": [ingredients["Gruyère"], ingredients["Olives"]]
    },
    "Pizza du chef": {
        "image": "veggie.jpg",
        "description": "Mixed vegetables and cheese",
        "sauce": sauces["rouge"],
        "ingredients": [ingredients["Gruyère"], ingredients["Olives"]]
    },
    "Pizza de Sophie": {
        "image": "hawaiian.jpg",
        "description": "Ham, pineapple, and cheese",
        "sauce": sauces["rouge"],
        "ingredients": [ingredients["Gruyère"], ingredients["Olives"]]
    }
}


planning = {}
orders = []
order = []
pizza = {
    "name": "",
    "size": "M",
    "sauce": "rouge",
    "supplements": [],
    "deplements": []
}

@app.route('/update_pizza', methods=['POST'])
def update_pizza():
    global pizza
    data = request.json
    pizza["name"] = data
    pizza["supplements"] = []
    
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

@app.route('/reset_order', methods=['POST'])
def reset_order():
    global order
    order = []
    
    return jsonify({'status': 'success'})

@app.route('/add_pizza_to_order', methods=['POST'])
def add_pizza_to_order():
    global order
    order.append(pizza.copy())
    
    return jsonify({'status': 'success'})

@app.route('/')
def index():
    return redirect(url_for('choose_pizza'))

@app.route('/order_entry', methods=['GET', 'POST'])
def order_entry():
    if request.method == 'POST':
        name = request.form['name']
        time_str = request.form['time']
        try:
            order_time = datetime.strptime(time_str, "%H:%M")
            orders.append({"name": name, "time": order_time})
            return redirect(url_for('order_display'))
        except ValueError:
            return "Invalid time format. Please use HH:MM format.", 400
    pizza = request.args.get('pizza', '')
    return render_template('order_entry.html', pizza=pizza)

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
    return render_template('choose_supplements.html', pizza=pizza, pizzas=pizzas, supplements=ingredients)

@app.route('/recap', methods=['GET', 'POST'])
def recap():
    if request.method == 'POST':
        name = request.form['name']
        time_str = request.form['time']
        try:
            # order_time = datetime.strptime(time_str, "%H:%M")
            # orders.append({"name": name, "pizzas": order.copy(), "time": order_time})
            if time_str in planning:
                planning[time_str].append({"name": name, "pizzas": order.copy()})
                
            else:
                planning[time_str] = [{"name": name, "pizzas": order.copy()}]
            
            return redirect(url_for('order_display'))
        except ValueError:
            return "Invalid time format. Please use HH:MM format.", 400
    return render_template('recap.html', order=order)


@app.route('/recap_order')
def recap_order():
    return render_template('recap_orderv3.html')

@app.route('/tab')
def tab():
    return render_template('tab.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)