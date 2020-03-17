import math

def polar(p):
    if(p[-1]=='C'):
        x,y,Type = p
        if((type(x)!=int and type(x)!=float) or (type(y)!=int and type(y)!=float)):
            raise Exception('error, while turning a c_point into a p_point, non numerical values were found')
        if(x != 0):
            if (x>0):
                a=math.degrees(math.atan(y/x))
            else:
                if(y==0):
                    a=180
                elif(y>0):
                    a=math.degrees(math.atan(y/x))+180
                else:
                    a=math.degrees(math.atan(y/x))-180
        else:
            if(y>0):
                a=90
            elif(y<0):
                a=270
            else:
                a=0
            
        return [math.sqrt(x**2+y**2),a,'P']
    
    if(p[-1]=='P'):
        return p
    if(p[-1]=='CV'):
        p1,p2,Type=p
        pp1=polar(p1)
        pp2=polar(p2)
        return vector(pp1,pp2)

def cart(p):
    if(p[2]=='C'):
        return p

    if(p[2]=='P'):
        m,a,Type=p
        a=math.radians(a)
        return([m*math.cos(a),m*math.sin(a),'C'])
    
def c_point(x,y):
    return [x,y,'C']

def p_point(m,a):
    return [m,a,'P']

def vector(p1,p2):
    if(o_type(p1)=='C' and o_type(p2)=='C'):
        return [p1,p2,'CV']
    if(o_type(p1)=='C' and o_type(p2)=='P'):
        return [p1,p2,'MIXV']
    if(o_type(p1)=='P' and o_type(p2)=='P'):
        return [p1,p2,'PV']
    
def mix_vector(v1):
    p1,p2=v1
    p1=cart(p1)
    p2=polar(p2)
    return [p1,p2,'MIXV']

def o_type(x):
    if(type(x[-1])==str):
        return x[-1]
    else:
        raise Exception('error, o_type() did not recieve a object from this module')
def origin():
    return [0,0,'C']

def sign(x):
    if(x==0):
        return 0
    else:
        return abs(x)/x

def mp(v):
    if(v[2]=='CV'):
        p1,p2,Type = v
        x1,y1,Type=p1
        x2,y2,Type=p2
        mp = [(x1+x2)/2,(y1+y2)/2,'C']
        return mp

def test():
    p1x = int(input('x coordinate for p1'))
    p1y = int(input('y coordinate for p1'))
    p1= c_point(p1x,p1y)
    print(polar(p1))

#while True:
    #test()

def crash(x):
    print(x)
    crash(x+1)
