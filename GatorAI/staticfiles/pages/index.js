const url = 'https://retail-store-product-information.p.rapidapi.com/getproductv2?url=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fproduct%2FB08Z8441FG';
const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': 'c5be5dde60msh9539b4baa0ab0b1p100a8ajsn728e700892ab',
		'X-RapidAPI-Host': 'retail-store-product-information.p.rapidapi.com'
	}
};

try {
	const response = await fetch(url, options);
	const result = await response.text();
	console.log(result);
} catch (error) {
	console.error(error);
}