"""
- DAY 10 -
- Find the Town Judge -

In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

Ex1:
Input: N = 2, trust = [[1,2]]
Output: 2

Ex2:
Input: N = 3, trust = [[1,3],[2,3]]
Output: 3

Ex3:
Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Ex4:
Input: N = 3, trust = [[1,2],[2,3]]
Output: -1

Constraints:
* 1 <= N <= 1000
* 0 <= trust.length <= 10^4
* trust[i].length == 2
* trust[i] are all different
* trust[i][0] != trust[i][1]
* 1 <= trust[i][0], trust[i][1] <= N
"""

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust) == 1: return trust[0][1]
        
        trusts = [0]*N
        judges = [i for i in range(1, N+1)]
        for t in trust:
            trusts[t[1] - 1] += 1
            if t[0] in judges: judges.remove(t[0])
       
        if max(trusts) == (N-1) and (trusts.index(max(trusts)) + 1) in judges:
            return judges[0]
        else:
            return -1