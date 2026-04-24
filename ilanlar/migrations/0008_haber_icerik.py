from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('ilanlar', '0007_hutbe'),
    ]

    operations = [
        migrations.AddField(
            model_name='haber',
            name='icerik',
            field=models.TextField(blank=True),
        ),
    ]
