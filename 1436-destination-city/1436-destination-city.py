class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # sets method
# source will contain City A
        source = set(path[0] for path in paths)
# destination will contain city B
        destination = set(path[1] for path in paths)
# the difference in destination and source will produce a city that is not in city A but only in city B and convert to list and return the element of list using pop() which returns the last and only element of list
        return list(destination - source).pop()