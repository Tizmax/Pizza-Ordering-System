function modifOrder(time,index) {
  // Configuration de la requête
  var requestOptions = {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ time: time, index: index })
  }; 

  const confirmModif = window.confirm("Modifier la pizza ?");
  if (confirmModif) {
    // Envoi de la requête au backend Flask
    fetch('/modif_order', requestOptions)
      .then(response => response.json())
      .then(time => console.log(time))
      .then(index => console.log(index))
      .catch(error => console.log('Erreur :', error));
  
    console.log("modif")
  }
}
function resetOrder() {
  // Configuration de la requête
  var requestOptions = {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    }
  }; 

  // Envoi de la requête au backend Flask
  fetch('/reset_order', requestOptions)
    .then(response => response.json())
    .catch(error => console.log('Erreur :', error));
}

function addPizzaToOrder() {
  // Configuration de la requête
  var requestOptions = {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    }
  }; 

  // Envoi de la requête au backend Flask
  fetch('/add_pizza_to_order', requestOptions)
    .then(response => response.json())
    .catch(error => console.log('Erreur :', error));
}

function removeOrder(time,index) {
  // Configuration de la requête
  var requestOptions = {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ time: time, index: index })
  }; 

  const confirmDelete = window.confirm("Supprimer la pizza ?");
  if (confirmDelete) {
    // Envoi de la requête au backend Flask
    fetch('/remove_order', requestOptions)
      .then(response => response.json())
      .then(time => console.log(time))
      .then(index => console.log(index))
      .catch(error => console.log('Erreur :', error));
  
    location.reload()
  }
}
function incQuantity(index, quantity) {
    // Configuration de la requête
    var requestOptions = {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify(index)
    }; 

    // Envoi de la requête au backend Flask
    fetch('/inc_quantity', requestOptions)
      .then(response => response.json())
      .then(index => console.log(index))
      .catch(error => console.log('Erreur :', error));

    location.reload()
}

function decQuantity(index) {
    var requestOptions = {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify(index)
    }; 
    
    fetch('/dec_quantity', requestOptions)
      .then(response => response.json())
      .then(index => console.log(index))
      .catch(error => console.log('Erreur :', error));

    location.reload()
}

function tryDecQuantity(index, quantity) {
  


  if (quantity - 1 === 0) {
    const confirmDelete = window.confirm("Supprimer la pizza ?");
    if (confirmDelete) {
        decQuantity(index);
    }
  } else {
    decQuantity(index);
  }

}

