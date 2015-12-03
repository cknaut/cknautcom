#use this on heroku run python manage.py shell

import csv
from citecheck.models import journal_info
# If you're using different field names, change this list accordingly.
# The order must also match the column order in the CSV file.
fields = ['Rank', 'Title', 'Type', 'ISSN', 'SJR', 'H_index', 'Total_Docs_Last_Year', 'Total_Docs_3years', 'Total_Refs', 'Total_Cites_3years', 'Cites_per_Doc_2years', 'Ref_per_Doc', 'Country']
#take this from heroku staticfile collector
for row in csv.reader(open("staticfiles/citecheck/scimagojr_20150811.7423b2a89c9c.csv")):
    journal_info.objects.create(**dict(zip(fields, row)))

