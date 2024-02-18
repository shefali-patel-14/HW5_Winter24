# Name:
# Student ID:
# Email:
# List who you have worked with on this homework:
# List any AI tool (e.g. ChatGPT, GitHub Copilot):

import re
import os
import unittest

def get_leader_info(file_name: str) -> list:
    """
    
    This function reads the file with the file name and returns a list of strings. 
    Each string should contain all the information for one leader.

    Args:
        file_name (str): file name of data

    Returns:
        leader_data (list): a list of strings with each leader’s information

    """
    # TODO: implement this function
    pass

def create_leader_dict(leader_data: list) -> dict:
    """
    
    This function returns a dictionary with keys as numbers (1 - 20) 
    and values as a tuple of each leader's first and last name.

    Args:
       leader_data (list): a list of strings with each leaders’s information

    Returns:
        names_dict (dictionary): a dictionary with keys as numbers (1 - 20) 
    and values as a tuple of each leader's first and last name.

    """
     # TODO: implement this function
    pass

def finding_long_words(leader_data: list) -> tuple:
    """
    
    This function gets a list of strings with each leaders’s information and returns a tuple.

    Args:
       leader_data (list): a list of strings with each president’s information

    Returns:
        long_words (tuple): the first value of the tuple should be a list of all long words
        found and the second value should be the average length of those found words

    """
    # TODO: implement this function
    pass

def compute_age_dict(leader_data: list) -> dict:
    """
    
    This function returns a dictionary with leader’s full names as keys and their birth year, death year,
    and age as values in tuples.

    Args:
       leader_data (list): a list of strings with each leaders’s information

    Returns:
        age_dict (dictionary): a dictionary with the leaders’s full names (including any suffixes such as Jr) 
        as keys and their birth year, death year, and age as values in tuples.

    """
    # TODO: implement this function
    pass

#Extra Credit
def find_abbr_dict(leader_data: list) -> dict:
    
      """
    This function finds all abbreviations and returns a dictionary with abbreviations as keys and full forms as values.
        - Abbreviations are made of consecutive uppercase letters inside a set of parentheses.
        - Full forms are consecutive words starting with an uppercase letter.

    Args:
        leader_data (list): a list of strings with each leader’s information

    Returns:
        abbr_dict (dictionary): a dictionary with abbreviations as keys and full forms as values
    """
    # TODO: implement this function
pass


class TestLeaderFunctions(unittest.TestCase):


    def setUp(self):
        # TODO: fill in the blank
        self.leader_data = ...
        self.names_dict = ...
        self.long_words = ...
        self.age_dict = ...
        self.abbr_dict = ...

    def test_get_leader_info(self):
        # TODO: implement this test case
        pass

    def test_create_leader_dict(self):
        # TODO: implement this test case
        pass

    def test_finding_long_words(self):
        # TODO: implement this test case
        pass

    def test_compute_age_dict(self):
        # TODO: implement this test case
        pass

#Extra Credit
    def test_find_abbr_dict(self):
        # TODO: implement this test case
        pass



def main():
    unittest.main(verbosity=2)


if __name__ == "__main__":
    main()
