def fct(d) :
    i = 0
    curr = []
    d = U(d)
    curr.append('U')
    r1 = fctU(d, i+1, curr)
    print(r1)
    curr.pop()
    d = U(d)
    curr.append('U2')
    r2 = fctU(d, i+1, curr)
    print(r2)
    curr.pop()
    d = U(d)
    curr.append('U-')
    r3 = fctU(d, i+1, curr)
    print(r3)
    curr.pop()
    d = U(d)
    d = R(d)
    curr.append('R')
    r4 = fctR(d, i+1, curr)
    print(r4)
    curr.pop()
    d = R(d)
    curr.append('R2')
    r5 = fctR(d, i+1, curr)
    print(r5)
    curr.pop()
    d = R(d)
    curr.append('R-')
    r6 = fctR(d, i+1, curr)
    print(r6)
    curr.pop()
    d = R(d)
    d = F(d)
    curr.append('F')
    r7 = fctF(d, i+1, curr)
    print(r7)
    curr.pop()
    d = F(d)
    curr.append('F2')
    r8 = fctF(d, i+1, curr)
    print(r8)
    curr.pop()
    d = F(d)
    curr.append('F-')
    r9 = fctF(d, i+1, curr)
    print(r9)
    curr.pop()
    d = F(d)
    mc = min_l([r1,r2,r3,r4,r5,r6,r7,r8,r9])
    return mc

def fctU(d, i, curr) :
    global dparf
    global k
    if d == dparf : 
        k = i
        return curr[:]
    if i >= k :
        return []
    d = R(d)
    curr.append('R')
    r4 = fctR(d, i+1, curr)
    curr.pop()
    d = R(d)
    curr.append('R2')
    r5 = fctR(d, i+1, curr)
    curr.pop()
    d = R(d)
    curr.append('R-')
    r6 = fctR(d, i+1, curr)
    curr.pop()
    d = R(d)
    d = F(d)
    curr.append('F')
    r7 = fctF(d, i+1, curr)
    curr.pop()
    d = F(d)
    curr.append('F2')
    r8 = fctF(d, i+1, curr)
    curr.pop()
    d = F(d)
    curr.append('F-')
    r9 = fctF(d, i+1, curr)
    curr.pop()
    d = F(d)
    mc = min_l([r4,r5,r6,r7,r8,r9])
    return mc
    

#jgvljglgdkhtd

def fctR(d, i, curr) :
    global dparf
    global k
    if d == dparf : 
        k = i
        return curr[:]
    if i >= k :
        return []
    d = U(d)
    curr.append('U')
    r1 = fctU(d, i+1, curr)
    curr.pop()
    d = U(d)
    curr.append('U2')
    r2 = fctU(d, i+1, curr)
    curr.pop()
    d = U(d)
    curr.append('U-')
    r3 = fctU(d, i+1, curr)
    curr.pop()
    d = U(d)
    d = F(d)
    curr.append('F')
    r7 = fctF(d, i+1, curr)
    curr.pop()
    d = F(d)
    curr.append('F2')
    r8 = fctF(d, i+1, curr)
    curr.pop()
    d = F(d)
    curr.append('F-')
    r9 = fctF(d, i+1, curr)
    curr.pop()
    d = F(d)
    mc = min_l([r1,r2,r3,r7,r8,r9])
    return mc

def fctF(d, i, curr) :
    global k
    global dparf
    if d == dparf : 
        k = i
        return curr[:]
    if i >= k :
        return []
    d = U(d)
    curr.append('U')
    r1 = fctU(d, i+1, curr)
    curr.pop()
    d = U(d)
    curr.append('U2')
    r2 = fctU(d, i+1, curr)
    curr.pop()
    d = U(d)
    curr.append('U-')
    r3 = fctU(d, i+1, curr)
    curr.pop()
    d = U(d)
    d = R(d)
    curr.append('R')
    r4 = fctR(d, i+1, curr)
    curr.pop()
    d = R(d)
    curr.append('R2')
    r5 = fctR(d, i+1, curr)
    curr.pop()
    d = R(d)
    curr.append('R-')
    r6 = fctR(d, i+1, curr)
    curr.pop()
    d = R(d)
    mc = min_l([r1,r2,r3,r4,r5,r6])
    return mc


