from MOS_6507_bus import bus_6507
from MOS_6507 import cpu_6507


    
def main():
    bus = bus_6507()
    cpu = cpu_6507(bus = bus)

    
    print(cpu.processor_statues_register)
    cpu.execute()
    print(cpu.processor_statues_register)
    

if __name__=="__main__":
    main()