import collections
def maxSlidingWindow(nums, k):
    results = []
    window = collections.deque()
    current_max = float('-inf')
    for i, v in enumerate(nums):
        window.append(v)############################################표시된 줄을 배워야한다.

        if i < k - 1:
            continue################################################초기 설정.

        # 새로 추가된 값이 기존 최대값보다 큰 경우 교체
        if current_max == float('-inf'):
            current_max = max(window)
        elif v > current_max:
            current_max = v

        results.append(current_max)##################################

        # 최대값이 윈도우에서 빠지면 초기화
        if current_max == window.popleft():###어차피 if문은 반드시 지나게 되어 있으니 pop이 가능함.
            current_max = float('-inf')
    return results
print(maxSlidingWindow([1,3,-1,-3,5,3,6,7],k=3))
# 왜 굳이 current_max를 -inf로 두냐는건 max가 나갔냐 어쨌냐를 무겁게 처리하는게 아니라 -inf라는거 한줄로 바로 처리할 수 있으니까.
# 내가 푼 방식이랑 logic은 동일하지만 더 깔끔하다. 전체를 for문으로 처리하냐 아니면 while로 끊냐 이 차이다.