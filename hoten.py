import random
# ho = [
#     "Ái",
#     "An",
#     "Anh",
#     "Ao",
#     "Ánh",
#     "Ân",
#     "Âu",
#     "Âu Dương",
#     "Ấu",
#     "Bá",
#     "Bạc",
#     "Bạch",
#     "Bàn",
#     "Bàng",
#     "Bành",
#     "Bảo",
#     "Bế",
#     "Bì",
#     "Biện",
#     "Bình",
#     "Bồ",
#     "Ca",
#     "Cà",
#     "Cái",
#     "Cai",
#     "Cam",
#     "Cảnh",
#     "Cao",
#     "Cáp",
#     "Cát",
#     "Cầm",
#     "Cấn",
#     "Chế",
#     "Chiêm",
#     "Chắng",
#     "Chung",
#     "Chúng",
#     "Chương",
#     "Chử",
#     "Cồ",
#     "Cổ",
#     "Công",
#     "Cống",
#     "Cung",
#     "Cù",
#     "Cự",
#     "Dã",
#     "Danh",
#     "Diêm",
#     "Diệp",
#     "Doãn",
#     "Du",
#     "Duy",
#     "Dư",
#     "Đái",
#     "Đan",
#     "Đàm",
#     "Đào",
#     "Đăng",
#     "Đắc",
#     "Đầu",
#     "Đậu",
#     "Đèo",
#     "Điêu",
#     "Điền",
#     "Điều",
#     "Đinh",
#     "Đình",
#     "Đoái",
#     "Đoàn",
#     "Đoạn",
#     "Đôn",
#     "Đống",
#     "Đồ",
#     "Đồng",
#     "Đổng",
#     "Đương",
#     "Đường",
#     "Đức",
#     "Giả",
#     "Giao",
#     "Giang",
#     "Giàng",
#     "Giản",
#     "Giảng",
#     "Giáp",
#     "Hưng",
#     "Hầu",
#     "Hà",
#     "Hạ",
#     "Hàn",
#     "Hàng",
#     "Hán",
#     "Hề",
#     "Hi",
#     "Hình",
#     "Hoa",
#     "Hoà",
#     "Hoài",
#     "Hoàng Phủ",
#     "Hồng",
#     "Hùng",
#     "Hứa",
#     "Hướng",
#     "Kinh",
#     "Kông",
#     "Kiểu",
#     "Kha",
#     "Khà",
#     "Khai",
#     "Khâu",
#     "Khiếu",
#     "Khoa",
#     "Khổng",
#     "Khu",
#     "Khuất",
#     "Khúc",
#     "Khương",
#     "Khưu",
#     "Kiều",
#     "Kim",
#     "Ly",
#     "Lý",
#     "La",
#     "Lữ",
#     "Lành",
#     "Lãnh",
#     "Lạc",
#     "Lại",
#     "Lăng",
#     "Lâm",
#     "Lầu",
#     "Lèng",
#     "Lều",
#     "Liên",
#     "Liệp",
#     "Liêu",
#     "Liễu",
#     "Linh",
#     "Loan",
#     "Lò",
#     "Lô",
#     "Lỗ",
#     "Lộ",
#     "Lộc",
#     "Luyện",
#     "Lục",
#     "Lư",
#     "Lương",
#     "Lường",
#     "Lưu",
#     "Ma",
#     "Mai",
#     "Mang",
#     "Mã",
#     "Mạc",
#     "Mạch",
#     "Mạnh",
#     "Mâu",
#     "Mầu",
#     "Mẫn",
#     "Minh",
#     "Mộc",
#     "Mông",
#     "Mùa",
#     "Mục",
#     "Miêu",
#     "Niê",
#     "Ngạc",
#     "Ngân",
#     "Nghiêm",
#     "Nghị",
#     "Ngọ",
#     "Ngọc",
#     "Ngôn",
#     "Ngũ",
#     "Ngụy",
#     "Nhan",
#     "Nhâm",
#     "Nhữ",
#     "Ninh",
#     "Nông",
#     "Ong",
#     "Ông",
#     "Phi",
#     "Phí",
#     "Phó",
#     "Phong",
#     "Phù",
#     "Phú",
#     "Phùng",
#     "Phương",
#     "Quản",
#     "Quán",
#     "Quang",
#     "Quàng",
#     "Quảng",
#     "Quách",
#     "Quế",
#     "Quốc",
#     "Quyền",
#     "Sái",
#     "Sâm",
#     "Sầm",
#     "Sơn",
#     "Sử",
#     "Sùng",
#     "Sỳ",
#     "Tán",
#     "Tào",
#     "Tạ",
#     "Tăng",
#     "Tấn",
#     "Tất",
#     "Tề",
#     "Thang",
#     "Thanh",
#     "Thái",
#     "Thành",
#     "Thào",
#     "Thạch",
#     "Thân",
#     "Thẩm",
#     "Thập",
#     "Thế",
#     "Thi",
#     "Thiều",
#     "Thiệu",
#     "Thịnh",
#     "Thiềm",
#     "Thoa",
#     "Thôi",
#     "Thóng",
#     "Thục",
#     "Tiêu",
#     "Tiết",
#     "Tiếp",
#     "Tinh",
#     "Tòng",
#     "Tô",
#     "Tôn",
#     "Tôn Nữ",
#     "Tôn Thất",
#     "Tông",
#     "Tống",
#     "Trang",
#     "Tráng",
#     "Trác",
#     "Trà",
#     "Trâu",
#     "Tri",
#     "Trì",
#     "Triệu",
#     "Trình",
#     "Trịnh",
#     "Trung",
#     "Trưng",
#     "Tuấn",
#     "Từ",
#     "Tưởng",
#     "Tướng",
#     "Ty",
#     "Uông",
#     "Ung",
#     "Ưng",
#     "Ứng",
#     "Vàng",
#     "Vâng",
#     "Vạn",
#     "Văn",
#     "Vi",
#     "Vĩnh",
#     "Viêm",
#     "Viên",
#     "Việt",
#     "Vòng",
#     "Vừ",
#     "Vương",
#     "Vưu",
#     "Vu",
#     "Xa",
#     "Xung",
#     "Y",
#     "Yên",
# ]

