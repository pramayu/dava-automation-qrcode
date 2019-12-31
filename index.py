import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys

path = r"D:\dava_auto_port\utils\chromedriver.exe"
options = ChromeOptions()
choose = input("Choose 1: ODP & 2: DROPCORE : ")
options.add_experimental_option("debuggerAddress","127.0.0.1:54958")
driver = webdriver.Chrome(path, options=options)
result = open(r"D:\dava_auto_port\utils\result.txt","w")

data = [
        {
            "SERVICE": "172413219054",
            "QRDROPCORE": "TF70RHX131Z1"
        },
        {
            "SERVICE": "172413210290",
            "QRDROPCORE": "TF70CB34KGVS"
        },
        {
            "SERVICE": "3614790032",
            "QRDROPCORE": "TF70Z523XD0P"
        },
        {
            "SERVICE": "172411803062",
            "QRDROPCORE": "TF707RLNXARL"
        },
        {
            "SERVICE": "172428804886",
            "QRDROPCORE": "TF70EZ3O9PAF"
        },
        {
            "SERVICE": "172413209748",
            "QRDROPCORE": "TF70U8GW6ZLL"
        },
        {
            "SERVICE": "172413211163",
            "QRDROPCORE": "TF70SPZX07HD"
        },
        {
            "SERVICE": "172408204918",
            "QRDROPCORE": "TF70IGO87ZCN"
        },
        {
            "SERVICE": "172408815070",
            "QRDROPCORE": "TF70SMYEAC1J"
        },
        {
            "SERVICE": "172408817624",
            "QRDROPCORE": "TF70892WKWGL"
        },
        {
            "SERVICE": "172408818207",
            "QRDROPCORE": "TF70XKM4Y811"
        },
        {
            "SERVICE": "172408205634",
            "QRDROPCORE": "TF702OOXA7LH"
        },
        {
            "SERVICE": "361952403",
            "QRDROPCORE": "TF70S1Y5DA1O"
        },
        {
            "SERVICE": "172408818420",
            "QRDROPCORE": "TF70F3W5ZOWV"
        },
        {
            "SERVICE": "172408812388",
            "QRDROPCORE": "TF70HGAG7GVY"
        },
        {
            "SERVICE": "172408806075",
            "QRDROPCORE": "TF70E4GKTE0I"
        },
        {
            "SERVICE": "172408806600",
            "QRDROPCORE": "TF70SZQUHPGD"
        },
        {
            "SERVICE": "172407215147",
            "QRDROPCORE": "TF700YU0CCJ1"
        },
        {
            "SERVICE": "172408808009",
            "QRDROPCORE": "TF70QQSU4YRO"
        },
        {
            "SERVICE": "172408818983",
            "QRDROPCORE": "TF70I771R1T5"
        },
        {
            "SERVICE": "172408817204",
            "QRDROPCORE": "TF70JVOZOPB6"
        },
        {
            "SERVICE": "361980514",
            "QRDROPCORE": "TF703MWVRF8J"
        },
        {
            "SERVICE": "172408815661",
            "QRDROPCORE": "TF703QDKCXEV"
        },
        {
            "SERVICE": "172428802845",
            "QRDROPCORE": "TF704EQBOBW5"
        },
        {
            "SERVICE": "172403226186",
            "QRDROPCORE": "TF709WBXVLMF"
        },
        {
            "SERVICE": "172428800718",
            "QRDROPCORE": "TF70Q6029EPX"
        },
        {
            "SERVICE": "172428803986",
            "QRDROPCORE": "TF70G721M6ZP"
        },
        {
            "SERVICE": "172428804245",
            "QRDROPCORE": "TF704HA93CO7"
        },
        {
            "SERVICE": "172405203586",
            "QRDROPCORE": "TF7005M11368"
        },
        {
            "SERVICE": "172405203832",
            "QRDROPCORE": "TF70LSANDX2P"
        },
        {
            "SERVICE": "172405803802",
            "QRDROPCORE": "TF70PLKEP2MT"
        },
        {
            "SERVICE": "172405803903",
            "QRDROPCORE": "TF70PQZYPGSR"
        },
        {
            "SERVICE": "172405203534",
            "QRDROPCORE": "TF70VICI2C6B"
        },
        {
            "SERVICE": "172405203532",
            "QRDROPCORE": "TF70I3XY11Z7"
        },
        {
            "SERVICE": "172405203523",
            "QRDROPCORE": "TF70OZ2WYORA"
        },
        {
            "SERVICE": "172405795333",
            "QRDROPCORE": "TF70BFL7BZGC"
        },
        {
            "SERVICE": "172408814739",
            "QRDROPCORE": "TF707ZQHJB0L"
        },
        {
            "SERVICE": "172408803290",
            "QRDROPCORE": "TF70RQA67HUW"
        },
        {
            "SERVICE": "172422216584",
            "QRDROPCORE": "TF70PM28YK2O"
        },
        {
            "SERVICE": "172408204785",
            "QRDROPCORE": "TF70T7L8IKDL"
        },
        {
            "SERVICE": "172408204795",
            "QRDROPCORE": "TF70824UHMG6"
        },
        {
            "SERVICE": "172411224251",
            "QRDROPCORE": "TF70E5RU8W1S"
        },
        {
            "SERVICE": "172428803304",
            "QRDROPCORE": "TF70A8VRZWQ1"
        },
        {
            "SERVICE": "172428804702",
            "QRDROPCORE": "TF70LEQB7VFR"
        },
        {
            "SERVICE": "361975642",
            "QRDROPCORE": "TF70ZL8L2DBM"
        },
        {
            "SERVICE": "361974252",
            "QRDROPCORE": "TF7032ZWZ1AP"
        },
        {
            "SERVICE": "361976246",
            "QRDROPCORE": "TF70KR72GALR"
        },
        {
            "SERVICE": "361972772",
            "QRDROPCORE": "TF709TXGINB0"
        },
        {
            "SERVICE": "361971888",
            "QRDROPCORE": "TF70FXCYU599"
        },
        {
            "SERVICE": "361970896",
            "QRDROPCORE": "TF70184K7AGZ"
        },
        {
            "SERVICE": "172408813171",
            "QRDROPCORE": "TF70F48ET8S8"
        },
        {
            "SERVICE": "172408813257",
            "QRDROPCORE": "TF70E52L0MB5"
        },
        {
            "SERVICE": "172408810936",
            "QRDROPCORE": "TF70A4G7BQPZ"
        },
        {
            "SERVICE": "172408819537",
            "QRDROPCORE": "TF70OK0BGU10"
        },
        {
            "SERVICE": "172408815153",
            "QRDROPCORE": "TF70X5U8V39G"
        },
        {
            "SERVICE": "172408809700",
            "QRDROPCORE": "TF70D757W45P"
        },
        {
            "SERVICE": "172408205047",
            "QRDROPCORE": "TF701S56WY93"
        },
        {
            "SERVICE": "172408205226",
            "QRDROPCORE": "TF70O9P3TXC"
        },
        {
            "SERVICE": "172408816571",
            "QRDROPCORE": "TF70BXXWPXLO"
        },
        {
            "SERVICE": "172428801617",
            "QRDROPCORE": "TF70SU7SQU5Q"
        },
        {
            "SERVICE": "172405800538",
            "QRDROPCORE": "TF70LZ08UU82"
        },
        {
            "SERVICE": "172405803766",
            "QRDROPCORE": "TF70RKT5KFRU"
        },
        {
            "SERVICE": "172405802817",
            "QRDROPCORE": "TF70ZAWPRGOF"
        },
        {
            "SERVICE": "172405203840",
            "QRDROPCORE": "TF70K29L6HCV"
        },
        {
            "SERVICE": "172405802272",
            "QRDROPCORE": "TF70WWKUCVA5"
        },
        {
            "SERVICE": "172405802590",
            "QRDROPCORE": "TF707QOXI9CS"
        },
        {
            "SERVICE": "172405802447",
            "QRDROPCORE": "TF70CE8893DT"
        },
        {
            "SERVICE": "172405800506",
            "QRDROPCORE": "TF70VPO6W351"
        },
        {
            "SERVICE": "172408808501",
            "QRDROPCORE": "TF70BLE8UUPQ"
        },
        {
            "SERVICE": "172408807175",
            "QRDROPCORE": "TF70D6IDSASL"
        },
        {
            "SERVICE": "172408203905",
            "QRDROPCORE": "TF70EKLZW7SP"
        },
        {
            "SERVICE": "172408820135",
            "QRDROPCORE": "TF70423M1QDD"
        },
        {
            "SERVICE": "172408806559",
            "QRDROPCORE": "TF70EKFQSYT1"
        },
        {
            "SERVICE": "172408807244",
            "QRDROPCORE": "TF70F8NW4QXP"
        },
        {
            "SERVICE": "172408815160",
            "QRDROPCORE": "TF70HJVM5EDF"
        },
        {
            "SERVICE": "172408817464",
            "QRDROPCORE": "TF70OHUWK23R"
        },
        {
            "SERVICE": "172408808205",
            "QRDROPCORE": "TF70QX3L9MNU"
        },
        {
            "SERVICE": "172408807763",
            "QRDROPCORE": "TF70S8V1XQFM"
        },
        {
            "SERVICE": "172408807747",
            "QRDROPCORE": "TF70LY865QT2"
        },
        {
            "SERVICE": "172408807410",
            "QRDROPCORE": "TF7019MD0XS6"
        },
        {
            "SERVICE": "172408815955",
            "QRDROPCORE": "TF707XUVTRMC"
        },
        {
            "SERVICE": "172408807453",
            "QRDROPCORE": "TF70GUCY302K"
        },
        {
            "SERVICE": "172428804903",
            "QRDROPCORE": "TF70CN419X79"
        },
        {
            "SERVICE": "172428804914",
            "QRDROPCORE": "TF70SS218PZP"
        },
        {
            "SERVICE": "172413806718",
            "QRDROPCORE": "TF70E9LMV1ED"
        },
        {
            "SERVICE": "172428801800",
            "QRDROPCORE": "TF703DI7T1AQ"
        },
        {
            "SERVICE": "172428801544",
            "QRDROPCORE": "TF70A945SYTO"
        },
        {
            "SERVICE": "172428801501",
            "QRDROPCORE": "TF70HVRU67CX"
        },
        {
            "SERVICE": "172413207934",
            "QRDROPCORE": "TF70VY121SR3"
        }
]

