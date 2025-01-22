from PIL import Image

print("img 폴더의 이미지의 주소를 복사해 입력해주세요.")
p = input()
img = Image.open(f'{p}')

a, b = map(int, input("이미지 사이즈 지정(16*16, 48*48, 128*128과 같이 입력)").split("*"))
img_resized = img.resize((a,b))

afterFolder = input("폴더를 지정해주세요.")
afterName = input("이름을 지정해주세요.(확장자 포함)")
img_resized.save(f'{afterFolder}/{afterName}')

print("작업 완료. after 폴더를 확인해주세요.")