import factory
from django.contrib.auth import get_user_model

User = get_user_model()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker('email')
    is_active = True
    is_staff = False
    is_superuser = False

    @factory.post_generation
    def set_password(obj, create, extracted, **kwargs):
        obj.set_password('password123')
        if create:
            obj.save()
