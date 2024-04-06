class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        string = list(map(str, s))
        ind_list = []
        for i in range(len(string)):
            if string[i] == c:
                ind_list.append(i)
        out_list = []
        for i in range(len(string)):
            if string[i] == c:
                out_list.append(0)
            else:
                min_list = []
                for j in ind_list:
                    min_list.append(abs(i-j))
                out_list.append(min(min_list))

        return out_list