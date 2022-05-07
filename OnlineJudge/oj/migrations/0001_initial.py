# Generated by Django 4.0.3 on 2022-05-04 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statement', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=1000)),
                ('code', models.CharField(max_length=10000)),
                ('difficulty', models.CharField(choices=[('Hard', 'Hard'), ('Medium', 'Medium'), ('Easy', 'Easy')], max_length=10)),
            ],
            options={
                'verbose_name': 'Problems',
            },
        ),
        migrations.CreateModel(
            name='TestCases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TC_input', models.CharField(max_length=5000)),
                ('TC_output', models.CharField(max_length=5000)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oj.problems')),
            ],
            options={
                'verbose_name': 'Test Case',
            },
        ),
        migrations.CreateModel(
            name='Solutions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verdict', models.CharField(max_length=50)),
                ('submission_timestamp', models.DateTimeField(auto_now=True)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oj.problems')),
            ],
            options={
                'verbose_name': 'Solutions',
            },
        ),
    ]
