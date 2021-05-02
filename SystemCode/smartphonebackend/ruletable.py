import re
import numpy as np
import pandas as pd

keyoperator = ["!=", ">=", "<=", "=", "<", ">"]


class ruletable:
    ruleList = None
    ruleTable = None

    def __init__(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            self.ruleList = f.readlines()
        self.ruleTable = pd.DataFrame(np.zeros((len(self.ruleList), 13)),
                                      columns=["input_type1", "input_value1", "input_type2", "input_value2",
                                               "relationship1", "relationship2", "input_relationship", "result_type1",
                                               "result_value1", "result_type2", "result_value2", "result_relationship1",
                                               "result_relationship2"])
        self.fill_table()
        self.result = {}

    def fill_table(self):
        """process rule.txt file and fill into "ruleTable" for the usage of reasoning"""
        ind = 0
        for con_r in self.ruleList:
            c = con_r.split(" then ")
            if re.search(' and', c[0]) is not None:  # input condition "and"
                self.ruleTable.loc[ind, 'input_relationship'] = 1
            elif re.search(' or', c[0]) is not None:  # input condition "or"
                self.ruleTable.loc[ind, 'input_relationship'] = 2

            con = re.split(" and| or", c[0])  # split if there 2 or more conditions
            con[0] = con[0][3:]
            con_num = 0
            for conditions in con:
                con_num += 1
                if re.search('\(', conditions) is not None:
                    typeflag = abs(conditions.index('(') - conditions.index(
                        ')'))  # use "(" to distiguish the type, if not contain then the string type
                else:
                    typeflag = 0  # default to be string
                conditions = re.sub(r'\([a-zA-Z]+\)', '', conditions)
                op_index = next((i for i, p in enumerate(keyoperator) if (re.search(p, conditions))), None)
                if op_index is not None:
                    self.ruleTable.loc[ind, 'relationship' + str(con_num)] = op_index
                else:
                    print("no op_index matched, please check")
                    break
                # self.ruleTable.loc[ind, 'relationship'+str(con_num)] = op_index
                contype = re.split(keyoperator[op_index], conditions)
                contype[0] = contype[0].strip()
                contype[1] = contype[1].strip()
                self.ruleTable.loc[ind, 'input_type' + str(con_num)] = contype[0]
                if typeflag == 4:
                    self.ruleTable.loc[ind, 'input_value' + str(con_num)] = int(contype[1])
                elif typeflag == 5:
                    self.ruleTable.loc[ind, 'input_value' + str(con_num)] = bool(int(contype[1]))
                elif typeflag == 6:
                    self.ruleTable.loc[ind, 'input_value' + str(con_num)] = float(contype[1])
                else:
                    self.ruleTable.loc[ind, 'input_value' + str(con_num)] = contype[1]
                # end of condition analysis

            res = re.split(" and", c[1])
            result_num = 0
            for result in res:
                result_num += 1
                if re.search('\(', result) is not None:
                    typeflag = abs(result.index('(') - result.index(')'))
                else:
                    typeflag = 0
                result = re.sub(r'\([a-zA-Z]+\)', '', result)
                op_index = next((i for i, p in enumerate(keyoperator) if (re.search(p, result))), None)
                if op_index is not None:
                    self.ruleTable.loc[ind, 'result_type' + str(result_num)] = op_index
                else:
                    print("no op_index matched, please check")
                    break
                # self.ruleTable.loc[ind, 'result_type'+str(result_num)] = op_index
                restype = re.split(keyoperator[op_index], result)
                restype[0] = restype[0].strip()
                restype[1] = restype[1].strip()
                self.ruleTable.loc[ind, 'result_type' + str(result_num)] = restype[0]
                if typeflag == 4:
                    self.ruleTable.loc[ind, 'result_value' + str(result_num)] = int(restype[1])
                elif typeflag == 5:
                    self.ruleTable.loc[ind, 'result_value' + str(result_num)] = bool(int(restype[1]))
                else:
                    self.ruleTable.loc[ind, 'result_value' + str(result_num)] = restype[1]

            ind += 1
            print("rule no.", ind, "has been built")

    def find_tag(self, tag):
        """
        use tag to find related rules from table and return an integer value (index of row in rule table),
         if not found return None.
        """
        rule = self.ruleTable.copy()
        ind_list = rule[(rule["input_type1"] == tag) | (rule["input_type2"] == tag)].index
        return ind_list

    @staticmethod
    def matching(con, value, op_index=3):
        """look for the index of operator and return bool value to take operator from "keyoperator" """
        try:
            if op_index == 0:
                if con != value:
                    return True
                else:
                    return False
            elif op_index == 1:
                if con >= value:
                    return True
                else:
                    return False
            elif op_index == 2:
                if con <= value:
                    return True
                else:
                    return False
            elif op_index == 3:
                if con == value:
                    return True
                else:
                    return False
            elif op_index == 4:
                if con < value:
                    return True
                else:
                    return False
            elif op_index == 5:
                if con > value:
                    return True
                else:
                    return False
        except TypeError:
            print("matching type error, integer cannot be compare with string, please check rules input file")

    def con_judge(self, index, case):
        """read the rule table and store in memory to judge value input conditions"""
        rule = self.ruleTable.copy()
        con_type1 = rule.loc[index, "input_type1"]
        con_value1 = rule.loc[index, "input_value1"]
        con_type2 = rule.loc[index, "input_type2"]
        con_value2 = rule.loc[index, "input_value2"]
        operator_flag1 = rule.loc[index, "relationship1"]
        operator_flag2 = rule.loc[index, "relationship2"]
        if rule.loc[index, "input_relationship"] == 1:  # check for rule with 2 conditions
            if case.get(con_type1) and case.get(con_type2):
                con_check1 = ruletable.matching(case[con_type1], con_value1, operator_flag1)
                con_check2 = ruletable.matching(case[con_type2], con_value2, operator_flag2)
                if con_check1 and con_check2:
                    return True
        else:
            if case.get(con_type1):
                con_check1 = ruletable.matching(case[con_type1], con_value1, operator_flag1)
                return con_check1
            if case.get(con_type2):
                con_check2 = ruletable.matching(case[con_type2], con_value2, operator_flag2)
                return con_check2
        return False

    def reasoning_1_time(self, case):
        """input case as a dict and output a result (a dictionary) after checking rules table"""
        keys_from_input = case.keys()
        for k in keys_from_input:
            indList = self.find_tag(k)
            if indList.size < 1:
                continue
            else:
                for i in indList:
                    if self.con_judge(i, case):
                        result_type1 = self.ruleTable.loc[i, 'result_type1']
                        result_value1 = self.ruleTable.loc[i, 'result_value1']
                        self.result[result_type1] = result_value1
                        result_type2 = self.ruleTable.loc[i, 'result_type2']
                        if result_type2 != 0:
                            result_value2 = self.ruleTable.loc[i, 'result_value2']
                            self.result[result_type2] = result_value2
        return self.result

    def reasoning(self, case):
        self.result.clear()
        while (1):
            len1 = len(case)
            reason_result = self.reasoning_1_time(case)
            self.result.update(reason_result)
            case.update(reason_result)
            if len(case) == len1:
                break
        return self.result


if __name__ == "__main__":
    filepath = "E:\\Python project\\NUS-ISS project\\SmartPhoneRecommender\\Data\\rules.txt"
    rt = ruletable(filepath)
    # rule_table = rt.ruleTable
    case = {'price': 500, 'purpose': 'video', 'Screen_size': '1'}
    res = rt.reasoning(case)
    print(res)
    print()
