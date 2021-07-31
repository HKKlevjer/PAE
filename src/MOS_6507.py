from MOS_6507_bus import bus_6507

class cpu_6507:
    
    
    
    #
    a_register = 0x0000
    x_register = 0x0000
    y_register = 0x0000
    stack_pointer = 0x0000
    program_counter = 0x000
    
    
    
    #2D list represation of the processor statues register
    processor_statues_register = [["CARRY",False],["ZERO",False],["DISABLE INTERRUPT",False],
                                  ["DECIMAL MODE", False], ["Break", False], ["Decimal", False]
                                  ,["OVERFLOW", False], ["Negative",False]]
    
    
    #addressing modes
    def IMP():
        pass
    
    def ZP0():
        pass
    
    def ZPY():
        pass
    
    def ABS():
        pass
    
    def ABY():
        pass
    
    def IZX():
        pass
    
    def IMM():
        pass
    
    def ZPX():
        pass
    
    def REL():
        pass
    
    def ABX():
        pass
    
    def IND():
        pass
    
    def IZY():
        pass
    
    #method reperesenting of Opcodes
    def ADC():
        pass
    
    def AND():
        pass
    
    def ASL():
        pass
    
    def BCC():
        pass
    
    def BCS():
        pass
    
    def BEQ():
        pass
    
    def BIT():
        pass
    
    def BMI():
        pass
    
    def BNE():
        pass
    
    def BPL():
        pass
    
    def BRK():
        pass
    
    def BVC():
        pass
    
    def BVS():
        pass
    
    def CLC():
        pass
    
    def CLD():
        pass
    
    def CLI():
        pass
    
    def CLV():
        pass
    
    def CMP():
        pass
    
    def CPX():
        pass
    
    def CPY():
        pass
    
    def DEC():
        pass
    
    def DEX():
        pass
    
    def DEY():
        pass
    
    def EOR():
        pass
    
    def INC():
        pass
    
    def INX():
        pass
    
    def INY():
        pass
    
    def JMP():
        pass
    
    def JSR():
        pass
    
    def LDA():
        pass
    
    def LDX():
        pass
    
    def LDY():
        pass
    
    def NOP():
        pass
    
    def ORA():
        pass
    
    def PHA():
        pass
    
    def PHP():
        pass
    
    def PLA():
        pass
    
    def PLP():
        pass
    
    def ROL():
        pass
    
    def ROR():
        pass
    
    def RTI():
        pass
    
    def RTS():
        pass
    
    def SBC():
        pass
    
    def SEC():
        pass
    
    def SED():
        pass

    def SEI():
        pass
    
    def STA():
        print("ping")
    
    def STX():
        pass
    
    def STY():
        pass
    
    def TAX():
        pass
    
    def TAY():
        pass
    
    def TSX():
        pass
    
    def TXA():
        pass
    
    def TXS():
        pass
    
    def TYA():
        pass
    
    #function called when an illegal code is used
    def illegal_opcode():
        pass
    
    def clock():
        pass
    
    def reset():
        pass
    
    def irq():
        pass
    
    def nmi():
        pass
    
    
    def fetch():
        pass
    
    fetched = 0x0000
    
    addr_abs = 0x000
    addr_rel = 0x000
    
    current_opcode = 0x000
    
    cycles = 0
    
    #initat instacen of bus || change to pointer later
    bus = bus_6507()

    
    def __init__(self):
        pass
    
    def read(self,addr):
        return self.bus.read(addr)
    
    def write(self,addr, data):
        self.bus.write(addr, data)    

    opcode_lookup = [
    ["BRK",BRK(),IMM(),7], ["ORA",ORA(),IZX(),6], ["???",illegal_opcode(),IMP(),2], ["???",illegal_opcode(),IMP(),8], ["???",NOP(),IMP(),3], ["ORA",ORA(),ZP0(),3], ["ASL",ASL(),ZP0(),5], ["???",illegal_opcode(),IMP(),5], ["PHP",PHP(),IMP(),3], ["ORA",ORA(),IMM(),2], ["ASL",ASL(),IMP(),2], ["???",illegal_opcode(),IMP(),2], ["???",NOP(),IMP(),4], ["ORA", ORA(),ABS(),4], ["ASL",ASL(),ABS(),6], ["???",illegal_opcode(),IMP(),6],
    ["BPL",BPL(),REL(),2], ["ORA",ORA(),IZY(),5], ["???",illegal_opcode(),IMP(),2], ["???",illegal_opcode(),IMP(),8], ["???",NOP(),IMP(),4], ["ORA",ORA(),ZPX(),4], ["ASL",ASL(),ZPX(),6], ["???",illegal_opcode(),IMP(),6], ["CLC",CLC(),IMP(),2], ["ORA",ORA(),ABY(),4], ["???",NOP(),IMP(),2], ["???",illegal_opcode(),IMP(),7], ["???",NOP(),IMP(),4], ["ORA", ORA(),ABX(),4], ["ASL",ASL(),ABX(),7], ["???",illegal_opcode(),IMP(),7],
    ["JSR",JSR(),ABS(),6], ["AND",AND(),IZX(),6], ["???",illegal_opcode(),IMP(),2], ["???",illegal_opcode(),IMP(),8], ["BIT",BIT(),ZP0(),3], ["AND",AND(),ZP0(),3], ["ROL",ASL(),ZP0(),5], ["???",illegal_opcode(),IMP(),5], ["PLP",PLP(),IMP(),4], ["AND",AND(),IMM(),2], ["ROL",ROL(),IMP(),2], ["???",illegal_opcode(),IMP(),2], ["BIT",BIT(),ABS(),4], ["AND", AND(),ABS(),4], ["ROL",ROL(),ABS(),6], ["???",illegal_opcode(),IMP(),6],
    ["BMI",BMI(),REL(),2], ["AND",AND(),IZY(),5], ["???",illegal_opcode(),IMP(),2], ["???",illegal_opcode(),IMP(),8], ["???",NOP(),IMP(),4], ["AND",AND(),ZPX(),4], ["ROL",ASL(),ZPX(),6], ["???",illegal_opcode(),IMP(),6], ["SEC",SEC(),IMP(),2], ["AND",AND(),ABY(),4], ["???",NOP(),IMP(),2], ["???",illegal_opcode(),IMP(),7], ["???",NOP(),IMP(),4], ["AND", AND(),ABX(),4], ["ROL",ROL(),ABX(),7], ["???",illegal_opcode(),IMP(),7],
    ["RTI",RTI(),IMP(),6], ["EOR",EOR(),IZX(),6], ["???",illegal_opcode(),IMP(),2], ["???",illegal_opcode(),IMP(),8], ["???",NOP(),IMP(),3], ["EOR",EOR(),ZP0(),3], ["LSR",ASL(),ZP0(),5], ["???",illegal_opcode(),IMP(),5], ["PHA",PHA(),IMP(),3], ["EOR",EOR(),IMM(),2], ["LSR",LSR(),IMP(),2], ["???",illegal_opcode(),IMP(),2], ["JMP",JMP(),ABS(),3], ["EOR", EOR(),ABS(),4], ["LSR",ROL(),ABs(),6], ["???",illegal_opcode(),IMP(),6]]




cpu_2 = cpu_6507()

cpu_2.opcode_lookup[0][1]


