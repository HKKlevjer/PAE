from MOS_6507_bus import bus_6507
from MOS_6507 import cpu_6507


    
def main():
    bus = bus_6507()
    cpu = cpu_6507(bus = bus)

    
    print(bin(cpu.a_register))
    print(cpu.processor_statues_register[0][1])
    cpu.execute()
    print(bin(cpu.a_register))
    print(cpu.processor_statues_register[0][1])
    

if __name__=="__main__":
    main()