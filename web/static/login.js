/** window onload function generate current data */
function windowonload(){
    birthday.max = new Date().toISOString().split("T")[0];
}

/** function close log page division*/
function closelog(){
    document.getElementById("log-page").style.display='none';
}

/**function close register division */
function closeRegister(){
    document.getElementById("register-page").style.display='none';
}

/** If all the input field pass the validation checking, the function will record all answers. */
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

    //alert(JSON.stringify(registationJson));
}

/** Name validation check*/
function InvalidName(textbox){
    /**set up regex only allow characters */
    var regular = /^[A-Za-z]+$/;

    /**update validation textbox content */
    if (textbox.value === '') {
        textbox.setCustomValidity('Entering an Name is necessary!');
    }else if (!textbox.value.match(regular)) {
        textbox.setCustomValidity('Please enter an valid name');
    }else{
        textbox.setCustomValidity('');
    }
    return true;
}

/**function check validation of password input */
function InvalidPwd(textbox){
    /**set regex require character and number with minimum 8 length */
    var regular=/^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;

    /**update validation textbox content */
    if (textbox.value === '') {
        textbox.setCustomValidity('Entering an password is necessary!');
    }else if (!textbox.value.match(regular)) {
        textbox.setCustomValidity('Please enter password Minimum eight characters, at least one letter and one number');
    }else{
        textbox.setCustomValidity('');
    }
    return true;
}
/**function check validation of email */
function InvalidEmail(textbox){
    /**set regex for email. Patter specify string before @ and after @ */
    var regular=/^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    /**update validation textbox content */
    if (textbox.value === '') {
        textbox.setCustomValidity('Entering an email is necessary!');
    }else if (!textbox.value.match(regular)) {
        textbox.setCustomValidity('Please enter valid email address');
    }else{
        textbox.setCustomValidity('');
    }
    return true;

}

/** function check the validation of phone input */
function InvalidPhone(textbox){
    /** Set regex as start with 61 and with 8 digital input*/
    var regular=/(?:\+?61)?(?:\(0\)[23478]|\(?0?[23478]\)?)\d{8}/;

    /**update validation textbox content */
    if (textbox.value === '') {
        textbox.setCustomValidity('Entering an Phone number is necessary!');
    }else if (!textbox.value.match(regular)) {
        textbox.setCustomValidity('Please enter valid AU phone number');
    }else{
        textbox.setCustomValidity('');
    }
    return true;
}

/** function check the validation of birth input */
function InvalidBirth(textbox){
    /**read user selection input from calendar */
    var birth = parseInt(textbox.value.substring(0, 4));
    /**Calculate age of user */
    var age = 2021 - birth;
    
    /**update validation textbox content */
    if (textbox.value === '') {
        textbox.setCustomValidity('Entering an Birthday is necessary!');
    }else if (age <= 12) {
        textbox.setCustomValidity('Test requirs minimum 12 years old');
    }else{
        textbox.setCustomValidity('');
    }
    return true;
}
