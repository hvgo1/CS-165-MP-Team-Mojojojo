Crime Database 

Developers:
->Carm Corpuz
->Hannah Go
->Jessica Pabico


To POPULATE Database:
Assumed done:
* "crimedb" is already created through postgres and connected to django
* Template paths are changed to your own in Template dirs in settings.py ( Currently in the settings.py: '/home/jecca/Documents/CS165MP/crime165/crime165/templates',
	'/home/jecca/Documents/CS165MP/crime165/crime/templates' )

->Run python manage.py syncdb in the terminal to create tables and create the superuser/user to view the admin.
->Also run python populate_db.py, ignore the errors created
->Again, run python manage.py syncdb. 
->Check the Admin (127.0.0.1:8000/admin)to check if the populate script worked.

T GO to the APP:
> Type in to your browser: 127.0.0.1:8000/crime
