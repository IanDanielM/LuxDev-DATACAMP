import requests,json
import pandas as pd

def get_data():
    male_gender=[]
    response = requests.get("https://randomuser.me/api/?gender=male")
    page=1
    while page<100:
        response = requests.get("https://randomuser.me/api/?page="+str(page)+"&gender=male")
        page+=1
        data=response.json()
        for i in data["results"]:
            genderZ=i['gender']
            name=i["name"]["first"]
            male_gender.append((genderZ,name))


    with open('jsonmale.json', 'w') as males:
        json.dump(male_gender,males)
    df=pd.read_json('jsonmale.json')
    headers=['gender','name']
    df.to_csv('csvmale.csv',index=False,header=headers)
   

    

    

    


       


get_data()