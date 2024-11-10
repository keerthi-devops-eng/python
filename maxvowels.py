def findSubstring(s, k):
   n = len(s)
   max_vowels = 0
   output = ""
   vowels = {'a', 'e', 'i', 'o', 'u'}
  
   count = len([char for char in s[:k] if char in vowels])
   max_vowels = count
   if count > 0:
       output = s[:k]
  
   for i in range(1, n - k + 1):
       if s[i - 1] in vowels:
           count -= 1
       if s[i + k - 1] in vowels:
           count += 1
       if count > max_vowels:
           max_vowels = count
           output = s[i:i + k]
          
   return output if output else "Not found!"
