# Generated by Django 3.2.10 on 2021-12-20 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Activites',
                'verbose_name_plural': 'Activites',
            },
        ),
        migrations.CreateModel(
            name='Collaborateur',
            fields=[
                ('user', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Collaborateur',
                'verbose_name_plural': 'Collaborateurs',
            },
        ),
        migrations.CreateModel(
            name='Tache',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('stagiaireAttribue', models.IntegerField(null=True)),
                ('dateDeb', models.DateField(blank=True)),
                ('dateFin', models.DateField(blank=True)),
                ('dateValidation', models.DateTimeField(blank=True, default=None, null=True)),
                ('activite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tache', to='reporting_journalier_activites.activite')),
            ],
            options={
                'verbose_name': 'Tache',
                'verbose_name_plural': 'Taches',
            },
        ),
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('user_creator', models.IntegerField()),
                ('collaborateurs', models.ManyToManyField(to='reporting_journalier_activites.Collaborateur')),
            ],
            options={
                'verbose_name': 'Projet',
                'verbose_name_plural': 'Projets',
            },
        ),
        migrations.CreateModel(
            name='Outil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('tache', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outil', to='reporting_journalier_activites.tache')),
            ],
            options={
                'verbose_name': 'Outil',
                'verbose_name_plural': 'Outils',
            },
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('user', models.IntegerField()),
                ('dateComment', models.DateField(auto_now_add=True)),
                ('tache', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaire', to='reporting_journalier_activites.tache')),
            ],
            options={
                'verbose_name': 'Commentaire',
                'verbose_name_plural': 'Commentaires',
            },
        ),
        migrations.AddField(
            model_name='activite',
            name='projet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activite', to='reporting_journalier_activites.projet'),
        ),
    ]
