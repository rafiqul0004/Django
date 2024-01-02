const getparams = () => {
    const params = new URLSearchParams(window.location.search).get('productId');
    fetch(`https://fakestoreapi.com/products/${params}`)
        .then((res) => res.json())
        .then((data) => displayDetail(data));
    
}

const displayDetail = (product) => { 
    const parent = document.getElementById('detail-product');
    const div = document.createElement('div');
    div.innerHTML = `
    <div class="col-md-6">
    <img class="pro-img" src=${product.image} alt="">
    </div>
    <div class="col-md-6">
            <h1 class="text-cent">${product.title}</h1>
            <p>${product.description}</p>
            <button class="btn btn-warning mb-3">${product.category}</button> <br>
            <button class="btn btn-primary">price : $${product.price}</button>
    </div>
    `
    parent.appendChild(div)
}



getparams();