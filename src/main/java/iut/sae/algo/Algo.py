
class Algo(AlgoException) :
    def RLE(in_str) : 
        # Provide your algo here
        res = "" 
        count = 1  
        for i in range(len(in_str) - 1) :
            if in_str[i] == in_str[i+1] : 
                count+=1
            if count == 10 : 
                res += "9" + in_str[i] 
                count = 1 
            else : 
                res+= str(count) + int_str[i] 
                count = 1 
        rle += str(count) + in_str[-1]
        return res 
    

    def RLE(in_str, iteration)  :  
        # Provide your algo here
        return "NotYetImplemented"
                                                      

    def unRLE(in_str)  :
        # Provide your algo here
        return NotYetImplemented

    def unRLE(in_str, iteration)  : 
        # Provide your algo here
        return "NotYetImplemented"


