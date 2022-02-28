def newtons_sqrt_f(n):
    approx = n / 2.0
    print("n/2.0 = {}".format(n/2.0))
    while True:
          better = (approx + n/approx)/2.0
          print("better = {}".format(better))
          if abs(approx - better) < 0.00000001:
             print("The squart root of {} is {}".format(n, better))
             return better
          print("abs({}-{})={}".format(approx, better, abs(approx-better)))
          approx = better
          print("approx = better = {}".format(approx))

newtons_sqrt_f(25)



