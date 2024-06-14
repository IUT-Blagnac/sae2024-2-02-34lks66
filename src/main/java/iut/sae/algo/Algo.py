
class Algo(AlgoException) :
    def RLE(in_str) : 
        # Provide your algo here
        res = "" 
        count = 1 
        i = 0 
        while i < len(in_str) - 1 :
            if in_str[i] == in_str[i+1] : 
                count+=1
                if count == 10 : 
                    res += "9" + in_str[i] 
                    count = 1 
            else : 
                res+= str(count) + in_str[i] 
                count = 1 
            i+=1
        res += str(count) + in_str[-1]
        return res 
    

    def RLE(in_str, iteration)  :  
        # Provide your algo here
        rle = in_str 
        for rle in range(iteration) :
            rle = RLE(rle)
        return rle 
                                                      

    def unRLE(in_str)  :
        # Provide your algo here
        res = "" 
        i = 0 
        while i < len(in_str) :
            if in_str[i].isdigit() :
                cpt = int(in_str[i])
                i += 1
                if i < len(in_str) : 
                    res += in_str[i] * cpt
            else :
                res += in_str[i]
            i += 1 
        return res 

    def unRLE(in_str, iteration)  : 
        # Provide your algo here
        rle = in_str
        for rle in range(iteration) :
            rle = UnRLE(rle)
        return rle


