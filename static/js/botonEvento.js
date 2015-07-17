$('document').ready(function(){

	$('.evento').mouseenter(function(){
		$(this).addClass('hoverEvento');
	});

	$('.eliminar_div').mouseenter(function(){
		$('.evento').removeClass('hoverEvento');
	});

	$('.eliminar_div').mouseleave(function(){
		$('.evento').addClass('hoverEvento');
	});

	$('.evento').mouseleave(function(){
		$(this).removeClass('hoverEvento');
	});

	$('.evento').click(function(){
		if($(this).hasClass('hoverEvento')) {

			var a = $(this).find("h3").text();

			window.location = "http://localhost:8000/detalle/"+a;
		}
	});

	$('.eliminar_boton').click(function(){
		$('.evento').removeClass('hoverEvento');
		if(confirm("¿Eliminar actividad?")) {
			var eventoEliminar = $(this).parent().parent();
			$(eventoEliminar).hide("drop", { direction: "down" }, "slow");
			var url = "/listado/";
			var datos = "titulo=" + $(this).parent().parent().find("h3").text();
			$.ajax({
				method: "POST",
				url: url,
				data: datos,
				success: function(data){
					if(data.message==true){

					}
				}
			});
			return false;
		}
	});
});