import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

@csrf_exempt
def receive_data(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request
            data = json.loads(request.body)
            heart_rate = data.get('heart_rate')  # Only heart rate is sent

            # Store the data in the session for temporary access
            request.session['sensor_data'] = {
                'heart_rate': heart_rate,
            }

            # Send a success response
            return JsonResponse({'status': 'success', 'message': 'Heart rate data received'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

def display_data(request):
    # Retrieve the heart rate data from the session
    sensor_data = request.session.get('sensor_data', None)

    # Render the data to a template (or display a message if no data is available)
    return render(request, 'dashboard.html', {'data': sensor_data})
