from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import Context
from django.template.loader import get_template
from django.http import Http404
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.contrib.auth import logout
from django.template import RequestContext

from crime.models import CategoryForm,AgentForm,SuspectForm,LocationForm,CrimeForm

from django.views.generic.edit import UpdateView
from django.views import generic
from crime.models import Crime, Category

def addCrime(request):
    	if request.method == 'GET':
        	form = CrimeForm()
    	else:
       	        form = CrimeForm(request.POST)
	         
                if form.is_valid():
			form.save()
            		return HttpResponseRedirect('addcrime')
            
    	
    	return render(request,'crime/addcrime.html', {'form': form})
 
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

#def index(request, **kwargs):
	
#	if request.method == 'GET':
#        	form = CategoryForm()
#    	else:

#        	form = CategoryForm(request.POST)  
#		if form.is_valid():
#			form.save()
			
#			return HttpResponseRedirect('')
	
#    	return render(request,'crime/index.html', {'form': form})
class CrimeView(generic.ListView):
    #model = Crime
    template_name = 'crime/viewcrimes.html'
    context_object_name = 'latest_crime_list'
    
    def get_queryset(self):
        """Return the last five published crime."""
        return Crime.objects.order_by('-timedate')[:5]
#class CrimeUpdate(UpdateView):
#    model = Crime
#   template_name = 'crime/updatecrimes.html'
#    context_object_name = 'latest_crime_list'
#    def get_queryset(self):
#        """Return the last five published crime."""
	
