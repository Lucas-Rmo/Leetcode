class Solution(object):
    def interpret(self, command):
        returned_str = ""
        for i in range(len(command)):
            if command[i] not in "()":
                returned_str += command[i]
            try:
                if command[i] == "(" and command[i+1] == ")":
                    returned_str += "o"
            except:
                pass
        return returned_str
