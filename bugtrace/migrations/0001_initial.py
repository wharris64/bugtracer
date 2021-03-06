# Generated by Django 2.2.7 on 2019-11-26 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('ticket_status', models.CharField(max_length=2)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('ticket_assignee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticketassignee', to=settings.AUTH_USER_MODEL)),
                ('ticket_finisher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticketfinisher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
