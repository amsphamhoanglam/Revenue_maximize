# Theater operating hours
operating_hours = {
    'Monday': {'start': 18.00, 'end': 23.00},
    'Tuesday': {'start': 18.00, 'end': 23.00},
    'Wednesday': {'start': 18.00, 'end': 23.00},
    'Thursday': {'start': 18.00, 'end': 23.00},
    'Friday': {'start': 18.00, 'end': 24.00},
    'Saturday': {'start': 9.00, 'end': 24.00},
    'Sunday': {'start': 9.00, 'end': 23.00}
}

# Durations of the movies in minutes
action_duration = 117
romantic_duration = 78
horror_duration = 93

# Convert movie durations from minutes to hours
action_duration /= 60
romantic_duration /= 60
horror_duration /= 60

# Calculate the number of showtimes for each day
showtimes_per_day = {}

for day, hours in operating_hours.items():
    start_time = hours['start']
    end_time = hours['end']

    # Calculate the available time for movie screenings considering breaks
    available_time = end_time - start_time - 10 * (showtimes_per_day.get(day, 0) - 1)

    if day in ['Friday', 'Saturday']:
        min_duration = min(action_duration, romantic_duration, horror_duration)
        max_duration = max(action_duration, romantic_duration, horror_duration)

        if available_time >= max_duration:
            showtimes_per_day[day] = int(available_time // min_duration) + 1
        else:
            showtimes_per_day[day] = int(available_time // min_duration)
    else:
        showtimes_per_day[day] = int(available_time // action_duration)

# Print the calculated showtimes for each day
for day, showtimes in showtimes_per_day.items():
    print(f"{day}: {showtimes} showtimes")