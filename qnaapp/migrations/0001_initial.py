# Generated by Django 3.1 on 2020-09-01 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('userEmail', models.EmailField(max_length=30, primary_key=True, serialize=False, verbose_name='이메일(아이디)')),
                ('nickName', models.CharField(max_length=12, verbose_name='닉네임')),
                ('password', models.CharField(max_length=12, verbose_name='비밀번호')),
                ('registerDate', models.DateField(auto_now_add=True, null=True, verbose_name='가입시간')),
            ],
        ),
        migrations.CreateModel(
            name='Qnaboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('nickName', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('qnawriter', models.ForeignKey(db_column='userEmail', default='', on_delete=django.db.models.deletion.CASCADE, to='qnaapp.users')),
            ],
        ),
    ]
