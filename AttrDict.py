def setClass(k,atrr):
    cmd="class "+k+":\n"
    cmd+="  def __init__(self):\n"
    for i in atrr:
        cmd+="      self."+i+"=None\n"
    cmd+=k+"1="+k+"()"
    return cmd;


def makeDect(currentClass,d,object):
    if str(type(d)) == "<class 'dict'>":
        #print("dict "+str(type(d)))
        atr=[]
        for j in d:
            atr.append(j)
        #print(setClass(currentClass,atr))
        exec(setClass(currentClass,atr))
        for j in d:
            o=makeDect(j,d[j],eval(currentClass+"1"))
            if o!= None:
                exec(currentClass + "1." + j + "=" + "makeDect(j,d[j],eval(currentClass+\"1\"))")


        #print("class created: "+currentClass)
        return eval(currentClass+"1")

    else:
        #print("value "+str(type(d)))
        setattr(object,currentClass,d)
        return None

if __name__ == '__main__':
    currentClass=""
    d = {'person': {
        'name': 'ahmed',
        'age': 26,
        'contact': {
            'email': {
                'personal': 'xmonader@gmail.com',
                'work': 'thabeta@codescalers.com',
            },
            'phone': '01224124',
        }
    }}
    p= makeDect("person",d["person"],None)
    print(p.contact.phone)

