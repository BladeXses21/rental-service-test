from django.core.management.base import BaseCommand
from apps.users.factories import UserFactory
from apps.apartments.factories import ApartmentFactory

class Command(BaseCommand):
    help = 'Create test users and apartments'

    def add_arguments(self, parser):
        parser.add_argument(
            '--users',
            type=int,
            default=5,
            help='Number of users to create',
        )
        parser.add_argument(
            '--apartments',
            type=int,
            default=10,
            help='Number of apartments to create',
        )

    def handle(self, *args, **options):
        users_count = options['users']
        apartments_count = options['apartments']

        self.stdout.write(f'Creating {users_count} users...')
        users = UserFactory.create_batch(users_count)
        self.stdout.write('Users created.')

        self.stdout.write(f'Creating {apartments_count} apartments...')

        for _ in range(apartments_count):
            ApartmentFactory(owner=self._random_choice(users))
        self.stdout.write('Apartments created.')

    def _random_choice(self, users):
        import random
        return random.choice(users)
