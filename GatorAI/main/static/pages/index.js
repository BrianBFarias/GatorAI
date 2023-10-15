document.addEventListener('DOMContentLoaded', load);

function load(){

}

function AIsearch(){
	fetch(`/posts?start=${start}&end=${end}&spice=${localStorage.getItem('filterS') }&flavor=${localStorage.getItem('filterF') }`)
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