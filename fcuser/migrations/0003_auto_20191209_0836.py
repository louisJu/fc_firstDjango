# Generated by Django 3.0 on 2019-12-09 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0002_auto_20191209_0249'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fcuser',
            options={'verbose_name_plural': '사용자'},
        ),
        migrations.AddField(
            model_name='fcuser',
            name='user_email',
            field=models.EmailField(default='test1@gmail.com', max_length=128, verbose_name='e-mail'),
            preserve_default=False,
        ),
    ]
