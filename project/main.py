import requests
import re

url = 'http://econpy.pythonanywhere.com/ex/001.html'

if __name__ == '__main__':

    with open ('econpy.html','r') as file:
        content = file.read()
    # response = requests.get(url)

    # if response.status_code == 200:
    #     content = response.text #str
        # print(content)

        # modulo 1 imprimiendo datos de bayer manera 1
        regexa = '<div title="buyer-name">'
        regexb = '</div>'

    for line in content.split('\n'):

        if regexa in line:
            start = line.find(regexa) + len (regexa)

            end = line.find(regexb)
            title = line[start:end]

    #         print(title)
    # with open('econpy.html','w+') as file:
    #     file.write(content)


    # manera 2//

    regex = '<div title="buyer-name">(.+?)</div>'

    for title in re.findall(regex, content):
        print(title)