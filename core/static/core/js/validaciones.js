//Funciones auxiliares
function mensajeError(caja, mensaje) {
    $("#" + caja).html(mensaje)
    $("#" + caja).fadeIn()
}

function noError(caja) {
    $("#" + caja).fadeOut()
}
function formatEmail(email) {
    var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    // var regex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3,4})+$/;
    return regex.test(email);
}

function formatTelefono(telefono) {
    var regex = /^\d{8,10}$/;
    return regex.test(telefono);
}

function valNombre() {
    if ($("#txtNombre").val().trim().length == 0) {
        mensajeError("errorTxt", "Ingresa tu nombre")
        return false
    }else{
        noError("errorTxt")
        return true
    }
}

function valTitulo() {
    if ($("#txtTitulo").val().trim().length == 0) {
        mensajeError("errorTxt", "Ingresa el título de la noticia")
        return false
    }else{
        noError("errorTxt")
        return true
    }
}

function valAutor() {
    if ($("#txtAutor").val().trim().length == 0) {
        mensajeError("errorTxtAut", "Ingresa el nombre del autor")
        return false
    }else{
        noError("errorTxtAut")
        return true
    }
}

function valPassword() {
    if ($("#txtPass").val().trim().length == 0) {
        mensajeError("errorPassword", "Ingresa tu contraseña")
        return false
    }else{
        noError("errorPassword")
        return true
    }
}

function valCorreo() {
    if ($("#txtCorreo").val().trim().length == 0) {
        mensajeError("errorCorreo", "Ingresa tu correo electrónico")
        return false
    } else {

        if (!formatEmail($("#txtCorreo").val())) {
            mensajeError("errorCorreo", "Correo electrónico no válido")
            return false
        }else{
            noError("errorCorreo")
            return true
        }
    }
}

function valTelefono() {
    if ($("#txtTelefono").val().trim().length != 0) {
        if (!formatTelefono($("#txtTelefono").val())) {
            mensajeError("errorTel", "Ingresar teléfono válido")
            return false
        }else{
            noError("errorTel")
            return true
        }
    }else{
        noError("errorTel")
        return true
    }
}

function valContacto(largo) {
    if ($("#txaContacto").val().trim().length < largo) {
        mensajeError("errorCaja", "Escribe tu idea en al menos " + largo + " caracteres")
        return false
    } else {
        noError("errorCaja")
        return true
    }
}


function valCategoria() {
    if ($('#cboCategoria').val().trim() === "0") {
        mensajeError("errorCat", "Selecciona una categoría para la noticia")
        return false
    }else{
        noError("errorCat")
        return true
    }
}

function valNoticia(largo) {
    if ($("#txaNoticia").val().trim().length < largo) {
        mensajeError("errorCaja", "Describe la noticia en al menos " + largo + " caracteres")
        return false
    } else {
        noError("errorCaja")
        return true
    }
}

function valDireccion() {
    if ($("#txtLugar").val().trim().length == 0) {
        mensajeError("errorTxtDir", "Ingresa el lugar de los hechos")
        return false
    }else{
        noError("errorTxtDir")
        return true
    }
}

function recuperaContraseña(){
    alert("Se ha enviado un link a su correo para restablecer contraseña")
}



$(document).ready(function () {
    /*Configuración inicial del formulario*/

    //Todos los mensajes de error ocultos
    $(".invalid-feedback").hide()

    //Validar Nombre
    $("#txtNombre").blur(function () {
        exito = valNombre()
    });

    //Validar Título Noticia
    $("#txtTitulo").blur(function () {
        exito = valTitulo()
    });

    //Validar Nombre
    $("#txtAutor").blur(function () {
        exito = valAutor()
    });

    //Validar Nombre
    $("#txtPass").blur(function () {
        exito = valPassword()
    });

    //Validar Email
    $("#txtCorreo").blur(function () {
        exito = valCorreo()
    });

    //Validar Telefono
    $("#txtTelefono").blur(function () {
        exito = valTelefono()
    });

    //Validar Comentarios
    $("#txaContacto").blur(function () {
        exito = valContacto(20)
    });

    $("#txaContacto").keyup(function () {
        var totalcaracteres = $("#txaContacto").val().trim().length
        $("#contChar").text(totalcaracteres)
    });

    //Validar Noticia
    $("#txaNoticia").blur(function () {
        exito = valNoticia(100)
    });

    $("#txaNoticia").keyup(function () {
        var totalcaracteres = $("#txaNoticia").val().trim().length
        $("#contChar").text(totalcaracteres)
    });

    //Validar Categoría Noticia
    $("#cboCategoria").change(function () {
        exito = valCategoria()
    });

    //Validar Nombre
    $("#txtLugar").blur(function () {
        exito = valDireccion()
    });

    //Click en botón reset
    $('button[type="reset"]').click(function () {
        $('#fsId').prop('disabled', true)
        //Todos los mensajes de error ocultos
        $(".invalid-feedback").hide()
    });

    //Envío de formulario Contacto
    $("#formContacto").submit(function () {
        exito = false
        
        if (
            !valNombre() ||
            !valCorreo() ||
            !valTelefono() ||
            !valContacto(20)
        ) {
            event.preventDefault()
        }

    });

    //Envío de formulario Noticia
    $("#formNoticia").submit(function () {
        exito = false
        
        if (
            !valTitulo() ||
            !valAutor() ||
            !valCategoria() ||
            !valNoticia(100) ||
            !valDireccion ()
        ) {
            event.preventDefault()
        }

    });

    //Envío de formulario Creación Usuario
    $("#formCreaUsuario").submit(function () {
        exito = false
        
        if (
            !valNombre() ||
            !valCorreo() ||
            !valPassword()
        ) {
            event.preventDefault()
        }

    });

    //Envío de formulario Login
    $("#formLogin").submit(function () {
        exito = false
        
        if (
            !valCorreo() ||
            !valPassword()
        ) {
            event.preventDefault()
        }

    });

    //Envío de formulario Recuperar Contraseña
    $("#formPass").submit(function () {
        exito = false
        
        if (
            !valCorreo()
        ) {
            event.preventDefault()
        }

    });
});