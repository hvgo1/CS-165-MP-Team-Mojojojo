Crime Database 

Developers:
->Carm Corpuz
->Hannah Go
->Jessica Pabico


To POPULATE Database:

Assumed done:
* "crimedb" database and user "myuser" is already created through postgres and connected to django
  ("myuser" was granted access to crimedb by command 'GRANT ALL PRIVILEGES ON DATABASE crimedb to myuser;' in psql)
* Template paths are changed to your own in Template dirs in settings.py ( Currently in the settings.py: '/home/jecca/Documents/CS165MP/crime165/crime165/templates',
	'/home/jecca/Documents/CS165MP/crime165/crime/templates' )

->(Go to the path of the folder CS165MP/crime165) Run 'python manage.py syncdb' in the terminal to create tables and create the superuser/user to view the admin.

->Also run 'python populate_db.py', ignore if there are errors created

->Again, run 'python manage.py syncdb', then  run 'python manage.py runserver'

->Check the Admin (127.0.0.1:8000/admin)to check if the populate script worked.

TO GO to the APP:
> Type in to your browser: 127.0.0.1:8000/crime
