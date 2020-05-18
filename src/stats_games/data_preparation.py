from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.params import Params


def get_games():
    """
    This function get the links of games ended in bundesliga season
    :return: list with links of games to get info's
    """
    # make a driver to create a section were we going to work, and get the links of site
    driver = webdriver.Chrome(executable_path=Params.path_crome)
    driver.get('https://www.scoreboard.com/uk/football/germany/bundesliga/results/')
    # click in load more while button exists
    while True:
        try:
            WebDriverWait(driver, 120).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="live-table"]/div[1]/div/div/a'))).click()
        except:
            break
    #get page sourge read with BeautifulSoup
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    #get all div's where have lik of games
    games = soup.find_all('div', {'class': 'event__match event__match--static event__match--oneLine'})
    #make a list of links in list comprehension, quit drive and return list
    games = ['https://www.scoreboard.com/uk/match/' + item['id'].split('_')[2] + '/#match-summary' for item in games]
    driver.quit()
    return games
