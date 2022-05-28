#Check if two strings after processing backspace character are equal or not

def compare(s,t):
    def check(string):
        a=[]
        for i in string:
            if i!="#":
                a.append(i)
            else:
                a.pop()
        return "".join(a)
    s,t=check(s),check(t)
    return s==t
s = "geee#e#ks"
t = "gee##eeks"
if compare(s,t):
    print("true")
else:
    print("false")