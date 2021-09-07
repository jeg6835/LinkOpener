import time
from selenium import webdriver
import string
import random


def open_website(url, driver):
    url_base = url
    url_letters = generate_random_letter()
    url_numbers = generate_random_numbers()
    driver.get(url_base + url_letters + list_to_strings(url_numbers))


def list_to_strings(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += str(ele)

        # return string
    return str1


def generate_random_letter():
    letter_one = random.choice(string.ascii_letters).lower()
    letter_two = random.choice(string.ascii_letters).lower()
    combined = letter_one + letter_two
    print(letter_one + letter_two)
    return combined


def generate_random_numbers():
    random_nums = random.sample(range(0, 9), 4)
    return random_nums


def main():
    driver = webdriver.Firefox(executable_path=r"F:/geckodriver-v0.29.1-win64/geckodriver.exe")
    while True:
        open_website("https://prnt.sc/", driver)
        time.sleep(5)


if __name__ == '__main__':
    main()
