const loadServices = () => {
    fetch("https://testing-8az5.onrender.com/services/")
        .then(res => res.json())
        .then((data) => displayServices(data))
        .catch((err) => displayServices(err));
        
}

const displayServices = (services) => {
    services.forEach((service) => {
        const parent = document.getElementById('service-container');
        const li = document.createElement('li');
        li.innerHTML = `
        <div class="card shadow h-100">
                            <div class="ratio ratio-16x9">
                                <img src=${service.image} loading="lazy" alt="...">
                            </div>
                            <div class="card-body  p-3 p-xl-5">
                                <h3 class="card-title h5">${service.name} </h3>
                                <p class="card-text">${service.description.slice(0,140)} </p>
                                <a href="#" class="btn btn-primary">Details</a>
                            </div>
                        </div>
        `
        parent.appendChild(li)
    });
}

const loadDoctors = (search) => {
    fetch(`https://testing-8az5.onrender.com/doctor/list/?search=${search?search:""}`)
    .then(res => res.json())
        .then((data) => {
            console.log(data);
            displayDoctors(data?.results);
        })
}

const displayDoctors = (doctors) => { 
    doctors?.forEach((doctor) =>
    {
        const parent = document.getElementById('doctors')
        const div = document.createElement('div')
        div.classList.add('doc-card')
        div.innerHTML = `
                        <img class="doc-img" src=${doctor?.image} alt="">
                        <h1>${doctor?.full_name}</h1>
                        <h4>${doctor?.designation[0]}</h4>
                        <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Illum, amet?</p>
                        <p>
                        ${doctor?.specialization?.map((item) => {
                            return `<button>${item}</button>`
                        })}
                        </p>
                        <button>Detail</button>
        `
        parent.appendChild(div)
    }
    )

}
const loadDegignation = () => {
    fetch("https://testing-8az5.onrender.com/doctor/designation/")
    .then(res => res.json())
        .then((data) => {
            data?.forEach((item) => {
                const parent = document.getElementById('dop-deg')
                const li = document.createElement('li');
                li.classList.add('dropdown-item')
                li.innerHTML = item?.name
                parent.appendChild(li)
        })
    })
}

const loadSpecialization = () => {
    fetch("https://testing-8az5.onrender.com/doctor/specialization/")
    .then(res => res.json())
        .then((data) => {
            data?.forEach((item) => {
                const parent = document.getElementById('dop-spe')
                const li = document.createElement('li');
                li.classList.add('dropdown-item')
                li.innerHTML = item?.name
                parent.appendChild(li)
        })
    })
}
const handleSearch = () => { 
    const value = document.getElementById('search').value
    loadDoctors(value)
}
loadDoctors();
loadServices();
loadDegignation(); 
loadSpecialization()