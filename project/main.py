import requests

url = 'http://econpy.pythonanywhere.com/ex/001.html'

if __name__ == '__main__': 
    
    response = requests.get(url)

    if response.status_code == 200:
        content = response.text #str
        print(content)

     
    # with open('econpy.html','w+') as file:
    #     file.write(content)