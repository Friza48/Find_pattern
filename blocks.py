import re
import yaml

start = []
end = []
block = []
flag = False


with open('blocks.yaml', 'r') as i:
    instr = yaml.safe_load(i)
block_start = instr['block_start']
block_end = instr['block_end']


with open('gate-config.cfg', 'r') as f:
    lines = f.readlines()


for line in lines:
    if flag == False:
        
        start = re.findall (block_start, line) 
        if start == []:
            pass
        else:
            flag = True
    
    
    if flag == True:
        
        end = re.findall (block_end, line)
        if end == []:
            block += line
        else:
            flag = False
            block += line
            block = ''.join(block)
            print (block)
            start = []
            end = []
            block = []


    
    
    
    


        


