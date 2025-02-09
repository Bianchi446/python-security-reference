# Protocol lists

protocolList = []
protocolList.append("FTP")
protocolList.append("SSH")
protocolList.append("SMTP")
protocolList.append("HTTP")

# Position 

position = protocolList.index("SSH")
print(position)

# count

for protocol in protocolList:
    print(protocol)

print(len(protocolList))

# Update mathod in dictionaries 
services = {"ABC" : 1, "CDA" : 2, "BAC": 3}
services2 = {"ABCD" : 1, "ACDA" : 2, "BACE": 3}

services.update(services2)
print(services)

# finding valiues in dictionaries 

def contains(dictionary, item):
    for key,value in dictionary.items():
        if value == item:
            return True
        return False 

dictionary = {1:100, 2:200, 3:3000}

print(contains(dictionary, 300))
print(contains(dictionary, 200))
print(contains(dictionary, 350))


# Protocol object defitnion 

class Protocol(object):
    def __init__(self, name, number, description):
        self.name = name
        self.number = number
        self.description = description
    def GetProtocolInfo(self): 
        return self.name + " " + str(self.number) + " " + self.description

https_protocol = Protocol("HTTPS", 443, "Hypertext transfer protocol secure")

print(https_protocol.GetProtocolInfo())


# inheritance 

class BaseClass:
      def __init__(self, property):
        self.property = property
      def message(self):
        print("This is the base class")
      def message_base_class(self):
        print("This is a message from the base class")

class child_class(BaseClass):
    def __init__(self, property):
        BaseClass.__init__(self, property)
    def message(self):
        print("This is a message from the child class")


print(issubclass(BaseClass, child_class))

if __name__ == "__main__":
    base_obj = BaseClass('property')
    base_obj.message_base_class()
    child_obj = child_class('property')
    child_obj.message()



# try/except hadling 

try:
    print("10/0=", str(10/0))
except Exception as exception:
    print("Error=", str(exception))

try:
    list=[]
    elementList=list[0]
except Exception as exception:
    print("Exception=", str(exception))

# Exception handling for managing with files 

try: 
    file_handle = open('zfile.txt', 'r')
except IOError as exception:
    print("IO error: unable to read file", exception)
except Exception as exception:
    print("Exception", exception)
else:
    print("File read successfully")
    file_handle.close()


# Information from modules 

import sys

print(sys.builtin_module_names)
print("--------------------")
print(dir(sys))
