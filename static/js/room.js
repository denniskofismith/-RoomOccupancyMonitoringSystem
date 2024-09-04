document.addEventListener('DOMContentLoaded', function() {
    const rooms = ['room1', 'room2'];  // List of room IDs
    
    function updateRoomStatus(roomId) {
        fetch(`/api/rooms/${roomId}`)
            .then(response => response.json())
            .then(data => {
                document.getElementById(`${roomId}-status`).textContent = data.occupied ? 'Occupied' : 'Available';
                document.getElementById(`${roomId}-people`).textContent = data.people_count;
            })
            .catch(error => console.error('Error fetching room data:', error));
    }

    rooms.forEach(room => {
        updateRoomStatus(room);
        setInterval(() => updateRoomStatus(room), 5000);  // Update every 5 seconds
    });
});
