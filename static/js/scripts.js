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

document.addEventListener('DOMContentLoaded', function() {
  const pizzaCards = document.querySelectorAll('.pizza-card');
  const ingredientCards = document.querySelectorAll('.ingredient-card');
  const supplementCards = document.querySelectorAll('.supplement-card');  
  const ingredientsContainer = document.getElementById('ingredients-container');

  flatpickr("#time", {
      enableTime: true,
      noCalendar: true,
      dateFormat: "H:i",
      time_24hr: true,
      minuteIncrement: 15,
      defaultDate: "12:00"
  });

  // Function to add a new ingredient card
  function addIngredientCard(ingredientName, ingredientImg) {
    const card = document.createElement('div');
    card.classList.add('col-md-3', 'col-sm-6', 'mb-4');

    const innerDiv = document.createElement('div');
    innerDiv.classList.add('card', 'ingredient-card');
    // innerDiv.setAttribute('data-ingredient', ingredientData);

    const img = document.createElement('img');
    img.src =  `/static/images/${ingredientImg}`;
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
      const pizzaName = this.getAttribute('data-pizza');var selectedSupplements = [];
      
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

  ingredientCards.forEach(card => {
    card.addEventListener('click', function() {
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
    console.log(indice + "removed");
  }
});