# Generated by Django 3.2.5 on 2021-07-02 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShoeSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uk_size', models.DecimalField(decimal_places=1, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=60)),
                ('brand', models.CharField(max_length=60)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('photo', models.FileField(default=None, null=True, upload_to='')),
                ('available_sizes', models.ManyToManyField(related_name='shoe_sizes', to='api.ShoeSize')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=60)),
                ('client', models.CharField(max_length=60)),
                ('shoe_reference', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.shoe')),
                ('size', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.shoesize')),
            ],
        ),
    ]
