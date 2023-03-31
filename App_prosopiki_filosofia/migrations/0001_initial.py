# Generated by Django 4.1 on 2023-03-30 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=20)),
                ("subtitulo", models.CharField(max_length=40)),
                ("cuerpo", models.TextField()),
                ("autor", models.CharField(max_length=20)),
                ("fecha", models.DateTimeField()),
                ("imagen", models.ImageField(upload_to="img_post")),
            ],
        ),
    ]