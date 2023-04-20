#!/usr/bin/env python3

import sys
import re
    

class Сondition_checker:
    
    index_pattern = 0

    
    def __init__ (self):   
        file = sys.argv[-3]
        with open(file, 'r') as f:
            self.lines = f.readlines()
        
        self.index_pattern = list()
        
        # self.pattern = sys.argv[-2]
        

    
    def find_pattern(self):
        for line in self.lines:
            line = line.lower() # нижний регистр всей строки
            found_pattern = re.findall (self.pattern, line) 
            if found_pattern == "":
                pass
            else:
                self.index_pattern.append(self.lines.index(line))
        
    
    
    def conditions(self):
        if  self.index_pattern1!= 0 and self.index_pattern2 != 0 and self.index_pattern2 > self.index_pattern1:
            sys.exit(0)

if __name__=='__main__':
    checker = Сondition_checker()
    
    checker.find_pattern()
    
    checker.conditions() 
              





#index_user = 0
#index_cmd = 0
#both_found = False
#file = sys.argv[-3]
#pattern1 = sys.argv[-2]
#pattern2 = sys.argv[-1]

'''
    def find_pattern2(self):
        for line in self.lines:
            line = line.lower() # нижний регистр всей строки
            found_pattern2 = re.findall (self.pattern2, line)
            found_pattern2 = "".join(found_pattern2) # преобразования list в str
            self.pattern2 = "".join(j for j in self.pattern2 if j.isalnum())
            if found_pattern2 == self.pattern2:
                self.index_pattern2 = self.lines.index(line)
                break
        if found_pattern2 != self.pattern2:
            print ("pattern2 отсутствует или не в начале строки")
            sys.exit(-1)  
# Поиск User 
with open('Dockerfile') as text:
    for line in text:
        line = line.lower() # нижний регистр всей строки
        find_user = re.findall ('^user', line) 
        find_user = "".join(find_user) # преобразования list в str
        cnt_user += 1
        if find_user == 'user':
            break
    if find_user != 'user':
        print ("user отсутствует или не в начале строки")
        sys.exit(-1)
        cnt_user = 0

# Поиск cmd или entrypoint
with open('Dockerfile') as text:
    for line in text:
        line = line.lower() # нижний регистр всей строки
        find_cmd = re.findall ('^cmd', line) 
        find_entrypoint = re.findall ('^entrypoint', line) 
        find_cmd = "".join(find_cmd) # преобразования list в str
        find_entrypoint = "".join(find_entrypoint)
        cnt_cmd += 1
        if find_cmd == 'cmd' or find_entrypoint == 'entrypoint':
            break
    if find_cmd != 'cmd' and find_entrypoint != 'entrypoint':
        print ("cmd и entrypoint отсутствуют или не в начале строки")
        sys.exit(-1)
        cnt_cmd = 0
    
# Проверка всех условий 
if cnt_cmd != 0 and cnt_user != 0 and cnt_user < cnt_cmd:
    print ('Все успешно')
    sys.exit(0)
else:
    print ('Not ok')
    sys.exit(-1)
'''

'''
    def find_cmd(self):            for line in lines:
                line = line.lower() # нижний регистр всей строки
                find_cmd = re.findall ('^cmd', line) 
                find_entrypoint = re.findall ('^entrypoint', line) 
                find_cmd = "".join(find_cmd) # преобразования list в str
                find_entrypoint = "".join(find_entrypoint)
                cnt_cmd += 1
                if find_cmd == 'cmd' or find_entrypoint == 'entrypoint':
                    index_cmd = lines.index(line)
                    break
            if find_cmd != 'cmd' and find_entrypoint != 'entrypoint':
                print ("cmd и entrypoint отсутствуют или не в начале строки")
                sys.exit(-1)
                cnt_cmd = 0
 '''         