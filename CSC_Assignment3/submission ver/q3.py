from random import randint

class ecosystem():
    def __init__(self, river_len, fish_num, bear_num, steps):
        self.river_len = river_len
        self.fish_num = fish_num
        self.bear_num = bear_num
        self.steps = steps
    
    def getFirstRandomFishList(self):
        fish_list = []
        while len(fish_list) < self.fish_num:
            position = randint(0, self.river_len-1)
            if position not in fish_list:
                fish_list.append(position)
        return fish_list
    
    def getSecondRandomBearList(self, fish_list):
        bear_list = []
        while len(bear_list) < self.bear_num:
            position = randint(0, self.river_len-1)
            if position not in bear_list and position not in fish_list:
                bear_list.append(position)
        return bear_list
    
    def getRiverList(self):
        river_list = []
        fish_list = self.getFirstRandomFishList()
        bear_list = self.getSecondRandomBearList(fish_list)
        for i in range(self.river_len):
            if i in fish_list:
                river_list.append("F")
            elif i in bear_list:
                river_list.append("B")
            else:
                river_list.append("N")
        return river_list

    def randomPlace(self, river_list, animal):
        count = 0
        for i in range(len(river_list)):
            if river_list[i] == "N":
                count += 1
        if count > 0:
            position = randint(1, count)
            search = 0
            for i in range(len(river_list)):
                if river_list[i] == "N":
                    search += 1
                if search == position:
                    river_list[i] = animal
                    return i

    def fishAction(self, i, river_list, ex_list):
        action = randint(-1, 1)
        if (action == -1 and i == 0) or (action == 1 and i == len(river_list) - 1):
            pass
        elif action != 0:
            if river_list[i+action] == "N":
                river_list[i+action], river_list[i] = river_list[i], river_list[i+action]
                ex_list.append(i+action)
            elif river_list[i+action] == "B":
                river_list[i] = "N"
            elif river_list[i+action] == "F":
                ex_list.append(self.randomPlace(river_list, "F"))
                #print("ex_list",ex_list)
        print("Animal: F","Action: %d" % action)
    
    def bearAction(self, i, river_list, ex_list):
        action = randint(-1, 1)
        if (action == -1 and i == 0) or (action == 1 and i == len(river_list) - 1):
            pass
        elif action != 0:
            if river_list[i+action] == "N":
                river_list[i+action], river_list[i] = river_list[i], river_list[i+action]
                ex_list.append(i+action)
            elif river_list[i+action] == "F":
                river_list[i] = "N"
                river_list[i+action] = "B"
                ex_list.append(i+action)
            elif river_list[i+action] == "B":
                ex_list.append(self.randomPlace(river_list, "B"))
                #print("ex_list",ex_list)
        print("Animal: B","Action: %d" % action)


        
    def stepAction(self, river_list, step):
        print("The ecosystem at the beginning of the step %d:" % step)
        ex_list = []
        print(river_list)
        for i in range(len(river_list)):
            animal = river_list[i]
            if animal != "N" and (i not in ex_list):
                if animal == "F":
                    self.fishAction(i, river_list, ex_list)   
                    print("The current ecosystem after the action:")
                    print(river_list)
                elif animal == "B":
                    self.bearAction(i, river_list, ex_list)
                    print("The current ecosystem after the action:")
                    print(river_list)


    def simulation(self):
        from random import randint
        try:
            if self.river_len >= self.fish_num + self.bear_num:
                river_list = self.getRiverList()
                for i in range(1, self.steps + 1):
                    self.stepAction(river_list, i)
            else:
                print("Invalid input!")
        except:
            print("Invalid input!")
