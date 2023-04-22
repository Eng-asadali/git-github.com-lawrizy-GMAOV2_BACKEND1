# Generated by Django 4.2 on 2023-04-17 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WORKS', '0017_workorderstatusmodel_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkOrderArchiveModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('room', models.CharField(max_length=255)),
                ('job_type', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('equipment', models.CharField(blank=True, max_length=255, null=True)),
                ('reporter', models.CharField(max_length=255)),
                ('assignee', models.CharField(blank=True, max_length=255, null=True)),
                ('job', models.CharField(max_length=255)),
                ('domain', models.CharField(max_length=255)),
                ('creation_date', models.DateTimeField()),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AddIndex(
            model_name='workorderarchivemodel',
            index=models.Index(fields=['title', 'description', 'room', 'job_type', 'status', 'equipment', 'reporter', 'assignee', 'job', 'domain', 'creation_date', 'start_date', 'end_date'], name='work_order_archive_idx'),
        ),
    ]
