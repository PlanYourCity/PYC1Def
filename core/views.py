from django.contrib import auth
from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.template.loader import get_template
from core.models import ActOcio
from core.models import ActVivienda
from core.models import ActEmpleo
from django.template import Context
from django.contrib.auth.decorators import login_required

import json

# Create your views here.
#def Detalles(request):

def home(request):
   return render(request, 'home.html')

@login_required
def inicio(request):
	template = get_template("base.html")				
	return HttpResponse(template.render(Context()))	

@login_required
def lista_eventos(request):

	if request.user.is_authenticated():
		if request.method == "GET":
			record_ocio=""
			record_viv=""
			record_emp=""
			try:		
				record_ocio=ActOcio.objects.filter(Usuario_owner=request.user)
			except:
				print ("No actividades de ocio")

			try:		
				record_viv=ActVivienda.objects.filter(Usuario_owner=request.user)
			except:
				print ("No actividades de vivienda")

			try:		
				record_emp=ActEmpleo.objects.filter(Usuario_owner=request.user)
				print(record_emp)
			except:
				print ("No actividades de Empleo")

			template = get_template("listado_mis_actividades.html")		
			diccionario = {'record_ocio':record_ocio,'record_viv':record_viv,'record_emp':record_emp}	

			return HttpResponse(template.render(Context(diccionario)))

@login_required
def detalle(request, titulo):

	categoria=""
	Imag=""

	Act_ocio=ActOcio.objects.all()
	Act_viv=ActVivienda.objects.all()
	Act_Emp=ActEmpleo.objects.all()

	for i in Act_ocio:

		if titulo==i.Titulo:

			categoria="ocio"
			Tit=i.Titulo
			Imag=i.Imagen
			Prec=i.Precio
			Dirr=i.Direccion
			Hour=i.Hora
			Descri=i.Descripcion
			Afor= i.Aforo_Max
			fecha=i.Fecha
			diccionario = {'categoria':categoria,'titulo':Tit,'imagen':Imag,'precio':Prec,'direccion':Dirr,'hora':Hour,'descripcion':Descri,'aforo':Afor,'fecha':fecha}
	for i in Act_viv:

		if titulo==i.Titulo:

			categoria="vivienda"
			Tit=i.Titulo
			imag=i.Imagen
			prec=i.Precio
			Dirr=i.Direccion
			num_habt=i.NumHab
			Descri=i.Descripcion
			Toferta= i.TipoOferta
			diccionario = {'categoria':categoria,'titulo':Tit,'imagen':Imag,'precio':prec,'direccion':Dirr,'num_habt':num_habt,'descripcion':Descri,'Toferta':Toferta}		

	for i in Act_Emp:
		if titulo==i.Titulo:
			categoria="empleo"
			Tit=i.Titulo
			Imag="empleo.png"
			Sueldo=i.Sueldo
			Dirr=i.Direccion
			Periodo=i.Periodo
			Descri=i.Descripcion
			Plazas= i.Plazas
			diccionario = {'categoria':categoria,'titulo':Tit,'imagen':Imag,'Sueldo':Sueldo,'direccion':Dirr,'Periodo':Periodo,'descripcion':Descri,'Plazas':Plazas}		

	template = get_template("detalle_ocio.html")	
	return HttpResponse(template.render(Context(diccionario)))				


@login_required
def ofertar(request,categoria):


	if request.method=="GET":		
										
		template = get_template("form_ofertar.html")		
		diccionario = {'categoria':categoria}		
		return HttpResponse(template.render(Context(diccionario)))

	elif request.method == "POST":
		respuesta = {}			
		ciuda=request.POST['Ciudad']
		direccio=request.POST['Direccion']
		titul=request.POST['Titulo']
		descripcio=request.POST['Descripcion']	
		
		if categoria=="ocio":
				
			image=request.POST['Imagen']
			#ruta_imga="../../static/images/"

			preci=request.POST['Precio']
			fech=request.POST['Fecha']	
			hor=request.POST['Hora']	
			aforo_ma=request.POST['Aforo_Max']	
			propietari=request.user

			try:
				record=ActOcio.objects.get(Titulo=titul)
				response = {'message': False}
			except:
				Nueva_actividad_ocio=ActOcio(Ciudad=ciuda,Direccion=direccio,Titulo=titul,Descripcion=descripcio,Imagen=image,Precio=preci,Fecha=fech,Hora=hor,Aforo_Max=aforo_ma,Usuario_owner=propietari)
				Nueva_actividad_ocio.save()
				response = {'message': True}			
			#return HttpResponseRedirect("/ofertar/ocio")
			return HttpResponse(json.dumps(response), content_type="application/json")
		elif categoria=="vivienda":
			imagen=request.POST['Imagen']
			precio=request.POST['Precio']
			nhabit=request.POST['NumHab']	
			toferta=request.POST['TipoOferta']		
			propietario=request.user
			try:
				record=ActVivienda.objects.get(Titulo=titul)
				response = {'message': False}
			except:
				Nueva_vivienda=ActVivienda(Ciudad=ciuda,Direccion=direccio,Titulo=titul,Descripcion=descripcio,Imagen=imagen,Precio=precio,NumHab=nhabit,TipoOferta=toferta,Usuario_owner=propietario)
				Nueva_vivienda.save()
				response = {'message': True}
			#return HttpResponseRedirect("/ofertar/vivienda")
			return HttpResponse(json.dumps(response), content_type="application/json")

		elif categoria=="empleo":
			sueldo=request.POST["Sueldo"]
			periodo=request.POST["Periodo"]	
			plazas=request.POST["Plazas"]	
			propietario=request.user

			try:
				record=ActEmpleo.objects.get(Titulo=titul)
				response = {'message': False}
			except:

				Nueva_Empleo=ActEmpleo(Ciudad=ciuda,Direccion=direccio,Titulo=titul,Descripcion=descripcio,Sueldo=sueldo,Periodo=periodo,Plazas=plazas,Usuario_owner=propietario)
				Nueva_Empleo.save()
				response = {'message': True}			
			#return HttpResponseRedirect("/ofertar/empleo")
			return HttpResponse(json.dumps(response), content_type="application/json")
		#else
			#except:
			#canal="<h1> la url del canal introducido no es valida</h1>"
			#template = get_template("configurar_canales.html")
			#diccionario = {'css_user':css,'usuario':enlace,'canal':canal}
			#return HttpResponse(template.render(Context(diccionario)))

