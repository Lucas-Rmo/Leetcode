class Solution(object):
    def validIPAddress(self, queryIP):
        point_counter = 0
        two_point_counter = 0

        ipv6_values = ["a","b","c","d","e","f","A","B","C","D","E","F",
                       "0","1","2","3","4","5","6","7","8","9"]
        
        for value in queryIP:
            if value ==".":
                point_counter +=1
        
        if point_counter == 3:
            n1,n2,n3,n4 = queryIP.split(".")
            try:
                if n1[0] == "0" and len(n1)==0 or n2[0] == "0" and len(n2)==0 or n3[0] == "0" and len(n3)==0  or n4[0] == "0" and len(n4)==0:
                    return "Neither"
                if len(n1)>1 and n1[0] == "0" and int(n1)>=0:
                    return "Neither"
                if len(n2)>1 and n2[0] == "0" and int(n2)>=0:
                    return "Neither"
                if len(n3)>1 and n3[0] == "0" and int(n3)>=0:
                    return "Neither"
                if len(n4)>1 and n4[0] == "0" and int(n4)>=0:
                    return "Neither"
            except:
                return"Neither"
            try:         
                if int(n1)<=255 and int(n2)<=255 and int(n3)<=255 and int(n4)<=255:
                    return "IPv4"
            except:
                return "Neither"

        for value in queryIP:
            if value ==":":
                two_point_counter +=1
        
        if two_point_counter == 7:
            ipv6_numbers = queryIP.split(":")
           
            for number in ipv6_numbers:
                if len(number)>4:
                    return "Neither"
                if len(number)==0:
                    return "Neither"
                for value in number:
                    if value not in ipv6_values:
                        return "Neither"
            return "IPv6"
        return "Neither"
