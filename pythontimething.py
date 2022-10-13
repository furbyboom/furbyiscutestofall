file_ = open(".zshrc")
def read_wright(a, b):
    if a == True:
        return file_.read()
    open(".zshrc", "w").write(b)
    return file_.read()
data = read_wright(True, "")
data = data + "\n curl -O '" + input("url to extension") + "'"
data = data + "\n sh " + input("name of extension")
read_wrigh(False, data)
exit()
