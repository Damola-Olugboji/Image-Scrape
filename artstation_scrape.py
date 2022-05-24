from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


import sys, os, time
import requests
from random import randrange


def artstationScraper(driver, website_path, artist_name):
    driver.get(website_path)

    test = True
    timeout = 3

    element_present = EC.presence_of_element_located((By.CLASS_NAME, "img"))
    WebDriverWait(driver, timeout).until(element_present)
    image = driver.find_elements_by_class_name("img")
    src = image[0].get_attribute("src")
    save_image_to_file(src, artist_name)
    time.sleep(2)
    while test:
        try:
            time.sleep(3)
            actions = ActionChains(driver)
            actions.send_keys(Keys.ARROW_RIGHT)
            actions.perform()
            time.sleep(5)
            element_present = EC.presence_of_element_located((By.CLASS_NAME, "img"))
            WebDriverWait(driver, timeout).until(element_present)
            image = driver.find_elements_by_class_name("img")
            src = image[0].get_attribute("src")
            save_image_to_file(src, artist_name)
            time.sleep(3)

        except NoSuchElementException:
            test = False

    print("Closing Window...")
    driver.close()


def save_image_to_file(src, name):
    cwd = os.path.abspath(os.getcwd())
    save_dir = "Images/{}".format(name)
    full_path = os.path.join(cwd, save_dir)
    isDir = os.path.isdir(full_path)
    file_name = random_number() + ".jpg"

    response = requests.get(src)
    if response.status_code == 200:
        if isDir:
            full_path = os.path.join(full_path, file_name)
            with open(full_path, "wb") as f:
                f.write(response.content)
            print("Image {} saved in {} Folder\n".format(file_name, name))
            return True
        else:
            os.mkdir(full_path)
            print("\nDirectory Created for {} Folder".format(name))
            full_path = os.path.join(full_path, file_name)
            with open(full_path, "wb") as f:
                f.write(response.content)
            print("Image {} saved in {} Folder\n".format(file_name, name))
            return True
    else:
        return False


def random_number():
    return str(randrange(100000))


if __name__ == "__main__":
    webdriver_path = "/Users/damolaolugboji/drivers/chromedriver"
    driver = webdriver.Chrome(executable_path=webdriver_path)
    # site = sys.argv[1]
    # artist_name = sys.argv[2]
    site = "https://www.artstation.com/artwork/xYJ03O"
    artist_name = "Wyman Pang"
    # artist_name = Louis Lin
    # site = https://www.artstation.com/artwork/Vy0yAX

    artstationScraper(driver, site, artist_name)
