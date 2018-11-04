import re
import unittest


def sumNum(fileName):
    # Write a function sumNums(filename) to read from a
    # file when given the filename and look for integers (that are not phone numbers) using the re.findall(),
    # and then convert the extracted strings to integers and return the sum of the integers.

    Infile = open(fileName, "r")
    line = str(Infile.readlines())
    findallVar = re.findall(r"\d+", line)
    # phone_regex = re.compile(r"\d{3}-\d{3}-\d{4}")
    # findall_phones = re.findall(phone_regex, line)
    firstNum = map(int, findallVar)
    sumNum = sum(firstNum)
    return sumNum


def countWord(fileName, word):
    # Write a function countWord(filename,word) to return a count of the number of times a specified word appears in a file.
    # It should match the word when it starts a sentence also (starts with a capital letter).
    # It should not match any additional letters after the word.
    # For example, if called on “computer” it should match “Computer” and “computer” but not “computers”.
    # For file regex_sum_42.txt it will return 21 when called with the word “computer”.

    f = open(fileName, "r")
    regex_string = r"\b" + word.upper() + r"\b"
    all_instance_of_word = re.findall(regex_string, f.read().upper())
    return (len(all_instance_of_word))


def listURLs(fileName):
    # Write a function listURLs(fileName) to return a list of the URLs in the file when given the file name.
    # It should match URLs like www.cnn.com.
    # It doesn’t have to return the http:// part or the https:// part of the URL, but it can.
    # For file regex_sum_42.txt it will return a list of three URLs.

    inFile = open(fileName, "r")
    data = inFile.read()
    inFile.close()
    listUrls = re.findall(r'www.[(a-zA-Z0-9)]+.[(a-zA-Z0-9)]+', data)
    return listUrls


class TestHW6(unittest.TestCase):
    """ Class to test this homework """

    def test_sumNums1(self):
        """ test sumNums on the first file """
        self.assertEqual(sumNums("regex_sum_42.txt"), 445833)

    def test_sumNums2(self):
        """ test sumNums on the second file """
        self.assertEqual(sumNums("regex_sum_132198.txt"), 374566)

    def test_countWord(self):
        """ test count word on the first file """
        self.assertEqual(countWord("regex_sum_42.txt", "computer"), 21)

    def test_listURLs(self):
        """ test list URLs on the first file """
        self.assertEqual(len(listURLs("regex_sum_42.txt")), 3)


def main():
    # run the tests
    print(sumNums('regex_sum_132198.txt'))  # should be 27486
    print(sumNums('regex_sum_42.txt'))  # should be 27486

    # print(sumNums('regex_sum_132198.txt'))
    print(countWord('regex_sum_42.txt', "computer"))  # should be 21
    print(countWord('regex_sum_132198.txt', "computer"))


    print(listURLs("regex_sum_42.txt"))  # should have 3 urls
    print(listURLs("regex_sum_132198.txt"))  # should have 3 urls


if __name__ == "__main__":
    unittest.main(verbosity=2)
    # main()
