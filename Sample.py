def longestPalindrome(s):
    
    max_str = ""
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i:j] == s[i:j][::-1] and len(max_str)<len(s[i:j]):
                max_str = s[i:j]
    return max_str 
        

s = 'babad'      
print(longestPalindrome(s))