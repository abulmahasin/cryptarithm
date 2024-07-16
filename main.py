import itertools

def is_valid_equation(equation):
    if '=' not in equation:
        return False, "Persamaan harus memiliki tanda sama dengan (=)"
    left_side, right_side = equation.split('=')
    if '+' not in left_side and '-' not in left_side:
        return False, "Persamaan harus memiliki tanda tambah (+) atau kurang (-) di sisi kiri"
    
    letters = set(equation.replace(' ', '').replace('+', '').replace('-', '').replace('=', ''))
    letters = [l for l in letters if l.isalpha()]
    if len(letters) > 10:
        return False, "Terlalu banyak huruf unik untuk substitusi digit (maksimal 10 huruf)"
    
    return True, ""

def solve_cryptarithm(equation):
    is_valid, error_message = is_valid_equation(equation)
    if not is_valid:
        return f"Persamaan tidak valid: {error_message}"

    letters = set(equation.replace(' ', '').replace('+', '').replace('-', '').replace('=', ''))
    letters = [l for l in letters if l.isalpha()]
    
    digits = '0123456789'
    for perm in itertools.permutations(digits, len(letters)):
        trans = str.maketrans(''.join(letters), ''.join(perm))
        translated_eq = equation.translate(trans)
        left_side, right_side = translated_eq.split('=')
        
        if any(part.lstrip('0').isdigit() and part[0] == '0' for part in left_side.split('+')) or right_side.lstrip('0').isdigit() and right_side[0] == '0':
            continue
        
        try:
            if eval(left_side) == int(right_side):
                return f"Solusi ditemukan: {translated_eq}"
        except:
            continue
    return "Tidak ditemukan solusi untuk persamaan ini"

if __name__ == "__main__":
    equation = input("Masukkan persamaan cryptarithm (contoh: SEND + MORE = MONEY): ")
    solution = solve_cryptarithm(equation)
    print(solution)
