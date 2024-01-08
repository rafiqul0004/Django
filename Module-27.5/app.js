const userList = () => {
    fetch("https://fakestoreapi.com/users")
        .then((res) => res.json())
        .then((data) => {
            data.forEach((item) => {
                const parent = document.getElementById('table-body');
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td>${item.id}</td>
                    <td>${item.name.firstname}</td>
                    <td>${item.name.lastname}</td>
                    <td>${item.email}</td>
                    <td>${item.address.city}</td>
                    <td>${item.address.street}</td>
                    <td>${item.phone}</td>
                `
                
                parent.appendChild(tr)
        })
    })
}
userList();