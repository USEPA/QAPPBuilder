# Created on 2020-01-30 15:57
# pylint: skip-file

import os
from django.core import serializers
from django.db import migrations, transaction
from django.db.utils import IntegrityError

fixture_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../fixtures'))
fixture_filename = 'sectionb_type.json'

def load_fixture(_apps, _schema_editor):
    """Load data from a fixture when running migrations"""
    fixture_file = os.path.join(fixture_dir, fixture_filename)
    fixture = open(fixture_file, 'rb')
    objects = serializers.deserialize('json', fixture, ignorenonexistent=True)
    for obj in objects:
        try:
            with transaction.atomic():
                obj.save()
        except IntegrityError:
            pass    # Ignore if duplicate obj already exists in db
    fixture.close()

class Migration(migrations.Migration):

    dependencies = [
        ('qapp_builder', '0002_division_fixture'),
    ]

    operations = [
        migrations.RunPython(load_fixture),
    ]
