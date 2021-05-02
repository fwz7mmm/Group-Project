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
    
    var n = parseInt(num);
    n = n + 1;
    num = n;
    var check = document.getElementById(num);
    
    if(check != null){
        var divs = document.getElementsByClassName("question-list");
        /** hide all divisions */
        for(var i=0; i<divs.length; i++){
            divs[i].style.display = 'none';
        }
        /** display first part */
        //divs[0].style.display='block';
        document.getElementById(num).style.display ='block';
    }else{
        alert("This is the last question")
    }
}

function previousqs(){
    num = num - 1;
    if(num >= 1){
        var divs = document.getElementsByClassName("question-list");
        /** hide all divisions */
        for(var i=0; i<divs.length; i++){
            divs[i].style.display = 'none';
        }
        /** display first part */
        //divs[0].style.display='block';
        document.getElementById(num).style.display ='block';
    }else{
        alert("This is first question");
    }
}