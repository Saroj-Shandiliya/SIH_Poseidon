# console/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import AuthenticationForm
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from .models import ClassifiedWaterFlowData
from django.db import models
from django.http import FileResponse
from django.db.models import Sum, F, IntegerField
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image,
    PageBreak,
)
from reportlab.lib.styles import getSampleStyleSheet
from operator import itemgetter
import pandas as pd
from django.http import FileResponse
import numpy as np
import matplotlib
matplotlib.use('Agg')
from django.http import JsonResponse
from django.db.models.functions import ExtractYear, ExtractMonth

def console_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            zoneID = form.cleaned_data.get('username')  # Use 'username' for zoneID
            secretKey = form.cleaned_data.get('password')  # Use 'password' for secretKey
            user = authenticate(request, username=zoneID, password=secretKey)
            if user is not None:
                login(request, user)
                return redirect('http://localhost:3000/dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'console/console_login.html', {'form': form})

# from django.contrib.auth import authenticate, login
# from django.http import JsonResponse

# def console_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             request.session['is_authenticated'] = True
#             return JsonResponse({'isAuthenticated': True})
#         else:
#             print('Authentication failed')
#     return JsonResponse({'isAuthenticated': False})



def console_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('console_login')

    # Load data from the CSV file
    csv_file = 'console/static/csv/Data.csv'
    data = pd.read_csv(csv_file)

    # Perform data analysis and create plots
    # Example: Creating a bar plot
    plt.figure(figsize=(10, 6))
    plt.bar(data['Month'], data['Real Losses (in cubic meters)'])
    plt.xlabel('Month')
    plt.ylabel('Real Losses (in cubic meters)')
    plt.title('Real Losses Over Months')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Convert the plot to a base64-encoded image
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data_uri = base64.b64encode(buffer.read()).decode()
    buffer.close()

    # Pass the plot data to the template
    context = {'plot_data_uri': plot_data_uri}
    return render(request, 'console/console_dashboard.html', context)


def outgoing_flow(request):
    # Generate synthetic data for Normal flow, Expected flow, and Real-time flow
    x_values = np.linspace(0, 24, 100)  # Time range (hours)
    normal_flow = np.random.uniform(10.1, 10.8, 100)  # Normal flow data
    expected_flow = np.random.uniform(10.1, 10.8, 100)  # Expected flow data
    real_time_flow = np.random.uniform(10.1, 10.8, 100)  # Real-time flow data

    # Ensure Normal flow < Expected flow < Real-time flow
    normal_flow.sort()
    expected_flow.sort()
    real_time_flow.sort()

    # Create a line chart
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, normal_flow, marker='o', label='Normal Flow', color='blue')
    plt.plot(x_values, expected_flow, marker='o', label='Expected Flow', color='green')
    plt.plot(x_values, real_time_flow, marker='o', label='Real-time Flow', color='red')
    plt.xlabel('Time (hours)')
    plt.ylabel('Flow Rate')
    plt.title('Outgoing Flow Analysis')
    plt.legend()
    plt.grid(True)

    # Save the line chart as an image
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    response = FileResponse(img, content_type='image/png')
    return response
def calculate_mean_values(request):
    # Generate synthetic data for Normal flow, Expected flow, and Real-time flow
    x_values = np.linspace(0, 24, 100)  # Time range (hours)
    normal_flow = np.random.uniform(10.1, 10.8, 100)  # Normal flow data
    expected_flow = np.random.uniform(10.1, 10.8, 100)  # Expected flow data
    real_time_flow = np.random.uniform(10.1, 10.8, 100)  # Real-time flow data

    # Ensure Normal flow < Expected flow < Real-time flow
    normal_flow.sort()
    expected_flow.sort()
    real_time_flow.sort()

    # Calculate the mean values
    normal_flow_mean = round(np.mean(normal_flow),3)
    expected_flow_mean = round(np.mean(expected_flow),3)
    real_time_flow_mean = round(np.mean(real_time_flow),3)

    # Create a dictionary with the mean values
    mean_values = {
        'normal_flow_mean': normal_flow_mean,
        'expected_flow_mean': expected_flow_mean,
        'real_time_flow_mean': real_time_flow_mean,
    }

    return JsonResponse(mean_values)

