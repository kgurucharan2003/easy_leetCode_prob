from typing import List
class Solution:
  def maxProfit(self,prices:List[int])->int:
    n=len(prices)
    maxprofit=0
    current_profit=0
    for i in range(1,n):
      current_profit+=prices[i]-prices[i-1]
      if current_profit>0:
        pass
      else:
        current_profit=0
      maxprofit=max(maxprofit,current_profit)
    return maxprofit 
obj=Solution()
print(obj.maxProfit([2,4,1]))
