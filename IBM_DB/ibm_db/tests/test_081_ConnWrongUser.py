#
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#

from __future__ import print_function
import sys
import unittest
import ibm_db
import config
from testfunctions import IbmDbTestFunctions

class IbmDbTestCase(unittest.TestCase):

    def test_081_ConnWrongUser(self):
        obj = IbmDbTestFunctions()
        obj.assert_expect(self.run_test_081)

    def run_test_081(self):
        try:
            conn = ibm_db.connect(config.database, "y", config.password)
            print("??? No way.")
        except:
            print(ibm_db.conn_error())

        #if conn:
        #  print "??? No way."
        #else:
        #  err = ibm_db.conn_error
        #  print err

#__END__
#__LUW_EXPECTED__
#08001
#__ZOS_EXPECTED__
#08001
#__SYSTEMI_EXPECTED__
#08001
#__IDS_EXPECTED__
#08001
