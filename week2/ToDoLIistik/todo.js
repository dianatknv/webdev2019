var cnt = 0;
function checkboxClicked(className){

    let ch = document.body.getElementsByClassName("check " + className)[0];
    if(ch.checked == true){
        document.body.getElementsByClassName("taskText " + className)[0].setAttribute("style","text-decoration: line-through;");
    }else{
        document.body.getElementsByClassName("taskText " + className)[0].setAttribute("style","text-decoration: none;");

    }
}
function erase(className){
    document.body.removeChild(document.body.getElementsByClassName("tasks " + className)[0]);

}
function buttonClicked(e){

    cnt++;

    let task = document.getElementById("text");
    if(task.value == ""){
        alert("Type something to add");
    }else{
    
        let div = document.createElement("div");
        div.className = "tasks " + cnt;
    
        let checkbox = document.createElement("input");
        checkbox.setAttribute("type","checkbox");
        checkbox.className = "check " + cnt;
        checkbox.setAttribute("onclick",`checkboxClicked(${checkbox.className.split(' ')[1]})`);

    
        let taskText = document.createElement("label");
        taskText.textContent = task.value;
        taskText.className = "taskText " + cnt;
    
        let img = document.createElement("img");
        img.src = "trash.png";
        img.className = "rubbish " + cnt;
        img.setAttribute("onclick",`erase(${img.className.split(' ')[1]})`);
    
    
        div.appendChild(checkbox);
        div.appendChild(taskText);
        div.appendChild(img);
    
        document.body.appendChild(div);
 
        task.value  = "";
    
    }
    

}