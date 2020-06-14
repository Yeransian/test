jQuery(document).ready(function() {

    console.log("custom javascript loaded");
    console.log(document.title);
    console.log(jQuery.version);
    let title = document.title;
    let index = document.getElementById("index");
    $('#send-request').click(function (){
        let firstname = $('input[id="first-name"]').val();
        let lastname = $('input[id="last-name"]').val();
        let selectedservice = $('#service-list option:selected').val();
        let phone = $('input[id="phone-number"]').val();
        let message = $('#message').val();
        console.log(firstname, lastname, selectedservice, phone, message);
        let data = {
            'first_name': firstname,
            'last_name': lastname,
            'service': selectedservice,
            'phone_number': phone,
            'message': message
        };
        console.log(data);
        $.ajax('http://127.0.0.1:5000/consultation', {
            data: data,
            type: 'POST',
            dataType: 'json'
        });
    });
});


