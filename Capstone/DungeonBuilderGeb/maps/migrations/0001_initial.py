# Generated by Django 2.2.6 on 2019-10-08 17:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Layout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x_position', models.IntegerField()),
                ('y_position', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Obj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('appearance', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('background', models.ImageField(upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('obj', models.ManyToManyField(through='maps.Layout', to='maps.Obj')),
            ],
        ),
        migrations.AddField(
            model_name='layout',
            name='map',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maps.Map'),
        ),
        migrations.AddField(
            model_name='layout',
            name='obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maps.Obj'),
        ),
    ]
