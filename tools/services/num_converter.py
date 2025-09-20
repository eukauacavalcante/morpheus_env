def oct_to_dec(oct: str) -> int:
    return int(oct, 8)


def dec_to_oct(decimal: int) -> str:
    return oct(decimal)[2:]


def bin_to_dec(binary: str) -> int:
    return int(binary, 2)


def dec_to_bin(decimal: int) -> str:
    return bin(decimal)[2:]


def hex_to_dec(hex: str) -> int:
    return int(hex, 16)


def dec_to_hex(decimal: int) -> str:
    return hex(decimal)[2:].upper()
