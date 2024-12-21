# ----- Cyclic Redundancy Check (CRC) Implementation -----
def xor(a, b):
    result = []
    for i in range(1, len(b)):
        result.append('1' if a[i] != b[i] else '0')
    return ''.join(result)

def divide(data, divisor):
    pick = len(divisor)
    tmp = data[:pick]

    while pick < len(data):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + data[pick]
        else:
            tmp = xor('0' * pick, tmp) + data[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)
    
    return tmp

def crc(data, generator):
    l_gen = len(generator)
    appended_data = data + '0' * (l_gen - 1)
    remainder = divide(appended_data, generator)
    return data + remainder

# ----- Checksum Implementation -----
def calculate_checksum(data):
    return sum(ord(char) for char in data) % 256

def verify_checksum(data, received_checksum):
    calculated_checksum = calculate_checksum(data)
    return calculated_checksum == received_checksum

# ----- Parity Check Implementation -----
def calculate_parity(data):
    total_ones = sum(bin(ord(char)).count('1') for char in data)
    return total_ones % 2

def verify_parity(data, received_parity):
    calculated_parity = calculate_parity(data)
    return calculated_parity == received_parity

# ----- Main Function -----
def main():
    """
    Main function to demonstrate CRC, Checksum, and Parity Check.
    """
    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"

    print(f"{BOLD}{CYAN}===== Cyclic Redundancy Check (CRC), Checksum, and Parity Check ====={RESET}\n")
    
    # ----- CRC Calculation -----
    print(f"{YELLOW}=== CRC Demonstration ==={RESET}")
    data = input(f"{BOLD}Enter the binary data: {RESET}").strip()
    generator = input(f"{BOLD}Enter the generator polynomial (binary): {RESET}").strip()
    transmitted_data = crc(data, generator)
    print(f"{GREEN}Original Data         : {RESET}{data}")
    print(f"{GREEN}Generator Polynomial  : {RESET}{generator}")
    print(f"{GREEN}Transmitted Data (CRC): {RESET}{transmitted_data}\n")

    # ----- Checksum Demonstration -----
    print(f"{YELLOW}=== Checksum Demonstration ==={RESET}")
    text_data = input(f"{BOLD}Enter text data for checksum: {RESET}")
    checksum = calculate_checksum(text_data)
    print(f"{GREEN}Original Data         : {RESET}{text_data}")
    print(f"{GREEN}Calculated Checksum   : {RESET}{checksum}")
    
    is_checksum_valid = verify_checksum(text_data, checksum)
    validity_msg = f"{GREEN}Valid{RESET}" if is_checksum_valid else f"{RED}Invalid{RESET}"
    print(f"{BOLD}Checksum Valid        : {RESET}{validity_msg}\n")
    
    # ----- Parity Check Demonstration -----
    print(f"{YELLOW}=== Parity Check Demonstration ==={RESET}")
    parity = calculate_parity(text_data)
    print(f"{GREEN}Original Data         : {RESET}{text_data}")
    print(f"{GREEN}Calculated Parity     : {RESET}{parity} ({'Even' if parity == 0 else 'Odd'})")
    
    is_parity_valid = verify_parity(text_data, parity)
    parity_msg = f"{GREEN}Valid{RESET}" if is_parity_valid else f"{RED}Invalid{RESET}"
    print(f"{BOLD}Parity Valid          : {RESET}{parity_msg}")
    
    print(f"\n{BOLD}{CYAN}===== End of Demonstration ====={RESET}")

if __name__ == "__main__":
    main()
