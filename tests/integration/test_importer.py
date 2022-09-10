"""This is tests for importer"""
# !/usr/bin/python3
# encoding: utf-8

import unittest
from src.importer.pdf import PDF, extract_text, file_finder
import pandas as pd
import os


class TestImportPDF(unittest.TestCase):
    """This class is intended for testing the importer"""

    FIRST_FILE = './tests/integration/testdata/tech_prog_python_Pandas_Работа_с_данными_t2_m8.pdf'
    SECOND_FILE = './tests/integration/testdata/math_algorithm_Algoritmy_Samy_kratkiy_i_ponyatny_kurs_d2022_m8.pdf'
    THIRD_FILE = './tests/integration/testdata/tech_prog_python_ai_Shabloni_i_praktika_glubokogo_obucheniya_m8.pdf'
    TEST_DATA_PATH = './tests/integration/testdata'
    FILE_WITH_DATA = '/tmp/books.csv'
    LEN_FIRST_BOOK = 152837
    LEN_SECOND_BOOK = 320617
    LEN_THIRD_BOOK = 1141344

    def test_file_finder(self):
        """Checking the function operation for file_finder"""
        file_names = file_finder(self.TEST_DATA_PATH)

        first_book = next(file_names)
        second_book = next(file_names)
        third_book = next(file_names)

        self.assertEqual(
            first_book, self.FIRST_FILE)
        self.assertEqual(
            second_book, self.SECOND_FILE)

        self.assertEqual(
            third_book, self.THIRD_FILE)

    def test_extract_text(self):
        """Checking the function operation for extract_text"""
        text = extract_text(self.FIRST_FILE)
        self.assertEqual(len(text), self.LEN_FIRST_BOOK)

        text = extract_text(self.SECOND_FILE)
        self.assertEqual(len(text), self.LEN_SECOND_BOOK)

        text = extract_text(self.THIRD_FILE)
        self.assertEqual(len(text), self.LEN_THIRD_BOOK)

    def test_processing(self):
        """Checking the function operation for processing"""
        if os.path.exists(self.FILE_WITH_DATA):
            os.remove(self.FILE_WITH_DATA)

        i_pdf = PDF(self.TEST_DATA_PATH, self.FILE_WITH_DATA)
        i_pdf.processing()

        check_csv = pd.read_csv(self.FILE_WITH_DATA, header=None)
        self.assertEqual(
            len(check_csv.iloc[0:1, 0:1].values[0][0]), self.LEN_FIRST_BOOK)
        self.assertEqual(
            len(check_csv.iloc[1:2, 0:1].values[0][0]), self.LEN_SECOND_BOOK)
        self.assertEqual(
            len(check_csv.iloc[2:3, 0:1].values[0][0]), self.LEN_THIRD_BOOK)


if __name__ == '__main__':
    unittest.main()