def min_l(l) :
    distmin = 120
    imin = None
    for i in range(len(l)) :
        if len(l[i]) != 0 :
            if len(l[i]) <= distmin :
                distmin = len(l[i])
                imin = i
    if imin == None :
        return []
    return l[imin]





def U(d) :
    d['U2'],d['U3'],d['U4'],d['U1'] = d['U1'],d['U2'],d['U3'],d['U4'] 
    d['L1'],d['B1'],d['R1'],d['F1'] = d['F1'],d['L1'],d['B1'],d['R1'] 
    d['L2'],d['B2'],d['R2'],d['F2'] = d['F2'],d['L2'],d['B2'],d['R2'] 
    return d

def R(d) :
    d['R2'],d['R3'],d['R4'],d['R1'] = d['R1'],d['R2'],d['R3'],d['R4'] 
    d['U2'],d['B4'],d['D2'],d['F2'] = d['F2'],d['U2'],d['B4'],d['D2'] 
    d['U3'],d['B1'],d['D3'],d['F3'] = d['F3'],d['U3'],d['B1'],d['D3']
    return d

def F(d) :
    d['F2'],d['F3'],d['F4'],d['F1'] = d['F1'],d['F2'],d['F3'],d['F4'] 
    d['D1'],d['L2'],d['U3'],d['R4'] = d['R4'],d['D1'],d['L2'],d['U3']
    d['R1'],d['D2'],d['L3'],d['U4'] = d['U4'],d['R1'],d['D2'],d['L3']
    return d

def parfait(d):
    #ne prend pas en compte que on pourrait avoir des faces cohérentes entre elles mais inattégnables
    if d['U1']==d['U2']==d['U3']==d['U4']  and d['F1']==d['F2']==d['F3']==d['F4'] and d['D1']==d['D2']==d['D3']==d['D4'] and d['B1']==d['B2']==d['B3']==d['B4']:
        return True
    return False


k = 11

dparf = {'U1' : 'yellow', 'U2' : 'yellow', 'U3' : 'yellow', 'U4' : 'yellow',
         'F1' : 'orange', 'F2' : 'orange', 'F3' : 'orange', 'F4' : 'orange',
         'B1' : 'red', 'B2' : 'red', 'B3' : 'red', 'B4' : 'red',
         'L1' : 'green', 'L2' : 'green', 'L3' : 'green', 'L4' : 'green',
         'D1' : 'white', 'D2' : 'white', 'D3' : 'white', 'D4' : 'white',
         'R1' : 'blue', 'R2' : 'blue', 'R3' : 'blue', 'R4' : 'blue',}


d = {'U1': 'yellow', 'U2': 'yellow', 'U3': 'orange', 'U4': 'orange',
     'F1': 'blue', 'F2': 'blue', 'F3': 'white', 'F4': 'orange',
     'B1': 'green', 'B2': 'green', 'B3': 'red', 'B4': 'yellow',
     'L1': 'orange', 'L2': 'white', 'L3': 'green', 'L4': 'green',
     'D1': 'white', 'D2': 'red', 'D3': 'red', 'D4': 'white',
     'R1': 'yellow', 'R2': 'red', 'R3': 'blue', 'R4': 'blue'}

d2 = {'U1': 'blue', 'U2': 'yellow', 'U3': 'white', 'U4': 'blue', 
      'F1': 'red', 'F2': 'orange', 'F3': 'blue', 'F4': 'orange', 
      'B1': 'blue', 'B2': 'red', 'B3': 'red', 'B4': 'red', 
      'L1': 'yellow', 'L2': 'white', 'L3': 'yellow', 'L4': 'green', 
      'D1': 'green', 'D2': 'orange', 'D3': 'yellow', 'D4': 'white', 
      'R1': 'green', 'R2': 'orange', 'R3': 'green', 'R4': 'white'}

print(fct(d2))
        
