import pandas as pd
def read_csv():
    # csv = open("START.csv","r","encoding = utf-8")
    dataset = pd.read_csv("START.csv")
    name = (dataset.iloc[:, 0:1]).values.tolist()
    logo = (dataset.iloc[:, 5:6]).values.tolist()
    status = (dataset.iloc[:, 1:2]).values.tolist()
    fund = (dataset.iloc[:, 8:9]).values.tolist()
    website_link = (dataset.iloc[:, 9:10]).values.tolist()
    founded = (dataset.iloc[:, 2:3]).values.tolist()
    categories = (dataset.iloc[:, 4:5]).values.tolist()
    
    # print(categories)
    categories = sum(categories, [])
    name = sum(name, [])
    logo = sum(logo, [])
    status = sum(status, [])
    fund = sum(fund,[])
    website_link = sum(website_link, [])
    founded = sum(founded, [])

    # for x in categories:
    #     #print(x)
    #     if ("Media") in str(x):
    #         print(x)

    startup_name = []
    startup_logo = []
    startup_foundedat =[]
    startup_website = []
    startup_status = []

    for j in range(len(categories)-1):
        if ("Media") in str(categories[j]):
            startup_name.append(name[j])
            startup_logo.append(logo[j])
            startup_foundedat.append(founded[j])
            startup_website.append(website_link[j])
            startup_status.append(status[j])
    
    print(startup_name, startup_foundedat)
    
read_csv()