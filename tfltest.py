import requests

def parse_journey(journey):
    legs = journey.get('legs', [])
    duration = journey.get('duration', 0)
    start_time = journey.get('startDateTime', '')
    arrival_time = journey.get('arrivalDateTime', '')
    mode = journey.get('mode', {}).get('name', '')
    
    print(f"Journey Details:")
    print(f"  Mode of Transportation: {mode}")
    print(f"  Start Time: {start_time}")
    print(f"  Arrival Time: {arrival_time}")
    print(f"  Total Duration: {duration} minutes")
    
    for leg in legs:
        instruction = leg.get('instruction', {}).get('summary', '')
        departure_point = leg.get('departurePoint', {}).get('commonName', '')
        arrival_point = leg.get('arrivalPoint', {}).get('commonName', '')
        leg_duration = leg.get('duration', 0)
        
        print(f"\n  Leg Details:")
        print(f"    Instruction: {instruction}")
        print(f"    Departure Point: {departure_point}")
        print(f"    Arrival Point: {arrival_point}")
        print(f"    Duration: {leg_duration} minutes")

def get_route(from_stop, to_stop):
    # Construct the API URL with start and end stops
    url = f"https://api.tfl.gov.uk/Journey/JourneyResults/{from_stop}/to/{to_stop}"
    
    # Make the HTTP GET request
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Return the response data
        return response.json()
    else:
        # Print error message if request failed
        print(f"Error: {response.status_code}")
        return None

# Example usage: Get route from Hammersmith to Waterloo
from_stop = "SE17AD"
to_stop = "W60PJ"
route = get_route(from_stop, to_stop)

if route:
    for r in route:
        parse_journey(r)
else:
    print("No routes found.")