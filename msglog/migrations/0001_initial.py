# Generated by Django 4.0.4 on 2022-07-02 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('evcharger', '0001_initial'),
        ('evuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Msglog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_direction', models.IntegerField(verbose_name='메세지오리진')),
                ('msg_name', models.CharField(max_length=128, verbose_name='메세지이름')),
                ('msg_content', models.TextField(verbose_name='메세지본문')),
                ('connection_id', models.IntegerField(verbose_name='커넥션아이디')),
                ('register_dttm', models.DateTimeField(auto_now_add=True, verbose_name='등록일시')),
                ('cpname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evcharger.evcharger', verbose_name='충전기번호')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evuser.evuser', verbose_name='사용자명')),
            ],
            options={
                'verbose_name': '충전로그정보',
                'verbose_name_plural': '충전로그정보',
                'db_table': 'evsp_msglog',
            },
        ),
    ]
