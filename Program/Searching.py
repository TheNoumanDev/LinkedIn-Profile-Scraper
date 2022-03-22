from re import search

class Searching:
    def search(self,data,key):
        final = []
        
        for i in range(len(data)):
            tempp = []*len(data[0])
            for k in range(len(data[0])):
                if ( search(key,data[i][k])):
                    tempp = data[i]
            if len(tempp) != 0:
                final.append(tempp)
        return final
                    
                    
    def Search_ad(self,data,name,name_a,name_col,user,user_a,user_col,comp,comp_a,comp_col,count,count_a,count_col,connec,connec_col):
        
        #print("in search function")
        #final = [[] for i in range(len(data))]
        final = []
        size = len(data)
        for i in range (size):
            a = data[i][connec_col].replace("+","")
            a = a.replace(",","")
            data[i][connec_col] = a
            #print(data[i][connec_col])
        
        if ( name_a == 'AND' ):
            #print(str(user)+" "+str(name)+ " " +str(name_a))
            for i in range(size):
                if ( search(name,data[i][name_col]) and search(user,data[i][user_col]) ):
                    final.append(data[i])
        elif ( name_a == 'OR'):
            for i in range(size):
                if ( search(name,data[i][name_col]) or search(user,data[i][user_col]) ):
                    final.append(data[i])
        #print(str(user)+" "+str(comp)+ " " +str(user_a))
        #print(len(final))
        if ( user_a == 'AND' ):
            #print(str(user)+" "+str(comp)+ " " +str(user_a))
            if( len(final) == 0):
                
                for i in range(size):
                    if ( search(user,data[i][user_col]) and search(comp,data[i][comp_col]) ):
                        final.append(data[i])
            else:
                for j in range(len(final)):
                    item = final[j][user_col]
                    for i in range(size):
                        if ( search(item,data[i][user_col]) and search(comp,data[i][comp_col]) ):
                            if (final[j] != data[i]):
                                final.append(data[i])
        elif ( user_a == 'OR'):
            if( len(final) == 0):
                
                for i in range(size):
                    if ( search(user,data[i][user_col]) or search(comp,data[i][comp_col]) ):
                        final.append(data[i])
            else:
                for j in range(len(final)):
                    item = final[j][user_col]
                    for i in range(size):
                        if ( search(item,data[i][user_col]) or search(comp,data[i][comp_col]) ):
                            if (final[j] != data[i]):
                                final.append(data[i])
        #print(len(final))
        if ( comp_a == 'AND' ):
            #print(str(comp)+" "+str(count)+ " " +str(comp_a))
            if( len(final) == 0):
                
                for i in range(size):
                    if ( search(comp,data[i][comp_col]) and search(count,data[i][count_col]) ):
                        final.append(data[i])
            else:
                for j in range(len(final)):
                    item = final[j][comp_col]
                    for i in range(size):
                        if ( search(item,data[i][comp_col]) and search(count,data[i][count_col]) ):
                            if (final[j] != data[i]):
                                final.append(data[i])
        elif ( comp_a == 'OR'):
            if( len(final) == 0):
                
                for i in range(size):
                    if ( search(comp,data[i][comp_col]) or search(count,data[i][count_col]) ):
                        final.append(data[i])
            else:
                for j in range(len(final)):
                    item = final[j][comp_col]
                    for i in range(size):
                        if ( search(item,data[i][comp_col]) or search(count,data[i][count_col]) ):
                            if (final[j] != data[i]):
                                final.append(data[i])
        if ( count_a == 'AND' ):
            #print(str(count)+" "+str(connec)+ " " +str(count_a))
            if( len(final) == 0):
                
                for i in range(size):
                    if ( search(count,data[i][count_col]) and search(connec,data[i][connec_col]) ):
                        final.append(data[i])
            else:
                for j in range(len(final)):
                    item = final[j][count_col]
                    for i in range(size):
                        if ( search(item,data[i][count_col]) and search(connec,data[i][connec_col]) ):
                            if (final[j] != data[i]):
                                final.append(data[i])
        elif ( count_a == 'OR'):
            if( len(final) == 0):
                
                for i in range(size):
                    if ( search(count,data[i][count_col]) or search(connec,data[i][connec_col]) ):
                        final.append(data[i])
            else:
                for j in range(len(final)):
                    item = final[j][count_col]
                    for i in range(size):
                        if ( search(item,data[i][count_col]) or search(connec,data[i][connec_col]) ):
                            if (final[j] != data[i]):
                                final.append(data[i])
        return final
        
    