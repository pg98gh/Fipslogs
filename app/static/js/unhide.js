document.getElementById('namespaceForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    const formData = new FormData(this);

    fetch('/submit_namespace', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Update the nodes and pods sections with the returned HTML
        document.getElementById('nodes').innerHTML = data.nodesHTML;
        document.getElementById('pods').innerHTML = data.podsHTML;

        // Unhide the sections
        document.getElementById('nodes').classList.remove('hidden');
        document.getElementById('pods').classList.remove('hidden');
    })
    .catch(error => console.error('Error:', error));
});
