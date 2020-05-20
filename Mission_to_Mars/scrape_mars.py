from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

mars_data = {}

# NASA Mars news
def mars_news():
    try:
        # initialize browser, create html objects, and parse with Beautiful Soup
        browser = init_browser()
        url1 = https://mars.nasa.gov/news/
        browser.visit(url1)
        html1 = browser.html
        soup1 = bs(html1, 'html.parser')

        article = soup.select_one('ul.item_list li.slide')

        # news article and descriptive paragraph 
        news_title = article.find('div', class_='content_title').text
        news_p = article.find('div', class_ = 'article_teaser_body').text

        # append to mars_data dictionary
        mars_data['news_title'] = news_title
        mars_data['news_p'] = news_p

        return mars_data
    
    # end browser session
    finally:
        browser.quit()

# NASA JPL image
def mars_image():
    try:
        # initialize browser, create html objects, and parse with Beautiful Soup
        browser = init_browser()
        url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(url2)
        html2 = browser.html
        soup2 = BeautifulSoup(html2, 'html.parser')

        # find image, navigate into full image rl and extract url
        featured_image = soup2.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]
        base_url = 'https://www.jpl.nasa.gov'
        featured_image_url = base_url + featured_image

        # append to mars_data dictionary
        mars_data['featured_image_url'] = featured_image_url

        return mars_data

    # end browser
    finally:
        browser.quit()


# Mars weather twitter
def mars_weather():
    try:


# Mars info table
def mars_facts():
    try:
        # initialize browser
        browser = init_browser()

        # read url with pandas, create dataframe, and convert to html table
        mars_data = pd.read_html('https://space-facts.com/mars/')[0]
        mars_dataf = pd.DataFrame(mars_data)
        mars_df.columns = ["Description", "Value"]
        mars_table = mars_df.to_html(header = False, index = False)

        # append to mars_data dictionary
        mars_data['mars_table'] = mars_table

        return mars_data
    
    # end browser
    finally:
        browser.quit()

def mars_hemispheres():
    try:
        # initialize browser, create html objects, and parse with Beautiful Soup
        url4 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(url4)
        html4 = browser.html
        soup4 = BeautifulSoup(html4, 'html.parser')
        
        # create empty list to store images and image titles as dictionary
        hemisphere_img_urls = [] 

        # navigate into 'items' class to extract title and url
        articles = soup4.find('div', class_ = 'result-list')
        imgs = articles.find_all('div', class_ = 'item')

        # for loop to go through each 'item' class
        for img in imgs:
            
            # extract image title, remove "Enhanced" from each title
            title = img.find('h3').text
            title = title.replace(" Enhanced", "")

            # extract image url and append to base url
            link = img.find('a')['href']
            full_url = 'https://astrogeology.usgs.gov/' + link

            # create new browser/bs session to navigate into full image pages
            browser.visit(full_url)
            html_link = browser.html
            soup = BeautifulSoup(html_link, 'html.parser')

            # extract full image url and append to hemisphere_image_urls list
            downloads = soup.find('div', class_ = 'downloads')
            img_url = downloads.find('a')['href']
            hemisphere_img_urls.append({"title": title, "img_url": img_url})
        
        # append to mars_data dictionary
        mars_data['hemisphere_img_urls'] = hemisphere_img_urls

        return mars_data
    
    # end browser
    finally:
        browser.quit()