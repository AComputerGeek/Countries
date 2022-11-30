# Author:   Amir Armion
# Version:  V.01

import assignment2 as asg2
from data import countries_and_capitals, countries, capitals, countries_capitals_dictionary
import re


def main():
    asg2.write_countries_capitals_to_file("0123456789.txt")
    asg2.save_capitals()


if __name__ == "__main__":
    main()
