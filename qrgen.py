import qrcodegen
from PIL import Image, ImageDraw, ImageFont
import openpyxl

list_of_data = []

def generate_qr_code(data, filename, error_correction_level=qrcodegen.QrCode.Ecc.MEDIUM, module_size=5, frame_width=10):
    qr = qrcodegen.QrCode.encode_text(data, error_correction_level)
    if module_size < 1:
        module_size = 1
    if frame_width < 1:
        frame_width = 1

    image_size = qr._size * module_size + 2 * frame_width
    img = Image.new("RGB", (image_size, image_size), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, image_size, image_size), outline="white", width=frame_width)
    
    for y in range(qr._size):
        for x in range(qr._size):
            if qr.get_module(x, y):
                draw.rectangle((x * module_size + frame_width, y * module_size + frame_width, (x + 1) * module_size + frame_width, (y + 1) * module_size + frame_width), fill="black")
    font = ImageFont.truetype("arial.ttf", 20 * module_size)
    draw.text((10 * module_size + frame_width, image_size + 10 * module_size), "Scan this QR code", font=font, fill="black")

    img.save(filename)
    
def read_data_from_excel(file_path):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    data = []
    for row in sheet.iter_rows(values_only=True):
        data.append(row)
    return data

info = read_data_from_excel("data.xlsx")
for i in range(1,len(info)):
    list_of_data.append(info[i][-1])

filename = "qr_code.png"
for i in range(0,len(list_of_data)):
    generate_qr_code(list_of_data[i], 'images/qr_code' + str(i+1) + '.png')
    