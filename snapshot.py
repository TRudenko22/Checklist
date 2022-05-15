#########################################
# Author: Tim Rudenko                   #
# Class: Snapshot                       #
# Purpose: Takes a snapshot of state.   # 
#########################################


class Snapshot:
    def __init__(self, file_name) -> None:
        self.file_name = file_name

    def take_snapshot(self, data: list) -> None:
        with open(self.file_name, 'w') as f:
            for line in data:
                if '\n' in line:
                    f.write(str(line))
                else:
                    f.write(str(line) + '\n')

    def retrieve(self) -> list:
        with open(self.file_name, 'r') as f:
            return f.readlines()
    
    def clear(self) -> None:
        with open(self.file_name, 'w') as f:
            f.write('')
