# Generated by Django 4.0.4 on 2022-07-06 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='회원아이디')),
                ('password', models.CharField(max_length=128, verbose_name='비밀번호')),
                ('usernumber', models.CharField(max_length=64, verbose_name='회원번호')),
                ('name', models.CharField(max_length=64, verbose_name='회원이름')),
                ('email', models.EmailField(max_length=128, verbose_name='이메일')),
                ('phone', models.CharField(max_length=64, verbose_name='전화번호')),
                ('category', models.CharField(choices=[('일반', '일반'), ('법인', '법인'), ('기타', '기타')], default='일반', max_length=64, verbose_name='회원구분')),
                ('status', models.CharField(choices=[('정상', '정상'), ('해지', '해지'), ('유예', '유예')], default='정상', max_length=64, verbose_name='회원상태')),
                ('address', models.TextField(verbose_name='주소')),
                ('level', models.CharField(choices=[('admin', 'admin'), ('user', 'user')], max_length=8, verbose_name='등급')),
                ('last_use_dttm', models.DateTimeField(auto_now_add=True, verbose_name='최근사용시간')),
                ('register_dttm', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
            ],
            options={
                'verbose_name': '사용자',
                'verbose_name_plural': '사용자',
                'db_table': 'evsp_evuser',
            },
        ),
    ]
