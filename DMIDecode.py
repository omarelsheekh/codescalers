class DMIDCode:
    def __init__(self,s):
       arr=s.split("\n")
       self.dict={}
       i=6
       arr.append(':')
       while i< len(arr)-1:
        k=arr[i].split(":")[0].strip()
        v=arr[i].split(':')[1].strip()
        while not ':' in arr[i+1]:
            v+='\n'+arr[i+1].strip()
            i+=1
        i+=1
        self.dict[k]=v

    def getValue(self,s):
        return self.dict[s]

data= """# dmidecode 3.1
Getting SMBIOS data from sysfs.
SMBIOS 2.6 present.

Handle 0x0001, DMI type 1, 27 bytes
Bios Information
        Vendor: LENOVO
        Version: 29CN40WW(V2.17)
        Release Date: 04/13/2011
        ROM Size: 2048 kB
        Characteristics:
                PCI is supported
                BIOS is upgradeable
                BIOS shadowing is allowed
                Boot from CD is supported
                Selectable boot is supported
                EDD is supported
                Japanese floppy for NEC 9800 1.2 MB is supported (int 13h)
                Japanese floppy for Toshiba 1.2 MB is supported (int 13h)
                5.25"/360 kB floppy services are supported (int 13h)
                5.25"/1.2 MB floppy services are supported (int 13h)
                3.5"/720 kB floppy services are supported (int 13h)
                3.5"/2.88 MB floppy services are supported (int 13h)
                8042 keyboard services are supported (int 9h)
                CGA/mono video services are supported (int 10h)
                ACPI is supported
                USB legacy is supported
                BIOS boot specification is supported
                Targeted content distribution is supported
        BIOS Revision: 1.40
"""
dmid=DMIDCode(data)
print(dmid.getValue("ROM Size"))
print(dmid.getValue("Characteristics"))

