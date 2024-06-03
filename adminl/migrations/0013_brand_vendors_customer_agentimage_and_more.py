# Generated by Django 4.1.7 on 2023-04-21 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminl', '0012_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='vendors',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='adminl.vendor'),
        ),
        migrations.AddField(
            model_name='customer',
            name='agentimage',
            field=models.ImageField(null=True, upload_to='uploads/customers/'),
        ),
        migrations.AddField(
            model_name='delivpart',
            name='agentimage',
            field=models.ImageField(null=True, upload_to='uploads/delivpar/'),
        ),
        migrations.AddField(
            model_name='finmanager',
            name='agentimage',
            field=models.ImageField(null=True, upload_to='uploads/finman/'),
        ),
        migrations.AddField(
            model_name='invman',
            name='agentimage',
            field=models.ImageField(null=True, upload_to='uploads/invman/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='null', upload_to='uploads/products/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendor',
            name='agentimage',
            field=models.ImageField(null=True, upload_to='uploads/vendors/'),
        ),
    ]
