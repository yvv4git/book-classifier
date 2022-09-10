"""This module contains an implementation of a class for importing pdf files"""

# !/usr/bin/python3
# encoding: utf-8

from io import DEFAULT_BUFFER_SIZE
import os
import fitz
import pandas as pd


def extract_text(file_name: str) -> str:
    """Extract text from file"""
    text = ""
    if not os.path.exists(file_name):
        return text

    with fitz.open(file_name) as doc:
        for page in doc:
            text += page.get_text()

    return text


def file_finder(path: str):
    """Returns the name of the file to process"""
    for address, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(".pdf"):
                file_name = os.path.join(address, name)
                yield file_name


class PDF:
    """This class contains an implementation of pdf import"""
    DEFAULT_BOOK_CLASS = 'unknown'

    def __init__(self, path, result_file) -> None:
        self.path: str = path
        self.result_file: str = result_file

    def processing(self) -> None:
        """Processing the directory with pdf files"""
        for file_name in file_finder(self.path):
            text = extract_text(file_name)

            payload = {
                'Text': [text],
                'Class': [self.DEFAULT_BOOK_CLASS],
            }

            df = pd.DataFrame(payload)
            df.to_csv(self.result_file, mode='a', index=False, header=False)
