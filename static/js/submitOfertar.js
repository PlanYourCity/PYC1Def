$('document').ready(function(){/*

	/*VALIDACION CAMPO DE TEXTO*//*
	function caracteresEspeciales(valInput, name){
 		var regex = /[\$\%\&\(\)\=\¿\?\*\^\{\}\_\-\"\'\<\>]/g;

 		if(regex.test(valInput)){
 			$('#formOfertar input[name="'+name+'"] ~ .msgError').text("* Campo erroneo");
			$('#formOfertar input[name="'+name+'"]').css('box-shadow','0px 0px 5px red');
			$('#formOfertar input[name="'+name+'"] ~ .msgError').animate({
				opacity: 1
			}, 
			1000);
 		}else{
 			$('#formOfertar input[name="'+name+'"]').css('box-shadow','0px 0px 0px red');
			$('#formOfertar input[name="'+name+'"] ~ .msgError').animate({
				opacity: 0
			}, 
			1000,
			function(){$('#formOfertar input[name="'+name+'"] ~ .msgError').text("");}
			);
 		}

	}

	/*VALIDACION DE CAMPO OBLIGATORIO*//*
	function campoVacio(valInput, name){
		
		if(valInput === ''){
			$('#formOfertar input[name="'+name+'"] ~ .msgError').text("* Campo requerido");
			$('#formOfertar input[name="'+name+'"]').css('box-shadow','0px 0px 5px red');
			$('#formOfertar input[name="'+name+'"] ~ .msgError').animate({
				opacity: 1
			}, 
			1000);
		}else{
			caracteresEspeciales(valInput, name);
		}

	}

	/*EVENTO PARA COMPROBAR CAMPO*//*
	$('#formOfertar input').blur(function(){
		var valInput = $(this).val();
		var name = $(this).attr("name");

		campoVacio(valInput, name);
		
	});*/

	$('#buttonForm').click(function(e){
		alert("hola");
		var error = $('.msgError').text();
		error="";

		if(error == ""){
			var url = "/ofertar/"+$('input[type="hidden"]').val()+"/";
			var img = "&Imagen="+$('input[type="file"]').val();
			var datosForm = $('#formOfertar').serialize();
			alert(datosForm);

			$.ajax({
			  method: "POST",
			  url: url,
			  data: datosForm+img,
			  success: function(data){
			  	alert("hola2");
			  	if(data.message == true){
			  		alert("hola3");
			  		alertify.set('notifier','position','top-right');
					alertify.success('¡¡Evento registrado!!');
			  	}
			  	else{
			  		alert("error");
			  		alertify.set('notifier','position','top-right');
					alertify.error('¡¡El evento ya existe!!');
			  	}
			  }
			});

			return false;
		}

		return false;	
	});
		
});