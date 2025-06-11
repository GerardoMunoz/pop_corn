# cambios a realizar.
#     data es bytearray
#     Se anexa una string de 4 caracters con el formato
#     se debe hacer un buffer o lista o diccionarion para almacenar published
#     debe permitir adicionar al principio o al final o borrar la lista
#from pop_corn.queue import Queue
from uqueue import uQueue


class PubSub:
    def __init__(self):
        self.topics = {}

    def subscribe(self, topics, who, callback_name):
        self.log("subscribe:"+str(topics)+" "+str( who)+" "+str( callback_name))
        for  topic in topics.split():
            if topic not in self.topics:
                self.topics[topic] = []
            self.topics[topic].append({"who":who,"callback_name":callback_name})

#     def unsubscribe(self, topic, who, callback_name):
#         if topic in self.topics:
#             try:
#                 self.topics[topic].remove(callback)
#                 if not self.topics[topic]:
#                     del self.topics[topic]
#             except ValueError:
#                 pass  # Callback not found

    def publish(self, topics, data=None):
        self.log("publish:"+str(topics)+" "+str( data))
        for  topic in topics.split():
            if topic in self.topics:
                for info in self.topics[topic]:
                    info["who"].published(info|{"data":data,"topic":topic, "who":self.get_name()})
            
    def log(self, string):
        print(string)
        
    def get_name(self):
        return "PubSub"



        
# class Who:
#     def __init__(self,name):
#         self.name=name
#         
#     def published(self, data=None):
#         print("Who published",self.name,data)


class Who:
    def __init__(self, name, pubsub, subscriptions):
        self.name = name
        self.queues = {}  # callback_name -> Queue()
        self.ps=pubsub

        # Subscribe to each topic using provided PubSub
        for topic, callback_name in subscriptions:
            self.ensure_queue(callback_name)
            pubsub.subscribe(topic, self, callback_name)

    def ensure_queue(self, callback_name):
        if callback_name not in self.queues:
            self.queues[callback_name] = uQueue(callback_name)

    def published(self, data):
        callback_name = data.get("callback_name")
        control= data.get("control","appendlast")
        if callback_name is None:
            return
        self.ensure_queue(callback_name)
        if control=="appendlast":
            self.queues[callback_name].appendlast(data)
        if control=="appendfirst":
            self.queues[callback_name].appendfirst(data)
        if control=="clear_appendfirst":
            self.queues[callback_name].clear()
            self.queues[callback_name].appendfirst(data)

    def process(self, callback_name):
        queue = self.queues.get(callback_name)
        if queue:
            #while len(queue):
                msg = queue.popfirst()
                print(f"{self.name}:{callback_name} received ->", msg)
        else:
            print(f"{self.name}:{callback_name} No_received")



if __name__ == "__main__":




    ps = PubSub()

    Host = Who(
        name="Host",
        pubsub=ps,
        subscriptions=[
            ("all_dev/frame", "on_frame"),
            ("all_dev/alert", "on_alert")
        ]
    )
    deviceA = Who(
        name="DeviceA",
        pubsub=ps,
        subscriptions=[
            ("all_dev/arm devA/arm", "on_arm"),
            ("all_dev/move devA/move", "on_arm")
        ]
    )
    deviceB = Who(
        name="DeviceB",
        pubsub=ps,
        subscriptions=[
            ("all_dev/arm devB/arm", "on_arm"),
            ("all_dev/move devB/move", "on_move")
        ]
    )

    Host.ps.publish("devA/arm", {"value": 23})
    Host.ps.publish("all_dev/move", {"value": "10"})

    deviceA.process("on_arm")
    deviceB.process("on_arm")
    deviceA.process("on_move")
    deviceB.process("on_move")
    deviceA.process("on_arm")
    deviceB.process("on_arm")
    deviceA.process("on_move")
    deviceB.process("on_move")
    deviceA.process("on_arm")
    deviceB.process("on_arm")
    deviceA.process("on_move")
    deviceB.process("on_move")

# 
# 
#     # Create PubSub instance
#     pubsub = PubSub()
# 
# 
# 
# 
# ###############################################
#     who1=Who(1)
# #     In who1 ->
# #     def temperature_handler(data):
# #         print("Temperature update:", data)
#     pubsub.subscribe("temperature cool", who1, "temperature_handler")
# ###############################################
#     who2=Who(2)
# #     In who2 ->
# #     def humidity_handler(data):
# #         print("Humidity update:", data)
#     pubsub.subscribe("humidity rain",who2 , "humidity_handler")
# ###############################################
#     
#     # Publish some data
#     pubsub.publish("temperature cool", 25.6)
#     pubsub.publish("rain", 65)
#     pubsub.publish("humidity", 60)
