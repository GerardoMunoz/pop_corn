import math
from pop_corn.matrix import Matrix, Vec
from pop_corn.mainscene import MainScene
from pop_corn.disc import Disc
from pop_corn.py.context_tkinter import Context_Tkinter as Context


class Wall_e(Disc):
    def __init__(self,scene,i,j,host,net):
        self.host=host
        self.i,self.j=i,j
        super().__init__(scene)
        self.steering_angle_degrees=1
        self.wheelbase=200
        self._t_circle=100
        self.set_speed(5)
        self.poligons=[
            {"points":Matrix(4,2,[3,5, 3,15, 18,15, 18,5]),"options":{}},
            {"points":Matrix(4,2,[-3,5, -3,15, -18,15, -18,5]),"options":{}},
            {"points":Matrix(4,2,[-3,-5, -3,-15, -18,-15, -18,-5]),"options":{}},
            {"points":Matrix(4,2,[3,-5, 3,-15, 18,-15, 18,-5]),"options":{}},
            {"points":Matrix(8,2,[7,-2, 20,-2, 20,-5, 30,-5, 30,5, 20,5, 20,2, 7,2]),"options":{"fill":"yellow"}},
                      ]
        host.subscribe(self.get_name()+" All_Wall_es", self, "Command")
    #def __init__(self, ip, network):
        self.ip = f"127.0.{i}.{j}:8000"
        self.net = net
        net.open(self.ip,"IP_AP")
        self.inbox = []

#     def send(self, target_ip, message):
#         print(f"{self.ip} sending to {target_ip}: {message}")
#         self.network.transmit(self.ip, target_ip, message)
# 
#     def receive(self, src_ip, message):
#         print(f"{self.ip} received from {src_ip}: {message}")
#         self.inbox.append((src_ip, message))        
        
#    def send(self,dest,data):
#        pass

#     def get_ip(self):
#         return f"127.0.{i}.{j}:8000"
#     
#     def recive(self,dest,data):
#         pass
        
    

    def get_name(self):
        return f"Walle_{self.i}_{self.j}"

    def published(self, data=None):
        print("Who published",self.get_name(),data)
        if data["callback_name"]=="Command":
            if "steering_angle_deg" in data["data"]:
                self.steering_angle_degrees=data["data"]["steering_angle_deg"]
                #print("steering_angle_degrees",data["data"]["steering_angle_deg"],self.steering_angle_degrees)
            if "speed_cm_s" in data["data"]:
                self.set_speed(data["data"]["speed_cm_s"])
                #print("speed_cm_s",data["data"]["speed_cm_s"],self.get_speed())
            if "duration_seg" in data["data"]:
                self._t_circle=data["data"]["duration_seg"]
                #print("duration_seg",data["data"]["duration_seg"],self._t_circle)        
        
    @staticmethod
    def default_control(self,t):
        #print("wall_w t",self.i,self.j,self.steering_angle_degrees)
        
        if self._t_circle>0:
        
            v=self.get_speed()
            # Actualización del ángulo del carro
            self.add_angle((v / self.wheelbase) * math.tan(self.steering_angle_degrees*math.pi/180)*t)

            # Desplazamiento en el sistema global
            theta = self._angle  # orientación actual del carro
            dx = v * math.cos(theta) * t
            dy = v * math.sin(theta) * t

            desp = Matrix(1,2,[dx, dy])
            self.add_pos(desp)
            self._t_circle-=t
            #print("wall_w t",t)



