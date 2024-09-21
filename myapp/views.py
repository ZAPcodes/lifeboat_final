import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

# Global variable to temporarily hold heart rate data
latest_heart_rate = None

@csrf_exempt
def receive_data(request):
    global latest_heart_rate  # Use the global variable to store the latest heart rate
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request
            data = json.loads(request.body)
            heart_rate = data.get('heart_rate')  # Only heart rate is sent

            # Update the global variable with the latest heart rate
            latest_heart_rate = heart_rate

            # Send a success response
            return JsonResponse({
                'status': 'success',
                'message': 'Heart rate data received',
                'heart_rate': latest_heart_rate  # Include heart rate in response
            })
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

def display_data(request):
    global latest_heart_rate  # Access the global variable to get the latest heart rate data
    sensor_data = {
        'heart_rate': latest_heart_rate,
    } if latest_heart_rate else None  # Only pass data if it's available

    # Render the data to the template
    return render(request, 'dashboard.html', {'data': sensor_data})
