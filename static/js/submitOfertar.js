$('document').ready(function(){

	/*VALIDACION CAMPO DE TEXTO*/
	function caracteresEspeciales(valInput, name, type){
 		var regex = /[\$\%\&\(\)\=\¿\?\*\^\{\}\_\-\"\'\<\>]/g;

 		if(regex.test(valInput)){
 			if(type == "textarea"){
 				$('textarea ~ .msgError').text("* Campo erroneo");
				$('textarea').css('box-shadow','0px 0px 5px red');
				$('textarea ~ .msgError').animate({
					opacity: 1
				}, 
				1000);
 			}else{
	 			$('#formOfertar input[name="'+name+'"] ~ .msgError').text("* Campo erroneo");
				$('#formOfertar input[name="'+name+'"]').css('box-shadow','0px 0px 5px red');
				$('#formOfertar input[name="'+name+'"] ~ .msgError').animate({
					opacity: 1
				}, 
				1000);
			}

 		}else{
 			if(type == "textarea"){
 				$('textarea').css('box-shadow','0px 0px 0px red');
				$('textarea ~ .msgError').animate({
					opacity: 0
				}, 
				1000,
				function(){$('textarea ~ .msgError').text("");}
				);
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

	}

	/*VALIDACION DE CAMPO OBLIGATORIO*/
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

	/*EVENTO PARA COMPROBAR CAMPO*/
	$('#formOfertar input, textarea').blur(function(){
		var valInput = $(this).val();
		var name = $(this).attr("name");
		var type = $(this).prop('tagName').toLowerCase();

		if(type == "input"){
			campoVacio(valInput, name);
		}else{
			caracteresEspeciales(valInput, name, type)
		}
		
	});

	$('#buttonForm').click(function(e){

		var error = $('.msgError').text();

		if(error == ""){
			var url = "/ofertar/"+$('input[type="hidden"]').val()+"/";
			var img = "&Imagen="+$('input[type="file"]').val();
			var datosForm = $('#formOfertar').serialize();

			$.ajax({
			  method: "POST",
			  url: url,
			  data: datosForm+img,
			  success: function(data){
			  	if(data.message == true){
			  		alertify.set('notifier','position','top-right');
					alertify.success('¡¡Evento registrado!!');
					$('#formOfertar')[0].reset();
			  	}
			  	else{
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