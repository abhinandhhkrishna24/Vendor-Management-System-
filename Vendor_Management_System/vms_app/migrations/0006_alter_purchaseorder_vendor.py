# Generated by Django 4.2.7 on 2023-12-03 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vms_app', '0005_alter_purchaseorder_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vms_app.vendorprofile'),
        ),
    ]