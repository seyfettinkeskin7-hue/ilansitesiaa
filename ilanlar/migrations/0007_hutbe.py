from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('ilanlar', '0006_haber_alter_ilanmedya_dosya'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hutbe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=200)),
                ('tarih', models.DateField()),
                ('normal_pdf', models.FileField(upload_to='hutbeler/')),
                ('telefon_pdf', models.FileField(upload_to='hutbeler/')),
                ('aktif', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-tarih'],
            },
        ),
    ]
