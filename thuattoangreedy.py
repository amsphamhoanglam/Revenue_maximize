def schedule_movies(movies, movie_durations, weekday_time_limit, weekend_time_limit):
    # Sắp xếp các bộ phim theo thứ tự thời lượng giảm dần
    sorted_movies = sorted(movies, key=lambda x: movie_durations[x], reverse=True)

    # Khởi tạo danh sách phòng chiếu và lịch chiếu rỗng
    theaters = ['Phòng 1', 'Phòng 2', 'Phòng 3', 'Phòng 4']
    schedules = {theater: [] for theater in theaters}

    # Lặp qua các bộ phim và thêm vào lịch chiếu phù hợp
    for movie in sorted_movies:
        duration = movie_durations[movie]
        scheduled = False

        # Kiểm tra các phòng chiếu
        for theater in theaters:
            schedule = schedules[theater]

            # Kiểm tra khung giờ tiếp theo cho ngày thường hoặc cuối tuần
            if theater.startswith('Phòng 4'):  # Nếu là ngày cuối tuần
                if sum([d[1] - d[0] for d in schedule]) + duration <= weekend_time_limit:
                    if schedule:
                        schedule.append((schedule[-1][1], schedule[-1][1] + duration))
                    else:
                        schedule.append((0, duration))
                    scheduled = True
                    break
            else:  # Nếu là ngày thường
                if sum([d[1] - d[0] for d in schedule]) + duration <= weekday_time_limit:
                    if schedule:
                        schedule.append((schedule[-1][1], schedule[-1][1] + duration))
                    else:
                        schedule.append((0, duration))
                    scheduled = True
                    break

        # Nếu không tìm thấy lịch chiếu phù hợp trong các phòng, thì thông báo không thể xếp lịch
        if not scheduled:
            print(f"Không thể xếp lịch cho bộ phim '{movie}'.")

    return schedules

# Các bộ phim và thông tin thời lượng của từng bộ phim
movies = ['Truy tìm cổ vật', 'Tình yêu mùa hè', 'Thám tử tập sự']
movie_durations = {'Truy tìm cổ vật': 117, 'Tình yêu mùa hè': 78, 'Thám tử tập sự': 93}

# Thời gian giới hạn cho mỗi loại ngày (phút)
weekday_time_limit = 840  # 14 giờ
weekend_time_limit = 900  # 15 giờ

# Lịch chiếu phim
schedules = schedule_movies(movies, movie_durations, weekday_time_limit, weekend_time_limit)

# In lịch chiếu phim
for theater, schedule in schedules.items():
    print(f'{theater}: {schedule}')