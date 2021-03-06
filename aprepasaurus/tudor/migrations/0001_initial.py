# Generated by Django 2.0 on 2017-12-03 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spec_text', models.CharField(max_length=200)),
                ('desc_text', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_name', models.CharField(max_length=200)),
                ('teaching_start_date', models.DateTimeField(verbose_name='start date')),
            ],
        ),
        migrations.AddField(
            model_name='specialty',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tudor.Tutor'),
        ),
    ]
