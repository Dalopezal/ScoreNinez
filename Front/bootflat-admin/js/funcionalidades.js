const HOST_REQUEST = "http://localhost:8088/"

function saveData() {
    let age = document.getElementById('age').value;
    let departament = document.getElementById('departament').value;
    let town = document.getElementById('town').value;
    localStorage.setItem('age', age);
    localStorage.setItem('departament', departament);
    localStorage.setItem('town', town);

    let dimension = document.getElementById('dimension').value;

    if (dimension==='material'){
        material();
    }

}


document.getElementById('calc').onclick = saveData;


function material(){
    /**
     * get values from the form material
     */
    let age = document.getElementById('age').value;
    let departament = document.getElementById('departament').value;
    let town = document.getElementById('town').value;
    let dimension = document.getElementById('dimension').value;
    let rooms = document.getElementById('rooms').value;
    let total_people = document.getElementById('total_people').value;
    let income = document.getElementById('income').value;
    let public_service = document.getElementById('public_service').value;

    let data = {
        age: age,
        departament: departament,
        town: town,
        dimension: dimension,
        rooms: rooms,
        total_people: total_people,
        income: income,
        public_service: public_service
    };

    console.log(data);

    let result = postAjax(HOST_REQUEST + 'bienestar-material', data, function (data) {
        console.log(data);
    });

}



function postAjax(url, data, success) {
    var params = typeof data == 'string' ? data : Object.keys(data).map(
            function(k){ return encodeURIComponent(k) + '=' + encodeURIComponent(data[k]) }
        ).join('&');

    var xhr = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject("Microsoft.XMLHTTP");
    xhr.open('POST', url);
    xhr.onreadystatechange = function() {
        if (xhr.readyState>3 && xhr.status===200) { success(xhr.responseText); }
    };
    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    //xhr.setRequestHeader('Access-Control-Allow-Origin', 'http://localhost:8000');
    //xhr.setRequestHeader('Allow-Headers', 'X-Requested-With, Content-Type, Accept, Origin');
    xhr.send(params);
    return xhr;
}

document.addEventListener('DOMContentLoaded', function () {
    if (localStorage.getItem('age') && localStorage.getItem('departament') && localStorage.getItem('town')) {

        $("#age").val(localStorage.getItem('age')).trigger("change");
        $("#departament").val(localStorage.getItem('departament')).trigger("change");
        $("#town").val(localStorage.getItem('town')).trigger("change");
    }
});