@login_required
def buscar(request,categoria):

	if request.method=="GET":		
									
		template = get_template("busqueda.html")		
		diccionario = {'categ':categoria}		
		return HttpResponse(template.render(Context(diccionario)))


	elif request.method == "POST":			
					
		ciudad=str(request.POST['provincia'])
		titulo=str(request.POST['titulo'])

		if categoria=="ocio":	
			precio=str(request.POST['precio'])
			fechaDesde=str(request.POST['fDesde'])
			fechaHasta=str(request.POST['fHasta'])
			aforo=str(request.POST['aMax'])
			direc= str(request.POST['direccion'])
			record=ActOcio.objects.all()
			
			if titulo!="":
				record=record.filter(Titulo__contains = titulo)
			if ciudad != "":
				record=record.filter(Ciudad=ciudad)
			if precio != "":
				record=record.filter(Precio=precio)
			if fechaDesde != "":
				record=record.filter(Fecha__gt=fechaDesde)
			if fechaHasta != "":
				record=record.filter(Fecha__lt=fechaHasta)
			if aforo != "":
				record=record.filter(Aforo_Max=aforo)
			if direc != "":
				record=record.filter(Direccion__contains=direc)

			if record != []:
				template = get_template("listado.html")		
				diccionario = {'record':record,'categoria':categoria}	
				return HttpResponse(template.render(Context(diccionario)))

			else:
				print("estoy aqui")
				template = get_template("listado.html")		
				return HttpResponse(template.render(Context("No existe actividad que cumpla los requisitos")))


		if categoria=="vivienda":	
			record=""
			precio=str(request.POST['precio'])
			numHab=str(request.POST['nHabit'])
			tipoOfer=str(request.POST["tipo"])
			direc= str(request.POST['direccion'])
			record=ActVivienda.objects.all()
			
			if titulo != "":
				record=record.filter(Titulo__contains = titulo)
			if ciudad != "":
				record=record.filter(Ciudad=ciudad)
			if precio != "":
				record=record.filter(Precio=precio)
			if tipoOfer != "":
				record=record.filter(TipoOferta=tipoOfer)
			if numHab != "":
				record=record.filter(NumHab=numHab)
			if direc != "":
				record=record.filter(Direccion__contains=direc)
	
			if record != []:
				template = get_template("listado.html")		
				print(categoria)
				diccionario = {'record':record,'categoria':categoria}	
				return HttpResponse(template.render(Context(diccionario)))

			else:
				print("estoy aqui")
				template = get_template("listado.html")		
				return HttpResponse(template.render(Context("No existe actividad que cumpla los requisitos")))


		if categoria=="empleo":	
			sueldo=str(request.POST['sueldo'])
			periodo=str(request.POST['periodo'])
			record=ActEmpleo.objects.all()
			Imag="empleo.png"
			if titulo != "":
				record=record.filter(Titulo__contains=titulo)
			if ciudad != "":
				record=record.filter(Ciudad=ciudad)
			if sueldo != "":
				record=record.filter(Sueldo=sueldo)
			if periodo != "":
				record=record.filter(Periodo=periodo)
		
			if record != []:
				template = get_template("listado.html")		
				diccionario = {'record':record,'Imag':Imag,'categoria':categoria}	
				return HttpResponse(template.render(Context(diccionario)))

			else:
				print("estoy aqui")
				template = get_template("listado.html")		
				return HttpResponse(template.render(Context("No existe actividad que cumpla los requisitos")))



@login_required
def calendario(request):
	if request.method == "GET":
		titulo="Calendario"
		template = get_template("enConstruccion.html")
		diccionario = {'titulo':titulo}
		
		return HttpResponse(template.render(Context(diccionario)))
