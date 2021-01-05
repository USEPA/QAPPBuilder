ORDER MATTERS!
Run these commands (in order) to import the data fixtures required for Projects module (from QA-TRACK).
I will work on creating migrations to import these automatically...

1) python manage.py loaddata offices/fixtures/offices.json

2) python manage.py loaddata labs/fixtures/labs.json

3) python manage.py loaddata immediate_offices/fixtures/immediate_offices.json

4) python manage.py loaddata divisions/fixtures/divisions.json

5) python manage.py loaddata branches/fixtures/branches.json

6) python manage.py loaddata persons/fixtures/persons.json

7) python manage.py loaddata organization/fixtures/organization.json

8) python manage.py loaddata rms/fixtures/rms.json


9) python manage.py loaddata projects/fixtures/projects.json
#  NOTE: I had to remove all projects.program from the fixture, that field doesn't exist in the model so fixture was breaking.
#        Also removed all lines (in section fields) containing the text    "program":
#        Also removed all sections for model "project_log"
#        Also removed all collaborators: [] (set to empty list) and set all persons to id 1.

10) python manage.py loaddata projects/fixtures/projectnumber.json

11) python manage.py loaddata projects/fixtures/projects_support.json
