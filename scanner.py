import cv2
import keyboard
import time
import openpyxl
import openpyxl.workbook

list_of_data = []
list_of_qr = []
last_row = 0

def create_excel_file():
    create_excel = openpyxl.Workbook()
    create_excel.save('datatest.xlsx')

create_excel_file()

def add_data_to_excel(code,stat):
    workbook = openpyxl.load_workbook('datatest.xlsx')
    
    sheet = workbook['Sheet']

    last_row = sheet.max_row + 1

    sheet.cell(row=last_row, column=1).value = code
    sheet.cell(row=last_row, column=2).value = stat

    workbook.save('datatest.xlsx')

def read_data_from_excel(file_path):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    data = []
    for row in sheet.iter_rows(values_only=True):
        data.append(row)
    return data

info = read_data_from_excel("data.xlsx")
for i in range(len(info)):
    list_of_data.append(info[i][0])

def scan_multiple_qr_codes():
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()

    while True:
        ret, frame = cap.read()

        if not ret:
            break
        data, _, _ = detector.detectAndDecode(frame)

        if data:
            list_of_qr.append(data)
            if data in list_of_data:
                print("VALID")
                add_data_to_excel(data,"VALID")
                list_of_data.remove(data)
            else:
                print("INVALID")
            time.sleep(3)
        
        cv2.imshow("QR Code Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":scan_multiple_qr_codes()


