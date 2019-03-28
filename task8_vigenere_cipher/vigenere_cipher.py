# file : vegenere_chiper.py
# This module cantains the vegenere class.


class VigenereCipher:
    """
    A class for working with decoding and coding text
    to vigenere cipher.
    """
    def __init__(self, keyword):
        self.keyword = keyword

    # def encode(self, plaintext):
    #     plaintext = plaintext.replace(" ", "").upper()
    #     cipher = []
    #     keyword = self.extend_keyword(len(plaintext))
    #     for p, k in zip(plaintext, keyword):
    #         cipher.append(combine_character(p, k))
    #     return "".join(cipher)

    def extend_keyword(self, number):
        """
        A method for extending extend keywords.
        :param number:
        :return: str
        """
        repeats = number // len(self.keyword) + 1
        return (self.keyword * repeats)[:number]

    # def decode(self, ciphertext):
    #     plain = []
    #     keyword = self.extend_keyword(len(ciphertext))
    #     for p, k in zip(ciphertext, keyword):
    #         plain.append(separate_character(p, k))
    #     return "".join(plain)

    def _code(self, text, combine_func):
        """
        A method for coding and decoding text.
        :param text: str
        :param combine_func: str
        :return: str
        """
        text = text.replace(" ", "").upper()
        combined = []
        keyword = self.extend_keyword(len(text))
        for p, k in zip(text, keyword):
            combined.append(combine_func(p, k))
        return "".join(combined)

    def encode(self, plaintext):
        """
        A method for encoding text.
        :param plaintext:
        :return: str
        """
        return self._code(plaintext, combine_character)

    def decode(self, ciphertext):
        """
        A method for decoding text.
        :param ciphertext: str
        :return: str
        """
        return self._code(ciphertext, separate_character)


def combine_character(plain, keyword):
    """
    The function which returns str in right for encoding / decoding.
    :param plain: str
    :param keyword: str
    :return: str
    """
    plain = plain.upper()
    keyword = keyword.upper()
    plain_num = ord(plain) - ord('A')
    keyword_num = ord(keyword) - ord('A')
    return chr(ord('A') + (plain_num + keyword_num) % 26)


def separate_character(cypher, keyword):
    """
    The function which returns str in right form for
    encoding / decoding.
    :param cypher: str
    :param keyword: str
    :return: str
    """
    cypher = cypher.upper()
    keyword = keyword.upper()
    cypher_num = ord(cypher) - ord('A')
    keyword_num = ord(keyword) - ord('A')
    return chr(ord('A') + (cypher_num - keyword_num) % 26)