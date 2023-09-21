# console/management/commands/populate_classified_data.py
import random
from django.core.management.base import BaseCommand
from ...models import ClassifiedWaterFlowData

ARBITRARY_LOSS_MIN = 300  # Set your minimum arbitrary loss value here
ARBITRARY_LOSS_MAX = 400  # Set your maximum arbitrary loss value here


class Command(BaseCommand):
    help = 'Populate classified data with random values'

    def handle(self, *args, **kwargs):
        classified_data = ClassifiedWaterFlowData.objects.all()

        for data in classified_data:
            # Generate random values for the new fields
            data.system_input_volume = round(random.uniform(9000, 10000), 2)
            data.build_consumer = round(random.uniform(7500, 9000), 2)
            
            # Calculate the Non-Revenue Water
            data.non_revenue_water = round(data.system_input_volume - data.build_consumer, 2)
            
            # Calculate unauthorized consumption
            data.unauthorised_consumption = round(float(data.non_revenue_water) - float(data.total_real_losses), 2)

            # Calculate arbitrary loss based on the specified range
            data.arbitrary_loss = round(min(max(2 / 5 * data.unauthorised_consumption, ARBITRARY_LOSS_MIN), ARBITRARY_LOSS_MAX),2)
            
            data.save()

        self.stdout.write(self.style.SUCCESS('Classified data populated with random values'))
