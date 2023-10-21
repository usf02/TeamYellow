function submitForm() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirmPassword").value;
    const usernameError = document.getElementById("usernameError");
    const passwordError = document.getElementById("passwordError");
    const confirmPasswordError = document.getElementById("confirmPasswordError");

    // Clear any previous error messages
    usernameError.innerText = "";
    passwordError.innerText = "";
    confirmPasswordError.innerText = "";

    let isValid = true;

    // Check username
    if (username.length < 3) {
        usernameError.innerText = "Username must be at least 3 characters.";
        isValid = false;
    }

    // Check password
    if (password.length < 6) {
        passwordError.innerText = "Password must be at least 6 characters.";
        isValid = false;
    }

    // Check password confirmation
    if (password !== confirmPassword) {
        confirmPasswordError.innerText = "Passwords do not match.";
        isValid = false;
    }

    if (isValid) {
        // If all validation passes, proceed to submit the form to the server
        const userData = {
            username: username,
            password: password
        };

        // Send the data to the backend (Python server) using fetch
        fetch('/createUser', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(userData)
        })
        .then(response => {
            console.log("Response status:", response.status);
            return response.json();
        })
        .then(data => {
            document.getElementById("message").innerText = data.message;
        })
        .catch(error => {
            console.error(error);
            document.getElementById("message").innerText = "An error occurred while processing your request.";
        });
    }
}
