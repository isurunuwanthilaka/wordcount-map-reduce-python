import requests

for i in range(1340, 1400):
    url = "http://www.gutenberg.org/files/{}/{}.txt".format(i, i)
    myfile = requests.get(url)
    open('./'+str(i)+'.txt', 'wb').write(myfile.content)
