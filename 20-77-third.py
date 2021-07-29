def longestrepeat(s,k):
    l,right=[],0
    a=k
    for left in range(len(s)):
        while k!=0 and right<len(s)-1:
            right += 1
            if s[right]!=s[left]and right<len(s):
                k-=1
        if right==len(s)-1:
            continue
        k=a-1
        l.append(right - left + 1)
        right=left

    left,right=len(s)-1,len(s)-1

    for left in range(len(s)):
        while k!=0 and right<len(s)-1:
            right -= 1
            if s[right]!=s[left] and right<len(s):
                k-=1
        if right==len(s)-1:
            continue
        k=a-1
        l.append(right - left + 1)
        right=left

    return max(l)
print(longestrepeat("ccaaac",k=2))
