class bus_6507:
    
    #note the MOS 6507 can only address 8kbit of memory
    ram = [0]*8*1024
    def __init__(self):
        pass

        
    def write(self, addr, data):
        if (addr > 0x000 and addr < 0xFFFF):
            self.ram[addr] = data
    
    def read(self, addr):
        return self.ram[addr]