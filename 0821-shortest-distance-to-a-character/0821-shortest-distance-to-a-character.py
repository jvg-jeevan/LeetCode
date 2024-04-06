class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
# convert the string_list to list
        string_list = list(map(str, s))

# create a list to store index of c in the string_list
        index_list = [i for i in range(len(string_list)) if string_list[i]==c]

# create a list res to store difference of element index and c index
        res = []

# iterate through the list 
        for i in range(len(string_list)):
        # if element is same as c add 0 to list

            if string_list[i] == c:
                res.append(0)
                
        # get the min difference of index of element and index of c
            else:
            # for every occurrence of index find the difference
                min_list = [abs(i-j) for j in index_list]
            # append the min difference to res
                res.append(min(min_list))
# return the res
        return res