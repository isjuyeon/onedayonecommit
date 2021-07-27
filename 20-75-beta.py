from collections import deque
def maxSlidingWindow(nums,k):
    result = []
    deq = deque()
    for i in range(k):
        deq.append(nums.pop(0))
    maximum = max(deq)
    result.append(maximum)
    while nums != []:
        popV = deq.popleft()
        if popV == maximum and nums != []:
            deq.append(nums.pop(0))
            maximum = max(deq)
            result.append(maximum)
        elif popV != maximum and nums != []:
            if nums[0] > maximum and nums != []:
                maximum = nums.pop(0)
                deq.append(maximum)
                result.append(maximum)
            elif nums[0] <= maximum and nums != []:
                deq.append(nums.pop(0))
                result.append(maximum)
    return result

print(maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
#if, if문으로 걸거나 if,elif로 걸어도 조건 확인만 해도 pop되어버리는 불상사가 발생한다.
#그래서 어차피 한번 해야되는거 변수에다가 저장해서 쓰면 됨****