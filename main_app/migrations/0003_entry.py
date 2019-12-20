# Generated by Django 2.2.7 on 2019-12-20 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mood', models.CharField(choices=[('H', 'Happy'), ('M', 'Meh'), ('S', 'Sad')], default='M', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('week', models.CharField(max_length=15)),
                ('notes', models.CharField(max_length=150)),
                ('Sun', models.BooleanField(default=False)),
                ('Mon', models.BooleanField(default=False)),
                ('Tue', models.BooleanField(default=False)),
                ('Wed', models.BooleanField(default=False)),
                ('Thu', models.BooleanField(default=False)),
                ('Fri', models.BooleanField(default=False)),
                ('Sat', models.BooleanField(default=False)),
                ('resolution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Resolution')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]