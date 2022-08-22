"""This file contains the tokenize function to segment the IUPAC name."""
import json
import re
from typing import List


class KMESegmentation(object):
    """Segmentation the Chemical IUPAC name using regular expression."""

    def __init__(self, path: str = None) -> None:
        """Initialize the class with the path to the bag of words file.

        Args:
            path (str): Path to bag of words json file. Defaults to None.
        """
        self.list_of_bag_words = []

        with open(path, 'r') as bag_words_file:
            bag_of_words = json.load(bag_words_file)

        for words in bag_of_words.values():
            self.list_of_bag_words.extend(words)

        self.list_of_bag_words.sort(key=len, reverse=True)

    def segment(self, iupac_name: str) -> List[str]:
        """Segment the iupac_name string using the bag of words.

        Args:
            iupac_name (str): Chemical IUPAC name that need to be segmented.

        Returns:
            List[str]: Results of the segmentation.
        """
        segmented_word = []
        joined_bag_words = '|'.join(self.list_of_bag_words)
        format_bag_words = '({0})'.format(joined_bag_words)
        raw_output = re.split(format_bag_words, iupac_name)

        for word in raw_output:
            if word != '' and word is not None:
                segmented_word.append(word)

        return segmented_word
