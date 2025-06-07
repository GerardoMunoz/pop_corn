
class Dummy_network:
    def __init__(self):
        self.connected={}
    
    def scan(self,type_):
        return  {k:v for k,v in self.connected.items89 if v.get('type') == type_}
    
    def open(self,name,type_,dest=None):
        if type_=="IP_AP":
            if name in self.connected:
                text=f"There is already an AP with the name: {name}"
                print(text)
                #return text
            else:
                self.connected[name]={type_:{"connected":[],"buffer":bytearray()}}
        elif type_=="IP_STA":
            if dest not in self.connected or "IP_AP" not in self.connected[dest]:
                text=f"There is no AP with the name: {dest}"
                print(text,self.connected)
                raise ValueError(text)
                #return text
            elif name  in self.connected and "IP_STA" in self.connected[name]:
                text=f"There is already an STA with the name: {name} connected to AP: {self.connected[name]['IP_STA']['IP_AP']}"
                print(text,self.connected)
                raise ValueError(text,)
                #return text 
            else:
                self.connected[dest]['IP_AP']["connected"].append(name)
                self.connected[name]|={type_:{"buffer":bytearray(),"IP_AP":dest}}
        

    def close(self,name,type_):
        if name in self.connected:
                if isinstance(self.connected[name], dict):
                    if type_ in self.connected[name]:
                        self.connected[name].pop(type_, None)
                    else:
                        text=f"There is no {type_} with the name: {name}"
                        print(text,self.connected)
                        raise ValueError(text)
 
        else:
                text=f"There is no the name: {name}"
                print(text,self.connected)
                raise ValueError(text)
            
    def write(self,name,type_,bytearray_):
        if name in self.connected:
            if type_ in self.connected[name]:
                self.connected[name][type_]["buffer"]+=bytearray_
            else:
                text=f"There is no {type_} with the name: {name}"
                print(text,self.connected)
                raise ValueError(text)
        else:            
            text=f"There is no the name: {name}"
            print(text,self.connected)
            raise ValueError(text)
    
    def read(self,name,type_):
        if name in self.connected:
            if type_ in self.connected[name]:
                buf=self.connected[name][type_]["buffer"]
                self.connected[name][type_]["buffer"]=bytearray()
                return buf
            else:
                text=f"There is no {type_} with the name: {name}"
                print(text,self.connected)
                raise ValueError(text)
        else:            
            text=f"There is no the name: {name}"
            print(text,self.connected)
            raise ValueError(text)
    
    
            
if __name__ == "__main__":

    net = Dummy_network()

    net.open("127,0,1,1:8000","IP_AP") 
    net.open("127,0,1,2:8000","IP_AP") 
    net.open("127,0,1,3:8000","IP_AP") 
    net.open("127,0,2,1:8000","IP_AP") 
    net.open("127,0,2,2:8000","IP_AP") 
    net.open("127,0,1,2:8000","IP_STA","127,0,1,1:8000") 
    net.open("127,0,1,3:8000","IP_STA","127,0,1,2:8000")
    print(net.connected)
    net.close("127,0,1,3:8000","IP_AP")    
    print(net.connected)
    net.write("127,0,2,1:8000","IP_AP",bytearray(b"Hello "))
    net.write("127,0,2,1:8000","IP_AP",bytearray(b"World"))
    print(net.read("127,0,2,1:8000","IP_AP"))
    net.write("127,0,2,1:8000","IP_AP",bytearray(b"World2"))
    print(net.connected)




