jQuery(document).ready(function() {

    console.log("custom javascript loaded");
    console.log(document.title);
    console.log(jQuery.version);
    let title = document.title;
    let index = document.getElementById("index");
    $('#send-request').click(function (){
        let name = $('input[id="name"]').val();
        let email = $('input[id="email"]').val();
        let subject = $('input[id="subject"]').val();
        let message = $('#message').val();
        console.log(name, email, subject, message);
        let data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        };
        console.log(data);
        $.ajax('http://127.0.0.1:5000/send_contact', {
            data: data,
            type: 'POST',
            dataType: 'json'
        });
        alert("Your message has been sent! We will be in touch.")
    });
});


