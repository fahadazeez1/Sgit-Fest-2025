# Generated by Django 5.1.1 on 2024-11-02 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0003_remove_registration2_id_alter_registration2_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='basket',
            fields=[
                ('teamname', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('mob', models.IntegerField(max_length=12)),
                ('captain', models.CharField(max_length=45)),
                ('player2', models.CharField(max_length=45)),
                ('player3', models.CharField(max_length=45)),
                ('player4', models.CharField(max_length=45)),
                ('player5', models.CharField(max_length=45)),
                ('player6', models.CharField(max_length=45)),
                ('player7', models.CharField(max_length=45)),
                ('player8', models.CharField(max_length=45)),
                ('player9', models.CharField(max_length=45)),
                ('player10', models.CharField(max_length=45)),
            ],
        ),
    ]