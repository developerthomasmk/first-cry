function addUser() {
    document.getElementById('register_btn').addEventListener('click', async function (event) {
        event.preventDefault();
        let username = document.getElementById('username').value;
        let password = document.getElementById('password').value;
        let cnf_password = document.getElementById('confirm_password').value;

        try {
            let response = await fetch("{{url_for(login.addUser)}}", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ username: username, password: password, confirm_password: cnf_password})
            });

            if (response.ok) {
                let result = await response.json();
                if (result.success) {
                    // User added successfully, redirect to next page
                    window.location.href = "{{ url_for('login.go_to_home') }}";
                } else {
                    alert('Failed to add user: ' + result.error);
                }
            } else {
                alert('Failed to add user');
            }
        } catch (error) {
            console.error('Error adding user:', error);
        }
    });
}

