import tkinter as tk
from PIL import Image, ImageTk
import os
from data import region_activities
from weather import get_weather
from outfit import recommend_outfit

import os
print("현재 작업 디렉토리:", os.getcwd())
# API 키 입력
API_KEY = "307c271fa08680788fa001c9bb3385dc"  # 예: "307c27..."

# 지역명 → 영문 매핑 (OpenWeather API용)
region_eng_map = {
    "서울": "Seoul", "인천": "Incheon", "수원": "Suwon", "춘천": "Chuncheon", "청주": "Cheongju",
    "강릉": "Gangneung", "전주": "Jeonju", "대전": "Daejeon", "안동": "Andong",
    "울릉/독도": "Ulleungdo", "포항": "Pohang", "울산": "Ulsan", "부산": "Busan",
    "대구": "Daegu", "목포": "Mokpo", "광주": "Gwangju", "여수": "Yeosu", "제주": "Jeju"
}

# 창 생성
root = tk.Tk()
root.title("놀러가기 준비 OK")
root.geometry("800x800")

# 지도 불러오기 (resize 제거!)
map_image = Image.open("C:/exercise/happy/korea_map_dummy.png")
map_photo = ImageTk.PhotoImage(map_image)

canvas = tk.Canvas(root, width=800, height=800)
canvas.pack()
canvas.create_image(0, 0, anchor="nw", image=map_photo)

# 지역 버튼 클릭 시 놀거리 팝업
def on_region_click(region_name):
    popup = tk.Toplevel(root)
    popup.title(f"{region_name}의 추천 놀거리")
    popup.geometry("300x200")

    label = tk.Label(popup, text=f"{region_name}에서 갈만한 곳은?", font=("맑은 고딕", 12))
    label.pack(pady=10)

    for place in region_activities[region_name]:
        btn = tk.Button(popup, text=place, command=lambda p=place: on_place_select(popup, region_name, p))
        btn.pack(pady=5)

# 놀거리 선택 시 → 날씨 + 코디 추천
def on_place_select(popup, region, place):
    popup.destroy()

    eng_name = region_eng_map.get(region, region)
    temp, desc = get_weather(eng_name, API_KEY)

    if temp is None:
        show_result_popup(region, place, "날씨 정보를 불러올 수 없습니다.", None)
        return

    outfit_text, image_path = recommend_outfit(temp)
    result_text = f"[{region} - {place}]\n☁️ 날씨: {desc}\n🌡 현재 기온: {temp:.1f}℃\n\n👕 옷차림 추천:\n{outfit_text}"
    show_result_popup(region, place, result_text, image_path)

# 결과 팝업
def show_result_popup(region, place, text, image_path):
    result = tk.Toplevel(root)
    result.title("여행 정보 추천 결과")
    result.geometry("400x500")

    label = tk.Label(result, text=text, wraplength=350, justify="left", font=("맑은 고딕", 11))
    label.pack(pady=10)

    if image_path and os.path.exists(image_path):
        img = Image.open(image_path)
        img = img.resize((300, 300))
        photo = ImageTk.PhotoImage(img)
        img_label = tk.Label(result, image=photo)
        img_label.image = photo
        img_label.pack()

# 지역 버튼 좌표
region_buttons = [
    ("서울", 270, 180), ("인천", 230, 190), ("수원", 270, 220), ("춘천", 360, 150),
    ("청주", 320, 300), ("강릉", 480, 180), ("전주", 270, 410), ("대전", 300, 345),
    ("안동", 460, 320), ("울릉/독도", 580, 200), ("포항", 500, 400), ("울산", 495, 460),
    ("부산", 470, 500), ("대구", 420, 420), ("목포", 190, 530), ("광주", 230, 490),
    ("여수", 310, 550), ("제주", 190, 680)
]

for name, x, y in region_buttons:
    btn = tk.Button(root, text=name, command=lambda n=name: on_region_click(n))
    canvas.create_window(x, y, window=btn)

root.mainloop()
