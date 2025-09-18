def checkmate(board):
    # เช็คว่าตัวแปรเป็น str ไหม
    if not isinstance(board, str):
        return print("Error")

    # แยก str แต่ละบรรรัดแล้วใส่ใน list
    rows = board.splitlines()
    # เช็คว่าเป็น str เปล่าไหม [] หรือ แต่ละบรรทัดเป็น str เปล่าไหม ['', '']
    if not rows or all(r == "" for r in rows):
        return print("Error")

    # จำนวนบรรทัด
    n_rows = len(rows)
    # จำนวน str ในแต่ละแถว
    row_lens = {len(r) for r in rows}

    # เช็คว่าจำนวนในแต่ละแถวเท่ากันทั้งหมด เพราะใช้ set ถ้าค่าซ้ำกันจะมีแค่ตัวเดียว
    if len(row_lens) != 1:
        return print("Error")

    # ดึงค่าจำนวน str
    n_cols = row_lens.pop()
    # เช็คจำนวนในคอมลัมน์
    if n_cols == 0 or n_cols != n_rows:
        return print("Error")

    # ตัวแปรไว้เช็คหมาก
    PIECES = set("KPRBQ")
    # ฟังก์ชันเช็คตัวหมาก คืนค่า True False
    def is_piece(ch: str) -> bool:
        return ch in PIECES

    # ตัวแปรตำแหน่งและจำนวน king
    king_pos = None
    king_count = 0


    for r in range(n_rows):
        for c in range(n_cols):
            # ตัวแปรเก็บค่าในช่อง
            ch = rows[r][c]
            # ถ้าเจอ K
            if ch == 'K':
                king_count += 1
                king_pos = (r, c)
                # ถ้าเจอ K มากกว่า 1
                if king_count > 1:
                    return print("Error")

    # ถ้าไม่เจอ K
    if king_pos is None:
        return print("Error")

    # แยกแถวและคอลัมน์ของ K
    kr, kc = king_pos

    # เช็คหมาก P อยู่รอบๆ หมาก K
    for dc in (-1, 1):
        # ขยับลง 1 แถว แล้วเช็คซ้ายกับขวา
        pr, pc = kr + 1, kc + dc
        # เช็คว่ายังอยู่ในกระดาน
        if 0 <= pr < n_rows and 0 <= pc < n_cols:
            # ถ้ามีหมาก P อยู่ในระยะ
            if rows[pr][pc] == 'P':
                return print("Success")

    # ทิศทางการเดิน
    # ทิศทางการเดินแนวนอนและแนวตั้ง (หมาก R, หมาก Q)
    ortho_dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    # ทิศทางการเดินแทยง (หมาก B, หมาก Q)
    diag_dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    # ฟังก์ชันค้นหาตัวหมากตัวแรกในทิศทางที่กำหนด (จากตำแหน่งกษัตริย์)
    def first_piece_in_direction(start_r: int, start_c: int, dr: int, dc: int):
        # ตำแหน่งแรก
        r, c = start_r + dr, start_c + dc
        steps = 0
        # จำกัดจำนวนเพื่อป้องกันลูปไม่รู้จบ
        while 0 <= r < n_rows and 0 <= c < n_cols and steps <= n_rows + n_cols:
            # เดินทีละช่องจนกว่าจะเจอตัวหมาก แล้วคืนค่าตัวหมากนั้น
            ch = rows[r][c]
            # เช็คว่าเจอหมากไหม
            if is_piece(ch):
                return ch
            # เดินช่อง
            r += dr
            c += dc
            steps += 1
        return None

    # ทิศทางการเดินแนวนอนและแนวตั้ง (หมาก R, หมาก Q)
    for dr, dc in ortho_dirs:
        seen = first_piece_in_direction(kr, kc, dr, dc)
        if seen in ('R', 'Q'):
            return print("Success")

    # ทิศทางการเดินแทยง (หมาก B, หมาก Q)
    for dr, dc in diag_dirs:
        seen = first_piece_in_direction(kr, kc, dr, dc)
        if seen in ('B', 'Q'):
            return print("Success")

    # ไม่เข้า return ไหนเลย
    print("Fail")