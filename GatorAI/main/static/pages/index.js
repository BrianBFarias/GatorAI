document.addEventListener('DOMContentLoaded', load);

function load(){

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