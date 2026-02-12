from checkmate import checkmate
import io
from contextlib import redirect_stdout

def run(board: str) -> str:
    # สร้าง buffer เพื่อดักจับสิ่งที่ checkmate ปริ้นออกมา (Success/Fail)
    buf = io.StringIO()
    with redirect_stdout(buf):
        try:
            checkmate(board)
        except Exception as e:
            # ถ้าโปรแกรมพัง ให้ปริ้น Error ออกมาแทน
            print(f"Error: {e}")
            
    return buf.getvalue().strip()

tests = [
    # 1. Pawn (P) โจมตีเฉียงขึ้น
    ("R...\n.K..\n..P.\n....", "Success", "pawn attacks (from bottom-right)"),
    ("R...\n.K..\nP...\n....", "Success", "pawn attacks (from bottom-left)"),

    # 2. Pawn ไม่โจมตี (อยู่ผิดตำแหน่ง หรือไกลเกิน)
    ("....\n.K..\n...P\n....", "Fail", "pawn no attack (too far)"),
    ("....\n.P..\n.K..\n....", "Fail", "pawn cannot attack backward"),

    # 3. Rook (R) โจมตีแนวตรง
    (".R..\n....\n.K..\n....", "Success", "rook attacks vertical"),
    ("...R\n...K\n....\n....", "Success", "rook attacks vertical 2"),
    ("K..R\n....\n....\n....", "Success", "rook attacks horizontal"),

    # 4. Rook ถูกบล็อก
    (".R..\n.P..\n.K..\n....", "Fail", "rook blocked by P"),

    # 5. Bishop (B) โจมตีแนวทแยง
    ("B...\n....\n..K.\n....", "Success", "bishop attacks diagonal"),

    # 6. Bishop ถูกบล็อก
    ("B...\n.P..\n..K.\n....", "Fail", "bishop blocked by P"),

    # 7. Queen (Q) แนวตรงและทแยง
    ("..Q.\n....\n..K.\n....", "Success", "queen attacks vertical"),
    ("Q...\n....\n..K.\n....", "Success", "queen attacks diagonal"),

    # 8. Queen ถูกบล็อก
    ("Q...\n.P..\n..K.\n....", "Fail", "queen blocked"),

    # 9. กระดานเล็กสุด 1x1
    ("K", "Fail", "1x1 safe"),

    # 10.Error (ไม่มี King หรือ King เยอะไป)
    ("....\n.P..\n....\n....", "Fail", "missing king -> fail"),
    
    #ตัวอักษรขยะ (มองเป็นช่องว่าง)
    ("xRxx\nxKxx\nxxxx\nxxxx", "Success", "treat unknown chars as empty"),
]

def main():
    passed_count = 0
    total = len(tests)
    
    print(f"{'TEST NAME':<35} | {'RESULT':<6} | {'DETAIL'}")
    print("-" * 60)

    for board, expected, name in tests:
        got = run(board)
        
        if got == expected:
            print(f"{name:<35} | \033[92mPASS\033[0m   | Got: {got}")
            passed_count += 1
        else:
            print(f"{name:<35} | \033[91mFAIL\033[0m   | Exp: {expected}, Got: {got}")
            # ถ้าอยากเห็นบอร์ดที่ผิด ให้ uncomment บรรทัดล่างนี้
            # print(f"--- Board ---\n{board}\n-------------")

    print("-" * 60)
    print(f"Summary: Passed {passed_count}/{total}")

if __name__ == "__main__":
    main()