from pywinauto import Application
import time


# -----------------------------
# CONNECT PROGRAM
# -----------------------------
def connect_program():

    EXE_PATH = r"C:\Program Files (x86)\EssentialCP\EGDesktop-CP.exe"

    app = Application(backend="uia").connect(path=EXE_PATH)
    main = app.window(title_re=".*Riposte POS Application.*")

    main.wait("visible", timeout=30)

    return app, main


# -----------------------------
# FLOW : รับฝากสิ่งของ
# -----------------------------
def send_parcel(main):

    # เข้าหน้า รับฝากสิ่งของ
    main.child_window(title="รับฝากสิ่งของ", control_type="Button").click()
    time.sleep(2)

    # อ่านบัตรประชาชน
    main.child_window(title="อ่านบัตรประชาชน").click()
    time.sleep(3)

    # กรอกรหัสไปรษณีย์ต้นทาง
    main.child_window(auto_id="PostalCode").type_keys("10400")
    time.sleep(1)

    # เบอร์โทร
    main.child_window(auto_id="PhoneNumber").type_keys("0812345678")

    main.child_window(title="ถัดไป").click()
    time.sleep(2)

    # กำหนดขนาดเอง
    main.child_window(title="กำหนดขนาดเอง").click()
    time.sleep(1)

    main.child_window(title="ถัดไป").click()
    time.sleep(1)

    # ยืนยัน
    main.child_window(auto_id="Confirmed").click()
    time.sleep(1)

    # น้ำหนัก
    main.child_window(auto_id="EG_WEIGHT_INPUT_ELEMENT").type_keys("20")

    # ขนาด
    main.child_window(auto_id="Length").type_keys("25")
    main.child_window(auto_id="Width").type_keys("14")
    main.child_window(auto_id="Height").type_keys("0")

    main.child_window(title="ถัดไป").click()
    time.sleep(2)

    # รหัสปลายทาง
    main.child_window(auto_id="PostCodeDestination").type_keys("10400")

    main.child_window(title="ดำเนินการ").click()
    time.sleep(3)

    # เลือก Shipping
    main.child_window(auto_id="ShippingService_8509").click()

    main.child_window(title="ถัดไป").click()
    time.sleep(1)

    main.child_window(title="ถัดไป").click()
    time.sleep(1)

    main.child_window(title="ถัดไป").click()
    time.sleep(1)

    # ค้นหาที่อยู่
    main.child_window(auto_id="SearchField1").type_keys("ปัตตานี")

    main.child_window(title="ตกลง").click()
    time.sleep(2)

    # ข้อมูลลูกค้า
    main.child_window(auto_id="CustomerFirstName").type_keys("ทดสอบ")
    main.child_window(auto_id="CustomerLastName").type_keys("ระบบ")

    main.child_window(auto_id="AdministrativeArea").type_keys("กรุงเทพ")
    main.child_window(auto_id="Locality").type_keys("พญาไท")
    main.child_window(auto_id="DependentLocality").type_keys("พญาไท")

    main.child_window(auto_id="StreetAddress1").type_keys("11")

    main.child_window(auto_id="PhoneNumber").type_keys("0987654321")

    main.child_window(title="ถัดไป").click()

    # รอ popup
    time.sleep(5)

    # กดไม่
    main.child_window(auto_id="No").click()

    # รับเงิน
    main.child_window(title="รับเงิน").click()

    time.sleep(1)

    # Fast Cash
    main.child_window(title="Fast Cash").click()

    print("ออกใบเสร็จสำเร็จ")


# -----------------------------
# MAIN
# -----------------------------
def main():

    app, main = connect_program()

    send_parcel(main)

    print("Automation Flow สำเร็จ")


if __name__ == "__main__":
    main()