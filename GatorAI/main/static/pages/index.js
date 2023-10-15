document.addEventListener('DOMContentLoaded', load);

function load(){

}

function AIsearch(){
	input = document.querySelector('.inputSearch').value;

	console.log(input)

	fetch(`/search?input=${input}`)
    .then(response => response.json())
    .then(async data => {
        if(!data){

        }
        else{

          for (const product of data) {
			
          }
        }
      });
}