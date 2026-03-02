from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

def register(request, params):
    username = params.get("username")
    password = params.get("password")
    email = params.get("email")

    is_active = params.get("is_active", True)

    if not username or not password:
        return {"status": False, "error": "Логин и пароль обязательны!"}

    if len(username) < 5:
        return {"status": False, "error": "Слишком короткое имя. Нужно минимум 5 символов."}

    if len(password) < 5:
        return {"status": False, "error": "Слабый пароль, давай от 5 символов и больше."}

    check_user = User.objects.filter(username=username).first()
    if check_user:
        return {"status": False, "error": "Такой юзер уже есть в базе. Придумай другой логин."}

    # Создаем обычного юзера
    new_user = User.objects.create_user(
        username=username,
        email=email,
        password=password
    )

    # Присваиваем статусы (ты молодец, что закрыл доступ к админке)
    new_user.is_active = is_active
    new_user.is_staff = False
    new_user.is_superuser = False

    # Сохраняем
    new_user.save()

    token, created = Token.objects.get_or_create(user=new_user)

    return {
        "status": True,
        "message": "Ура! Успешно зарегистрировались!",
        "token": token.key,
        "username": new_user.username,
        "is_active": new_user.is_active
    }