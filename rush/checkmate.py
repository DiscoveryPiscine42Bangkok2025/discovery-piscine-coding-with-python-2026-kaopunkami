def checkmate(board):
    if not board:
        print("Fail")
        return

    # แยกบรรทัดเก็บลง list
    data = board.splitlines()
    rows = len(data)
    
    # หาตำแหน่ง King (K)
    k_r, k_c = -1, -1
    for r in range(rows):
        for c in range(len(data[r])):
            if data[r][c] == 'K':
                k_r = r
                k_c = c
                break
        if k_r != -1:
            break
            
    if k_r == -1:
        print("Fail")
        return

    # 1. เช็ค Pawn (P)
    # Pawn กินขึ้นบนเป็นตัว V แปลว่าถ้า King จะโดนกิน P ต้องอยู่แถวล่างถัดไป (r+1)
    try:
        if k_r + 1 < rows:
            # เช็คซ้ายล่าง
            if k_c - 1 >= 0 and data[k_r+1][k_c-1] == 'P':
                print("Success")
                return
            # เช็คขวาล่าง
            if k_c + 1 < len(data[k_r+1]) and data[k_r+1][k_c+1] == 'P':
                print("Success")
                return
    except:
        pass

    # 2. เช็คแนวตรง (Rook / Queen)
    # เดินขึ้น
    for r in range(k_r - 1, -1, -1):
        if data[r][k_c] in 'RQ':
            print("Success")
            return
        elif data[r][k_c] != '.':
            break
    # เดินลง
    for r in range(k_r + 1, rows):
        if data[r][k_c] in 'RQ':
            print("Success")
            return
        elif data[r][k_c] != '.':
            break
    # เดินซ้าย
    for c in range(k_c - 1, -1, -1):
        if data[k_r][c] in 'RQ':
            print("Success")
            return
        elif data[k_r][c] != '.':
            break
    # เดินขวา
    for c in range(k_c + 1, len(data[k_r])):
        if data[k_r][c] in 'RQ':
            print("Success")
            return
        elif data[k_r][c] != '.':
            break

    # 3. เช็คแนวทแยง (Bishop / Queen)
    # ทแยงบนซ้าย
    r, c = k_r - 1, k_c - 1
    while r >= 0 and c >= 0:
        if data[r][c] in 'BQ':
            print("Success")
            return
        elif data[r][c] != '.':
            break
        r -= 1
        c -= 1
    
    # ทแยงบนขวา
    r, c = k_r - 1, k_c + 1
    while r >= 0 and c < len(data[r]):
        if data[r][c] in 'BQ':
            print("Success")
            return
        elif data[r][c] != '.':
            break
        r -= 1
        c += 1

    # ทแยงล่างซ้าย
    r, c = k_r + 1, k_c - 1
    while r < rows and c >= 0:
        if data[r][c] in 'BQ':
            print("Success")
            return
        elif data[r][c] != '.':
            break
        r += 1
        c -= 1

    # ทแยงล่างขวา
    r, c = k_r + 1, k_c + 1
    while r < rows and c < len(data[r]):
        if data[r][c] in 'BQ':
            print("Success")
            return
        elif data[r][c] != '.':
            break
        r += 1
        c += 1

    print("Fail")