def anagram(str1, str2):
    s1 = str1.replace(" ", "").lower()
    s2 = str2.replace(" ", "").lower()
    
    return (sorted(s1) == sorted(s2))



anagram("dog", "god")