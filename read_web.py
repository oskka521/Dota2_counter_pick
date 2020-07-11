from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
"from bs4 import BeautifulSoup
"import requests


PATH = 'C:\Program Files (x86)\chromedriver.exe'
URL = 'https://www.dotabuff.com/heroes/'
# driver.get('https://dotapicker.com')


class Best_hero:
    def __init__(self,):
        pass

    def update1(self, n, a):
        self.Name = n
        self.Advantage = float(a)

    def update2(self, w):
        self.Win_rate = float(w)

    def update3(self, m):
        self.Matches = int(m[:m.find(',')])*1000

    Name = ""
    Advantage = 0.0
    Win_rate = 0.0
    Matches = 0


def extract_set(structure):
    the_text = structure.text.split('\n')[3:]
    hero_arr = []
    start_hero = Best_hero()
    line_counter = 0
    for line in the_text:
        if '%' in line:
            line = line.replace('%', '')
        check = any(c.isalpha() for c in line)

        if check:
            start_hero = Best_hero()
            line_counter = 0
            where = 0
            for c in line:
                if c.isnumeric():
                    break
                where += 1
            start_hero.update1(line[:where-1], float(line[where:]))

        else:
            line_counter += 1
            if line_counter == 1:
                start_hero.update2(line)
            elif line_counter == 2:
                start_hero.update3(line)
                hero_arr.append(start_hero)
    return(hero_arr)


def run(hero, hero_iter, hero_len):
    global PATH, URL
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(PATH, options=options)
    driver.get(URL+hero)

    print(driver.title)
    A = driver.find_elements_by_class_name('skin-container')[0]
    B = A.find_elements_by_class_name('col-8')[0]
    C = B.find_elements_by_tag_name('section')
    i = 0
    Best_counter = 0
    Worst_counter = 0
    for ele in C:
        temp = ele.text
        # for line in temp.split('\n'):
        if "BEST VERSUS" in temp:
            Best_counter = i

        elif "WORST VERSUS" in temp:
            Worst_counter = i
        i += 1
    print(Best_counter, Worst_counter)

    best_arr = extract_set(C[Best_counter])
    worst_arr = extract_set(C[Worst_counter])

    for obj in best_arr:
        print(obj.Name, obj.Advantage, obj.Win_rate, obj.Matches)
    print(" ")
    for obj in worst_arr:
        print(obj.Name, obj.Advantage, obj.Win_rate, obj.Matches)

    if hero_iter != hero_len - 1:
        driver.quit()
    else:
        print("end")
        driver.close()

    return(best_arr, worst_arr)


if __name__ == "__main__":
    hero_list = ['abaddon', 'alchemist', 'ancient-apparition',
                 'anti-mage', 'sniper', 'axe', 'phantom-assassin']
    for i, hero in enumerate(hero_list):
        counter_heros = run(hero, i, len(hero_list))
