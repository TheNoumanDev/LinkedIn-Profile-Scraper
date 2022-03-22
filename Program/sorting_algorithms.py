

class algorithm:
    
    #################################################################################################
    ######################################## Selection  Sort ########################################
    #################################################################################################
    def Selection_ascend(self,array,col):
        if( col != 5):
            size=len(array)
            
            for i in range(0,size-1):
                min = i
                for j in range(i+1,size):
                    if(array[j][col]<array[min][col]):
                        min=j
                if(min !=i):
                    array[i],array[min]=array[min],array[i]
        else:
            size=len(array)
            for i in range(0,size-1):
                min = i
                for j in range(i+1,size):
                    
                    a = array[j][col].replace("+","")
                    a = a.replace(",","")
                    
                    b = array[min][col].replace("+","")
                    b = b.replace(",","")
                    if( a == ''):
                        a = '0'
                    if( b == ''):
                        b = '0'
                    if int(a)< int(b):
                        min=j
                if(min !=i):
                    array[i],array[min]=array[min],array[i]
        return array
    def Selection_decend(self,array,col):
        if( col != 5):
            size=len(array)
            for i in range(0,size-1):
                min = i
                for j in range(i+1,size):
                    if(array[j][col]>array[min][col]):
                        min=j
                if(min !=i):
                    array[i],array[min]=array[min],array[i]
        else:
            size=len(array)
            for i in range(0,size-1):
                min = i
                for j in range(i+1,size):
                    
                    a = array[j][col].replace("+","")
                    a = a.replace(",","")
                    
                    b = array[min][col].replace("+","")
                    b = b.replace(",","")
                    if( a == ''):
                        a = '0'
                    if( b == ''):
                        b = '0'
                    if int(a)> int(b):
                        min=j
                if(min !=i):
                    array[i],array[min]=array[min],array[i]
        return array
    
    #################################################################################################
    ######################################## CockTails  Sort ########################################
    #################################################################################################
    
    def CocktailSort_ascend(self,A,col):
        if(col != 5):
            isSwapped = True
            start = 0
            end = len(A) - 1

            while (isSwapped == True):

                isSwapped = False
                i = start
                while ( i < end ):
                    if (A[i][col] > A[i + 1][col]):
                        A[i], A[i + 1] = A[i + 1], A[i]
                        isSwapped = True
                    i += 1

                if (isSwapped == False):
                    break
                isSwapped = False
                i = end - 2
                while(  i > start - 1):
                    if (A[i][col] > A[i + 1][col]):
                        A[i], A[i + 1] = A[i + 1], A[i]
                        isSwapped = True
                    i = i - 1

                start = start + 1

            return A
        else:
            isSwapped = True
            start = 0
            end = len(A) - 1

            while (isSwapped == True):

                isSwapped = False
                i = start
                while ( i < end ):
                    a = A[i][col].replace("+","")
                    a = a.replace(",","")
                    if( a == ''):
                        a = '0'
                    a = int(a)
                    b = A[i+1][col].replace("+","")
                    b = b.replace(",","")
                    if( b == ''):
                        b = '0'
                    b = int(b)
                    if (a > b):
                        A[i], A[i + 1] = A[i + 1], A[i]
                        isSwapped = True
                    i += 1

                if (isSwapped == False):
                    break
                isSwapped = False
                i = end - 2
                while(  i > start - 1):
                    a = A[i][col].replace("+","")
                    a = a.replace(",","")
                    if( a == ''):
                        a = '0'
                    a = int(a)
                    b = A[i+1][col].replace("+","")
                    b = b.replace(",","")
                    if( b == ''):
                        b = '0'
                    b = int(b)
                    if (a > b):
                        A[i], A[i + 1] = A[i + 1], A[i]
                        isSwapped = True
                    i = i - 1

                start = start + 1

            return A

    def CocktailSort_decend(self,A,col):
        if( col != 5) :
            isSwapped = True
            start = 0
            end = len(A) - 1

            while (isSwapped == True):

                isSwapped = False
                i = start
                while ( i < end ):
                    if (A[i][col] < A[i + 1][col]):
                        A[i], A[i + 1] = A[i + 1], A[i]
                        isSwapped = True
                    i += 1

                if (isSwapped == False):
                    break
                isSwapped = False
                i = end - 2
                while(  i > start - 1):
                    if (A[i][col] < A[i + 1][col]):
                        A[i], A[i + 1] = A[i + 1], A[i]
                        isSwapped = True
                    i = i - 1

                start = start + 1

            return A
        else:
            isSwapped = True
            start = 0
            end = len(A) - 1

            while (isSwapped == True):

                isSwapped = False
                i = start
                while ( i < end ):
                    a = A[i][col].replace("+","")
                    a = a.replace(",","")
                    if( a == ''):
                        a = '0'
                    a = int(a)
                    b = A[i+1][col].replace("+","")
                    b = b.replace(",","")
                    if( b == ''):
                        b = '0'
                    b = int(b)
                    if (a < b):
                        A[i], A[i + 1] = A[i + 1], A[i]
                        isSwapped = True
                    i += 1

                if (isSwapped == False):
                    break
                isSwapped = False
                i = end - 2
                while(  i > start - 1):
                    a = A[i][col].replace("+","")
                    a = a.replace(",","")
                    if( a == ''):
                        a = '0'
                    a = int(a)
                    b = A[i+1][col].replace("+","")
                    b = b.replace(",","")
                    if( b == ''):
                        b = '0'
                    b = int(b)
                    if (a < b):
                        A[i], A[i + 1] = A[i + 1], A[i]
                        isSwapped = True
                    i = i - 1

                start = start + 1

            return A
    
    #################################################################################################
    ######################################## ComboSort  Sort ########################################
    #################################################################################################
    
    def divideNum(self,n):
        
        n = n / 1.3
    
        return 1 if n < 1 else int(n)

    def CombSort_ascend(self,A,col):
        if (col != 5):
            n = len(A)
            swap = True

            while not n == 1 or swap == True:

                n = self.divideNum(n)

                swap = False
                for i in range(0, len(A) - n): 
                    
                    if A[i][col] > A[i + n][col]:
                    
                        A[i], A[i + n] = A[i + n], A[i]

                        swap = True
            return A
        else:
            n = len(A)
            swap = True

            while not n == 1 or swap == True:

                n = self.divideNum(n)

                swap = False
                for i in range(0, len(A) - n): 

                    a = A[i][col].replace("+","")
                    a = a.replace(",","")
                    if( a == ''):
                        a = '0'
                    a = int(a)
                    b = A[i + n][col].replace("+","")
                    b = b.replace(",","")
                    if( b == ''):
                        b = '0'
                    b = int(b)
                    if a > b:
                    
                        A[i], A[i + n] = A[i + n], A[i]

                        swap = True
            return A
    def CombSort_decend(self,A,col):
        if (col != 5):
            n = len(A)
            swap = True

            while not n == 1 or swap == True:

                n = self.divideNum(n)

                swap = False
                for i in range(0, len(A) - n): 

                    if A[i] < A[i + n]:
                    
                        A[i], A[i + n] = A[i + n], A[i]

                        swap = True
            return A
        else:
            n = len(A)
            swap = True

            while not n == 1 or swap == True:

                n = self.divideNum(n)

                swap = False
                for i in range(0, len(A) - n): 

                    a = A[i][col].replace("+","")
                    a = a.replace(",","")
                    if( a == ''):
                        a = '0'
                    a = int(a)
                    b = A[i +n][col].replace("+","")
                    b = b.replace(",","")
                    if( b == ''):
                        b = '0'
                    b = int(b)
                    if a < b:
                    
                        A[i], A[i + n] = A[i + n], A[i]

                        swap = True
            return A
                    
    #################################################################################################
    ######################################## Shell  Sort ########################################
    #################################################################################################
    
    def shell_sort_ascend(self,array,col) :
        if(col != 5):
            n = len(array)
            gap = n//2
            while gap >= 1 :
              for i in range(gap,n):
                temp = array[i]
                j = i - gap
                while j >= 0 and array[j][col] > temp[col] :
                  array[j+gap] = array[j]
                  j -= gap
                array[j+gap] = temp
              gap = gap//2
            return array
        else:
            n = len(array)
            gap = n//2
            while gap >= 1 :
              for i in range(gap,n):
                temp = array[i]
                j = i - gap
                a = array[j][col].replace("+","")
                a = a.replace(",","")
                if( a == ''):
                    a = '0'
                a = int(a)
                b = array[i][col].replace("+","")
                b = b.replace(",","")
                if( b == ''):
                    b = '0'
                b = int(b)
                while j >= 0 and a > b :
                  array[j+gap] = array[j]
                  j -= gap
                array[j+gap] = temp
              gap = gap//2
            return array
    def shell_sort_decend(self,array,col) :
        if(col != 5):
            n = len(array)
            gap = n//2
            while gap >= 1 :
              for i in range(gap,n):
                temp = array[i]
                j = i - gap
                while j >= 0 and array[j][col] < temp[col] :
                  array[j+gap] = array[j]
                  j -= gap
                array[j+gap] = temp
              gap = gap//2
            return array
        else:
            n = len(array)
            gap = n//2
            while gap >= 1 :
              for i in range(gap,n):
                temp = array[i]
                j = i - gap
                a = array[j][col].replace("+","")
                a = a.replace(",","")
                if( a == ''):
                    a = '0'
                a = int(a)
                b = array[i][col].replace("+","")
                b = b.replace(",","")
                if( b == ''):
                    b = '0'
                b = int(b)
                while j >= 0 and a < b :
                  array[j+gap] = array[j]
                  j -= gap
                array[j+gap] = temp
              gap = gap//2
            return array
            
    #################################################################################################
    ######################################## Insertion  Sort ########################################
    #################################################################################################
    
    def InsertionSort_ascend(self,array,col):
        if( col != 5):
            size=len(array)
            for j in range(1,size):
                key=array[j]
                i=j-1
                while(i>=0 and key[col]<array[i][col]):
                    array[i+1]=array[i]
                    i=i-1
                array[i+1]=key
            return array
        else:
            size=len(array)
            for j in range(1,size):
                key=array[j]
                a = key[col].replace("+","")
                a = a.replace(",","")
                if( a == ''):
                    a = '0'
                i=j-1
                while(True):
                    b = array[i][col].replace("+","")
                    b = b.replace(",","")
                    if( b == ''):
                        b = '0'
                    if(i>=0 and int(a)<int(b)):
                        array[i+1]=array[i]
                        i=i-1
                    else:
                        break;
                array[i+1]=key
            return array
            
    def InsertionSort_decend(self,array,col):
        if( col != 5):
            size=len(array)
            for j in range(1,size):
                key=array[j]
                i=j-1
                while(i>=0 and key[col]>array[i][col]):
                    array[i+1]=array[i]
                    i=i-1
                array[i+1]=key
            return array
        else:
            size=len(array)
            for j in range(1,size):
                key=array[j]
                a = key[col].replace("+","")
                a = a.replace(",","")
                if( a == ''):
                    a = '0'
                i=j-1
                while(True):
                    b = array[i][col].replace("+","")
                    b = b.replace(",","")
                    if( b == ''):
                        b = '0'
                    if(i>=0 and int(a)>int(b)):
                        array[i+1]=array[i]
                        i=i-1
                    else:
                        break;
                array[i+1]=key
            return array
        
    #################################################################################################
    ######################################## QuickSort  Sort ########################################
    #################################################################################################
    
    def quickSort_ascend(self,array,low, high,col):
        if (low<high):
           pi = self.partition_ascend(array, low, high,col)
           self.quickSort_ascend(array, low, pi - 1,col)        
           self.quickSort_ascend(array, pi + 1, high,col)
        return array
    def partition_ascend(self,arr, low, high,col):
        if (col != 5):
            pivot = arr[high]         
            i = (low - 1)           
            for j in range(low,high):
                if (arr[j][col] < pivot[col]):         
                    i=i+1 
                    temp=arr[i]
                    arr[i]=arr[j]
                    arr[j]=temp
            temp=arr[i+1]
            arr[i+1]=arr[high]
            arr[high]=temp 
            return (i + 1)
        else:
            pivot = arr[high]         
            i = (low - 1)           
            for j in range(low,high):
                a = arr[j][col].replace("+","")
                a = a.replace(",","")
                
                b = pivot[col].replace("+","")
                b = b.replace(",","")
                if( a == ''):
                    a = '0'
                a = int(a)
                if( b == ''):
                    b = '0'
                b = int(b)
                
                if ( a < b ):         
                    i=i+1 
                    temp=arr[i]
                    arr[i]=arr[j]
                    arr[j]=temp
            temp=arr[i+1]
            arr[i+1]=arr[high]
            arr[high]=temp 
            return (i + 1)
    
    def quickSort_decend(self,array,low, high,col):
        if (low<high):
           pi = self.partition_decend(array, low, high,col)
           self.quickSort_decend(array, low, pi - 1,col)        
           self.quickSort_decend(array, pi + 1, high,col)
        return array
    def partition_decend(self,arr, low, high,col):
        if (col != 5):
            
            pivot = arr[high]         
            i = (low - 1)           
            for j in range(low,high):
                if (arr[j][col] > pivot[col]):         
                    i=i+1 
                    temp=arr[i]
                    arr[i]=arr[j]
                    arr[j]=temp
            temp=arr[i+1]
            arr[i+1]=arr[high]
            arr[high]=temp 
            return (i + 1)
        else:
            pivot = arr[high]         
            i = (low - 1)           
            for j in range(low,high):
                a = arr[j][col].replace("+","")
                a = a.replace(",","")
                
                b = pivot[col].replace("+","")
                b = b.replace(",","")
                if( a == ''):
                    a = '0'
                a = int(a)
                if( b == ''):
                    b = '0'
                b = int(b)
                
                if (a > b):         
                    i=i+1 
                    temp=arr[i]
                    arr[i]=arr[j]
                    arr[j]=temp
            temp=arr[i+1]
            arr[i+1]=arr[high]
            arr[high]=temp 
            return (i + 1)
    
    #################################################################################################
    ######################################## Bubble  Sort ########################################
    #################################################################################################
    
    def Bubble_ascend(self,Array,col):
        if ( col != 5):
            n=len(Array)-1
            for i in range(0,n):
                swap=0
                for j in range(n):
                    if(Array[j][col]>Array[j+1][col]):
                        temp=Array[j]
                        Array[j]=Array[j+1]
                        Array[j+1]=temp
                        swap=1
                if(swap==0):
                    break
            return Array
        else:
            n=len(Array)-1
            for i in range(0,n):
                swap=0
                for j in range(n):
                    a = Array[j][col].replace("+","")
                    a = a.replace(",","")
                    
                    b = Array[j+1][col].replace("+","")
                    b = b.replace(",","")
                    if( a == ''):
                        a = '0'
                    a = int(a)
                    if( b == ''):
                        b = '0'
                    b = int(b)
                    if(a > b):
                        temp=Array[j]
                        Array[j]=Array[j+1]
                        Array[j+1]=temp
                        swap=1
                if(swap==0):
                    break
            return Array

    def Bubble_decend(self,Array,col):
        if ( col != 5):
            n=len(Array)-1
            for i in range(0,n):
                swap=0
                for j in range(n):
                    if(Array[j][col]<Array[j+1][col]):
                        temp=Array[j]
                        Array[j]=Array[j+1]
                        Array[j+1]=temp
                        swap=1
                if(swap==0):
                    break
            return Array
        else:
            n=len(Array)-1
            for i in range(0,n):
                swap=0
                for j in range(n):
                    a = Array[j][col].replace("+","")
                    a = a.replace(",","")
                    
                    b = Array[j+1][col].replace("+","")
                    b = b.replace(",","")
                    if( a == ''):
                        a = '0'
                    a = int(a)
                    if( b == ''):
                        b = '0'
                    b = int(b)
                    if(a < b):
                        temp=Array[j]
                        Array[j]=Array[j+1]
                        Array[j+1]=temp
                        swap=1
                if(swap==0):
                    break
            return Array
    
    #################################################################################################
    ######################################## Merge Sort ########################################
    #################################################################################################
    
    def MergeSort_ascend(self,Array,low,high,col):
        if(low==high):
            return Array
        else:
            m=int((low+high)//2)
            self.MergeSort_ascend(Array,low,m,col)
            self.MergeSort_ascend(Array,m+1,high,col)
            self.Merge_ascend(Array,low,m,high,col)
        return Array
    
    def Merge_ascend(self,A,a,m,b,col):
        if (col != 5):
            
            R=[]
            L=[]
            for i in range(a,m+1):
                L.append(A[i])
            for j in range(m+1,b+1):
                R.append(A[j])
            i=0
            j=0
            for k in range(a,b+1):
                if(i<len(L) and j<len(R) and L[i][col]<R[j][col]):
                    A[k]=L[i]
                    i=i+1
                elif(j<len(R) and i<len(L)and L[i][col]>=R[j][col]):
                    A[k]=R[j]
                    j=j+1
                elif(i<len(L)):
                    A[k]=L[i]
                    i=i+1
                elif(j<len(R)):
                    A[k]=R[j]
                    j=j+1
            return A
        else:
             
            R=[]
            L=[]
            for i in range(a,m+1):
                L.append(A[i])
            for j in range(m+1,b+1):
                R.append(A[j])
            i=0
            j=0
            for k in range(a,b+1):
               
                if(i<len(L) and j<len(R) ):
                    # print(R[j][col])
                    # print(j)
                    # print(col)
                    z = L[i][col].replace("+","")
                    z = z.replace(",","")
                    if( z == ''):
                        z = '0'
                    z = int(z)
                    y = R[j][col].replace("+","")
                    y = y.replace(",","")
                    if( y == ''):
                        y = '0'
                    y = int(y)
                    if(z<y):
                        A[k]=L[i]
                        i=i+1
                    else:
                        A[k]=R[j]
                        j=j+1
               
                elif(i<len(L)):
                    A[k]=L[i]
                    i=i+1
                elif(j<len(R)):
                    A[k]=R[j]
                    j=j+1
            return A
    
    def MergeSort_decend(self,Array,low,high,col):
        if(low==high):
            return Array
        else:
            m=int((low+high)//2)
            self.MergeSort_decend(Array,low,m,col)
            self.MergeSort_decend(Array,m+1,high,col)
            self.Merge_decend(Array,low,m,high,col)
        return Array
    
    def Merge_decend(self,A,a,m,b,col):
        if col != 5:
            R=[]
            L=[]
            for i in range(a,m+1):
                L.append(A[i])
            for j in range(m+1,b+1):
                R.append(A[j])
            i=0
            j=0
            for k in range(a,b+1):
                
                
                if(i<len(L) and j<len(R) and L[i][col]>R[j][col]):
                    A[k]=L[i]
                    i=i+1
                elif(j<len(R) and i<len(L)and L[i][col]<=R[j][col]):
                    A[k]=R[j]
                    j=j+1
                elif(i<len(L)):
                    A[k]=L[i]
                    i=i+1
                elif(j<len(R)):
                    A[k]=R[j]
                    j=j+1
            return A
        else:
            R=[]
            L=[]
            for i in range(a,m+1):
                L.append(A[i])
            for j in range(m+1,b+1):
                R.append(A[j])
            i=0
            j=0
            for k in range(a,b+1):
               
                if(i<len(L) and j<len(R) ):
                    # print(R[j][col])
                    # print(j)
                    # print(col)
                    z = L[i][col].replace("+","")
                    z = z.replace(",","")
                    if( z == ''):
                        z = '0'
                    z = int(z)
                    y = R[j][col].replace("+","")
                    y = y.replace(",","")
                    if( y == ''):
                        y = '0'
                    y = int(y)
                    if(z>y):
                        A[k]=L[i]
                        i=i+1
                    else:
                        A[k]=R[j]
                        j=j+1
               
                elif(i<len(L)):
                    A[k]=L[i]
                    i=i+1
                elif(j<len(R)):
                    A[k]=R[j]
                    j=j+1
            return A
    
    #################################################################################################
    ######################################## Tim Sort ###############################################
    #################################################################################################
    
    def timsort_ascending(self,arr,col):
        RUN = 2
        for x in range (0,len(arr),RUN):
            arr[x:x+RUN] = self.InsertionSort_ascend(arr[x:x+RUN],col)
        r = RUN
        while r < len(arr):
            for x in range(0,len(arr),2* r):
                arr[x:x+ 2*r] = self.merge_asccending(arr[x:x+r],arr[x+r:x+2*r],col)
            r = r*2
        return arr
    def timsort_decending(self,arr,col):
        RUN = 2
        for x in range (0,len(arr),RUN):
            arr[x:x+RUN] = self.InsertionSort_decend(arr[x:x+RUN],col)
        r = RUN
        while r < len(arr):
            for x in range(0,len(arr),2* r):
                arr[x:x+ 2*r] = self.merge_decending(arr[x:x+r],arr[x+r:x+2*r],col)
            r = r*2
        return arr
    def merge_asccending(self,ar,br,col):
        a = 0
        b = 0
        c = []
        while a < len(ar) and b < len(br):
            if(ar[a][col] < br[b][col]):
                c.append(ar[a])
                a += 1
            elif(ar[a][col] > br[b][col]):
                c.append(br[b])
                b += 1
            else:
                c.append(ar[a])
                c.append(br[b])
                a += 1
                b += 1
        while a < len(ar):
            c.append(ar[a])
            a += 1
        while b < len(br):
            c.append(br[b])
            b += 1
        return c
    def merge_decending(self,ar,br,col):
        a = 0
        b = 0
        c = []
        while a < len(ar) and b < len(br):
            if(ar[a][col] > br[b][col]):
                c.append(ar[a])
                a += 1
            elif(ar[a][col] < br[b][col]):
                c.append(br[b])
                b += 1
            else:
                c.append(ar[a])
                c.append(br[b])
                a += 1
                b += 1
        while a < len(ar):
            c.append(ar[a])
            a += 1
        while b < len(br):
            c.append(br[b])
            b += 1
        return c