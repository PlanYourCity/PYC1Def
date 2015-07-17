$('document').ready(function(){

	$('#follow_me').click(function(e){

		var titulo = $('#activity_title').text();
		
		var url = "/detalle/"+titulo+"/";
		var datos = $('#formDetalle').serialize();
		var textoBoton = $(this).text();

		if(textoBoton === "¡Sígueme!"){
			var accion = "follow";
		}else{
			var accion = "unfollow";
		}

		$.ajax({
		  method: "POST",
		  url: url,
		  data: datos+"&action="+accion,
		  success: function(data){
		  	if(data.message == true){
		  		if(textoBoton === "¡Sígueme!"){
					$("#follow_me").animate({
						backgroundColor: "red"
					},500);
					$("#follow_me").text("Dejar de seguir");
				}else{
					$("#follow_me").animate({
						backgroundColor: "#2E6EA5"
					},500);
					$("#follow_me").text("¡Sígueme!");
				}
		  	}
		  	else{
		  		alertify.set('notifier','position','top-right');
				alertify.error('Se ha producido un error');
		  	}
		  }
		});

		return false;

	});
	
});