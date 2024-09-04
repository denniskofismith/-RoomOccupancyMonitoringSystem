

document.addEventListener("DOMContentLoaded", function() {
    fetch('/api/classrooms')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById("classroom-container");

            data.forEach(classroom => {
                const card = document.createElement("div");
                card.className = `col-md-4 mb-4 ${classroom.status === "available" ? "available" : "unavailable"}`;
                card.innerHTML = `
                    <div class="card">
                        <img src="${classroom.img}" class="card-img-top" alt="${classroom.name}">
                        <div class="card-body">
                            <h5 class="card-title">${classroom.name}</h5>
                            <p class="card-text">${classroom.status === "available" ? "Available" : "Unavailable"}</p>
                        </div>
                    </div>
                `;
                container.appendChild(card);
            });
        })
        .catch(error => console.error('Error fetching classroom data:', error));
});


// document.addEventListener("DOMContentLoaded", function() {
//     fetch('/api/classrooms')
//         .then(response => response.json())
//         .then(data => {
//             const container = document.getElementById("classroom-container");

//             data.forEach(classroom => {
//                 const card = document.createElement("div");
//                 card.className = `col-md-4 mb-4 ${classroom.status}`;
//                 card.innerHTML = `
//                     <div class="card">
//                         <img src="${classroom.img}" class="card-img-top" alt="${classroom.name}">
//                         <div class="card-body">
//                             <h5 class="card-title">${classroom.name}</h5>
//                             <p class="card-text">${classroom.status === "available" ? "Available" : "Unavailable"}</p>
//                         </div>
//                     </div>
//                 `;
//                 container.appendChild(card);
//             });
//         })
//         .catch(error => console.error('Error fetching classroom data:', error));
// });
