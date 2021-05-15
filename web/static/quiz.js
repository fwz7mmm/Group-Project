/**Global variabes */
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

/**function direct to next question */
function nextqs(){   
    /**dynamic change the question id to next question */
    n = parseInt(num);
    n = n + 1;
    var check = document.getElementById(n);
    /**check if the user finish current question choice */
    if(!radiocheck()){
        alert("Please select an answer");
    }
    /**check if question is the last question */
    else if(check == null && radiocheck()){
        /**generate all the selections from user for the entire quiz */
        generate_anwser(num);
        /**replace next button as submit button */
        openform();
        alert("This is the last question, Click submit button to finish the test.");
    }
    /**Check if the question is not the last question */
    else if(check != null && radiocheck()){
        /**update answer array */
        generate_anwser(num);
        /**hide current question */
        document.getElementById(num).style.display ='none';
        num = n;
        /**display next question */
        document.getElementById(num).style.display ='block';
    }
}

/**function to direct back to previous quesiton */
function previousqs(){
    /**if question is not the first question */
    if(num > 1){
        /**delete last answer element from answers array */
        answers.splice(-1,1);
        /**hide current question */
        document.getElementById(num).style.display ='none';
        num = num - 1;
        /**go to previous question */
        document.getElementById(num).style.display ='block';
    }else{
        alert("This is first question");
    }
}

/**function to test if radio buttons of a question has been checked */
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

/**function to add answer of current question to final answers array */
function generate_anwser(num){
    var div = document.getElementById(num);
    var qs_id = div.getAttribute("name");
    let answer = {
        "questionId": qs_id,
        "answer": selectradio
    }
    /**add answer in to array */
    answers.push(answer);
}

/**function once user finish all the question it will allow user to submit quiz answers */
function openform(){
    /**display submit button */
    document.getElementById("quiz-submit").style.display = 'block';
    /**hide questions*/
    document.getElementById("quiz-page").style.display = 'none';
    var r =JSON.stringify(answers);
    document.getElementById("answers").value=r;
}

/** function go back to quiz page */
function hideform(){
    answers.splice(-1,1);
    document.getElementById("quiz-submit").style.display = 'none';
    document.getElementById("quiz-page").style.display = 'block';
}