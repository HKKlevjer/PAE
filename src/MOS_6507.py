from MOS_6507_bus import bus_6507

class cpu_6507():
    a_register = 0x0000
    x_register = 0x0000
    y_register = 0x0000
    stack_pointer = 0x0000
    program_counter = 0x000
    
    
    
    #2D list represation of the processor statues register
    processor_statues_register = [["CARRY",False],["ZERO",False],["DISABLE INTERRUPT",False],
                                  ["DECIMAL MODE", False], ["Break", False], ["Decimal", False]
                                  ,["OVERFLOW", False], ["Negative",False]]
    
    addr_abs = 0x000
    addr_rel = 0x000
    
    current_opcode = 0x000
    
    cycles = 1
    
    
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
        return self.read_from_buss(self.program_counter)
    
    def IMM(self):
        print("carring out addressing mode IMM")
        self.addr_abs =  self.program_counter + 1
        return self.read_from_bus(self.program_counter)

    
    def ZP0(self):
        self.addr_abs = self.program_counter
        self.program_counter = self.program_counter + 1
        self.addr_abs = 255
        
    def ZPX(self):
        self.addr_abs = self.program_counter + self.x_register
        self.program_counter = self.program_counter + 1
        self.addr_abs = 255
    
    def ZPY(self):
        self.addr_abs = self.program_counter + self.y_register
        self.program_counter = self.program_counter + 1
        self.addr_abs = 255
    
    def ABS(self):
        Addr_low = self.program_counter
        self.program_counter = self.program_counter + 1
        Addr_high = self.program_counter
        self.addr_abs = Addr_low + (Addr_high << 8)
    
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
        Addr_low = self.program_counter
        self.program_counter = self.program_counter + 1
        Addr_high = self.program_counter
        self.program_counter = self.program_counter + 1


    
    def IZX(self):
        pass
    
    def IZY(self):
        pass
       
    def REL(self):
        pass
    
    #method reperesenting of Opcodes
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
        pass
    
    def CLD(self):
        pass
    
    def CLI(self):
        pass
    
    def CLV(self):
        pass
    
    def CMP(self):
        pass
    
    def CPX(self):
        pass
    
    def CPY(self):
        pass
    
    def DEC(self):
        pass
    
    def DEX(self):
        pass
    
    def DEY(self):
        pass
    
    def EOR(self):
        pass
    
    def INC(self):
        pass
    
    def INX(self):
        pass
    
    def INY(self):
        pass
    
    def JMP(self):
        pass
    
    def JSR(self):
        pass
    
    def LDA(self,data):
         print("carring out instuction mode LDA")
         self.a_register = data
    
    def LDX(self):
        pass
    
    def LDY(self):
        pass
    
    def LSR(self):
        pass
    
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
        pass
    
    def SED(self):
        pass

    def SEI(self):
        pass
    
    def STA(self):
        print("ping")
    
    def STX(self):
        pass
    
    def STY(self):
        pass
    
    def TAX(self):
        pass
    
    def TAY(self):
        pass
    
    def TSX(self):
        pass
    
    def TXA(self):
        pass
    
    def TXS(self):
        pass
    
    def TYA(self):
        pass
    
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
        data = self.read_from_bus(self.program_counter)
        self.program_counter = self.program_counter + 1
        self.cycles = self.cycles -1
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
           opcode = self.fetch_next()
           data = eval("self." + self.opcode_lookup_string[opcode][1] + "()")
           eval("self." + self.opcode_lookup_string[opcode][0] + "(data)")
           
           
        
        
        
        