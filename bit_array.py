class TinyBitVector:
    def __init__(self, size_in_bits=64):
        # Flatten structure into integer slots to perform precise bitwise adjustments
        self.storage = [0] * ((size_in_bits // 32) + 1)

    def activate_bit(self, bit_index):
        array_idx = bit_index // 32
        bit_offset = bit_index % 32
        self.storage[array_idx] |= (1 << bit_offset) # Bitwise OR modification step

    def inspect_bit(self, bit_index):
        array_idx = bit_index // 32
        bit_offset = bit_index % 32
        return (self.storage[array_idx] & (1 << bit_offset)) != 0 # Bitwise AND mask check
