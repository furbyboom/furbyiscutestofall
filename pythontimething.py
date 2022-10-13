file_ = open(".zshrc")
def read_wright(a, b):
    if a == True:
        return file_.read()
    open(".zshrc", "w").write(b)
    return file_.read()
data = read_wright(True, "")
data = data + "\ncurl -O '" + input("url to extension") + "'"
data = data + "\nsh " + input("name of extension")
read_wright(False, data)
exit()
