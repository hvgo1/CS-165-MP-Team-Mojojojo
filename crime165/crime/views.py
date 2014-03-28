from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect,HttpResponse, QueryDict
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import Context, loader
from django.template.loader import get_template
from django.http import Http404
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.contrib.auth import logout
from django.template import RequestContext
from crime.models import CategoryForm,AgentForm,SuspectForm,LocationForm,CrimeForm,Crime, Category
from django.views.generic.edit import UpdateView
from django.core.paginator import Paginator, InvalidPage,EmptyPage, PageNotAnInteger


def addCrime(request):
    	if request.method == 'GET':
        	form = CrimeForm()
    	else:
       	        form = CrimeForm(request.POST)
	         
                if form.is_valid():
			form.save()
            		return HttpResponseRedirect('addcrime')
            
    	
    	return render(request,'crime/addcrime.html', {'form': form})

def deleteCrime(request,id):
    Crime.objects.get(id=id).delete()
    message = "crime deleted"
    return HttpResponseRedirect('crimelist')

def updateCrime(request,id):
    crime = Crime.objects.get(id=id)
    
    if request.method == 'GET':
        form = CrimeForm(instance = crime)
    else:
        form = CrimeForm(request.POST)         
    	if form.is_valid():
		crime.category_id = request.POST["category"]
		crime.timedate = request.POST["timedate"]
		crime.location_id = request.POST["location"]
		crime.suspect_id = request.POST["suspect"]
		crime.agent_id= request.POST["agent"]	
		crime.save()
        	return HttpResponseRedirect('crimelist')
    return render(request,'crime/updatecrime.html',{'crime':crime,'form':form,'action':'update/'+id})


def viewCrime(request,id):
    crime = Crime.objects.get(id=id)    
    
    return render(request,'crime/viewcrime.html',{'crime':crime})

 
def addSuspect(request):
    	if request.method == 'GET':
        	form = SuspectForm()
    	else:
       	        form = SuspectForm(request.POST)
	         
                if form.is_valid():
			form.save()
            		return HttpResponseRedirect('addsuspect')
            
    	
    	return render(request,'crime/addsuspect.html', {'form': form})

def addLocation(request):
    	if request.method == 'GET':
        	form = LocationForm()
    	else:
       	        form = LocationForm(request.POST)
	         
                if form.is_valid():
			form.save()
            		return HttpResponseRedirect('addlocation')
            
    	
    	return render(request,'crime/addlocation.html', {'form': form})

def addAgent(request):
    	if request.method == 'GET':
        	form = AgentForm()
    	else:
       	        form = AgentForm(request.POST)
	         
                if form.is_valid():
			form.save()
            		return HttpResponseRedirect('addagent')
            
    	
    	return render(request,'crime/addagent.html', {'form': form}) 

def addCategory(request):
    	if request.method == 'GET':
        	form = CategoryForm()
    	else:
       	        form = CategoryForm(request.POST)
	         
                if form.is_valid():
			form.save()
            		return HttpResponseRedirect('addcategory')
            
    	
    	return render(request,'crime/addcategory.html', {'form': form})

def index(request, **kwargs):
	
	if request.method == 'GET':
       	  	form = CategoryForm()
    	else:

        	form = CategoryForm(request.POST)  
		if form.is_valid():
			form.save()
			
			return HttpResponseRedirect('')
	
    	return render(request,'crime/index.html', {'form': form})

def CrimeList(request):

    crimelist = Crime.objects.all()
    paginator = Paginator(crimelist,5)
    page = request.GET.get('page')
    try:
    	crimes = paginator.page(page) 
    except PageNotAnInteger:
        crimes = paginator.page(1)
    except EmptyPage:
        crimes = paginator.page(paginator.num_pages)

    return render_to_response('crime/crimelist.html',{'crimes':crimes})

