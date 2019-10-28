# Suppose this is the searched URL
url="https://www.amazon.in/gp/product/B01D4EYNUG/ref=s9_acsd_top_hd_bw_b1W0qP9_c_x_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-11&pf_rd_r=T9Z83C5P5N19APX9B0BV&pf_rd_t=101&pf_rd_p=f8fced53-30f6-5525-9f0c-3a9c2535ccf2&pf_rd_i=1389177031"

def convert(sample):     # function to convert string to int
    str=""
    for c in sample:
        if(c=='.'):
            break
        elif(c!=' ' and c!=','):
            str+=c
    return(int(str))

from selenium import webdriver		#Importing packages

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome("C:\\Users\MOHAN KUMAR SAH\Documents\My Work\PakkaIndia\chromedriver",chrome_options=chrome_options)		#create a new instance of google chrome

driver.get(url)		#access google chrome and open our website whose url is mentioned in the variable url

data1=driver.find_elements_by_id('productTitle')
data2=driver.find_elements_by_id('priceblock_ourprice')
data4=driver.find_elements_by_css_selector('td.a-span12.a-color-price.a-size-base')
data3=driver.find_elements_by_css_selector('a.cfs-details.cfs-free-shipping')


if(len(data1)!=0):
    print("Product Name : ",data1[0].text)
    
a=0
b=0
if(len(data2)!=0):
    if(len(data2[0].text)!=0):
        price=convert(data2[0].text)
        a=1   
if(len(data4)!=0):
    if(len(data4[0].text)!=0):
        save=convert(data4[0].text)
        b=1
if(a and b):
    mrp=price+save
    print("MRP : ",mrp)

    
if(a):
    print("Price : ",price)

if(b):
    print("You Save : ",save)
    
if(len(data3)!=0):
    print("Details : ",data3[0].get_attribute('href'))

driver.quit()
