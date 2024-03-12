# Generated by Django 4.2.2 on 2023-07-15 22:57

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cvd_service', '0003_alter_cvdreport_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvdreport',
            name='email',
            field=django_cryptography.fields.encrypt(models.EmailField(max_length=254)),
        ),
        migrations.AlterField(
            model_name='cvdreport',
            name='first_name',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=100, null=True)),
        ),
        migrations.AlterField(
            model_name='cvdreport',
            name='last_name',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=100, null=True)),
        ),
        migrations.AlterField(
            model_name='cvdreport',
            name='pgp_key',
            field=django_cryptography.fields.encrypt(models.TextField()),
        ),
        migrations.AlterField(
            model_name='cvdreport',
            name='phone',
            field=django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=20, null=True)),
        ),
    ]
