class KeyVal:
    def __init__(self,key,val):
        self.key=key
        self.val=val

class INI:
    def __init__(self,s):
        self.sectionsName=[]
        self.sectionsMaps=[[]]
        i=0
        for line in s.split("\n"):
            if self.is_comment(line) or self.is_empty(line):
                continue
            elif self.is_section(line):
                secName=line[1:-1]
                self.add_section(secName)
                i=self.sectionsName.index(secName)
            elif self.is_keyval(line):
                kv=KeyVal(line.split('=')[0],line.split('=')[1])
                self.sectionsMaps[i].append(kv)
            else:
                raise Exception("Can't process line {}".format(line))
        # j=0
        # for s in self.sectionsName:
        #     print(print(s))
        #     for m in self.sectionsMaps[j]:
        #         print(m.key + m.val )
        #     j+=1

    def is_keyval(self, line):
        pos = line.find('=');
        return pos != -1 and line[0:pos].find('=') == -1 and line[0:pos].find(';') == -1

    def is_section(self, line):
        return line[0] == '[' and line[-1] == ']' and line[1:-1].find(']') == -1

    def is_comment(self, line):
        return len(line) > 0 and (line[0] == ';' or line[0] == '#')

    def is_empty(self, line):
        return len(line) == 0
    def add_section(self,name):
        self.sectionsName.append(name)
        self.sectionsMaps.append([])
    def get_properity(self,secName,k):
        i=self.sectionsName.index(secName)
        mapArr=self.sectionsMaps[i]
        for mm in mapArr:
            if mm.key == k:
                return mm.val
        return None
    def has_section(self,secName):
        return  secName in self.sectionsName
    def has_properity(self,secName,k):
        i = self.sectionsName.index(secName)
        mapArr = self.sectionsMaps[i]
        for mm in mapArr:
            if mm.key == k:
                return True
        return False

sample1 = """
[general]
appname=configparser
version=0.1
[author]
name=xmonader
email=notxmonader@gmail.com
"""
ini=INI(sample1)
print(ini.get_properity("general","appname"))
print(ini.has_properity("author","email"))
print(ini.has_properity("author","pass"))
