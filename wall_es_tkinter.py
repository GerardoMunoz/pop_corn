from pop_corn.matrix import Matrix, Vec
from pop_corn.mainscene import MainScene
from pop_corn.disc import Disc
from pop_corn.pub_sub import PubSub
from pop_corn.py.context_tkinter import Context_Tkinter as Context
from wall_e import Wall_e
from wall_e_net import Dummy_network


class Host(PubSub):
    def __init__(self,zones_num,net):
        super().__init__()
        self.ip = f"127.0.0.0:8000"
        self.zones_num=zones_num
        self.net=net
        net.open(self.ip,"IP_AP")
        #self.pubsub = PubSub()
        pass
     
    def start(self):
        for i in range(self.zones_num[0]):
            for j in range(self.zones_num[1]):
                name=f"Walle_{i}_{j}"
                self.publish(name, {"steering_angle_deg":20*i+5*j,"speed_cm_s":2, "duration_seg":300})
        #self.publish("All_Wall_es", {"steering_angle_deg":0,"speed_cm_s":20, "duration_seg":2})      


    def animate(self):
        pass
    
    def get_name(self):
        return "Host"

if __name__ == "__main__":
    
    t_anim = 50
    zones_num=(3,4)
    zones_size=(250,250)
    
    net = Dummy_network()
    host = Host(zones_num,net)
    ctx=Context()
    scene = MainScene()#bg='img/UD_@8.xbm', foreground="white", background="black")
    disc0 = Disc(scene)
    
    wall_es=[]
    for i in range(zones_num[0]):
        list_tmp=[]
        for j in range(zones_num[1]):
            disc_tmp=Wall_e(scene,i,j,host,net)
            name=disc_tmp.get_name()
            #disc_tmp.name=f"Walle_{i}_{j}"
            #disc1.color='blue'
            disc_tmp.set_pos(int((i-zones_num[0]/2 +.5)*zones_size[0]),int((j-zones_num[1]/2+0.5)*zones_size[1]))
            #disc1.set_vel(Vec(5,0.5))
            #host.subscribe(disc_tmp.name+" All_Wall_es", disc_tmp, "Command")
            list_tmp.append(list_tmp)
            #host.publish(disc_tmp.name, {"steering_angle_deg":20*i+5*j,"speed_cm_s":15, "duration_seg":5})
            
        wall_es.append(list_tmp)
    
    #host.publish("All_Wall_es", {"steering_angle_deg":0,"speed_cm_s":20, "duration_seg":2})
        
    canvas = ctx.canvas(scene,height=zones_num[1]*zones_size[1],width=zones_num[0]*zones_size[0])

    def anim_loop():    
        ctx.after_ms(t_anim,anim_loop)
        scene.refresh()
        host.animate()
  
    host.start()
    anim_loop() 
    ctx.mainloop()
    
