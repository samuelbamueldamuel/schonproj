# Generated by Django 4.2.4 on 2023-09-17 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scone', '0003_remove_companyy_id_companyy_name_companyy_symbol'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyy',
            name='CT',
        ),
        migrations.RemoveField(
            model_name='companyy',
            name='ESG',
        ),
        migrations.RemoveField(
            model_name='companyy',
            name='EV',
        ),
        migrations.RemoveField(
            model_name='companyy',
            name='FS',
        ),
        migrations.RemoveField(
            model_name='companyy',
            name='NH',
        ),
        migrations.CreateModel(
            name='NatureHarmony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='NHcompany', to='scone.companyy')),
            ],
        ),
        migrations.CreateModel(
            name='FeldScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FScompany', to='scone.companyy')),
            ],
        ),
        migrations.CreateModel(
            name='ESG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ESGcompany', to='scone.companyy')),
            ],
        ),
        migrations.CreateModel(
            name='EcoVitality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='EVompany', to='scone.companyy')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyTurnover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CTcompany', to='scone.companyy')),
            ],
        ),
    ]