# console/views.py
def incoming_flow(request):
    
    # Generate synthetic data for Normal flow, Expected flow, and Real-time flow
    x_values = np.linspace(0, 24, 100)  # Time range (hours)
    normal_flow = np.random.uniform(10.2, 10.5, 100)  # Normal flow data
    expected_flow = np.random.uniform(10.2, 10.5, 100)  # Expected flow data
    real_time_flow = np.random.uniform(10.2, 10.5, 100)  # Real-time flow data

    # Ensure Normal flow < Expected flow < Real-time flow
    normal_flow.sort()
    expected_flow.sort()
    real_time_flow.sort()

    # Create a line chart
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, normal_flow, marker='o', label='Normal Flow', color='blue')
    plt.plot(x_values, expected_flow, marker='o', label='Expected Flow', color='green')
    plt.plot(x_values, real_time_flow, marker='o', label='Real-time Flow', color='red')
    plt.xlabel('Time (hours)')
    plt.ylabel('Flow Rate')
    plt.title('Incoming Flow Analysis')
    plt.legend()
    plt.grid(True)

    # Save the line chart as an image
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    response = FileResponse(img, content_type='image/png')
    return response


## For checking
##################################################################################################################################


def classified_data_view(request):
    # classified_data = ClassifiedWaterFlowData.objects.all()  # Fetch all the classified data
    classified_data = ClassifiedWaterFlowData.objects.order_by('year', 'month')
    return render(request, 'console/classified_data.html', {'classified_data': classified_data})


def generate_non_revenue_water_plot():
    # Retrieve data from the database
    data = ClassifiedWaterFlowData.objects.all()

    # Group data by year and month and calculate the total non-revenue water
    non_revenue_water_data = data.values('year', 'month').annotate(total_non_revenue_water=models.Sum('non_revenue_water'))

    # Extract years and months from the data
    years = [entry['year'] for entry in non_revenue_water_data]
    months = [entry['month'] for entry in non_revenue_water_data]

    # Calculate the total non-revenue water for each month
    total_non_revenue_water = [entry['total_non_revenue_water'] for entry in non_revenue_water_data]

    # Create the plot
    plt.figure(figsize=(12, 6))
    plt.bar(range(len(months)), total_non_revenue_water)
    plt.xticks(range(len(months)), months, rotation=45)
    plt.xlabel('Month')
    plt.ylabel('Total Non-Revenue Water')
    plt.title('Total Non-Revenue Water per Month')
    
    # Save the plot as an image
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_data_uri = base64.b64encode(img.read()).decode()

    return plot_data_uri


import matplotlib.pyplot as plt
import mpld3
from django.shortcuts import render

def generate_line_chart(request):
    # Retrieve data from the database
    data = ClassifiedWaterFlowData.objects.all()

    # Extract system input volume and build consumer data
    system_input_volume = data.values_list('system_input_volume', flat=True)
    build_consumer = data.values_list('build_consumer', flat=True)

    # Create a Matplotlib line chart
    plt.figure(figsize=(8,6 ))
    plt.plot(system_input_volume, label='System Input Volume', marker='o')
    plt.plot(build_consumer, label='Billed Consumer', marker='x')
    plt.xlabel('Month')
    plt.ylabel('Volume')
    plt.title('System Input Volume vs. Billed Consumer')
    # plt.legend()

    # Convert the Matplotlib plot to an interactive HTML representation
    chart_html = mpld3.fig_to_html(plt.gcf())

    # Save the line chart as an image
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Create a FileResponse for the image
    response = FileResponse(img, content_type='image/png')
    return response

