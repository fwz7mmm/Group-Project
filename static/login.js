function windowonload(){
    birthday.max = new Date().toISOString().split("T")[0];
}

function closelog(){
    document.getElementById("log-page").style.display='none';
}

function closeRegister(){
    document.getElementById("register-page").style.display='none';
}

function SucRegister(){
    var username=document.getElementById("username").value;
    var password=document.getElementById("psw").value;
    var email=document.getElementById("email").value;
    var birthday=document.getElementById("birthday").value;
    var phone=document.getElementById("phone").value;

    var registationJson = {
        Username: username,
        Password: password,
        Email: email,
        Phone: phone,
        Birthday: birthday 
    };

    alert(JSON.stringify(registationJson));
}

function InvalidName(textbox){
    var regular = /^[A-Za-z]+$/;

    if (textbox.value === '') {
        textbox.setCustomValidity('Entering an Name is necessary!');
    }else if (!textbox.value.match(regular)) {
        textbox.setCustomValidity('Please enter an valid name');
    }else{
        textbox.setCustomValidity('');
    }
    return true;
}

function InvalidPwd(textbox){
    var regular=/^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;

    if (textbox.value === '') {
        textbox.setCustomValidity('Entering an password is necessary!');
    }else if (!textbox.value.match(regular)) {
        textbox.setCustomValidity('Please enter password Minimum eight characters, at least one letter and one number');
    }else{
        textbox.setCustomValidity('');
    }
    return true;
}

function InvalidEmail(textbox){
    var regular=/^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

    if (textbox.value === '') {
        textbox.setCustomValidity('Entering an email is necessary!');
    }else if (!textbox.value.match(regular)) {
        textbox.setCustomValidity('Please enter valid email address');
    }else{
        textbox.setCustomValidity('');
    }
    return true;

}

function InvalidPhone(textbox){
    var regular=/(?:\+?61)?(?:\(0\)[23478]|\(?0?[23478]\)?)\d{8}/;

    if (textbox.value === '') {
        textbox.setCustomValidity('Entering an Phone number is necessary!');
    }else if (!textbox.value.match(regular)) {
        textbox.setCustomValidity('Please enter valid AU phone number');
    }else{
        textbox.setCustomValidity('');
    }
    return true;
}

function InvalidBirth(textbox){
    
    var birth = parseInt(textbox.value.substring(0, 4));
    var age = 2021 - birth;
    
    if (textbox.value === '') {
        textbox.setCustomValidity('Entering an Birthday is necessary!');
    }else if (age <= 12) {
        textbox.setCustomValidity('Test requirs minimum 12 years old');
    }else{
        textbox.setCustomValidity('');
    }
    return true;
}