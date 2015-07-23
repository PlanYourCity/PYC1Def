$('document').ready(function() {

    /*DATEPICKER PARA LA FECHA*/
    $( ".calendar" ).datepicker({
        showOn: "button",
        buttonImage: "/static/images/iconos/calendar.svg",
        altField: "input[name='Fecha']"
    });

    $.datepicker.regional['es'] = {
        closeText: 'Cerrar',
        prevText: '<Ant',
        nextText: 'Sig>',
        currentText: 'Hoy',
        monthNames: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        monthNamesShort: ['Ene','Feb','Mar','Abr', 'May','Jun','Jul','Ago','Sep', 'Oct','Nov','Dic'],
        dayNames: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'],
        dayNamesShort: ['Dom','Lun','Mar','Mié','Juv','Vie','Sáb'],
        dayNamesMin: ['Do','Lu','Ma','Mi','Ju','Vi','Sá'],
        weekHeader: 'Sm',
        dateFormat: 'dd/mm/yy',
        firstDay: 1,
        isRTL: false,
        showMonthAfterYear: false,
        yearSuffix: '',
        minDate: 0
    };
    $.datepicker.setDefaults($.datepicker.regional['es']);
});

function rellenarCiudad(element) {
    $('#provincia').val($(element).text());
    $('#provinciaBD').attr("value",$(element).attr("value"));
    }

