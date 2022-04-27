let btn = document.querySelector("#btn");
let sidebar = document.querySelector(".sidebar");
let searchBtn = document.querySelector(".bx bx-search");

btn.onclick = function() {
    sidebar.classList.toggle("active");
}

searchBtn.onclick = function() {
    sidebar.classList.toggle("active");
}

/* javascript for register/login page */

/* 
var x = document.getElementById("login");
var y = document.getElementById("register");
var z = document.getElementById("btnr");

function register(){
    x.style.left = "-400px";
    y.style.left = "50px"
    z.style.left = "110px"
}*/