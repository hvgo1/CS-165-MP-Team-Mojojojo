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
from crime.models import CategoryForm,AgentForm,SuspectForm,LocationForm,CrimeForm,Crime, Category,Suspect,Location,Agent,Crime_Agent,SearchCrimeForm,SearchSuspectForm, SearchAgentForm
from django.views.generic.edit import UpdateView
from django.core.paginator import Paginator, InvalidPage,EmptyPage, PageNotAnInteger
from django.db.models import Q

# HOME page
def home(request):
    return render(request,'crime/home.html')

# CREATE crime, suspect, location, agent, category
def addCrime(request):
    	if request.method == 'GET':
        	form = CrimeForm()
    	else:
       	        form = CrimeForm(request.POST)
                if form.is_valid():
			form.save()
            		return HttpResponseRedirect('crimelist')
    	return render(request,'crime/addcrime.html', {'form': form})
def addSuspect(request):
    	if request.method == 'GET':
        	form = SuspectForm()
    	else:
       	        form = SuspectForm(request.POST)
                if form.is_valid():
			form.save()
            		return HttpResponseRedirect('suspectlist')
    	return render(request,'crime/addsuspect.html', {'form': form})
def addLocation(request):
    	if request.method == 'GET':
        	form = LocationForm()
    	else:
       	        form = LocationForm(request.POST)
                if form.is_valid():
			form.save()
            		return HttpResponseRedirect('locationlist')
    	return render(request,'crime/addlocation.html', {'form': form})
def addAgent(request):
    	if request.method == 'GET':
        	form = AgentForm()
    	else:
       	        form = AgentForm(request.POST)
                if form.is_valid():
			form.save()
            		return HttpResponseRedirect('agentlist')
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

# READ crime, suspect, location, agent, category
def viewCrime(request,id):
    crime = Crime.objects.get(id=id)    
    return render(request,'crime/viewcrime.html',{'crime':crime})
def viewSuspect(request,id):
    suspect = Suspect.objects.get(id=id)    
    return render(request,'crime/viewsuspect.html',{'suspect':suspect})
def viewLocation(request,id):
    location = Location.objects.get(id=id)    
    return render(request,'crime/viewlocation.html',{'location':location})
def viewAgent(request,id):
    agent = Agent.objects.get(id=id)    
    return render(request,'crime/viewagent.html',{'agent':agent})
"""
def viewCategory(request,id):
    category = Category.objects.get(id=id)    
    return render(request,'crime/viewcategory.html',{'category':category})
"""
def CrimeList(request):
    crimelist = Crime.objects.order_by('timedate')
    paginator = Paginator(crimelist,5)
    page = request.GET.get('page')
    try:
    	crimes = paginator.page(page) 
    except PageNotAnInteger:
        crimes = paginator.page(1)
    except EmptyPage:
        crimes = paginator.page(paginator.num_pages)
    return render_to_response('crime/crimelist.html',{'crimes':crimes})

def SuspectList(request):
    suspectlist = Suspect.objects.order_by('id')
    paginator = Paginator(suspectlist,5)
    page = request.GET.get('page')
    try:
    	suspects = paginator.page(page) 
    except PageNotAnInteger:
        suspects = paginator.page(1)
    except EmptyPage:
        suspects = paginator.page(paginator.num_pages)
    return render_to_response('crime/suspectlist.html',{'suspects':suspects})
def LocationList(request):
    locationlist = Location.objects.order_by('id')
    paginator = Paginator(locationlist,5)
    page = request.GET.get('page')
    try:
    	locations = paginator.page(page) 
    except PageNotAnInteger:
        locations = paginator.page(1)
    except EmptyPage:
        locations = paginator.page(paginator.num_pages)
    return render_to_response('crime/locationlist.html',{'locations':locations})
def AgentList(request):
    agentlist = Agent.objects.order_by('id')
    paginator = Paginator(agentlist,5)
    page = request.GET.get('page')
    try:
    	agents = paginator.page(page) 
    except PageNotAnInteger:
        agents = paginator.page(1)
    except EmptyPage:
        agents = paginator.page(paginator.num_pages)
    return render_to_response('crime/agentlist.html',{'agents':agents})

def InvList(request):
    invlist = Crime.objects.order_by('id')
    
    paginator = Paginator(invlist,5)
    page = request.GET.get('page')
    try:
    	crimes = paginator.page(page) 
    except PageNotAnInteger:
        crimes = paginator.page(1)
    except EmptyPage:
        crimes = paginator.page(paginator.num_pages)
    return render_to_response('crime/invlist.html',{'crimes':crimes})

def CriminalHistory(request):
    historylist = Crime.objects.filter(status="sol").order_by('timedate')
    
    paginator = Paginator(historylist,5)
    page = request.GET.get('page')
    try:
    	crimes = paginator.page(page) 
    except PageNotAnInteger:
        crimes = paginator.page(1)
    except EmptyPage:
        crimes = paginator.page(paginator.num_pages)
    return render_to_response('crime/historylist.html',{'crimes':crimes})

"""
def CategoryList(request):
    categorylist = Category.objects.all()
    paginator = Paginator(categorylist,5)
    page = request.GET.get('page')
    try:
    	categorys = paginator.page(page) 
    except PageNotAnInteger:
        categorys = paginator.page(1)
    except EmptyPage:
        categorys = paginator.page(paginator.num_pages)
    return render_to_response('crime/categorylist.html',{'categorys':categorys})
"""
# DELETE crime, suspect, location, agent, category
def deleteCrime(request,id):
   crime = Crime.objects.get(id=id)       
   if request.method == 'POST':    
   
   	Crime.objects.get(id=id).delete()
   	#message = "crime deleted"
	return HttpResponseRedirect('crimelist')
            		
   return render(request,'crime/deletecrime.html',{'crime':crime})