document.addEventListener('DOMContentLoaded', function() {
  const pizzaCards = document.querySelectorAll('.pizza-card');
  const sauceCards = document.querySelectorAll('.sauce-card');
  const tailleCards = document.querySelectorAll('.taille-card');
  const ingredientCards = document.querySelectorAll('.ingredient-card');
  const supplementCards = document.querySelectorAll('.supplement-card');  
  const ingredientsContainer = document.getElementById('ingredients-container');

  flatpickr("#time", {
      enableTime: true,
      noCalendar: true,
      dateFormat: "H:i",
      time_24hr: true,
      minuteIncrement: 15,
  });

  // Function to add a new ingredient card
  function addIngredientCard(ingredientName, ingredientImg) {
    const card = document.createElement('div');
    card.classList.add('col-md-3', 'col-sm-6', 'mb-4', 'ingredient-card');

    const innerDiv = document.createElement('div');
    innerDiv.classList.add('card');
    // innerDiv.setAttribute('data-ingredient', ingredientData);

    const img = document.createElement('img');
    img.src =  `/static/images/ingredients/${ingredientImg}`;
    img.classList.add('card-img-top');
    // img.alt = ingredientData.description;

    const cardBody = document.createElement('div');
    cardBody.classList.add('card-body');

    const title = document.createElement('h5');
    title.classList.add('card-title', 'text-center');
    title.textContent = ingredientName;

    const description = document.createElement('p');
    description.classList.add('card-text', 'text-center');
    // description.textContent = ingredientData.description;

    innerDiv.appendChild(img);
    cardBody.appendChild(title);
    cardBody.appendChild(description);
    innerDiv.appendChild(cardBody);
    card.appendChild(innerDiv);

    
    card.addEventListener('click', function() {
      const index = Array.from(ingredientsContainer.children).indexOf(card);
      const length = Array.from(ingredientsContainer.children).length;
      remove_supplement(index - length);
      card.remove();
    });

    ingredientsContainer.appendChild(card);
  }

  pizzaCards.forEach(card => {
    card.addEventListener('click', function() {
      const pizzaName = this.getAttribute('data-pizza');
      
      // Configuration de la requête
      var requestOptions = {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify(pizzaName)
      };
      
      // Envoi de la requête au backend Flask
      fetch('/update_pizza', requestOptions)
          .then(response => response.json())
          .then(pizzaName => console.log(pizzaName))
          .catch(error => console.log('Erreur :', error));
      window.location.href = `/choose_supplements?pizza=${encodeURIComponent(pizzaName)}`;
    });
  });

  sauceCards.forEach(card => {
    card.addEventListener('click', function () {
        // Remove 'selected' class from all ingredient cards
        sauceCards.forEach(c => c.classList.remove('selected-card'));
        
        // Add 'selected' class to the clicked card
        this.classList.add('selected-card');

        const sauceName = this.getAttribute('data-ingredient');

        // Configuration de la requête
        var requestOptions = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(sauceName)
        };

        // Envoi de la requête au backend Flask
        fetch('/update_sauce', requestOptions)
            .then(response => response.json())
            .then(data => console.log(data))
            .catch(error => console.log('Erreur :', error));
        });
    });

    tailleCards.forEach(card => {
      card.addEventListener('click', function () {
          // Remove 'selected' class from all ingredient cards
          tailleCards.forEach(c => c.classList.remove('selected-card'));
          
          // Add 'selected' class to the clicked card
          this.classList.add('selected-card');
  
          const tailleName = this.getAttribute('data');
  
          // Configuration de la requête
          var requestOptions = {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json'
              },
              body: JSON.stringify(tailleName)
          };
  
          // Envoi de la requête au backend Flask
          fetch('/update_taille', requestOptions)
              .then(response => response.json())
              .then(data => console.log(data))
              .catch(error => console.log('Erreur :', error));
          });
      });

  ingredientCards.forEach(card => {
    card.addEventListener('click', function() {
      const ingredient = card.firstElementChild.getAttribute('data-ingredient');
      console.log(ingredient);
      add_deplement(ingredient);
      card.remove()
    });
  });

  supplementCards.forEach(card => {
    card.addEventListener('click', function() {
      const supplementName = this.getAttribute('name-supplement');
      const supplementImg = this.getAttribute('img-supplement');
      
      // Configuration de la requête
      var requestOptions = {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify(supplementName)
      };
      
      // Envoi de la requête au backend Flask
      fetch('/add_supplement', requestOptions)
          .then(response => response.json())
          .then(supplementName => console.log(supplementName))
          .catch(error => console.log('Erreur :', error));

      addIngredientCard(supplementName, supplementImg)
    });
  });
  function remove_supplement(indice) {
    // Configuration de la requête
    var requestOptions = {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify(indice)
    }; 
  
    // Envoi de la requête au backend Flask
    fetch('/remove_supplement', requestOptions)
      .then(response => response.json())
      .then(indice => console.log(indice))
      .catch(error => console.log('Erreur :', error));
  }
function add_deplement(ingredient) {
  // Configuration de la requête
  var requestOptions = {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(ingredient)
  }; 

  // Envoi de la requête au backend Flask
  fetch('/add_deplement', requestOptions)
    .then(response => response.json())
    .then(ingredient => console.log(ingredient))
    .catch(error => console.log('Erreur :', error));
}
});