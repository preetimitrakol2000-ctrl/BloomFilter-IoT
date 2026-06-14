from bit_array import TinyBitVector

class IoTBloomFilter:
    def __init__(self, size=64):
        self.bits = TinyBitVector(size)
        self.size = size

    def _generate_hashes(self, element_string):
        """Generates two unique array positions using alternative multiplication steps."""
        hash_a = 0
        hash_b = 5381
        for char in element_string:
            hash_a = (hash_a * 31 + ord(char)) % self.size
            hash_b = (((hash_b << 5) + hash_b) + ord(char)) % self.size
        return [hash_a, hash_b]

    def authorize_identity(self, signature):
        for position in self._generate_hashes(signature):
            self.bits.activate_bit(position)

    def evaluate_membership(self, signature):
        for position in self._generate_hashes(signature):
            if not self.bits.inspect_bit(position):
                return False # Confirmed Definite Outlier (No False Negatives)
        return True # Probable network match indicator
