class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        fraction = ""
        list_fractions = []
        list_fractions_div = []
        dict_fractions = {}
        return_list = []

        for i in range(len(arr) - 1):
            fraction = str(arr[i]) + "/" + str(arr[i+1])
            try:
                for j in range(i,len(arr)):
                    fraction = str(arr[i]) + "/" + str(arr[j+1])
                    list_fractions.append(fraction)
            except:
                pass
        for i in range(len(list_fractions)):
            
            v4 = list_fractions[i]
            v1,v2 = v4.split("/")
            v3 = float(v1)/float(v2)
            dict_fractions[v3] = list_fractions[i]
            list_fractions_div.append(v3)
        
    
        list_fractions_div.sort()
        return_fraction = dict_fractions[list_fractions_div[k-1]]
        val1,val2 = return_fraction.split("/")
        return_list.append(int(val1))
        return_list.append(int(val2))
        return return_list
