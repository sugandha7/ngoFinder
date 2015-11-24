from django.core.management.base import BaseCommand
from writeDB.models import ngo
from writeDB import parse_fields

class Command(BaseCommand):
    help = 'Populates the database with NGO information.'
    args = '[writeDB]'

    def handle(self, *args, **options):
	ngo.objects.all().delete()
        total_result = parse_fields.get_result()
        for result in total_result:
            ngo.objects.get_or_create(name=result[0],address=result[1],phone=result[2],mobile=result[3],email=result[4],\
            website=result[5],person=result[6],purpose=result[7],aim=result[8],latitude=result[9],longitude=result[10])
            #cursor.save()
            
