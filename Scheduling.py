import itertools

# Các thông tin về phim và lịch chiếu
films = [
    {"name": "Tình yêu mùa hè", "duration": 78, "price": 120000, "rating": 75},
    {"name": "Thám tử tập sự", "duration": 93, "price": 150000, "rating": 90},
    {"name": "Truy tìm cổ vật", "duration": 117, "price": 150000, "rating": 80}
]

# Thời gian mở cửa và đóng cửa trong mỗi ngày
opening_time = {"Mon": "18:00", "Tue": "18:00", "Wed": "18:00", "Thu": "18:00", "Fri": "18:00", "Sat": "09:00", "Sun": "09:00"}
closing_time = {"Mon": "23:00", "Tue": "23:00", "Wed": "23:00", "Thu": "23:00", "Fri": "00:00", "Sat": "00:00", "Sun": "23:00"}

#Thông tin phòng chiếu
room = {"Room 1", "Room 2", "Room 3", "Room 4"}
# Sức chứa của các phòng chiếu
room_capacities = {"Room 1": 120, "Room 2": 100, "Room 3": 60, "Room 4": 60}

# Thời gian nghỉ giữa các lần chiếu
intermission_times = {"Room 1": 10, "Room 2": 9, "Room 3": 8, "Room 4": 8}

# Tính toán tổng số tiền thu được cho một lịch chiếu
def calculate_total_revenue(schedule):
    total_revenue = 0
    for film in films:
        for showtime in room:
            if film["name"] == "Thám tử tập sự" and film["name"] in showtime:  # Ưu tiên phim 2
                total_revenue += film["price"]
            elif film["name"] == "Tình yêu mùa hè" and film["name"] in showtime:  # Sau đó là phim 1
                total_revenue += film["price"]
            elif film["name"] == "Truy tìm cổ vật" and film["name"] in showtime:  # Cuối cùng là phim 3
                total_revenue += film["price"]      
    return total_revenue


# Tạo tất cả các lịch chiếu có thể
all_schedules = list(itertools.product(
    itertools.permutations(["Thám tử tập sự", "Tình yêu mùa hè", "Truy tìm cổ vật"]),
    itertools.permutations(["Room 1", "Room 2", "Room 3", "Room 4"])
))

# Chọn ra 4 lịch chiếu có tổng số tiền thu được cao nhất
top_4_schedules = sorted(all_schedules, key=lambda schedule: calculate_total_revenue(schedule), reverse=True)[:4]

# In kết quả
for i, schedule in enumerate(top_4_schedules):
    print(f"Lịch chiếu {i+1}:")
    for j, (film, room) in enumerate(zip(schedule[0], schedule[1])):
        print(f"Phim {j+1}: {film} - Phòng chiếu: {room}")
    print(f"Tổng số tiền thu được: {calculate_total_revenue(schedule)}")
    print()
