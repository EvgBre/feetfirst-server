# Generated by Django 4.1.3 on 2023-08-01 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_placed', models.DateField()),
                ('payment_type', models.IntegerField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=7)),
                ('is_completed', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=50)),
                ('profile_image_url', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('image_url', models.CharField(max_length=5000)),
                ('added_on', models.DateField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feetfirstapi.category')),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feetfirstapi.order')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feetfirstapi.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feetfirstapi.user'),
        ),
    ]
