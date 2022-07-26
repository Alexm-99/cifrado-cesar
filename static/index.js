function datos(){
    let person = prompt("Ingrese un nombre o apodo", "Anónimo");

    if (person != null) {
     $('#apodo').attr('value', person ); //Cambiando valor a mostrar
    }else{
        $('#apodo').attr('value', "Anónimo" ); //Cambiando valor a mostrar
    }
    
    do {
        let clave = prompt("Ingrese la clave entre 1 a 26", "10");
        $('#clave').attr('value', clave ); //Cambiando valor a mostrar
    } while (clave<=26 && clave > 0);
}
function PostMenu(){
    datos();     
    // $('#formularioCifrado').attr('action', `{% url 'index' %}` ); //Cambiando valor a mostrar

 document.getElementById("formularioCifrado").submit();

 }

 function consulta(id){
    document.getElementById(id).submit();
 }

function envioclave(id){
    let clave =prompt("Ingrese la clave");
 
    if (clave != null ) {
    $(`#${id}`).attr('value', clave ); //Cambiando valor a mostrar
        
    }else{
        alert("No ingreso ninguna clave");
    }
}
function timeDC(llave, id){
    if(llave=="1"){
        inicio();
        // window.location.href = `/delete/${id}`;
    // $(`#envio`).attr('action', `{% url 'delete' ${id} %}` ); //Cambiando valor a mostrar
        // alert("xdddd");
      
    }

}
function paddedFormat(num) {
    return num < 10 ? "0" + num : num; 
}

function startCountDown(duration, element) {

    let secondsRemaining = duration;
    let min = 0;
    let sec = 0;

    let countInterval = setInterval(function () {

        min = parseInt(secondsRemaining / 60);
        sec = parseInt(secondsRemaining % 60);

        element.textContent = `${paddedFormat(min)}:${paddedFormat(sec)}`;

        secondsRemaining = secondsRemaining - 1;
        if (secondsRemaining < 0) { clearInterval(countInterval) ;  document.getElementById("envio").submit()};

    }, 1000);
}

function inicio() {
    let time_minutes = 0; // Value in minutes
    let time_seconds = 10; // Value in seconds

    let duration = time_minutes * 60 + time_seconds;

    element = document.querySelector('#count-down-timer');
    element.textContent = `${paddedFormat(time_minutes)}:${paddedFormat(time_seconds)}`;

    startCountDown(--duration, element);
};