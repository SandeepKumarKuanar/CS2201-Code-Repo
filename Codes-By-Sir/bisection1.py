def f(x):
    return 10**x + x - 4


def bisection_simple(a, b):
    if(f(a)*f(b)>=0):
        print("Invalid interval!")
        return

    #print("Current interval, mid and f-value: [%f, %f]: %f %f" %(a, b, a, f(a)))
    mid = a
   

    
    while (b - a) >= 0.0001:
        
        mid = (a + b)/2.0

        #print("a, f-value, b, f-value, mid, f-value: %f %f %f %f %f" %(a, f(a), b, f(b), mid, f(mid)))
        #print("a = %f f(a) = %f b = %f f(b) = %f mid = %f f(mid) = %f" %(a, f(a), b, f(b), mid, f(mid)))
        print("%f %f %f %f %f %f %f" %(a, f(a), b, f(b), mid, f(mid), b-a))
        if(f(a)*f(mid) < 0):
            b = mid
        else:
            a = mid    

        #print("Current interval, mid and f-value: [%f, %f]: %f %f" %(a, b, mid, f(mid)))

        
    print("Final Accuracy = %f" %(b-a))
    
    return mid





sol = bisection_simple(0.5, 0.6)
print("The root is ", "%.4f"%sol)
