# Generated by Django 2.1.2 on 2018-11-02 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181101_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moteur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Voiture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=25)),
                ('moteur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.Moteur')),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='categorie',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.Categorie'),
            preserve_default=False,
        ),
    ]
