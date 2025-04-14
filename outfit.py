import random
import os

def recommend_outfit(temp):
    # 현재 파일의 절대경로 기준으로 images 폴더 접근
    base_path = os.path.dirname(os.path.abspath(__file__))

    if temp >= 25:
        folder = os.path.join(base_path, "images", "1_very_hot")
        text = "무더운 날씨엔 반팔, 반바지, 시원한 옷차림 추천!"
    elif 18 <= temp < 25:
        folder = os.path.join(base_path, "images", "2_warm")
        text = "따뜻한 날씨엔 얇은 셔츠나 면바지가 좋아요."
    elif 8 <= temp < 18:
        folder = os.path.join(base_path, "images", "3_mild")
        text = "선선한 날씨엔 가디건이나 얇은 니트 추천!"
    elif -1 <= temp < 8:
        folder = os.path.join(base_path, "images", "4_chilly")
        text = "쌀쌀한 날씨엔 재킷이나 맨투맨이 좋아요."
    else:
        folder = os.path.join(base_path, "images", "5_cold")
        text = "추운 날씨엔 패딩, 목도리, 니트모자 필수!"

    # 폴더 내 이미지 랜덤 선택
    image_list = os.listdir(folder)
    image_file = random.choice(image_list)
    image_path = os.path.join(folder, image_file)

    return text, image_path
