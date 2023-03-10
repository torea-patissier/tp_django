# Generated by Django 4.1.5 on 2023-02-16 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emprunter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_pret', models.DateField()),
                ('date_retour', models.DateField()),
                ('est_rendu', models.BooleanField(default=False)),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.client')),
                ('id_film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.film')),
            ],
        ),
    ]
