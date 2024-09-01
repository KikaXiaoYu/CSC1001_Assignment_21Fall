from q2 import *
test_list = ['2*x^3+3*x^2+5*x+1','2*x^3+3*y^2+5*x+1','2*y^3+3*y^2+5*y+1','2*y^6-3*y^8+5*y+1',10]
for i in range(0,5):
    locals()["test" + str(i)] = process_derivative(test_list[i])
    locals()["result" + str(i)] = locals()["test" + str(i)].get_first_derivative()
    print(locals()["result" + str(i)])


from q3 import *
eco = ecosystem(5,2,1,3)
river = eco.simulation()