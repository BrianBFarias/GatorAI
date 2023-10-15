document.addEventListener('DOMContentLoaded', load);

function load(){


// Highlight newly displayed products
let products = document.querySelectorAll('.product');  // Assuming each product has a class 'product'
products.forEach(product => {
    product.classList.add('highlighted-product');  // Add the highlight

    // Remove the highlight after 3 seconds
    setTimeout(() => {
        product.classList.remove('highlighted-product');
    }, 3000);  // 3 seconds to match the CSS animation duration
});
}

function AIsearch(){
	input = document.querySelector('.inputSearch').value;

	console.log(input)

	allProducts = document.getElementById('productsDisplay');
	if(input == ''){
		return
	}
	fetch(`/search?input=${input}`)
    .then(response => response.json())
    .then(async data => {
        if(!data){
			console.log("empty")
        }
        else if(data[0].model){
			allProducts.innerHTML ='';

          for (const product of data) {

			const word = product.type
			const firstLetter = word.charAt(0)
			const firstLetterCap = firstLetter.toUpperCase()
			const remainingLetters = word.slice(1)
			const capitalizedWord = firstLetterCap + remainingLetters

			console.log(product)
			const item = document.createElement('div');
			item.className = 'product';

			item.innerHTML = `
			<div class="first">
				<h1>$${product.price}</h1>
			</div>
			<div>
				<h1>${capitalizedWord}</h1>
			</div>
			<div>
				<h2> ${product.model}</h2>
			</div>
			<div class="spec">
				<h2>${product.storage}gb</h2>
				<h3>Cameras: ${product.camera}</h3>
			</div>`

			allProducts.appendChild(item)
          }
        }
		else{
			allProducts.innerHTML ='';

			for (const product of data) {
			  var data_quant=null
			  
			  if(product.data == 999){
				data_quant = "Unlimited"
			  }
			  else{
				data_quant = product.data
			  }
  
			  console.log(product)
			  const item = document.createElement('div');
			  item.className = 'product';
  
			  item.innerHTML = `
			  <div class="first">
				  <h1>$${product.rate} / Month</h1>
			  </div>
			  <div>
				  <h1>${product.type}</h1>
			  </div>
			  <div class="spec">
				  <h2>Lines: ${product.lines}</h2>
				  <h3>${data_quant} gb Data</h3>
			  </div>`
  
			  allProducts.appendChild(item)
			}
		}
      });
}


let suggestions = ['iPhone', 'Samsung Galaxy', 'Google Pixel', 'Network plan', 'Mobile', 'Home network', '256GB storage', '3 cameras', 'Unlimited data', '4 lines', '5G', '4G', '$1000', '$500'];

document.querySelector('.inputSearch').addEventListener('input', function() {
    let inputVal = this.value;
    let suggestionBox = document.getElementById('suggestionBox');
    
    // If no input or input is too short, hide suggestions
    if (inputVal.length < 2) {
        if (suggestionBox) suggestionBox.remove();
        return;
    }

    // Filter suggestions based on user input
    let filteredSuggestions = suggestions.filter(suggestion => suggestion.toLowerCase().includes(inputVal.toLowerCase()));

    // If suggestionBox doesn't exist, create it
    if (!suggestionBox) {
        suggestionBox = document.createElement('div');
        suggestionBox.id = 'suggestionBox';
        suggestionBox.style.border = '1px solid #ccc';
        suggestionBox.style.backgroundColor = '#fff';
        suggestionBox.style.position = 'absolute';
        suggestionBox.style.width = 'calc(100% - 6px)';
        suggestionBox.style.maxHeight = '150px';
        suggestionBox.style.overflowY = 'auto';
        suggestionBox.style.zIndex = '1000';
        this.parentNode.appendChild(suggestionBox);
    } else {
        suggestionBox.innerHTML = '';  // Clear previous suggestions
    }

    // Populate the suggestion box
    for (let suggestion of filteredSuggestions) {
        let item = document.createElement('div');
        item.innerText = suggestion;
        item.style.padding = '8px';
        item.style.cursor = 'pointer';
        
        // Highlight item on hover
        item.addEventListener('mouseenter', function() {
            this.style.backgroundColor = '#f5f5f5';
        });
        item.addEventListener('mouseleave', function() {
            this.style.backgroundColor = '#fff';
        });
        
        // Set input value on click and hide suggestionBox
        item.addEventListener('click', function() {
            document.querySelector('.inputSearch').value = this.innerText;
            suggestionBox.remove();
        });

        suggestionBox.appendChild(item);
    }
});

// Hide suggestions when clicking outside the search box
document.addEventListener('click', function(event) {
    if (!event.target.closest('.inputSearch')) {
        let suggestionBox = document.getElementById('suggestionBox');
        if (suggestionBox) suggestionBox.remove();
    }
});

// After displaying the new products in AIsearch function
let products = document.querySelectorAll('.product');  // Assuming each product has a class 'product'
products.forEach(product => {
    product.classList.add('highlighted-product');  // Add the highlight

    // Remove the highlight after 3 seconds
    setTimeout(() => {
        product.classList.remove('highlighted-product');
    }, 3000);  // 3 seconds to match the CSS animation duration
});
