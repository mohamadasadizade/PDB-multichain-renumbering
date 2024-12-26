
"""
author: Mohammad Assadizadeh
 
"""

def readfile(filepath):
    with open(filepath) as f:
        return [ i.strip() for i in f.readlines()]
    


def rearranged_pdb_list(pdb_list , outputPath):
    output = open(outputPath ,'w')
    for i in range(len(pdb_list)):
        if i >= 608 and i <= 4056 :
            if pdb_list[i][21] == 'B':
                new_line = pdb_list[i][:23] + str(int(pdb_list[i][23:26])+407) + pdb_list[i][26:]
                output.write(new_line+'\n')
            else:
                output.write(pdb_list[i]+'\n')
        else:
            output.write(pdb_list[i]+'\n')
    output.close()    
    return output 


rearranged_pdb_list(readfile('input.pdb'),'output.pdb')






    



