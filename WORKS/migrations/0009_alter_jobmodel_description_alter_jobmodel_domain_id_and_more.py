# Generated by Django 4.1.2 on 2022-12-06 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("WORKS", "0008_alter_workordermodel_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobmodel",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="jobmodel",
            name="domain_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="jobs",
                to="WORKS.domainmodel",
            ),
        ),
        migrations.AlterField(
            model_name="jobmodel",
            name="job_type_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="jobs",
                to="WORKS.jobtypemodel",
            ),
        ),
    ]
