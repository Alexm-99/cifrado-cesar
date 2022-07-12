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


