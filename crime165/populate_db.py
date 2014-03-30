import os
import datetime

def populate():
    add_cat('duckface')
    add_cat('libel')
    add_cat('homicide')
    add_cat('noisy')
    add_cat('standing')
    add_cat('cutting class')

    add_loc(brgy='Okinawa', city='Tokyo', country='Japan')
    add_loc(brgy='Mintal', city='Davao', country='Philippines')
    add_loc(brgy='Cati', city='Merqua', country='Slovakia')
    add_loc(brgy='0923', city='Springfields', country='USA')
    add_loc(brgy='Manny', city='Gloria', country='Colombia')
    add_loc(brgy='Turkhi', city='Awol', country='Uzbekistan')
    add_loc(brgy='Caesar', city='Yogurt', country='Greece')
    add_loc(brgy='Okinawa', city='Tokyo', country='Singapore')
    add_loc(brgy='Havaiana', city='El Rio', country='Brazil')
    add_loc(brgy='Pnam', city='Siam', country='Thailand')
    add_loc(brgy='Pedxing', city='Guah Zhong', country='China')
    add_loc(brgy='Pop', city='Krimea', country='Iceland')
    add_loc(brgy='Wizz', city='Chezze', country='Sweden')
    add_loc(brgy='Luff', city='Ballons', country='Germany')
    add_loc(brgy='Ikot', city='Pantranco', country='Egypt')
    add_loc(brgy='Modo', city='Cosi', country='Cuba')
    add_loc(brgy='Okinawa', city='Tokyo', country='Japan')
    add_loc(brgy='Hang', city='Maang', country='Chile')
    add_loc(brgy='Vera', city='Farmiga', country='Ukraine')
    add_loc(brgy='Machu', city='Pichu', country='Peru')
    add_loc(brgy='Peewee', city='Liverpool', country='England')

    add_agent(fname='Conana', lname='Mako', loc=1)
    add_agent(fname='Inspector', lname='Mills', loc=4)
    add_agent(fname='Santou', lname='Rinie', loc=4)
    add_agent(fname='Clea', lname='Ng', loc=5)
    add_agent(fname='Conan', lname='Makonochi', loc=1)


    add_suspect(fname='Ippo', lname='Man', loc=1)
    #add_suspect(fname='Bagnet', lname='Napulis', loc=2)
    add_suspect(fname='Homer', lname='Simpson', loc=3)
    add_suspect(fname='Taissa', lname='Farmiga', loc=4)
    add_suspect(fname='Zee', lname='Yous', loc=5)
    add_suspect(fname='Prince', lname='Charming', loc=1)
    add_suspect(fname='Matsi', lname='Pitso', loc=7)
    add_suspect(fname='Mito', lname='Watanagi', loc=1)

    add_crime(cat=5, tdate='2014-03-26 10:20:00', loc=1, suspect=5, stat='sol')
    add_crime(cat=3, tdate='2011-12-25 03:20:00', loc=6, suspect=None, stat='inv')
    add_crime(cat=3, tdate='2008-05-21 06:10:00', loc=10, suspect=2, stat='sol')
    add_crime(cat=6, tdate='2014-10-28 08:30:00', loc=3, suspect=None, stat='inv')
    add_crime(cat=1, tdate='2014-01-01 11:20:00', loc=5, suspect=3, stat='sol')
    add_crime(cat=2, tdate='2013-09-22 10:20:00', loc=2, suspect=None, stat='inv')
    add_crime(cat=4, tdate='2014-02-11 09:11:08', loc=9, suspect=4, stat='sol')
    add_crime(cat=2, tdate='2012-05-13 11:50:01', loc=13, suspect=None, stat='inv')

    add_cagent(agent=2,crime=5)
    add_cagent(agent=1,crime=1)
    add_cagent(agent=5,crime=2)
    add_cagent(agent=4,crime=8)
    add_cagent(agent=2,crime=4)
    add_cagent(agent=3,crime=3)
    add_cagent(agent=5,crime=3)
    add_cagent(agent=2,crime=5)
    add_cagent(agent=3,crime=7)
    add_cagent(agent=5,crime=3)
    add_cagent(agent=3,crime=6)
    add_cagent(agent=5,crime=6)
    # Print out what we have added to the user.
#    for c in Category.objects.all():
#        for p in Page.objects.filter(category=c):
#            print "- {0} - {1}".format(str(c), str(p))

def add_loc(brgy, city, country):
    l = Location.objects.get_or_create(barangay=brgy, city=city, country=country)[0]
    return l

def add_agent(fname, lname, loc):
    a = Agent.objects.get_or_create(firstname=fname,lastname=lname,location_id=loc)[0]
    return a

def add_suspect(fname, lname, loc):
    s = Suspect.objects.get_or_create(firstname=fname, lastname=lname, location_id=loc)[0]
    return s

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c

def add_crime(cat, tdate, loc, suspect, stat):
    c = Crime.objects.get_or_create(category_id=cat, timedate=tdate, location_id=loc, suspect_id=suspect, status=stat)[0]
    return c
def add_cagent(agent,crime):
    c = Crime_Agent.objects.get_or_create(agent_id = agent, crime_id = crime)[0]
    return c
# Start execution here!
if __name__ == '__main__':
    print "Starting crime population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crime165.settings')
    from crime.models import Location, Agent, Suspect, Category, Crime, Crime_Agent
    populate()

