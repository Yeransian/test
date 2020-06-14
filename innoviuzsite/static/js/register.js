jQuery(document).ready(function() {

    console.log("custom javascript loaded");
    console.log(document.title);
    console.log(jQuery.version);
    let title = document.title;
    let index = document.getElementById("index");
    $('#register-btn').click(function (){
        let username = $('input[id="username"]').val();
        let email = $('input[id="email"]').val();
        let password = $('input[id="password"]').val();
        let confirmpassword = $('input[id="confirmpassword"]').val();
        console.log(username, email, password, confirmpassword);
        let data = {
            'username': username,
            'email': email,
            'password': password,
            'confirmpassword': confirmpassword
        };
        console.log(data);
        $.ajax('http://127.0.0.1:5000/new_user', {
            data: data,
            type: 'POST',
            dataType: 'json'
        });
        alert("Your message has been sent! We will be in touch.")
    });
});


