$('document').ready(function(){

	$('.cardEvent').mouseenter(function(){
		$(this).addClass('hoverEvento');
	});

	$('.eliminar_boton').mouseenter(function(){
		$(this).parent().parent().removeClass('hoverEvento');
	});

	$('.eliminar_boton').mouseleave(function(){
		$(this).parent().parent().addClass('hoverEvento');
	});

	$('.cardEvent').mouseleave(function(){
		$(this).removeClass('hoverEvento');
	});

	$('.cardEvent').click(function(){
		if($(this).hasClass('hoverEvento')) {

			var tituloEvento = $(this).find("h2").text();

			window.location = "http://localhost:8000/detalle/"+tituloEvento;
		}
	});

	$('.eliminar_boton').click(function(){
		$('.evento').removeClass('hoverEvento');
		if(confirm("¿Eliminar actividad?")) {
			var eventoEliminar = $(this).parent().parent();
			var url = "/listado/";
			var datos = "titulo=" + $(this).parent().parent().find("h2").text();
			$.ajax({
				method: "POST",
				url: url,
				data: datos,
				success: function(data){
					$(eventoEliminar).hide("drop", { direction: "down" }, "slow");
				}
			});
			return false;
		}
	});
});