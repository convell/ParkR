# Generated by Django 2.0.2 on 2018-03-04 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('listing', '0002_auto_20180228_0849'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('P', 'Past Reservation'), ('C', 'Current Reservation'), ('F', 'Future Reservation')], default='F', max_length=1)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('reserved_time', models.DateTimeField(auto_now_add=True)),
                ('reservee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservee', to='listing.ParkingSpace')),
            ],
        ),
    ]
