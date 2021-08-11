from MOS_6507_bus import bus_6507

class cpu_6507():
    a_register = 0x0000
    x_register = 0x0000
    y_register = 0x0000
    stack_pointer = 0x0000
    program_counter = 0x000
    
    
    #2D list represation of the processor statues register
    processor_statues_register = [["CARRY",False],["ZERO",True],["DISABLE INTERRUPT",False],
                                  ["DECIMAL MODE", False], ["Break", False], ["Decimal", False]
                                  ,["OVERFLOW", False], ["Negative",False]]
    
    addr_abs = 0x000
    addr_rel = 0x000
    
    current_opcode = 0x000
    
    cycles = 3
    
    
    #initat instacen of bus || change to pointer later

    
    
    def __init__(self, bus = None):
        self.bus = bus
    
    def read_from_bus(self,addr):
        return self.bus.read(addr)
    
    def write_to_bus(self,addr, data):
        self.bus.write(addr, data)    

    #---------------------------------------------------------------------------#
    #                                                                           #
    #                        Addresing modes                                    #
    #                                                                           #
    #---------------------------------------------------------------------------#
    def IMP(self):
        pass
    
    def IMM(self):
        self.addr_abs =  self.program_counter + 1
        print(hex(self.addr_abs))

    
    def ZP0(self):
        self.addr_abs = self.read_from_bus(self.program_counter)
        self.program_counter = self.program_counter + 1
        
    def ZPX(self):
        self.addr_abs = self.read_from_bus(self.program_counter)
        self.addr_abs = self.addr_abs + self.x_register

        if(self.addr_abs > 0xFF):
            self.addr_abs = self.addr_abs - 0x100

        self.program_counter = self.program_counter + 1
    
    def ZPY(self):
        self.addr_abs = self.read_from_bus(self.program_counter + self.x_register)
        
        if(self.addr_abs > 0xFF):
            self.addr_abs = self.addr_abs - 0x100
        
        self.program_counter = self.program_counter + 1
    
    def ABS(self):
        self.program_counter = self.program_counter + 1
        low_byte = self.read_from_bus(self.program_counter)
        self.program_counter = self.program_counter + 1
        high_byte = self.read_from_bus(self.program_counter)
        self.addr_abs = low_byte + (high_byte << 8)
    
    
    def ABX(self):
        Addr_low = self.program_counter
        self.program_counter = self.program_counter + 1
        Addr_high = self.program_counter
        self.addr_abs = Addr_low + (Addr_high << 8) + self.x_register
    
    def ABY(self):
        Addr_low = self.program_counter
        self.program_counter = self.program_counter + 1
        Addr_high = self.program_counter
        self.addr_abs = Addr_low + (Addr_high << 8) + self.y_register
    
    def IND(self):
        Addr_low = self.read_from_bus(self.program_counter)
        self.program_counter = self.program_counter + 1
        Addr_high = self.read_from_bus(self.program_counter)
        self.program_counter = self.program_counter + 1
        self.addr_abs = Addr_low + (Addr_high << 8)

    
    def IZX(self):
        Addr_low = self.read_from_bus(self.program_counter)
        self.program_counter = self.program_counter + 1
        Addr_high = self.read_from_bus(self.program_counter)
        self.program_counter = self.program_counter + 1
        self.addr_abs = Addr_low + (Addr_high << 8) + self.x_register
    
    def IZY(self):
        Addr_low = self.read_from_bus(self.program_counter)
        self.program_counter = self.program_counter + 1
        Addr_high = self.read_from_bus(self.program_counter)
        self.program_counter = self.program_counter + 1
        self.addr_abs = Addr_low + (Addr_high << 8) + self.x_register
       
    def REL(self):
        pass
    

    #---------------------------------------------------------------------------#
    #                                                                           #
    #                              Instructions                                 #
    #                                                                           #
    #---------------------------------------------------------------------------#


    def ADC(self):
        pass
    
    def AND(self):
        pass
    
    def ASL(self):
        pass
    
    def BCC(self):
        pass
    
    def BCS(self):
        pass
    
    def BEQ(self):
        pass
    
    def BIT(self):
        pass
    
    def BMI(self):
        pass
    
    def BNE(self):
        pass
    
    def BPL(self):
        pass
    
    def BRK(self):
        pass
    
    def BVC(self):
        pass
    
    def BVS(self):
        pass
    
    def CLC(self):
        self.processor_statues_register[0][1] = False
    
    def CLD(self):
        self.processor_statues_register[3][1] = False
    
    def CLI(self):
        self.processor_statues_register[2][1] = False
   
    def CLV(self):
        self.processor_statues_register[6][1] = False
    
    def CMP(self):
        if(self.a_register >= self.read_from_bus(self.addr_abs)):
            self.processor_statues_register[0][1] = True
        elif(self.a_register >= self.read_from_bus(self.addr_abs)):
            self.processor_statues_register[1][1] = True
        elif(self.a_register - self.read_from_bus(self.addr_abs)< 0):
            self.processor_statues_register[6][1] = True
    
    def CPX(self):
        if(self.x_register >= self.read_from_bus(self.addr_abs)):
            self.processor_statues_register[0][1] = True
        elif(self.x_register >= self.read_from_bus(self.addr_abs)):
            self.processor_statues_register[1][1] = True
        elif(self.x_register - self.read_from_bus(self.addr_abs)< 0):
            self.processor_statues_register[6][1] = True
    
    def CPY(self):
        if(self.y_register >= self.read_from_bus(self.addr_abs)):
            self.processor_statues_register[0][1] = True
        elif(self.y_register >= self.read_from_bus(self.addr_abs)):
            self.processor_statues_register[1][1] = True
        elif(self.y_register - self.read_from_bus(self.addr_abs)< 0):
            self.processor_statues_register[6][1] = True
    
    def DEC(self):
        data = self.read_from_bus(self.addr_abs) - 1
        self.write_to_bus(self.addr_abs, data)
    
    def DEX(self):
        self.x_register = self.x_register - 1
        if(self.x_register == 0):
            self.processor_statues_register[1][1] = True
        elif((self.x_register & 0b10000000) > 0 ):
            self.processor_statues_register[7][1] = True
    
    
    def DEY(self):
        self.y_register = self.y_register - 1
    
    def EOR(self):
        pass
    
    def INC(self):
        data = self.read_from_bus(self.addr_abs) + 1
        self.write_to_bus(self.addr_abs, data)
        if(data == 0):
            self.processor_statues_register[1][1] = True
        elif((data & 0b10000000) > 0 ):
            self.processor_statues_register[7][1] = True
    
    def INX(self):
        self.x_register = self.x_register + 1
        if(self.x_register == 0):
            self.processor_statues_register[1][1] = True
        elif((self.x_register & 0b10000000) > 0 ):
            self.processor_statues_register[7][1] = True
    
    def INY(self):
        self.y_register = self.y_register + 1
        if(self.y_register == 0):
            self.processor_statues_register[1][1] = True
        elif((self.y_register & 0b10000000) > 0 ):
            self.processor_statues_register[7][1] = True
    
    def JMP(self):
        pass
    
    def JSR(self):
        self.stack_pointer = self.program_counter-1
        self.program_counter = self.addr_abs
    
    def LDA(self):
        data = self.read_from_bus(self.addr_abs)
        self.a_register = data
        if(data == 0):
            self.processor_statues_register[1][1] = True
        elif((data & 0b10000000) > 0 ):
            self.processor_statues_register[7][1] = True
         
    
    def LDX(self):
        data = self.read_from_bus(self.addr_abs)
        self.x_register = data
        if(data == 0):
            self.processor_statues_register[1][1] = True
        elif((data & 0b10000000) > 0 ):
            self.processor_statues_register[7][1] = True
    
    def LDY(self):
        data = self.read_from_bus(self.addr_abs)
        self.y_register = data
        if(data == 0):
            self.processor_statues_register[1][1] = True
        elif((data & 0b10000000) > 0 ):
            self.processor_statues_register[7][1] = True
    
    def LSR(self):
        if(self.current_opcode == 0x4A):
            data = self.a_register
            self.processor_statues_register[0][1] = (ddl & 0b00000001)
    
    def NOP(self):
        pass
    
    def ORA(self):
        pass
    
    def PHA(self):
        pass
    
    def PHP(self):
        pass
    
    def PLA(self):
        pass
    
    def PLP(self):
        pass
    
    def ROL(self):
        pass
    
    def ROR(self):
        pass
    
    def RTI(self):
        pass
    
    def RTS(self):
        pass
    
    def SBC(self):
        pass
    
    def SEC(self):
        self.processor_statues_register[0][1] = True
    
    def SED(self):
        self.processor_statues_register[3][1] = True


    def SEI(self):
        self.processor_statues_register[2][1] = True

    
    def STA(self):
        self.write_to_bus(self.addr_abs,self.a_register)
    
    def STX(self):
        self.write_to_bus(self.addr_abs,self.x_register)
    
    def STY(self):
        self.write_to_bus(self.addr_abs,self.y_register)
    
    def TAX(self):
        self.x_register = self.a_register
        if(self.x_register == 0):
            self.processor_statues_register[1][1] = True
        elif((self.x_register & 0b10000000) > 0 ):
            self.processor_statues_register[7][1] = True
    
    def TAY(self):
        self.y_register = self.a_register
        if(self.y_register == 0):
            self.processor_statues_register[1][1] = True
        elif((self.y_register & 0b10000000) > 0 ):
            self.processor_statues_register[7][1] = True
    
    def TSX(self):
        self.x_register = self.stack_pointer
        if(self.x_register == 0):
            self.processor_statues_register[1][1] = True
        elif((self.x_register & 0b10000000) > 0 ):
            self.processor_statues_register[7][1] = True
    
    def TXA(self):
        self.a_register = self.x_register
        if(self.a_register == 0):
            self.processor_statues_register[1][1] = True
        elif((self.a_register & 0b10000000) > 0 ):
            self.processor_statues_register[7][1] = True
    
    def TXS(self):
        self.stack_pointer = self.x_register
        
    
    def TYA(self):
        self.a_register = self.y_register
        if(self.a_register == 0):
            self.processor_statues_register[1][1] = True
        elif((self.a_register & 0b10000000) > 0 ):
            self.processor_statues_register[7][1] = True
    
    #function called when an illegal code is used
    def ILG(self):
        pass
    
    def clock(self):
        pass
    
    def reset(self):
        pass
    
    def irq(self):
        pass
    
    def nmi(self):
        pass
    
    def fetch_next(self):
        print(hex(self.program_counter))
        data = self.read_from_bus(self.program_counter)
        self.cycles = self.cycles - 1
        return data
    

    opcode_lookup_string = [
    ["BRK","IMM",7], ["ORA","IZX",6], ["ILG","IMP",2], ["ILG","IMP",8], ["NOP","IMP",3], ["ORA","ZP0",3], ["ASL","ZP0",5], ["ILG","IMP",5], ["PHP","IMP",3], ["ORA","IMM",2], ["ASL","IMP",2], ["ILG","IMP",2], ["NOP","IMP",4], ["ORA","ABS",4], ["ASL","ABS",6], ["ILG","IMP",6],
    ["BPL","REL",2], ["ORA","IZY",5], ["ILG","IMP",2], ["ILG","IMP",8], ["NOP","IMP",4], ["ORA","ZPX",4], ["ASL","ZPX",6], ["ILG","IMP",6], ["CLC","IMP",2], ["ORA","ABY",4], ["NOP","IMP",2], ["ILG","IMP",7], ["NOP","IMP",4], ["ORA","ABX",4], ["ASL","ABX",7], ["ILG","IMP",7],
    ["JSR","ABS",6], ["AND","IZX",6], ["ILG","IMP",2], ["ILG","IMP",8], ["BIT","ZP0",3], ["AND","ZP0",3], ["ROL","ZP0",5], ["ILG","IMP",5], ["PLP","IMP",4], ["AND","IMM",2], ["ROL","IMP",2], ["ILG","IMP",2], ["BIT","ABS",4], ["AND","ABS",4], ["ROL","ABS",6], ["ILG","IMP",6],
    ["BMI","REL",2], ["AND","IZY",5], ["ILG","IMP",2], ["ILG","IMP",8], ["NOP","IMP",4], ["AND","ZPX",4], ["ROL","ZPX",6], ["ILG","IMP",6], ["SEC","IMP",2], ["AND","ABY",4], ["NOP","IMP",2], ["ILG","IMP",7], ["NOP","IMP",4], ["AND","ABX",4], ["ROL","ABX",7], ["ILG","IMP",7],
    ["RTI","IMP",6], ["EOR","IZX",6], ["ILG","IMP",2], ["ILG","IMP",8], ["NOP","IMP",3], ["EOR","ZP0",3], ["LSR","ZP0",5], ["ILG","IMP",5], ["PHA","IMP",3], ["EOR","IMM",2], ["LSR","IMP",2], ["ILG","IMP",2], ["JMP","ABS",3], ["EOR","ABS",4], ["LSR","ABS",6], ["ILG","IMP",6],
    ["BVC","REL",2], ["EOR","IZY",5], ["ILG","IMP",2], ["ILG","IMP",8], ["NOP","IMP",4], ["EOR","ZPX",4], ["LSR","ZPX",6], ["ILG","IMP",6], ["CLI","IMP",2], ["EOR","ABY",4], ["NOP","IMP",2], ["ILG","IMP",7], ["NOP","IMP",4], ["EOR","ABX",4], ["LSR","ABX",7], ["ILG","IMP",7],
    ["RTS","IMP",6], ["ADC","IZX",6], ["ILG","IMP",2], ["ILG","IMP",8], ["NOP","IMP",3], ["ADC","ZP0",3], ["ROR","ZP0",5], ["ILG","IMP",5], ["PLA","IMP",4], ["ADC","IMM",2], ["ROR","IMP",2], ["ILG","IMP",2], ["JMP","IND",5], ["ADC","ABS",4], ["ROR","ABS",6], ["ILG","IMP",6],
    ["BVS","IMP",2], ["ADC","IZY",5], ["ILG","IMP",2], ["ILG","IMP",8], ["NOP","IMP",4], ["ADC","ZPX",4], ["ROR","ZPX",6], ["ILG","IMP",6], ["SEI","IMP",2], ["ADC","ABY",4], ["NOP","IMP",2], ["ILG","IMP",7], ["JMP","IMP",4], ["ADC","ABX",4], ["ROR","ABX",7], ["ILG","IMP",7],
    ["NOP","IMP",2], ["STA","IZX",6], ["ILG","IMP",2], ["ILG","IMP",6], ["STY","ZP0",3], ["STA","ZP0",3], ["STX","ZP0",3], ["ILG","IMP",3], ["DEY","IMP",2], ["NOP","IMP",2], ["TXA","IMP",2], ["ILG","IMP",2], ["STY","ABS",4], ["STA","ABS",4], ["STX","ABS",4], ["ILG","IMP",4],
    ["BCC","REL",2], ["STA","IZY",6], ["ILG","IMP",2], ["ILG","IMP",6], ["STY","ZPX",4], ["STA","ZPX",4], ["STX","ZPY",4], ["ILG","IMP",4], ["TYA","IMP",2], ["STA","ABY",5], ["TXS","IMP",2], ["ILG","IMP",5], ["NOP","IMP",5], ["STA","ABX",5], ["ILG","ABS",5], ["ILG","IMP",5],
    ["LDY","IMM",2], ["LDA","IZX",6], ["LDX","IMM",2], ["ILG","IMP",6], ["LDY","ZP0",3], ["LDA","ZP0",3], ["LDX","ZP0",3], ["ILG","IMP",3], ["TAY","IMP",2], ["LDA","IMM",2], ["TAX","IMP",2], ["ILG","IMP",2], ["LDY","ABS",4], ["LDA","ABS",4], ["LDX","ABS",4], ["ILG","IMP",4],
    ["BCS","REL",2], ["LDA","IZY",5], ["ILG","IMP",2], ["ILG","IMP",5], ["LDY","ZPX",4], ["LDA","ZPX",4], ["LDX","ZPY",4], ["ILG","IMP",4], ["CLV","IMP",2], ["LDA","ABY",4], ["TSX","IMP",2], ["ILG","IMP",4], ["LDY","ABX",4], ["LDA","ABX",4], ["LDX","ABY",4], ["ILG","IMP",4],
    ["CPY","IMM",2], ["CMP","IZX",6], ["NOP","IMP",2], ["ILG","IMP",8], ["CPY","ZP0",3], ["CMP","ZP0",3], ["DEC","ZP0",5], ["ILG","IMP",5], ["INY","IMP",2], ["CMP","IMM",2], ["DEX","IMP",2], ["ILG","IMP",2], ["CPY","ABS",4], ["CMP","ABS",4], ["DEC","ABS",6], ["ILG","IMP",6],
    ["BNE","REL",2], ["CMP","IZY",5], ["ILG","IMP",2], ["ILG","IMP",8], ["NOP","IMP",4], ["CMP","ZPX",4], ["DEC","ZPX",6], ["ILG","IMP",6], ["CLD","IMP",2], ["CMP","ABY",4], ["NOP","IMP",2], ["ILG","IMP",7], ["NOP","IMP",4], ["CMP","ABX",4], ["DEC","ABX",7], ["ILG","IMP",7],
    ["CPX","IMM",2], ["SBC","IZX",6], ["NOP","IMP",2], ["ILG","IMP",8], ["CPX","ZP0",3], ["SBC","ZP0",3], ["INC","ZP0",5], ["ILG","IMP",5], ["INX","IMP",2], ["SBC","IMM",2], ["NOP","IMP",2], ["SBC","IMP",2], ["CPX","ABS",4], ["SBC","ABS",4], ["INC","ABS",6], ["ILG","IMP",6],
    ["BEQ","REL",2], ["SBC","IZY",6], ["ILG","IMP",2], ["ILG","IMP",8], ["NOP","IMP",3], ["SBC","ZPX",4], ["INC","ZPX",6], ["ILG","IMP",6], ["SED","IMP",2], ["SBC","ABY",4], ["NOP","IMP",2], ["ILG","IMP",7], ["NOP","IMP",4], ["SBC","ABX",4], ["INC","ABX",7], ["ILG","IMP",7]]

    
    def execute(self):
        while(self.cycles > 0):
           self.current_opcode = self.fetch_next()
           data = eval("self." + self.opcode_lookup_string[opcode][1] + "()")
           eval("self." + self.opcode_lookup_string[opcode][0] + "()")
           
           
        
        
        
        