ho = [
    "Nguyễn",
    "Trần",
    "Lê",
    "Phạm",
    "Huỳnh",
    "Võ",
    "Phan",
    "Trương",
    "Bùi",
    "Đặng",
    "Đỗ",
    "Ngô",
    "Hồ",
    "Dương",
    "Đinh",
]

ten_nam = [
    "Khang",
    "Bảo",
    "Minh",
    "Phúc",
    "Anh",
    "Khoa",
    "Phát",
    "Đạt",
    "Khôi",
    "Long",
    "Nam",
    "Duy",
    "Quân",
    "Kiệt",
    "Thịnh",
    "Tuấn",
    "Hưng",
    "Hoàng",
    "Hiếu",
    "Nhân",
    "Trí",
    "Tài",
    "Phong",
    "Nguyên",
    "An",
    "Phú",
    "Thành",
    "Đức",
    "Dũng",
    "Lộc",
    "Khánh",
    "Vinh",
    "Tiến",
    "Nghĩa",
    "Thiện",
    "Hào",
    "Hải",
    "Đăng",
    "Quang",
    "Lâm",
    "Nhật",
    "Trung",
    "Thắng",
    "Tú",
    "Hùng",
    "Tâm",
    "Sang",
    "Sơn",
    "Thái",
    "Cường",
    "Vũ",
    "Toàn",
    "Ân",
    "Thuận",
    "Bình",
    "Trường",
    "Danh",
    "Kiên",
    "Phước",
    "Thiên",
    "Tân",
    "Việt",
    "Khải",
    "Tín",
    "Dương",
    "Tùng",
    "Quý",
    "Hậu",
    "Trọng",
    "Triết",
    "Luân",
    "Phương",
    "Quốc",
    "Thông",
    "Khiêm",
    "Hòa",
    "Thanh",
    "Tường",
    "Kha",
    "Vỹ",
    "Bách",
    "Khanh",
    "Mạnh",
    "Lợi",
    "Đại",
    "Hiệp",
    "Đông",
    "Nhựt",
    "Giang",
    "Kỳ",
    "Phi",
    "Tấn",
    "Văn",
    "Vương",
    "Công",
    "Hiển",
    "Linh",
    "Ngọc",
    "Vĩ",
]

ten_nu = [
    "Anh",
    "Vy",
    "Ngọc",
    "Nhi",
    "Hân",
    "Thư",
    "Linh",
    "Như",
    "Ngân",
    "Phương",
    "Thảo",
    "My",
    "Trân",
    "Quỳnh",
    "Nghi",
    "Trang",
    "Trâm",
    "An",
    "Thy",
    "Châu",
    "Trúc",
    "Uyên",
    "Yến",
    "Ý",
    "Tiên",
    "Mai",
    "Hà",
    "Vân",
    "Nguyên",
    "Hương",
    "Quyên",
    "Duyên",
    "Kim",
    "Trinh",
    "Thanh",
    "Tuyền",
    "Hằng",
    "Dương",
    "Chi",
    "Giang",
    "Tâm",
    "Lam",
    "Tú",
    "Ánh",
    "Hiền",
    "Khánh",
    "Minh",
    "Huyền",
    "Thùy",
    "Vi",
    "Ly",
    "Dung",
    "Nhung",
    "Phúc",
    "Lan",
    "Phụng",
    "Ân",
    "Thi",
    "Khanh",
    "Kỳ",
    "Nga",
    "Tường",
    "Thúy",
    "Mỹ",
    "Hoa",
    "Tuyết",
    "Lâm",
    "Thủy",
    "Đan",
    "Hạnh",
    "Xuân",
    "Oanh",
    "Mẫn",
    "Khuê",
    "Diệp",
    "Thương",
    "Nhiên",
    "Băng",
    "Hồng",
    "Bình",
    "Loan",
    "Thơ",
    "Phượng",
    "Mi",
    "Nhã",
    "Nguyệt",
    "Bích",
    "Đào",
    "Diễm",
    "Kiều",
    "Hiếu",
    "Di",
    "Liên",
    "Trà",
    "Tuệ",
    "Thắm",
    "Diệu",
    "Quân",
    "Nhàn",
    "Doanh",
]

N = 10
for _ in range(N):
    gioitinh = random.randint(0, 1)
    if gioitinh:
        ten = ten_nam
    else:
        ten = ten_nu
    t = f"{random.choice(ho)} {' '.join(   [(random.choice(ten)) for _ in range(random.randint(1,3)) ]  )}"
    print(t)
