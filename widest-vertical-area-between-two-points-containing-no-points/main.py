class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        width = [points[x][0] for x in range(len(points))]
        width.sort()
        max_area = 0
        
        
        
        for index in range(1,len(width)):
            
            temp = abs(width[index] - width[index-1])
            
            if temp > max_area: max_area = temp
            
        return max_area