if choose == '1':
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
		kapasitas = len(odp['PORT'])
		time.sleep(2)
		driver.find_element_by_link_text(f"{kapasitas}").click()
		i = 0
		x = 0
		while i < len(odp['PORT']):
			driver.find_elements_by_class_name("btn-circle")[x + 1].click()
			time.sleep(2)
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
		if drop['SERVICE'][0] == '3':
			driver.find_element_by_id("servid").send_keys(f"0{drop['SERVICE']}")
		else:
			driver.find_element_by_id("servid").send_keys(drop['SERVICE'])
		driver.find_element_by_id("servid").send_keys(Keys.ENTER)
		time.sleep(2)
		driver.find_elements_by_name("selecteds")[0].click()
		driver.find_element_by_link_text("DP/ODP").click()
		time.sleep(2)
		driver.find_elements_by_id("SERVICE_POINT_DP_DROPCABLE_QRCODE")[0].send_keys(drop['QRDROPCORE'])
		driver.find_elements_by_id("SERVICE_POINT_DP_DROPCABLE_QRCODE")[0].send_keys(Keys.ENTER)
		print(drop['SERVICE'])
		time.sleep(3)
		success = driver.find_elements_by_class_name("alert-success")
		danger = driver.find_elements_by_class_name("alert-danger")
		if success:
			result.write(f"{drop['SERVICE']} success \n")
		elif danger:
			result.write(f"{drop['SERVICE']} failed \n")
