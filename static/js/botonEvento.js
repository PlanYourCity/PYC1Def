$('document').ready(function(){

	$('.demo-card-wide').mouseenter(function(){
		$(this).addClass('hoverEvento');
	});

	$('.eliminar_div').mouseenter(function(){
		$(this).parent().removeClass('hoverEvento');
	});

	$('.eliminar_div').mouseleave(function(){
		$(this).parent().addClass('hoverEvento');
	});

	$('.demo-card-wide').mouseleave(function(){
		$(this).removeClass('hoverEvento');
	});

	$('.demo-card-wide').click(function(){
		if($(this).hasClass('hoverEvento')) {

			var a = $(this).find("h2").text();
			alert(a);

			window.location = "http://localhost:8000/detalle/"+a;
		}
	});

	$('.eliminar_boton').click(function(){
		$('.evento').removeClass('hoverEvento');
		if(confirm("¿Eliminar actividad?")) {
			var eventoEliminar = $(this).parent().parent();
			var url = "/listado/";
			var datos = "titulo=" + $(this).parent().parent().find("h3").text();
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