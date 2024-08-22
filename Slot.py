from datetime import datetime

# Sample data for charging stations
charging_stations = [
    {"id": 1, "location": "Downtown", "type": "Fast", "available_slots": 5},
    {"id": 2, "location": "Uptown", "type": "Standard", "available_slots": 3},
    {"id": 3, "location": "Suburbs", "type": "Fast", "available_slots": 2},
    {"id": 4, "location": "City Center", "type": "Standard", "available_slots": 0},
]

def find_stations(filter_type=None):
    """Find and list charging stations with optional filter for type."""
    stations = charging_stations
    if filter_type:
        stations = [station for station in stations if station["type"] == filter_type]

    if not stations:
        print("No charging stations found.")
    else:
        for station in stations:
            print(f"Station ID: {station['id']}, Location: {station['location']}, "
                  f"Type: {station['type']}, Available Slots: {station['available_slots']}")

def book_slot(station_id, time_slot):
    """Book a charging slot at a specific station."""
    station = next((s for s in charging_stations if s["id"] == station_id), None)
    if not station:
        print("Station not found.")
        return
    
    if station["available_slots"] > 0:
        # Assuming time_slot is validated elsewhere
        station["available_slots"] -= 1
        print(f"Slot booked at {station['location']} for {time_slot}.")
    else:
        print("No available slots at this station.")

# Example usage:

# Find all fast charging stations
print("Fast charging stations:")
find_stations(filter_type="Fast")

# Book a slot at station with ID 1
print("\nBooking a slot at station ID 1:")
book_slot(1, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Find all stations after booking
print("\nAll stations after booking:")
find_stations()
