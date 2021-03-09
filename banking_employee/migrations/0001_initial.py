# Generated by Django 3.1.7 on 2021-03-09 10:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=200, null=True)),
                ('rank', models.CharField(choices=[('Basic', 'Basic'), ('Silver', 'Silver'), ('Gold', 'Gold')], default='Basic', max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(choices=[('Bank Account', 'Bank Account'), ('Loan', 'Loan')], default='Bank Account', max_length=200)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banking_employee.customer')),
            ],
        ),
    ]
