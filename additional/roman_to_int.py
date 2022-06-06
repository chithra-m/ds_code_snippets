def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M' : 1000
        }
        
        count = 0
         
        for i in range(0, len(s)):
            print(i, is_skip)
            if is_skip:
                is_skip = False
                continue

            if i < len(s)-1:
                if s[i]+s[i+1] == 'IV':
                    count += 4
                    is_skip = True
                    i+=1

                elif s[i]+s[i+1] == 'IX':
                    count += 9
                    is_skip = True
                    i+=1

                elif s[i]+s[i+1] == 'XL':
                    count += 40
                    i+=1
                    is_skip = True

                elif s[i]+s[i+1] == 'XC':
                    count += 90
                    i+=1
                    is_skip = True

                elif s[i]+s[i+1] == 'CD':
                    count += 400
                    i+=1
                    is_skip = True

                elif s[i]+s[i+1] == 'CM':
                    count += 900
                    i+=1
                    is_skip = True

                elif s[i] in dict:
                    count += dict[s[i]]
                    # print(s[i],count)     
                print(i,count) 
            elif s[i] in dict:
                count += dict[s[i]]
                print(i,count) 

        return count  

print(romanToInt('CIV'))
print(romanToInt('MCMXCIV'))