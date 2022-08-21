import json
import re
from typing import List

class KMESegmentation(object):
    """Segmentation the Chemical IUPAC name using regular expression"""

    def __init__(self, path: str = None) -> None:
        """Initialize the class with the path to the bag of words file

        Args:
            path (str): Path to bag of words json file. Defaults to None.
        """
        self.list_of_bag_words = []

        if path is None:
            raise (ValueError("Path is not specified"))

        with open(path, "r") as f:
            bag_of_words = json.load(f)

        for values in bag_of_words.values():
            self.list_of_bag_words.extend(values)

        self.list_of_bag_words.sort(key=len, reverse=True)

    def segment(self, input: str) -> List[str]:
        """Segment the input string using the bag of words

        Args:
            input (str): Chemical IUPAC name that need to be segmented.

        Returns:
            List[str]: Results of the segmentation.
        """
        raw_output = re.split(rf"({'|'.join(self.list_of_bag_words)})", input)
        output = [word for word in raw_output if word]

        return output
