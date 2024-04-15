function saveData() {
    let age = document.getElementById('age').value;
    let departament = document.getElementById('departament').value;
    let town = document.getElementById('town').value;
    localStorage.setItem('age', age);
    localStorage.setItem('departament', departament);
    localStorage.setItem('town', town);
}


document.getElementById('calc').onclick = saveData;


document.addEventListener('DOMContentLoaded', function () {
    if (localStorage.getItem('age') && localStorage.getItem('departament') && localStorage.getItem('town')) {

        $("#age").val(localStorage.getItem('age')).trigger("change");
        $("#departament").val(localStorage.getItem('departament')).trigger("change");
        $("#town").val(localStorage.getItem('town')).trigger("change");
    }
});


