# Generated by Django 5.0.6 on 2024-10-09 03:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EngagementPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_id', models.IntegerField()),
                ('post_content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EngagementPostCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration_in_seconds', models.IntegerField()),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.collection')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.engagementpost')),
            ],
        ),
        migrations.CreateModel(
            name='EngagementPostContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_url', models.URLField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.engagementpost')),
            ],
        ),
        migrations.CreateModel(
            name='EngagementPostProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('product_image', models.CharField(max_length=255)),
                ('sku', models.CharField(max_length=255)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.engagementpost')),
            ],
        ),
    ]