import json
def generate_insights_report(request):
    # JSON data provided
    json_data = '''
    {
        "title": "Water Flow Insights Report",
        "total_non_revenue_water": {
            "value": 72336,
            "description": "Total Non-Revenue Water for the entire dataset."
        },
        "total_real_losses": {
            "value": 111737,
            "description": "Total Real Losses for the entire dataset."
        },
        "insights_by_year": [
            {
                "year": 2018,
                "total_non_revenue_water": 11940,
                "total_real_losses": 8980
            },
            {
                "year": 2019,
                "total_non_revenue_water": 14541,
                "total_real_losses": 9065
            },
            {
                "year": 2020,
                "total_non_revenue_water": 10582,
                "total_real_losses": 9302
            },
            {
                "year": 2021,
                "total_non_revenue_water": 14603,
                "total_real_losses": 9263
            },
            {
                "year": 2022,
                "total_non_revenue_water": 11181,
                "total_real_losses": 9107
            },
            {
                "year": 2023,
                "total_non_revenue_water": 9487,
                "total_real_losses": 66020
            }
        ]
    }
    '''

    # Parse the JSON data
    data = json.loads(json_data)

    # Extract relevant data
    years = [entry['year'] for entry in data['insights_by_year']]
    non_revenue_water_values = [entry['total_non_revenue_water'] for entry in data['insights_by_year']]
    real_losses_values = [entry['total_real_losses'] for entry in data['insights_by_year']]

    # Create a bar graph year-wise
    plt.figure(figsize=(12, 6))
    plt.bar(years, non_revenue_water_values, width=0.4, label='Total Non-Revenue Water', align='center')
    plt.bar(years, real_losses_values, width=0.4, label='Total Real Losses', align='edge')
    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.title(data['title'])
    plt.legend()
    plt.grid(True)

    # Save the plot as an image
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Return the image as a response
    response = FileResponse(img, content_type='image/png')
    return response


# ... (Other functions and imports)

def generate_pie_chart(request):
    # Retrieve data from the database
    data = ClassifiedWaterFlowData.objects.all()

    # Calculate the total values while handling negative values
    total_non_revenue_water = max(data.aggregate(total_non_revenue_water=models.Sum('non_revenue_water'))['total_non_revenue_water'] or 0, 0)
    total_real_losses = max(data.aggregate(total_real_losses=models.Sum('total_real_losses'))['total_real_losses'] or 0, 0)
    total_arbitrary_loss = max(data.aggregate(total_arbitrary_loss=models.Sum('arbitrary_loss'))['total_arbitrary_loss'] or 0, 0)
    # total_unauthorised_consumption = max(data.aggregate(total_unauthorised_consumption=models.Sum('unauthorised_consumption'))['total_unauthorised_consumption'] or 0, 0)

    # Create a pie chart
    labels = ['Non-Revenue Water', 'Real Losses', 'Arbitrary Loss']
    sizes = [total_non_revenue_water, total_real_losses, total_arbitrary_loss]
    colors = ['#ff9999', '#66b3ff', '#99ff99']

    plt.figure(figsize=(9, 5))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title('Distribution of Water Loss Components')

    # Save the pie chart as an image
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    # pie_chart_data_uri = base64.b64encode(img.read()).decode()
    # return pie_chart_data_uri
    response = FileResponse(img,content_type='image/png')
    return response

def generate_pie_chart_insights(request):
    # Retrieve data from the database
    data = ClassifiedWaterFlowData.objects.all()

    # Calculate the total values while handling negative values
    total_non_revenue_water = round(max(data.aggregate(total_non_revenue_water=models.Sum('non_revenue_water'))['total_non_revenue_water'] or 0, 0),3)
    total_real_losses = max(data.aggregate(total_real_losses=models.Sum('total_real_losses'))['total_real_losses'] or 0, 0)
    total_arbitrary_loss = max(data.aggregate(total_arbitrary_loss=models.Sum('arbitrary_loss'))['total_arbitrary_loss'] or 0, 0)

    # Calculate insights
    insights = {
        'Non-Revenue Water': total_non_revenue_water,
        'Real Losses': total_real_losses,
        'Arbitrary Loss': total_arbitrary_loss,
    }

    return JsonResponse(insights)  


