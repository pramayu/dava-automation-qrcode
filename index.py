import json
import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys

path = r"D:\dava_auto_port\utils\chromedriver.exe"
options = ChromeOptions()
choose = input("Choose 1: ODP & 2: DROPCORE : ")
version = input("Choose version: ")
options.add_experimental_option("debuggerAddress","127.0.0.1:53901")
driver = webdriver.Chrome(path, options=options)
result = open(r"D:\dava_auto_port\utils\result.txt","a+")
unused = open(r"D:\dava_auto_port\utils\unused.txt","a+")

with open('data\data.json','r') as f:
    data = json.load(f)

if choose == '1':
	driver.get("https://emas.telkom.co.id/DAVA/dataValidation/validOrderCapture/servicePoint")
	for odp in data:
		time.sleep(2)
		driver.find_elements_by_id("filter")[5].click()
		driver.find_elements_by_id("deviceLocation")[0].send_keys(odp['ODP'])
		driver.find_elements_by_id("deviceLocation")[0].send_keys(Keys.ENTER)
		# driver.find_elements_by_class_name("btn-circle")[1].click()
		# time.sleep(2)
		# driver.find_elements_by_id("showqrcode")[0].clear()
		# driver.find_elements_by_id("showqrcode")[0].send_keys(odp['QRODP'])
		# driver.find_elements_by_id("showqrcode")[0].send_keys(Keys.ENTER)
		kapasitas = len(odp['PORT'])
		time.sleep(2)
		driver.find_element_by_link_text(f"{kapasitas}").click()
		i = 0
		x = 0
		while i < len(odp['PORT']):
			driver.find_elements_by_class_name("btn-circle")[x + 1].click()
			time.sleep(3)
			driver.find_elements_by_id("showqrcode")[0].clear()
			print(odp['PORT'][i][f"{i}"])
			driver.find_elements_by_id("showqrcode")[0].send_keys(odp['PORT'][i][f"{i}"])
			driver.find_elements_by_id("showqrcode")[0].send_keys(Keys.ENTER)
			time.sleep(2)
			i +=1
			x +=2
		driver.get("https://emas.telkom.co.id/DAVA/dataValidation/validOrderCapture/servicePoint")

elif choose == '2':
    driver.get('https://emas.telkom.co.id/DAVA/dataValidation/validOrderCapture/omzetAccessNetwork/findByServiceId')
    for drop in data:
        driver.find_element_by_id("servid").clear()
        try:
            if drop['SERVICE'][0] == '3':
                driver.find_element_by_id("servid").send_keys(f"0{drop['SERVICE']}")
            else:
                driver.find_element_by_id("servid").send_keys(drop['SERVICE'])
            driver.find_element_by_id("servid").send_keys(Keys.ENTER)
            time.sleep(2)
            driver.find_elements_by_name("selecteds")[0].click()
            driver.find_element_by_link_text("DP/ODP").click()
            uii = driver.find_elements_by_id("SERVICE_POINT_current_DP_DROPCABLE_QRCODE")[0]
            xcv = uii.get_attribute('value')
            drp = drop['QRDROPCORE']
            if len(xcv) > 4:
                if version == '1':
                    if xcv != drp:
                        time.sleep(2)
                        driver.find_elements_by_id("SERVICE_POINT_DP_DROPCABLE_QRCODE")[0].send_keys(drop['QRDROPCORE'])
                        driver.find_elements_by_id("SERVICE_POINT_DP_DROPCABLE_QRCODE")[0].send_keys(Keys.ENTER)
                        print(drop['SERVICE'])
                        time.sleep(3)
                        success = driver.find_elements_by_class_name("alert-success")
                        danger = driver.find_elements_by_class_name("alert-danger")
                        if success:
                            result.write(f"{drop['SERVICE']} success\n")
                        elif danger:
                            result.write(f"{drop['SERVICE']} failed\n")
                    else:
                        print(drop['SERVICE'])
                        print("sama")
                        result.write(f"{drop['SERVICE']} success\n")
                        driver.get('https://emas.telkom.co.id/DAVA/dataValidation/validOrderCapture/omzetAccessNetwork/findByServiceId')
                else:
                    print(f"SKIP {drop['SERVICE']}")
                    unused.write(f"{drop['QRDROPCORE']}\n")
                    pass
            else:
                time.sleep(2)
                driver.find_elements_by_id("SERVICE_POINT_DP_DROPCABLE_QRCODE")[0].send_keys(drop['QRDROPCORE'])
                driver.find_elements_by_id("SERVICE_POINT_DP_DROPCABLE_QRCODE")[0].send_keys(Keys.ENTER)
                print(drop['SERVICE'])
                time.sleep(3)
                success = driver.find_elements_by_class_name("alert-success")
                danger = driver.find_elements_by_class_name("alert-danger")
                if success:
                    result.write(f"{drop['SERVICE']} success\n")
                elif danger:
                    result.write(f"{drop['SERVICE']} failed\n")
        except:
        	result.write(f"{drop['SERVICE']} service not found\n")
        	pass
        

elif choose == '3':
	driver.get("https://emas.telkom.co.id/DAVA/dataValidation/validOrderCapture/servicePoint")
	for odp in data:
		time.sleep(2)
		driver.find_elements_by_id("filter")[5].click()
		driver.find_elements_by_id("deviceLocation")[0].send_keys(odp['ODP'])
		driver.find_elements_by_id("deviceLocation")[0].send_keys(Keys.ENTER)
		driver.find_elements_by_class_name("btn-circle")[1].click()
		time.sleep(2)
		driver.find_elements_by_id("showqrcode")[0].clear()
		driver.find_elements_by_id("showqrcode")[0].send_keys(odp['QRODP'])
		driver.find_elements_by_id("showqrcode")[0].send_keys(Keys.ENTER)
		time.sleep(3)
		print(odp['ODP'])
		success = driver.find_elements_by_class_name("alert-success")
		danger = driver.find_elements_by_class_name("alert-danger")
		if success:
			result.write(f"{odp['ODP']} success\n")
		elif danger:
			result.write(f"{odp['ODP']} failed\n")
		driver.get("https://emas.telkom.co.id/DAVA/dataValidation/validOrderCapture/servicePoint")