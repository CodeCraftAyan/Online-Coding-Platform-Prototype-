from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Create admin automatically"

    def handle(self, *args, **kwargs):

        User = get_user_model()

        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                email="admin@example.com",
                password="admin123"
            )
            print("Superuser created")
        else:
            print("Superuser already exists")