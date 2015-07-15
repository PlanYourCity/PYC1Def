$('document').ready(function(){

	$('#follow_me').click(function(e){

	var titulo = $('#activity_title').text();
	
	var url = "/detalle/"+titulo+"/";
	var datos = $('#formDetalle').serialize();

	$.ajax({
	  method: "POST",
	  url: url,
	  data: datos,
	  success: function(data){
	  	if(data.message == true){
	  		alertify.set('notifier','position','top-right');
			alertify.success('¡¡Siguiendo evento!!');
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