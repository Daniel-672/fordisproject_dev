# Generated by Django 3.0.3 on 2020-09-04 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fordisapp', '0014_delete_reportslist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qnaboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('nickName', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('admin_content', models.TextField()),
                ('qnawriter', models.ForeignKey(db_column='userEmail', on_delete=django.db.models.deletion.CASCADE, to='fordisapp.Users')),
            ],
        ),
    ]
