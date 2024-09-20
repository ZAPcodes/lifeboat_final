import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

@csrf_exempt
def receive_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Get the JSON data from the request
            heart_rate = data.get('heart_rate')
            spo2 = data.get('spo2')
            body_temp = data.get('body_temp')

            # Store the data in the session for temporary access
            request.session['sensor_data'] = {
                'heart_rate': heart_rate,
                'spo2': spo2,
                'body_temp': body_temp
            }

            # Send a success response
            return JsonResponse({'status': 'success', 'message': 'Data received'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

def display_data(request):
    # Retrieve the sensor data from the session
    sensor_data = request.session.get('sensor_data', None)

    # Render the data to a template (or display a message if no data is available)
    return render(request, 'dashboard.html', {'data': sensor_data})
