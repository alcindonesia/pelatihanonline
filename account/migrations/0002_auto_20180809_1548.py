# Generated by Django 2.1 on 2018-08-09 08:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('program', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='events',
            field=models.ManyToManyField(through='account.Membership', to='program.Event'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='membership',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program.Event'),
        ),
        migrations.AddField(
            model_name='membership',
            name='userprofile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.UserProfile'),
        ),
    ]