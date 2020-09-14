def headless_driver(path: str):
    from selenium.webdriver.chrome.options import Options
    from selenium import webdriver
    chromeOptions = Options()
    chromeOptions.headless = True
    driver = webdriver.Chrome(executable_path=path, options=chromeOptions)
    return driver
def stock_update():
    from selenium import webdriver
    from selenium.webdriver.support.ui import Select
    import time
    import pandas as pd
    from datetime import datetime

    PATH = "/home/ahmed/selenimu_tutorial/chromedriver"
    driver = headless_driver(PATH)
    driver.get("https://dps.psx.com.pk/")
    time.sleep(3)
    select = Select(driver.find_element_by_name("DataTables_Table_0_length"))
    select.select_by_visible_text('All')
    #time.sleep(2)
    print(driver.title)
    table = driver.find_element_by_id("DataTables_Table_0_wrapper")
    headings = table.find_elements_by_tag_name("th")
    titles = []
    for heading in headings:
        titles.append(heading.text)
    print(titles)
    data_rows = table.find_element_by_class_name("tbl__body")
    data_rows = data_rows.find_elements_by_tag_name("tr")
    data = []
    for data_row in data_rows:
        tds = data_row.find_elements_by_tag_name("td")
        row = []
        for td in tds:
            row.append(td.text)
        data.append(row)
    driver.quit()
    t = str(datetime.now())
    print("Market summary at", t)
    df = pd.DataFrame(data, columns = titles)
    filename = "./data_" + str(t) + ".csv"
    f = open(filename, "w")
    df.to_csv(f, index = False)
    f.close()
stock_update()



