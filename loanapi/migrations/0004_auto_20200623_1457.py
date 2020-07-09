# Generated by Django 3.0.6 on 2020-06-23 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanapi', '0003_auto_20200525_2039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='approval',
            old_name='dependant',
            new_name='dependents',
        ),
        migrations.AlterField(
            model_name='approval',
            name='education',
            field=models.CharField(choices=[('Graduate', 'Graduate'), ('Not_Graduate', 'Not_Graduate')], help_text='Please indicate if you are a graduate or not', max_length=100, null=True),
        ),
    ]