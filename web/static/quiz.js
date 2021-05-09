var num = "1";
let answers = [];
var selectradio = "";
var divs = document.getElementsByClassName("question-list");

/**function that hide and show first divsion when page loaded, working as onload function */
function hideDiv(){
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
    if(!radiocheck()){
        alert("Please select an answer");
    }
    else if(check == null && radiocheck()){
        generate_anwser(num);
        openform();
        alert("This is the last question, Click submit button to finish the test.");
    }
    else if(check != null && radiocheck()){
        generate_anwser(num);
        document.getElementById(num).style.display ='none';
        num = n;
        /** hide all divisions */
        //for(var i=0; i<divs.length; i++){
        //    divs[i].style.display = 'none';
        //}
        /** display first part */
        //divs[0].style.display='block';
        document.getElementById(num).style.display ='block';
    }
}

function previousqs(){
    
    if(num > 1){
        answers.splice(-1,1);
        document.getElementById(num).style.display ='none';
        num = num - 1;
        /** hide all divisions */
        //for(var i=0; i<divs.length; i++){
         //   divs[i].style.display = 'none';
        //}
        /** display first part */
        document.getElementById(num).style.display ='block';
    }else{
        alert("This is first question");
    }
}

function radiocheck(){
    if(document.getElementById(num+"A").checked)
    {
        document.getElementById(num+"A").checked = true;
        selectradio = document.getElementById(num+"A").value;
        return true;
    }
    if(document.getElementById(num+"B").checked){
        document.getElementById(num+"B").checked = true;
        selectradio = document.getElementById(num+"B").value;
        return true;
    }
    if(document.getElementById(num+"C").checked){
        document.getElementById(num+"C").checked = true;
        selectradio = document.getElementById(num+"C").value;
        return true;
    }
    if(document.getElementById(num+"D").checked){
        document.getElementById(num+"D").checked = true;
        selectradio = document.getElementById(num+"D").value;
        return true;
    }
    else{
        return false;
    }
}

function generate_anwser(num){
    var div = document.getElementById(num);
    var qs_id = div.getAttribute("name");
    let answer = {
        "questionId": qs_id,
        "answer": selectradio
    }
    answers.push(answer);
}

function openform(){
    document.getElementById("quiz-submit").style.display = 'block';
    document.getElementById("quiz-page").style.display = 'none';
    var r =JSON.stringify(answers);
    document.getElementById("answers").value=r;
}

function hideform(){
    answers.splice(-1,1);
    document.getElementById("quiz-submit").style.display = 'none';
    document.getElementById("quiz-page").style.display = 'block';
}