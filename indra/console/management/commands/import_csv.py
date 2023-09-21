# yourapp/management/commands/import_csv.py

from django.core.management.base import BaseCommand
import pandas as pd
from ...models import CSVData

class Command(BaseCommand):
    help = 'Import data from CSV'

    def handle(self, *args, **kwargs):
        csv_file = 'console/static/csv/Data.csv'
        data = pd.read_csv(csv_file)
        for _, row in data.iterrows():
            CSVData.objects.create(
                year=row['Year'],
                month=row['Month'],
                day=row['Day'],
                real_losses=row['Real Losses (in cubic meters)'],
                flow_analysis_central=row['flow analysis (central)'],
                flow_analysis_receive=row['flow analysis (receive)'],
                loss_analysis=row['Loss Analysis'],
                alert_analysis=row['Alert Analysis']
            )
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
