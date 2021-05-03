var num = "1";

/**function that hide and show first divsion when page loaded, working as onload function */
function hideDiv(){
    var divs = document.getElementsByClassName("question-list");
    /** hide all divisions */
    for(var i=0; i<divs.length; i++){
        divs[i].style.display = 'none';
    }
    /** display first part */
    document.getElementById("1").style.display ='block';
}

function nextqs(){
    n = parseInt(num);
    n = n + 1;
    var check = document.getElementById(n);
    if(radiocheck()==false){
        alert("Please select an answer");
    }
    else if(check != null && radiocheck()){
        num = n;
        var divs = document.getElementsByClassName("question-list");
        /** hide all divisions */
        for(var i=0; i<divs.length; i++){
            divs[i].style.display = 'none';
        }
        /** display first part */
        //divs[0].style.display='block';
        document.getElementById(num).style.display ='block';
    }
    else{
        document.getElementById("next").style.display ='none';
        document.getElementById("submit-input").style.display ='block';
        alert("This is the last question, Click submit button to finish the test.");
    }
}

function previousqs(){
    
    if(num > 1){
        num = num - 1;
        var divs = document.getElementsByClassName("question-list");
        /** hide all divisions */
        for(var i=0; i<divs.length; i++){
            divs[i].style.display = 'none';
        }
        /** display first part */
        //divs[0].style.display='block';
        document.getElementById(num).style.display ='block';
        document.getElementById("next").style.display ='block';
        document.getElementById("submit-input").style.display ='none';
    }else{
        alert("This is first question");
    }
}

function radiocheck(){
    var div = document.getElementById(num);
    if(document.getElementById(num+"A").checked)
    {
        document.getElementById(num+"A").checked = true;
        return true;
    }
    if(document.getElementById(num+"B").checked){
        document.getElementById(num+"B").checked = true;
        return true;
    }
    if(document.getElementById(num+"C").checked){
        document.getElementById(num+"C").checked = true;
        return true;
    }
    if(document.getElementById(num+"D").checked){
        document.getElementById(num+"D").checked = true;
        return true;
    }
    else{
        return false;
    }
}