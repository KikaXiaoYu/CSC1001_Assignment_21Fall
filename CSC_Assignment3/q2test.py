from q2 import *

def test4():
    test_list = []
    test_list.append("24*xy^24-3*xy^4+3*xy^1+1")
    test_list.append("7")
    test_list.append("-45+37")
    test_list.append("-t")
    test_list.append("t+t-t")
    test_list.append("x^5+1")
    test_list.append("250-100*t^9+20*t")
    test_list.append("1*x^3+2*x^2")
    test_list.append("-y+4*y^4-34")
    test_list.append("250-100*t^9+20*y")
    test_list.append("2*x**3+3*x^2+5*x^1+1")
    test_list.append("2^x^3+3*x^2+5*x^1+1")
    test_list.append("-2*x^3+3*y^2+5*x+1")
    test_list.append("-2*y^3+3*y^2+5*y+1")
    test_list.append("2*y^6-3*y^8+5*y+1")
    test_list.append("10")
    mainvalue_list = [process_derivative(k) for k in test_list]
    print("")
    for i in range(0, len(test_list)):
        test = mainvalue_list[i]
        print("TO SOLVE  %s" % test_list[i],end = "    /////    ")
        #print(test.get_whole_seperated())
        result = test.get_first_derivative()
        print(result)
        print("")

test4()