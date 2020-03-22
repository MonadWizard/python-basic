class Accident(Exception):
    def __init__(self,msg):
        self.msg=msg
        # self.msg = " \n this is message. "
    def print_exception(self):
        print("User define exception : ",self.msg)
    def handle(self):
        print("accident occer. take detour")

try:
    raise Accident('\n :::::::::::::::: \n crash between two cars \n ::::::::::::::: \n')
except Accident as e:
    e.print_exception()
    e.handle()


