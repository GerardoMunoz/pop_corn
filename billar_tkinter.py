    




if __name__ == "__main__":

    from pop_corn.matrix import Matrix, Vec
    from pop_corn.mainscene import MainScene
    from pop_corn.disc import Disc
    from pop_corn.py.context_tkinter import Context_Tkinter as Context
    
    t_anim = 50

    ctx=Context()
    scene = MainScene()#bg='img/UD_@8.xbm', foreground="white", background="black")
    disc0 = Disc(scene)
    
    disc1 = Disc(scene)
    disc1.r=10
    disc1.color='blue'
    disc1.set_pos(-50,0)
    disc1.set_vel(Vec(5,0.5))

    canvas = ctx.canvas(scene)

    def anim_loop():    
        ctx.after_ms(t_anim,anim_loop)
        scene.refresh()

  
    anim_loop() 
    ctx.mainloop()
    
