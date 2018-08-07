# Generated by Django 2.1 on 2018-08-07 18:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False),
                ),
                ('name', models.CharField(max_length=255)),
                ('extension', models.CharField(blank=True, max_length=255)),
                ('content', models.BinaryField()),
                ('content_type', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]