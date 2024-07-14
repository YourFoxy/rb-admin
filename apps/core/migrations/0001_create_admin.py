from django.contrib.auth import get_user_model
from django.db import migrations


def create_superuser(_apps, _schema_editor):
    User = get_user_model()
    User.objects.create_superuser(
        username="admin",
        email="admin@mail.ru",
        password="Ey1uzFi4Y8stOo7VF1u8CpnshO0=",
    )


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.RunPython(create_superuser),
    ]
