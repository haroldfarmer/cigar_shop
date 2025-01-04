let numOfCigarsMap = new Map()
numOfCigarsMap.set('first',10);
numOfCigarsMap.set('second',10);
numOfCigarsMap.set('third',10);
numOfCigarsMap.set('fourth',10);
numOfCigarsMap.set('fifth',10);
numOfCigarsMap.set('sixth',10);


function get_cigar_data() {
    const promise = axios.get('http://127.0.0.1:8000/get_cigar_data');
    const dataPromise = promise.then((response) => response.data)
    return dataPromise

}

function getPrice() {
    getCigarData()
        .then(data => {
            price = data[0][3].toString();
            document.getElementById("price").innerText = 'Price: $' + price;
        })
        .catch(err => console.log(err))

}

function cigarBought(id) {
    let numOfCigars = numOfCigarsMap.get(id)
    numOfCigars--;
    numOfCigarsMap.set(id,numOfCigars)
    console.log(numOfCigars)
    if (numOfCigars < 1) {
        document.getElementById(id).innerText = 'Price: OUT OF ORDER';
    }
    else {
        let str_num_of_cigars = numOfCigars.toString();
        document.getElementById(id).innerText = 'Amount ' + str_num_of_cigars;
    }

}

window.onload = (event) => {
    console.log('The page has fully loaded');
    getPrice();
};