def deleteSuspect(request,id):
   suspect = Suspect.objects.get(id=id)       
   if request.method == 'POST':    
   
   	Suspect.objects.get(id=id).delete()
   	#message = "crime deleted"
	return HttpResponseRedirect('suspectlist')
            		
   return render(request,'crime/deletesuspect.html',{'suspect':suspect})
def deleteLocation(request,id):
   location = Location.objects.get(id=id)       
   if request.method == 'POST':    
   
   	Location.objects.get(id=id).delete()
   	#message = "crime deleted"
	return HttpResponseRedirect('locationlist')
            		
   return render(request,'crime/deletelocation.html',{'location':location})
def deleteAgent(request,id):
   agent = Agent.objects.get(id=id)       
   if request.method == 'POST':    
   
   	Agent.objects.get(id=id).delete()
   	#message = "crime deleted"
	return HttpResponseRedirect('agentlist')
            		
   return render(request,'crime/deleteagent.html',{'agent':agent})
"""
def deleteCategory(request,id):
    Category.objects.get(id=id).delete()
    message = "Category deleted"
    return HttpResponseRedirect('categorylist')
"""
# UPDATE crime, suspect, location, agent, category
def updateCrime(request,id):
    crime = Crime.objects.get(id=id)
#book_author = BookAuthor.objects.get(author=georfe, book=great_american_novel)
    #ag = Crime_Agent.objects.get(crime_id=id)
  
    if request.method == 'GET':
        form = CrimeForm(instance = crime)
    else:
        form = CrimeForm(request.POST,instance = crime)         
    	if form.is_valid():
		#crime = form.save(commit=False)
		crime.category_id = request.POST["category"]
		crime.timedate = request.POST["timedate"]
		crime.location_id = request.POST["location"]
		crime.suspect_id = request.POST["suspect"]		
                crime.status= request.POST["status"]
		
		crime.save()
		m = Crime_Agent(agent_id=request.POST["agent"],crime_id=crime.id)
		m.save()
				
        	return HttpResponseRedirect('crimelist')
    return render(request,'crime/updatecrime.html',{'crime':crime,'form':form,'action':'update/'+id})
def updateSuspect(request,id):
    suspect = Suspect.objects.get(id=id)
    if request.method == 'GET':
        form = SuspectForm(instance = suspect)
    else:
        form = SuspectForm(request.POST)         
    	if form.is_valid():
		suspect.firstname = request.POST["firstname"]
		suspect.lastname = request.POST["lastname"]
		suspect.location_id = request.POST["location"]
		suspect.save()
        	return HttpResponseRedirect('suspectlist')
    return render(request,'crime/updatesuspect.html',{'suspect':suspect,'form':form,'action':'update/'+id})
def updateLocation(request,id):
    location = Location.objects.get(id=id)
    if request.method == 'GET':
        form = LocationForm(instance = location)
    else:
        form = LocationForm(request.POST)         
    	if form.is_valid():
		location.barangay = request.POST["barangay"]
		location.city = request.POST["city"]
		location.country = request.POST["country"]
		location.save()
        	return HttpResponseRedirect('locationlist')
    return render(request,'crime/updatelocation.html',{'location':location,'form':form,'action':'update/'+id})
def updateAgent(request,id):
    agent = Agent.objects.get(id=id)
    if request.method == 'GET':
        form = AgentForm(instance = agent)
    else:
        form = AgentForm(request.POST)         
    	if form.is_valid():
		agent.firstname = request.POST["firstname"]
		agent.lastname = request.POST["lastname"]
		agent.location_id = request.POST["location"]
		agent.save()
        	return HttpResponseRedirect('agentlist')
    return render(request,'crime/updateagent.html',{'agent':agent,'form':form,'action':'update/'+id})
def searchCrime(request):
    form = SearchCrimeForm(request.GET)
    if form.is_valid():
    	#try:
       		cat = request.GET['category']
		loc = request.GET['location']
        	posts= Crime.objects.filter(category=cat)|Crime.objects.filter(location=loc) 
                
        	return render_to_response('crime/searchcrime.html', {'posts':posts, 'form':form})
    	#except KeyError:
    return render(request,'crime/searchcrime.html', {'form': form})

def searchSuspect(request):
    form = SearchSuspectForm(request.GET)
    if form.is_valid():
    	#try:
       		f = request.GET['firstname']
		l = request.GET['lastname']
        	posts= Suspect.objects.filter(firstname=f)|Suspect.objects.filter(lastname=l) 
                
        	return render_to_response('crime/searchsuspect.html', {'posts':posts, 'form':form})
    	#except KeyError:
    return render(request,'crime/searchsuspect.html', {'form': form})

def searchAgent(request):
    form = SearchAgentForm(request.GET)
    if form.is_valid():
    	#try:
       		f = request.GET['firstname']
		l = request.GET['lastname']
        	posts= Agent.objects.filter(firstname=f)|Agent.objects.filter(lastname=l) 
                
        	return render_to_response('crime/searchagent.html', {'posts':posts, 'form':form})
    	#except KeyError:
    return render(request,'crime/searchagent.html', {'form': form})
