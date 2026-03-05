from pywinauto import Application
import time
import re


# -----------------------------
# CONNECT PROGRAM
# -----------------------------
def connect_program():

    app = Application(backend="uia").connect(title_re=".*POS.*")
    main_window = app.window(title_re=".*POS.*")

    main_window.wait("visible", timeout=20)

    return app, main_window


# -----------------------------
# FLOW 1 : CREATE RECEIPT
# -----------------------------
def create_receipt(main):

    print("เริ่ม Flow 1 : ออกใบเสร็จ")

    # 1 เลือกบริการ
    main.child_window(title="เลือกบริการ").click()
    time.sleep(1)

    main.child_window(title="ไปรษณีย์ในประเทศ").click()
    time.sleep(1)

    # 2 กดออกใบเสร็จ
    main.child_window(title="ออกใบเสร็จ").click()

    time.sleep(3)

    # 3 อ่านเลข TR จาก popup หรือ textbox
    popup = main.child_window(title_re=".*สำเร็จ.*")

    popup.wait("visible", timeout=10)

    text = popup.window_text()

    print("ข้อความ popup :", text)

    tr_match = re.search(r'TR\d+', text)

    if tr_match:
        tr_number = tr_match.group()
    else:
        raise Exception("ไม่พบเลข TR")

    print("TR NUMBER =", tr_number)

    # ปิด popup
    popup.child_window(title="ตกลง").click()

    time.sleep(1)

    # 4 พิมพ์สำเนาใบเสร็จ
    main.child_window(title="สำเนาใบเสร็จ").click()

    time.sleep(2)

    return tr_number


# -----------------------------
# FLOW 2 : TAX INVOICE
# -----------------------------
def create_tax_invoice(main, tr_number):

    print("เริ่ม Flow 2 : ออกใบกำกับภาษี")

    # เปิดเมนูใบกำกับภาษี
    main.child_window(title="ใบกำกับภาษี").click()

    time.sleep(2)

    # กรอกเลข TR
    tr_box = main.child_window(auto_id="txtTR")

    tr_box.wait("visible", timeout=10)

    tr_box.type_keys(tr_number)

    time.sleep(1)

    # ค้นหา
    main.child_window(title="ค้นหา").click()

    time.sleep(2)

    # ออกใบกำกับภาษี
    main.child_window(title="ออกใบกำกับ").click()

    time.sleep(3)

    # พิมพ์สำเนาใบกำกับ
    main.child_window(title="สำเนาใบกำกับ").click()

    time.sleep(2)

    print("ออกใบกำกับภาษีสำเร็จ")


# -----------------------------
# MAIN
# -----------------------------
def main():

    app, main_window = connect_program()

    # FLOW 1
    tr_number = create_receipt(main_window)

    # FLOW 2
    create_tax_invoice(main_window, tr_number)

    print("Automation เสร็จสมบูรณ์")


if __name__ == "__main__":
    main()