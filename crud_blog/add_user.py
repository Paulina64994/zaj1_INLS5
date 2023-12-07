# add_user.py
import os
import django
from django.contrib.auth import authenticate, login

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zaj1_INLS5.settings")
django.setup()

from myapp.models import CustomUser

# add_user.py
def add_user(username, password, email):
    user = CustomUser.objects.create_user(username=username, password=password, email=email)
    print(f"Użytkownik {user.username} został dodany do bazy danych.")

    # Logowanie użytkownika po utworzeniu
    user = authenticate(username=username, password=password)
    if user is not None:
        login(user)
        print(f"Użytkownik {user.username} został zalogowany.")
    else:
        print("Błąd logowania.")