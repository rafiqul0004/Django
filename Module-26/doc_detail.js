const getparams = () => {
    const param = new URLSearchParams(window.location.search).get("doctorId")
    loadTime(param)
    fetch(`https://testing-8az5.onrender.com/doctor/list/${param}`)
        .then((res) => res.json())
        .then((data) => displayDetails(data));
    
    fetch(`https://testing-8az5.onrender.com/doctor/review/?doctor_id=${param}`)
        .then((res) => res.json())
    .then((data)=>docReview(data))
};

const docReview = (reviews) => {
    reviews.forEach((review) => {
        const parent = document.getElementById('doc-review-container');
        const div = document.createElement('div');
        div.classList.add('review-card');
        div.innerHTML = `
                    <img src="Images/girl.png" alt="">
                    <h4>${review.reviewer}</h4>
                    <p>${review.body.slice(0, 100)}</p>
                    <h6>${review.rating}</h6>
        `
        parent.appendChild(div)
    });
};

const displayDetails = (doctor) => {
    console.log(doctor);
    const parent = document.getElementById("doc-details")
    const div = document.createElement("div")
    div.classList.add("doc-details-container")
    div.innerHTML = `
    <div class="doctor-img">
    <img src=${doctor.image} alt="">
    </div>
    <div class="doc-info">
    <h1>${doctor.full_name}</h1>
    ${
        doctor.specialization.map((item) => {
            return `<button class="doc-spe-btn">${item}</button>`
        })
    }
    ${
        doctor.designation.map((item) => {
            return `<h4>${item}</h4>`
        })
    }
    <p class="w-50">Lorem ipsum dolor sit amet consectetur adipisicing elit. Laborum nam laboriosam voluptatum, eos delectus accusamus quae debitis temporibus nobis cumque?</p>
    <h4>Fee: 1000 BDT</h4>
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
    Take Appointment
  </button>
    </div>

    `
    parent.appendChild(div);
}

const loadTime = (id) => {
    fetch(`https://testing-8az5.onrender.com/doctor/availabletime/?doctor_id=${id}`)
        .then((res) => res.json())
        .then((data) => {
            data.forEach((item) => { 
                const parent = document.getElementById("time-container")
                const option = document.createElement("option")
                option.value = item.id
                option.innerHTML = item.name
                parent.appendChild(option)
            })
    })
}

const handleAppointment = () => { 
    const param = new URLSearchParams(window.location.search).get("doctorId")
    const status = document.getElementsByName("status");
    const selected = Array.from(status).find((button) => button.checked);
    const symptom = document.getElementById("symptom").value;
    const time = document.getElementById("time-container");
    const selectedTime = time.options[time.selectedIndex];
    console.log(selected.value, symptom, selectedTime.value);
    const info = {
    appointment_type: selected.value,
    appointment_status:"Pending",
    time: selectedTime.value,
    symptom: symptom,
    cancel: false,
    patient: 1,
    doctor: param

    }

    fetch("https://testing-8az5.onrender.com/appointment/",{
        method: "POST",
        headers: { 'content-type': 'application/json' },
        body: JSON.stringify(info)
    })
        .then((res) => res.json())
        .then((data) => { 
            console.log(data);
        })
}
getparams();
loadTime();