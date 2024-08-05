/*
add a new element to  connection
remove the current element from request
update to count subtract -1
update connection count by one if the person is add to the connection
add a new li element to connections
*/
var requestNum = 2;
var connectNum = 418;
function addRequest(element){
    var count = document.querySelector("#count1");
    var connectAdd = document.querySelector(".bottom-info");
    var count_connect = document.querySelector(".count2");
    count.innerHTML=requestNum -1;
    count_connect.innerHTML =connectNum +1;
    //add a new element to  connection
    var newLi = document.createElement('li');
    newLi.innerHTML="Adom";
    element.remove("#person1");
}

function removeRequest(element){
    var count = document.querySelector("#count2");
    var connectAdd = document.querySelector(".bottom-info");
        count.innerHTML=connectNum + 1;
}