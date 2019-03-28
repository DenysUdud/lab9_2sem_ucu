import unittest
from task8_vigenere_cipher.vigenere_cipher import VigenereCipher, combine_character, separate_character

class TestEncode(unittest.TestCase):
	def setUp(self):
		self.cipher = VigenereCipher("TRAIN")

	def test_encode(self):
		encoded = self.cipher.encode("ENCODEDINPYTHON")
		assert encoded == "XECWQXUIVCRKHWA"

	def test_encode_character(self):
		encoded = self.cipher.encode("E")
		assert encoded == "X"

	def test_encode_spaces(self):
		encoded = self.cipher.encode("ENCODED IN PYTHON")
		assert encoded == "XECWQXUIVCRKHWA"

	def test_encode_lowercase(self):
		encoded = self.cipher.encode("encoded in Python")
		assert encoded == "XECWQXUIVCRKHWA"

	def test_combine_character(self):
		assert combine_character("E", "T") == "X"
		assert combine_character("N", "R") == "E"

	def test_extend_keyword(self):
		extended = self.cipher.extend_keyword(16)
		assert extended == "TRAINTRAINTRAINT"

	def test_separate_character(self):
		assert separate_character("X", "T") == "E"
		assert separate_character("E", "R") == "N"

	def test_decode(self):
		decoded = self.cipher.decode("XECWQXUIVCRKHWA")
		assert decoded == "ENCODEDINPYTHON"
