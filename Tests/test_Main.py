from time import sleep
from Utils.Utilities import Testlinks
from Utils.Utilities import Intantiate
import openpyxl

Dict = {}
Dict_state = {}
Dict_district = {}

def test_setup():
    Intantiate.driver.get(Testlinks.BASE_URL)
    sleep(2)

def test_extract_state():
    state_name = Intantiate.driver.find_elements_by_xpath("//div[@class='location-column']")
    print(len(state_name))
    for val in state_name:
       val.find_element_by_xpath("//div[@class='location-column']")
       Dict_state["State"] = val.text
       #print(Dict1)
       val.click()
       sleep(2)
       district_name = Intantiate.driver.find_elements_by_xpath("//div[@class='location-column']")
       print(len(district_name))
       for district in district_name:
           district.find_element_by_xpath("//div[@class='location-column']")
           Dict_district["District"] = district.text
           print(Dict_district)
       Intantiate.driver.find_element_by_xpath("//div[@class='bookmarked' and contains(text(), 'MissionHumane.org')]").click()
       sleep(2)


def test_loadExcel():
    book = openpyxl.load_workbook("C:\\Training matrial\\Project Covid\\States.xlsx")
    sheet = book.active
    cell = sheet.cell(row=2, column=1)
    for i in range(2, sheet.max_row + 1):
            #print(sheet.cell(row=i, column=1).value)
            Dict["State"] = sheet.cell(row=i, column=1).value
            print(Dict)

def test_StateCompare():
    for key in list(Dict_state.keys()):
        if key in list(Dict.keys()):
            print(True)
        else:
            print(False)






# closing browser
def test_close():
    Intantiate.driver.quit()