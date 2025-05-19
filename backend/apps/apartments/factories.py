import factory
from apps.apartments.models import Apartment
from factory import Faker, SubFactory
from apps.users.factories import UserFactory

class ApartmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Apartment

    name = Faker('sentence', nb_words=3)
    description = Faker('paragraph')
    price = Faker('pydecimal', left_digits=5, right_digits=2, positive=True)
    number_of_rooms = Faker('random_int', min=1, max=5)
    square = Faker('pydecimal', left_digits=4, right_digits=2, positive=True)
    availability = True
    owner = SubFactory(UserFactory)
