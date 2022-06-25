import httplib2


h = httplib2.Http('.cache')
for i in range(1, 82):
    file1 = "https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/" + str(i) + ".png"
    file2 = r"C:/Users/Ilya/Desktop/New/" + str(i) + ".png"
    response, content = h.request(file1)
    out = open(file2, 'wb')
    out.write(content)
    out.close()