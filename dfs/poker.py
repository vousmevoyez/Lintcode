"""
Poker
Given an integer array cards representing poker cards in your hand. The points of each card will be in range of [1, 9]. There are three ways to discard cards:
Discard any single card
Discard two or more cards with the same points
Discard at least 5 consecutive and distinct cards (for example 2, 3, 4, 5, 6)
How many times at least to discard all cards?
Example
Example 1:
Input: cards = [2, 2, 2, 3, 4, 5, 7, 1]
Output: 3
Explanation: 
  1. Discard 1, 2, 3, 4, 5
  2. Discard 2, 2
  3. Discard 7
 
Example 2:
Input: cards = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
Output: 2
Explanation: 
  1. Discard 1, 2, 3, 4, 5
  2. Discard 5, 6, 7, 8, 9
"""

class Solution:
   """
   @param cards:
   @return: the minimal times to discard all cards
   """
   def getAns(self, cards):
       # Write your code here
       def dfs(cum):
           continuous = 0
           for i in xrange(1, 10):
               if cnt[i]:
                   continuous += 1
               else:
                   continuous = 0
 
               # 比如说目前i=8, 3,4,5,6,7,8是连续的，continuous=6. 这里不是3-8的cnt都要减一，而是从3开始，对(3,4,5,6,7,8), (4,5,6,7,8), ...做dfs,
               if continuous >= 5:
                   for j in xrange(i-continuous+1, i-5+2):
                       for k in xrange(j, i+1):
                           cnt[k] -= 1
                       dfs(cum+1)
                       for k in xrange(j, i+1):
                           cnt[k] += 1
                          
           for key in cnt:
               if cnt[key]:
                   cum += 1
           self.res = min(self.res, cum)
      
       import collections
       n = len(cards)
       self.res = n
       cnt = collections.Counter(cards)
       dfs(0)
       return res
      

