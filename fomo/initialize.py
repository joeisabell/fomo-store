import os
from datetime import datetime
from decimal import Decimal

# initialize django environment
os.environ['DJANGO_SETTINGS_MODULE'] = 'fomo.settings'
import django
django.setup()

from django.core import management
from django.db import connection
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType

from catalog import models as cmod
from account import models as amod

# drop and recreate database tables
with connection.cursor() as cursor:
    cursor.execute("DROP SCHEMA public CASCADE")
    cursor.execute("CREATE SCHEMA public")
    cursor.execute("GRANT ALL ON SCHEMA public TO postgres")
    cursor.execute("GRANT ALL ON SCHEMA public TO public")

# migrate
management.call_command('makemigrations')
management.call_command('migrate')

# add group
g1 = Group()
g1.name = 'Supers'
g1.save()

all_permissions = Permission.objects.all()
g1.permissions.set(all_permissions)
g1.save()

# add users
u1 = amod.FomoUser()
u1.set_password("Utslcw2014")
u1.last_login = datetime.now()
u1.is_superuser = True
u1.username = "isabell7"
u1.first_name = "Joe"
u1.last_name = "Isabell"
u1.email = "joeisabell0@gmail.com"
u1.is_staff = True
u1.is_active = True
u1.date_joined = datetime.now()
u1.address = "465 N 300 W Apt 29"
u1.city = "Provo"
u1.state = "UT"
u1.zip_code = "84601"
u1.phone = "479-802-9621"
u1.save()

u2 = amod.FomoUser()
u2.set_password("mypass")
u2.last_login = datetime.now()
u2.is_superuser = True
u2.username = "misabell"
u2.first_name = "Margo"
u2.last_name = "Isabell"
u2.email = "margobrockbank5@gmail.com"
u2.date_joined = datetime.now()
u2.address = "465 N 300 W Apt 29"
u2.city = "Provo"
u2.state = "UT"
u2.zip_code = "84601"
u2.phone = "479-802-9621"
u2.save()

u3 = amod.FomoUser()
u3.set_password("mypass")
u3.last_login = datetime.now()
u3.is_superuser = True
u3.username = "primeguard68"
u3.first_name = "Jim"
u3.last_name = "Fife"
u3.email = "jamesafife@bearriver.net"
u3.date_joined = datetime.now()
u3.address = "12695 Strawberry Ridge Road"
u3.city = "Bentonville"
u3.state = "AR"
u3.zip_code = "72712"
u3.phone = "479-898-3344"
u3.save()

u4 = amod.FomoUser()
u4.set_password("mypass")
u4.last_login = datetime.now()
u4.is_superuser = True
u4.username = "jackrabit"
u4.first_name = "Jack"
u4.last_name = "Rabbit"
u4.email = "jill@bearriver.net"
u4.date_joined = datetime.now()
u4.address = "12695 Strawberry Ridge Road"
u4.city = "Bentonville"
u4.state = "AR"
u4.zip_code = "72712"
u4.phone = "479-898-3344"
u4.save()

# add categories
cat1 = cmod.Category()
cat1.code = 'brass'
cat1.name = 'Brass Instruments'
cat1.save()

cat2 = cmod.Category()
cat2.code = 'wind'
cat2.name = 'Wind Instruments'
cat2.save()

cat3 = cmod.Category()
cat3.code = 'string'
cat3.name = 'String Instruments'
cat3.save()

# add products
# bulk products
bp1 = cmod.BulkProduct()
bp1.category = cat1
bp1.name = 'Kazoo'
bp1.brand = 'ToysRUs'
bp1.price = Decimal('90.50')
bp1.quantity = 20
bp1.reorder_point = 5
bp1.reorder_quantity = 10

bp2 = cmod.BulkProduct()
bp2.category = cat3
bp2.name = 'E String'
bp2.brand = 'String City'
bp2.price = Decimal('10.66')
bp2.quantity = 40
bp2.reorder_point = 10
bp2.reorder_quantity = 20

# unique products
up1 = cmod.UniqueProduct()
up1.category = cat3
up1.name = 'E String'
up1.brand = 'String City'
up1.price = Decimal('10.66')

up2 = cmod.UniqueProduct()
up2.category = cat3
up2.name = 'E String'
up2.brand = 'String City'
up2.price = Decimal('10.66')

up3 = cmod.UniqueProduct()
up3.category = cat3
up3.name = 'E String'
up3.brand = 'String City'
up3.price = Decimal('10.66')

# rental products
rp1 = cmod.RentalProduct()
rp1.category = cat3
rp1.name = 'E String'
rp1.brand = 'String City'
rp1.price = Decimal('10.66')

rp2 = cmod.RentalProduct()
rp2.category = cat3
rp2.name = 'E String'
rp2.brand = 'String City'
rp2.price = Decimal('10.66')

rp3 = cmod.RentalProduct()
rp3.category = cat3
rp3.name = 'E String'
rp3.brand = 'String City'
rp3.price = Decimal('10.66')
