import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")

import django
django.setup()

import random
from first_app.models import Topic, WebPage, AccessRecord
from faker import Faker

fakergen = Faker()
topics = ["Search", "Social", "News", "Marketplace", "Games"]

def add_topic():
    t = Topic.objects.get_or_create(name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        t = add_topic()
        fake_url = fakergen.url()
        fake_date = fakergen.date()
        fake_name = fakergen.company()

        wbpage = WebPage.objects.get_or_create(topic=t, url=fake_url, name=fake_name)[0]

        rec = AccessRecord.objects.get_or_create(webpage=wbpage, date=fake_date)[0]

if __name__ == '__main__':
    print("populating script")
    populate()
    print("populating complete")
