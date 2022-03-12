from flask import jsonify
from DAOs.test import TestDao

class TestController:

    def build_map_dic(self, row):
        result = {}
        result['uid'] = row[0]
        result['fname'] = row[1]
        result['lname'] = row[2]
        return result


    def getTest(self):
        dao = TestDao()
        usr_list = dao.getTest()
        result_list = []
        for row in usr_list:
            obj = self.build_map_dic(row)
            result_list.append(obj)
        return jsonify(Test = result_list)