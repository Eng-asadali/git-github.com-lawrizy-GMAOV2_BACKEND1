# Generated by Django 4.1.2 on 2023-01-08 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WORKS', '0013_alter_workordermodel_domain_alter_workordermodel_job_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='workstatusmodel',
            name='position',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddIndex(
            model_name='workordermodel',
            index=models.Index(fields=['title', 'description', 'room', 'job_type', 'status', 'equipment', 'reporter', 'assignee', 'job', 'domain', 'creation_date', 'start_date', 'end_date'], name='work_order_idx'),
        ),
        migrations.AddIndex(
            model_name='workorderstatusmodel',
            index=models.Index(fields=['work_order', 'event_date_time', 'status_before', 'status_after'], name='WORKS_worko_work_or_9c5441_idx'),
        ),
    ]
