/*document.addEventListener("DOMContentLoaded", function() {
    // Füge ein Event Listener für das Formular hinzu
    document.querySelector("form").addEventListener("submit", function(event) {
        event.preventDefault();  // Verhindert das Standardverhalten (Absenden des Formulars)
        
        // Zeige die versteckten Abschnitte
        document.getElementById("nodes").classList.remove("hidden");
        document.getElementById("pods").classList.remove("hidden");
    });
});*/
document.addEventListener("DOMContentLoaded", function() {
    // Füge einen Event Listener für das Formular hinzu
    document.querySelector("form").addEventListener("submit", function(event) {
        event.preventDefault();  // Verhindert das Standardverhalten (Absenden des Formulars)
        
        // Hole den ausgewählten Namespace aus dem Dropdown
        var selectedNamespace = document.getElementById("namespace").value;
        
        // Zeige die versteckten Abschnitte
        document.getElementById("nodes").classList.remove("hidden");
        document.getElementById("pods").classList.remove("hidden");
        
        // Füge den ausgewählten Namespace in den Pod Overview Titel ein
        var podOverviewTitle = document.querySelector("#pods h2");
        podOverviewTitle.textContent = `Pod Overview (Namespace: ${selectedNamespace})`;
    });
});

