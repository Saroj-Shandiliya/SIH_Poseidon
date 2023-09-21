# console/management/commands/classify_water_flow_data.py
from django.core.management.base import BaseCommand
from ...models import CSVData, ClassifiedWaterFlowData
from django.db.models import Sum
from django.db.models.functions import ExtractYear, ExtractMonth

class Command(BaseCommand):
    help = 'Classify and calculate water flow data'

    def handle(self, *args, **kwargs):
        classified_data = CSVData.objects.values(
            'year', 'month'
        ).annotate(
            total_real_losses=Sum('real_losses'),
            total_flow_analysis_central=Sum('flow_analysis_central'),
            total_flow_analysis_receive=Sum('flow_analysis_receive')
        ).order_by('year', 'month')

        for entry in classified_data:
            ClassifiedWaterFlowData.objects.create(
                year=entry['year'],
                month=entry['month'],
                total_real_losses=entry['total_real_losses'],
                total_flow_analysis_central=entry['total_flow_analysis_central'],
                total_flow_analysis_receive=entry['total_flow_analysis_receive']
            )

        self.stdout.write(self.style.SUCCESS('Data classified and calculated successfully'))
