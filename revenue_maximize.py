def optimize_schedule(movie_list, showtimes_matrix):
    # Khởi tạo mô hình tối ưu hóa
    model = gp.Model("MovieSchedule")

    # Tạo biến quyết định
    x = {}
    for movie_idx, movie in enumerate(movie_list):
        for day in range(len(showtimes_matrix)):
            for time in range(len(showtimes_matrix[day])):
                x[movie_idx, day, time] = model.addVar(vtype=GRB.BINARY, name=f"x_{movie_idx}_{day}_{time}")

    # Ràng buộc: Mỗi suất chiếu chỉ có thể chọn một bộ phim
    for day in range(len(showtimes_matrix)):
        for time in range(len(showtimes_matrix[day])):
            model.addConstr(gp.quicksum(x[movie_idx, day, time] for movie_idx in range(len(movie_list))) == 1)

    # Ràng buộc: Số lượng khán giả không vượt quá sức chứa của phòng chiếu
    for movie_idx, movie in enumerate(movie_list):
        for day in range(len(showtimes_matrix)):
            for time in range(len(showtimes_matrix[day])):
                model.addConstr(x[movie_idx, day, time] * movie.attendance <= showtimes_matrix[day][time])

    # Ràng buộc: Người trong nhóm 1 phải đi cùng đối tượng trong nhóm 2 hoặc 3
    for day in range(len(showtimes_matrix)):
        for time in range(len(showtimes_matrix[day])):
            for movie_idx in range(len(movie_list)):
                if movie_idx == 0:  # Chỉ áp dụng ràng buộc cho bộ phim đầu tiên (Truy tìm cổ vật)
                    model.addConstr(x[movie_idx, day, time] <= x[1, day, time] + x[2, day, time])

    # Hàm mục tiêu: Tối đa hóa doanh thu
    total_revenue = gp.quicksum(x[movie_idx, day, time] * movie_list[movie_idx].revenue for movie_idx in range(len(movie_list))
                                for day in range(len(showtimes_matrix)) for time in range(len(showtimes_matrix[day])))
    model.setObjective(total_revenue, GRB.MAXIMIZE)

    # Giải bài toán tối ưu
    model.optimize()

    # In lịch chiếu tối ưu
    for day in range(len(showtimes_matrix)):
        for time in range(len(showtimes_matrix[day])):
            for movie_idx in range(len(movie_list)):
                if x[movie_idx, day, time].x > 0.5:
                    print(f"Day {day+1}, Time {time+1}: {movie_list[movie_idx].name}")

    # In doanh thu tối ưu
    print(f"Optimized revenue: {model.objVal}")