import datetime
from django.db import models
from django.utils import timezone
from django.forms import ModelForm
from django.contrib.admin import widgets   

class Location(models.Model):
	def __unicode__(self):  
	#return self.country
		return u'%s, %s, %s' %(self.barangay,self.city,self.country)
	barangay = models.CharField(max_length=200)
	city= models.CharField(max_length=200)
	country = models.CharField(max_length=200)

class Agent(models.Model):
	def __unicode__(self):  
	#return self.lastname
		return u'%s,%s' %(self.lastname,self.firstname)
	firstname = models.CharField(max_length=200)
	lastname = models.CharField(max_length=200)
	location = models.ForeignKey(Location)
    
class Suspect(models.Model):
	def __unicode__(self): 
	#return self.lastname
		return u'%s,%s' %(self.lastname,self.firstname)
	firstname = models.CharField(max_length=200)
	lastname= models.CharField(max_length=200)
	location = models.ForeignKey(Location)

class Category(models.Model):
	def __unicode__(self):  
		return self.name
	name = models.CharField(max_length=200,unique = True)


	
class Crime(models.Model):
	def __unicode__(self):  
	#return unicode(self.timedate)
	return u'CATEGORY:%s; DATE&TIME:%s; LOCATION:%s; SUSPECT:%s; AGENT(s):%s' % (self.category,self.timedate, self.location,self.suspect,self.agent)
	STATUS_CHOICES = (
	('inv', 'Investigated'),
	('sol', 'Solved'),
	)
            
	category = models.ForeignKey(Category)
	timedate = models.DateTimeField('Date and Time( Format:YYYY-mm-dd HH:MM:SS)')
	location = models.ForeignKey(Location)
	suspect = models.ForeignKey(Suspect,null=True,blank=True)
	agent = models.ManyToManyField(Agent,through='Crime_Agent',null=False,blank=False) 
	status = models.CharField(max_length=300,choices=STATUS_CHOICES,default='inv')
    
	#def was_published_recently(self):
	#return self.timedate >= timezone.now() - datetime.timedelta(days=1)
	#was_published_recently.admin_order_field = 'timedate'
	#was_published_recently.boolean = True
	#was_published_recently.short_description = 'Published recently?'

class Crime_Agent(models.Model):
	def __unicode__(self):    
		return self.id
	agent = models.ForeignKey(Agent)
	crime = models.ForeignKey(Crime)

class CrimeForm(ModelForm):
	class Meta:
		model = Crime

class CategoryForm(ModelForm):
	class Meta:
		model = Category

class LocationForm(ModelForm):
	class Meta:
		model = Location

class AgentForm(ModelForm):
	class Meta:
		model = Agent

class SuspectForm(ModelForm):
	class Meta:
		model = Suspect
class SearchCrimeForm(ModelForm):
	class Meta:
		model = Crime
		fields = ['category','location']
class SearchSuspectForm(ModelForm):
	class Meta:
		model = Suspect
		fields = ['firstname','lastname']
class SearchAgentForm(ModelForm):
	class Meta:
		model = Agent
		fields = ['firstname','lastname']
