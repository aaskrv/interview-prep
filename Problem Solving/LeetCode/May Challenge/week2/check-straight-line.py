"""
- DAY 8 -
- Check If It Is a Straight Line -

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

Ex1:
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Ex2:
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false

Constraints:
* 2 <= coordinates.length <= 1000
* coordinates[i].length == 2
* -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
* coordinates contains no duplicate point.
"""

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2: return True
        
        (x0, y0), (x1, y1) = coordinates[: 2]
        
        for point in coordinates[2:]:
            cross = x0*(y1 - point[1]) + x1*(point[1] - y0) + point[0]*(y0 - y1)
            if cross != 0:
                return False
        
        return True