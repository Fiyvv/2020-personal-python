import unittest
import mypython
class MyTestCase(unittest.TestCase):
    def test_pretreatment(self):
        data= mypython.DataProcessing(False)
        self.assertTrue(data.pretreatment("data"))
        
    def test_loadData(self):
        data = mypython.DataProcessing(False)
        self.assertTrue(data.loadData())
    def test_value(self):
        data = mypython.DataProcessing(True,"data")
        data.__init__(False)
        self.assertEqual(data.getEventsByUsers("izuzero","PushEvent"), 13)
        self.assertEqual(data.getEventsByRepos("sheimi/SGit", "IssuesEvent"), 3)
        self.assertEqual(data.getEventsByUsersAndRepos("izuzero","izuzero/xe-module-ajaxboard","PushEvent"),8)
if __name__ == '__main__':
    unittest.main()