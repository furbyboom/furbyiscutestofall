file_ = open(".zshrc")
_file = open(".zshrc", "w")
def read_wright(a, b):
    if a == True:
        return file_.read()
    _file.write(b)
    return file_.read()
data = read_wright(1, "")
data = data + "\n curl -O '" + input("url to extension") + "'"
data = data + "\n sh " + input("name of extension")
exit()
