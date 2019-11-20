from photos.models import Photo
import csv

with open('data.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = Photo(url=row['image_url'])
        p.save()