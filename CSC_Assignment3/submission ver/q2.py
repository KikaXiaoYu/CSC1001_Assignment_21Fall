class process_derivative():
    def __init__(self, expression):
        self.expression = expression
    
    def get_whole_sign(self):
        expression = str(self.expression)
        sign_list = []
        if expression[0] != "-":
            sign_list.append("+")
        for i in expression:
            if i == "+" or i == "-":
                sign_list.append(i)
        return sign_list

    def get_whole_seperated(self):
        expression = str(self.expression)
        if expression[0] == "-":
            expression = expression[1:]
        expression = (expression.replace("+","C"))
        expression = (expression.replace("-","C"))
        whole_seperated_list = expression.split("C")
        return whole_seperated_list
    
    def get_part_seperated(self, part_expression):
        power = 0
        variable = ""
        first_seperated = str(part_expression).split("*")
        try:
            coefficient = float(first_seperated[0])
        except:
            coefficient = 1
            first_seperated.insert(0,"1")
        if len(first_seperated) == 2:
            second_seperated = str(first_seperated[1]).split("^")
            variable = second_seperated[0]
            power = 1
            if len(second_seperated) == 2:
                try:
                    power = int(second_seperated[1])
                except:
                    return ("invalid input!")
        if len(first_seperated) > 2:
            return ("invalid input!")
        return coefficient, variable, power

    def get_part_derivative(self, part_expression):
        coefficient, variable, power = self.get_part_seperated(part_expression)
        new_coefficient = coefficient * power
        if power <= 1:
            new_variable = ""
        else:
            new_variable = variable
        new_power = power - 1
        if new_coefficient > 1:
            part_derivative = str("%g" % new_coefficient)
        else:
            part_derivative =str()
        if new_coefficient == 0:
            return 0
        else:
            if new_variable:
                if new_coefficient > 1 :
                    part_derivative += "*"
                part_derivative += new_variable
                if new_power > 1:
                    part_derivative += "^" + str(new_power)
            else:
                part_derivative = str("%g" % new_coefficient)
            return str(part_derivative)
        
    def get_first_derivative(self):
        try:
            first_derivative = str()
            variable_list = []
            for i in range(0, len(self.get_whole_seperated())):
                variable = self.get_part_seperated(self.get_whole_seperated()[i])[1]
                variable_list.append(variable)
                if variable:
                    for j in range(0,i):
                        if variable != variable_list[j] and variable_list[j] != "" or len(variable) > 1:
                                return "invalid input!"
            for i in range(0, len(self.get_whole_seperated())):
                sign = self.get_whole_sign()[i]
                value = self.get_part_derivative(self.get_whole_seperated()[i])
                if (i != 0 or sign == "-") and value:
                    first_derivative += str(self.get_whole_sign()[i])
                if value or (len(self.get_whole_seperated()) == 1 and value == 0):
                    first_derivative += str(self.get_part_derivative(self.get_whole_seperated()[i]))
            if first_derivative == "":
                first_derivative = 0
            return first_derivative
        except:
            return "Invalid input!"
