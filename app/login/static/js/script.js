document.getElementById('register_btn').addEventListener('click', async function (event) {
    event.preventDefault();
    let firstname = document.getElementById('firstname').value;
    let lastname = document.getElementById('lastname').value;
    let email = document.getElementById('email').value;
    let mobile = document.getElementById('mobile').value;
    let address_line1 = document.getElementById('address_line1').value;
    let address_line2 = document.getElementById('address_line2').value;
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;
    let cnf_password = document.getElementById('confirm_password').value;
    let checkbox = document.getElementById('is_admin');
    let is_admin = '0'
    if (checkbox.checked) {
        is_admin = '1'
    } else {
        is_admin = '0'
    }

    const formData = new FormData();
    formData.append('firstname', firstname);
    formData.append('lastname', lastname);
    formData.append('email', email);
    formData.append('mobile', mobile);
    formData.append('address_line1', address_line1);
    formData.append('address_line2', address_line2);
    formData.append('username', username);
    formData.append('password', password)
    formData.append('confirm_password', cnf_password)
    formData.append('is_admin', is_admin)

    fetch(postDataUrl, {
        method: 'POST',
        body: formData

    })
        .then(response => response.json())
        .then(data => {
            window.location.href = goToLogin;
            console.log('Success:', data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
});