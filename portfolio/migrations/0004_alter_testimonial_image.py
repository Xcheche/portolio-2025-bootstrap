# Generated by Django 5.2.1 on 2025-06-08 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_testimonial_alter_portfolio_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='testimonials/%Y/%m/%d/'),
        ),
    ]
