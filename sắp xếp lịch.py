from datetime import datetime, timedelta

# Thông tin phim
films = [
    {"name": "Tình yêu mùa hè", "duration": timedelta(hours=1, minutes=18), "price": 120000},
    {"name": "Thám tử tập sự", "duration": timedelta(hours=1, minutes=33), "price": 150000},
    {"name": "Truy tìm cổ vật", "duration": timedelta(hours=1, minutes=57), "price": 150000}
]

# Thời gian hoạt động của rạp từ thứ 2 đến chủ nhật
schedule = {
    "Monday": {"open": "6:00 PM", "close": "11:00 PM"},
    "Tuesday": {"open": "6:00 PM", "close": "11:00 PM"},
    "Wednesday": {"open": "6:00 PM", "close": "11:00 PM"},
    "Thursday": {"open": "6:00 PM", "close": "11:00 PM"},
    "Friday": {"open": "6:00 PM", "close": "12:00 AM"},
    "Saturday": {"open": "9:00 AM", "close": "10:30 PM"},
    "Sunday": {"open": "9:00 AM", "close": "9:30 PM"}
}

# Sức chứa tối đa của các phòng chiếu
room_capacities = {
    "Room 1": 120,
    "Room 2": 100,
    "Room 3": 60,
    "Room 4": 60
}

# Thời gian nghỉ giữa 2 lần chiếu phim
break_times = [10, 9, 8, 8]

# Xếp lịch chiếu cho từng ngày trong tuần từ thứ 2 đến chủ nhật
for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
    print(f"Lịch chiếu cho ngày {day}:")
    showtime = datetime.strptime(schedule[day]["open"], "%I:%M %p")
    
    for _ in range(4):
        film = films[_ % len(films)]
        duration = film["duration"]
        room = None
        
        # Tìm phòng chiếu phù hợp cho phim
        for room_name, capacity in room_capacities.items():
            if capacity >= 1:
                room = room_name
                room_capacities[room_name] -= 1
                break
        
        # In thông tin lịch chiếu
        if room is not None:
            end_time = showtime + duration
            print(f"- Phim: {film['name']} - Phòng chiếu: {room}")
            print(f"  Khung thời gian: {showtime.strftime('%I:%M %p')} - {end_time.strftime('%I:%M %p')}")
            showtime = end_time + timedelta(minutes=break_times[_ % len(break_times)])
        else:
            print(f"- Phim: {film['name']} - Không có phòng chiếu trống")
    
    print(f"Giờ đóng cửa: {schedule[day]['close']}\n")
