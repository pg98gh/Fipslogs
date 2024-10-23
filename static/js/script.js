function validateForm() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    var errorMessage = document.getElementById('error-message');

    // Hier könntest du die Benutzerdaten überprüfen und den Login-Prozess durchführen
    // Beispiel: if (username === 'admin' && password === 'pass') { ... }
    // Andernfalls zeige die Fehlermeldung an
    if (username !== 'admin' || password !== 'superduperroot') {
        errorMessage.innerHTML = 'Falsches Passwort ;)';
        errorMessage.style.display = 'block';

        // Animation für das Wackeln hinzufügen
        var passwordInput = document.getElementById('password');
        passwordInput.style.animation = 'shake 5s ease-in-out';
        setTimeout(function() {
            passwordInput.style.animation = ''; // Animation zurücksetzen
        }, 5000);

        return false; // Verhindere das Absenden des Formulars
    }

    return true; // Erlaube das Absenden des Formulars
}