def demo(request):
    # Generate plots
    non_revenue_water_plot = generate_non_revenue_water_plot()
    pie_chart = generate_pie_chart(request)
    line_chart = generate_line_chart()

    return render(request, 'console/demo.html', {
        'non_revenue_water_plot': non_revenue_water_plot,
        'pie_chart': pie_chart,
        'line_chart': line_chart,
    })
    

# Define a mapping between month names and their corresponding numeric values
month_mapping = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12,
}

def generate_report(request):
    # Retrieve data from the database
    data = ClassifiedWaterFlowData.objects.order_by('year', 'month')

    # Calculate insights
    total_non_revenue_water = data.aggregate(Sum('non_revenue_water'))['non_revenue_water__sum']
    total_real_losses = data.aggregate(Sum('total_real_losses'))['total_real_losses__sum']

    # Create a Pandas DataFrame for data manipulation
    df = pd.DataFrame(list(data.values()))

    # Convert the month names to corresponding numeric values using the mapping
    df['month'] = df['month'].map(month_mapping)

    # Sort the data by year and month
    df = df.sort_values(by=['year', 'month'])

    # Create a PDF document
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    # Define styles for text using ReportLab
    styles = getSampleStyleSheet()
    normal_style = styles['Normal']
    title_style = styles['Title']

    # Add a title to the PDF
    elements.append(Paragraph("Water Flow Data Report", title_style))

    # Add structured data to the PDF
    data_table = [['Year', 'Month', 'Non-Revenue Water', 'Total Real Losses']]
    for index, row in df.iterrows():
        data_table.append([row['year'], row['month'], row['non_revenue_water'], row['total_real_losses']])

    table = Table(data_table)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), (0.7, 0.7, 0.7)),
        ('TEXTCOLOR', (0, 0), (-1, 0), (0, 0, 0)),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), (0.95, 0.95, 0.95)),
        ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)),
    ]))

    elements.append(table)
    elements.append(Spacer(1, 12))  # Add space between table and insights

    # Add insights to the PDF
    elements.append(Paragraph("Insights:", normal_style))
    elements.append(Paragraph(f"Total Non-Revenue Water: {total_non_revenue_water}", normal_style))
    elements.append(Paragraph(f"Total Real Losses: {total_real_losses}", normal_style))

    # Generate additional plots

    # Create a bar chart for total non-revenue water and total real losses
    plt.figure(figsize=(8, 4))
    plt.bar(['Non-Revenue Water', 'Real Losses'], [total_non_revenue_water, total_real_losses], color=['blue', 'red'])
    plt.xlabel('Category')
    plt.ylabel('Amount')
    plt.title('Comparison of Non-Revenue Water and Real Losses')
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    chart_image = Image(img_buffer, width=400, height=250)
    elements.append(chart_image)

    # Add a page break before the next chart
    elements.append(PageBreak())

    # Create a line chart for System Input Volume and billed Consumer
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['system_input_volume'], label='System Input Volume', marker='o')
    plt.plot(df.index, df['build_consumer'], label='billed Consumer', marker='x')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.title('System Input Volume vs. billed Consumer')
    plt.xticks(rotation=45)
    plt.legend()
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    chart_image = Image(img_buffer, width=600, height=350)
    elements.append(chart_image)

    # Build the PDF document
    doc.build(elements)
    buffer.seek(0)

    # Return the PDF as a response
    response = FileResponse(buffer, as_attachment=True, filename='report.pdf')
    return response



from rest_framework import generics
# from .models import ClassifiedWaterFlowData
from .serializers import ClassifiedWaterFlowDataSerializer

# ... Other code remains the same ...

class ClassifiedWaterFlowDataListCreateView(generics.ListCreateAPIView):
    queryset = ClassifiedWaterFlowData.objects.all()
    serializer_class = ClassifiedWaterFlowDataSerializer


