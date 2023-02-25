let num_of_cigars= 10;


function get_cigar_data() {
    const promise = axios.get('http://127.0.0.1:5000/get');
    const dataPromise = promise.then((response) => response.data)
    return dataPromise
    
}

function get_price() {
    get_cigar_data()
        .then(data => {
            price = data[0][3].toString();
            document.getElementById("price").innerText = 'Price: $' + price; 
        })
        .catch(err => console.log(err))

    
}

function cigar_bought() {

    num_of_cigars--;
    if (num_of_cigars < 1) {
        document.getElementById("num_cigars").innerText = 'Price: OUT OF ORDER';
    }
    else {
        let str_num_of_cigars = num_of_cigars.toString();
        document.getElementById("num_cigars").innerText = 'Price: $' + str_num_of_cigars;
    }

}

window.onload = (event) => {
    console.log('The page has fully loaded');
    get_price();
};


