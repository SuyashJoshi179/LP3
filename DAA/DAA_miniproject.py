
d = 256
# pat  -> pattern
# txt  -> text
# q    -> A prime number
 
def search(pat, txt, q):
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0    # hash value for pattern
    t = 0    # hash value for txt
    h = 1
 
    for i in range(M-1):
        h = (h*d) % q
 
 
    for i in range(M):
        p = (d*p + ord(pat[i])) % q
        t = (d*t + ord(txt[i])) % q
 
    # Slide the pattern over text one by one
    for i in range(N-M+1):
        # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters one by one
        if p == t:
            # Check for characters one by one
            for j in range(M):
                if txt[i+j] != pat[j]:
                    break
                else:
                    j += 1
 
            # if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
            if j == M:
                print("Pattern found at index " + str(i))
 
        # Calculate hash value for next window of text
   
        if i < N-M:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+M])) % q
 
            if t < 0:
                t = t+q
 
 
if __name__ == '__main__':
    txt = "There are two types of string matching algorithm Naive String Matching and Rabin-Karp Algorithm for string Searching"
    pat = "string"
    q = 101

    search(pat, txt, q)


# def search(pat, txt):
#     M = len(pat)
#     N = len(txt)

#     for i in range(N - M + 1):
#         j = 0

#         while(j < M):
#             if (txt[i + j] != pat[j]):
#                 break
#             j += 1
 
#         if (j == M):
#             print("Pattern found at index ", i)
 
 
# if __name__ == '__main__':
#     txt = "There are two types of string matching algorithm Naive String Matching and Rabin-Karp Algorithm for string Searching"
#     pat = "tring"
     

#     search(pat, txt)