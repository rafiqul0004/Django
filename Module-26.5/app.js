const loadcategory = () => {
    fetch("https://fakestoreapi.com/products/categories")
        .then((res) => res.json())
        .then((data) => {
            data?.forEach((item) => {
                const parent = document.getElementById('cat-list');
                const li = document.createElement('li')
                li.classList.add('dropdown-item');
                li.innerHTML = `<li onclick="loadcategoryproducts('${item}')">${item}</li>`;
                parent.appendChild(li);
            });
    })
}
const loadcategoryproducts = (category) => { 
    fetch(`https://fakestoreapi.com/products/category/${category}`)
        .then((res) => res.json())
    .then((data) => displayProducts(data))
}
const loadProducts = () => { 
    fetch('https://fakestoreapi.com/products')
        .then((res) => res.json())
    .then((data) => displayProducts(data));
}

const displayProducts = (data) => { 
    const parent = document.getElementById('product-container');
    parent.innerHTML = "";
    data.forEach((item) => {
        const div = document.createElement('div');
        div.classList.add('card');
        div.innerHTML = `
                        <img src=${item.image} class="card-img-top" alt="product">
                        <div class="card-body">
                          <h5 class="card-title">${item.title}</h5>
                          <p class="card-text">${item.description}</p>
                          <p class="card-text">${item.category}</p>
                          <a target="_blank" href="product_details.html?productId=${item.id}" class="btn btn-primary">Details</a>
                        </div>
        `
        parent.appendChild(div);
        
    })

}

loadcategory();
loadProducts();