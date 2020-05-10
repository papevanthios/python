def pal(s):
    s = s.replace(' ','')
    if s == s[::-1]:
        print(True)
pal('helleh')
pal('sakas')
pal('nurses run')