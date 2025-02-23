from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from contracts.models import Contract
from django.utils.timezone import now
from datetime import timedelta

class Command(BaseCommand):
    help = 'Send email reminders for contracts nearing expiration'

    def handle(self, *args, **kwargs):
        today = now().date()
        upcoming_contracts = Contract.objects.filter(end_date__lte=today + timedelta(days=7))

        for contract in upcoming_contracts:
            send_mail(
                subject=f'Reminder: Contract "{contract.name}" is nearing expiration',
                message=f'The contract "{contract.name}" will expire on {contract.end_date}. Please take necessary actions.',
                from_email='mirahnilamterminal@gmail.com',  # Ganti dengan email Anda
                recipient_list=['peluangusahadimedan@gmail.com'],  # Ganti dengan penerima
            )
            self.stdout.write(f'Email reminder sent for contract: {contract.name}')
