function openform(obj){
    document.getElementById("submit-form").style.display = 'block';
    document.getElementById("test-page").style.display = 'none';
    document.getElementById("level").value=obj.value;
    document.getElementById("topic").value=obj.parentNode.id;
}

function hideform(){
    document.getElementById("submit-form").style.display = 'none';
    document.getElementById("test-page").style.display = 'block';
}
