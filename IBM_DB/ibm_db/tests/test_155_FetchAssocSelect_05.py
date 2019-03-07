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

    def test_155_FetchAssocSelect_05(self):
        obj = IbmDbTestFunctions()
        obj.assert_expect(self.run_test_155)

    def run_test_155(self):
        conn = ibm_db.connect(config.database, config.user, config.password)
        serverinfo = ibm_db.server_info( conn )

        result = ibm_db.exec_immediate(conn, "select * from employee where lastname in ('HAAS','THOMPSON', 'KWAN', 'GEYER', 'STERN', 'PULASKI', 'HENDERSON', 'SPENSER', 'LUCCHESSI', 'OCONNELL', 'QUINTANA', 'NICHOLLS', 'ADAMSON', 'PIANKA', 'YOSHIMURA', 'SCOUTTEN', 'WALKER', 'BROWN', 'JONES', 'LUTZ', 'JEFFERSON', 'MARINO', 'SMITH', 'JOHNSON', 'PEREZ', 'SCHNEIDER', 'PARKER', 'SMITH', 'SETRIGHT', 'MEHTA', 'LEE', 'GOUNOT')")
        i=0
        row = ibm_db.fetch_assoc(result)
        while ( row ):
            i += 1
            if (serverinfo.DBMS_NAME[0:3] == 'IDS'):
                if (row['midinit'] == None):
                    row['midinit'] = ''
                print("%6s %12s %s %-15s%3s %4s %10s %-8s%4d %s%10s %12s %12s %12s" % \
                  (row['empno'], row['firstnme'], row['midinit'], row['lastname'], row['workdept'], \
                  row['phoneno'], row['hiredate'], row['job'], row['edlevel'], row['sex'], \
                  row['birthdate'], row['salary'], row['bonus'], row['comm']))
                row = ibm_db.fetch_assoc(result)
            else:
                if (row['MIDINIT'] == None):
                    row['MIDINIT'] = ''
                print("%6s %12s %s %-15s%3s %4s %10s %-8s%4d %s%10s %12s %12s %12s" % \
                  (row['EMPNO'], row['FIRSTNME'], row['MIDINIT'], row['LASTNAME'], row['WORKDEPT'], \
                  row['PHONENO'], row['HIREDATE'], row['JOB'], row['EDLEVEL'], row['SEX'], \
                  row['BIRTHDATE'], row['SALARY'], row['BONUS'], row['COMM']))
                row = ibm_db.fetch_assoc(result)
        print("%d record(s) selected." % i)

#__END__
#__LUW_EXPECTED__
#000010    CHRISTINE I HAAS           A00 3978 1965-01-01 PRES      18 F1933-08-24     52750.00      1000.00      4220.00
#000020      MICHAEL L THOMPSON       B01 3476 1973-10-10 MANAGER   18 M1948-02-02     41250.00       800.00      3300.00
#000030        SALLY A KWAN           C01 4738 1975-04-05 MANAGER   20 F1941-05-11     38250.00       800.00      3060.00
#000050         JOHN B GEYER          E01 6789 1949-08-17 MANAGER   16 M1925-09-15     40175.00       800.00      3214.00
#000060       IRVING F STERN          D11 6423 1973-09-14 MANAGER   16 M1945-07-07     32250.00       500.00      2580.00
#000070          EVA D PULASKI        D21 7831 1980-09-30 MANAGER   16 F1953-05-26     36170.00       700.00      2893.00
#000090       EILEEN W HENDERSON      E11 5498 1970-08-15 MANAGER   16 F1941-05-15     29750.00       600.00      2380.00
#000100     THEODORE Q SPENSER        E21 0972 1980-06-19 MANAGER   14 M1956-12-18     26150.00       500.00      2092.00
#000110     VINCENZO G LUCCHESSI      A00 3490 1958-05-16 SALESREP  19 M1929-11-05     46500.00       900.00      3720.00
#000120         SEAN   OCONNELL       A00 2167 1963-12-05 CLERK     14 M1942-10-18     29250.00       600.00      2340.00
#000130      DOLORES M QUINTANA       C01 4578 1971-07-28 ANALYST   16 F1925-09-15     23800.00       500.00      1904.00
#000140      HEATHER A NICHOLLS       C01 1793 1976-12-15 ANALYST   18 F1946-01-19     28420.00       600.00      2274.00
#000150        BRUCE   ADAMSON        D11 4510 1972-02-12 DESIGNER  16 M1947-05-17     25280.00       500.00      2022.00
#000160    ELIZABETH R PIANKA         D11 3782 1977-10-11 DESIGNER  17 F1955-04-12     22250.00       400.00      1780.00
#000170    MASATOSHI J YOSHIMURA      D11 2890 1978-09-15 DESIGNER  16 M1951-01-05     24680.00       500.00      1974.00
#000180      MARILYN S SCOUTTEN       D11 1682 1973-07-07 DESIGNER  17 F1949-02-21     21340.00       500.00      1707.00
#000190        JAMES H WALKER         D11 2986 1974-07-26 DESIGNER  16 M1952-06-25     20450.00       400.00      1636.00
#000200        DAVID   BROWN          D11 4501 1966-03-03 DESIGNER  16 M1941-05-29     27740.00       600.00      2217.00
#000210      WILLIAM T JONES          D11 0942 1979-04-11 DESIGNER  17 M1953-02-23     18270.00       400.00      1462.00
#000220     JENNIFER K LUTZ           D11 0672 1968-08-29 DESIGNER  18 F1948-03-19     29840.00       600.00      2387.00
#000230        JAMES J JEFFERSON      D21 2094 1966-11-21 CLERK     14 M1935-05-30     22180.00       400.00      1774.00
#000240    SALVATORE M MARINO         D21 3780 1979-12-05 CLERK     17 M1954-03-31     28760.00       600.00      2301.00
#000250       DANIEL S SMITH          D21 0961 1969-10-30 CLERK     15 M1939-11-12     19180.00       400.00      1534.00
#000260        SYBIL P JOHNSON        D21 8953 1975-09-11 CLERK     16 F1936-10-05     17250.00       300.00      1380.00
#000270        MARIA L PEREZ          D21 9001 1980-09-30 CLERK     15 F1953-05-26     27380.00       500.00      2190.00
#000280        ETHEL R SCHNEIDER      E11 8997 1967-03-24 OPERATOR  17 F1936-03-28     26250.00       500.00      2100.00
#000290         JOHN R PARKER         E11 4502 1980-05-30 OPERATOR  12 M1946-07-09     15340.00       300.00      1227.00
#000300       PHILIP X SMITH          E11 2095 1972-06-19 OPERATOR  14 M1936-10-27     17750.00       400.00      1420.00
#000310        MAUDE F SETRIGHT       E11 3332 1964-09-12 OPERATOR  12 F1931-04-21     15900.00       300.00      1272.00
#000320       RAMLAL V MEHTA          E21 9990 1965-07-07 FIELDREP  16 M1932-08-11     19950.00       400.00      1596.00
#000330         WING   LEE            E21 2103 1976-02-23 FIELDREP  14 M1941-07-18     25370.00       500.00      2030.00
#000340        JASON R GOUNOT         E21 5698 1947-05-05 FIELDREP  16 M1926-05-17     23840.00       500.00      1907.00
#
#32 record(s) selected.
#__ZOS_EXPECTED__
#000010    CHRISTINE I HAAS           A00 3978 1965-01-01 PRES      18 F1933-08-24     52750.00      1000.00      4220.00
#000020      MICHAEL L THOMPSON       B01 3476 1973-10-10 MANAGER   18 M1948-02-02     41250.00       800.00      3300.00
#000030        SALLY A KWAN           C01 4738 1975-04-05 MANAGER   20 F1941-05-11     38250.00       800.00      3060.00
#000050         JOHN B GEYER          E01 6789 1949-08-17 MANAGER   16 M1925-09-15     40175.00       800.00      3214.00
#000060       IRVING F STERN          D11 6423 1973-09-14 MANAGER   16 M1945-07-07     32250.00       500.00      2580.00
#000070          EVA D PULASKI        D21 7831 1980-09-30 MANAGER   16 F1953-05-26     36170.00       700.00      2893.00
#000090       EILEEN W HENDERSON      E11 5498 1970-08-15 MANAGER   16 F1941-05-15     29750.00       600.00      2380.00
#000100     THEODORE Q SPENSER        E21 0972 1980-06-19 MANAGER   14 M1956-12-18     26150.00       500.00      2092.00
#000110     VINCENZO G LUCCHESSI      A00 3490 1958-05-16 SALESREP  19 M1929-11-05     46500.00       900.00      3720.00
#000120         SEAN   OCONNELL       A00 2167 1963-12-05 CLERK     14 M1942-10-18     29250.00       600.00      2340.00
#000130      DOLORES M QUINTANA       C01 4578 1971-07-28 ANALYST   16 F1925-09-15     23800.00       500.00      1904.00
#000140      HEATHER A NICHOLLS       C01 1793 1976-12-15 ANALYST   18 F1946-01-19     28420.00       600.00      2274.00
#000150        BRUCE   ADAMSON        D11 4510 1972-02-12 DESIGNER  16 M1947-05-17     25280.00       500.00      2022.00
#000160    ELIZABETH R PIANKA         D11 3782 1977-10-11 DESIGNER  17 F1955-04-12     22250.00       400.00      1780.00
#000170    MASATOSHI J YOSHIMURA      D11 2890 1978-09-15 DESIGNER  16 M1951-01-05     24680.00       500.00      1974.00
#000180      MARILYN S SCOUTTEN       D11 1682 1973-07-07 DESIGNER  17 F1949-02-21     21340.00       500.00      1707.00
#000190        JAMES H WALKER         D11 2986 1974-07-26 DESIGNER  16 M1952-06-25     20450.00       400.00      1636.00
#000200        DAVID   BROWN          D11 4501 1966-03-03 DESIGNER  16 M1941-05-29     27740.00       600.00      2217.00
#000210      WILLIAM T JONES          D11 0942 1979-04-11 DESIGNER  17 M1953-02-23     18270.00       400.00      1462.00
#000220     JENNIFER K LUTZ           D11 0672 1968-08-29 DESIGNER  18 F1948-03-19     29840.00       600.00      2387.00
#000230        JAMES J JEFFERSON      D21 2094 1966-11-21 CLERK     14 M1935-05-30     22180.00       400.00      1774.00
#000240    SALVATORE M MARINO         D21 3780 1979-12-05 CLERK     17 M1954-03-31     28760.00       600.00      2301.00
#000250       DANIEL S SMITH          D21 0961 1969-10-30 CLERK     15 M1939-11-12     19180.00       400.00      1534.00
#000260        SYBIL P JOHNSON        D21 8953 1975-09-11 CLERK     16 F1936-10-05     17250.00       300.00      1380.00
#000270        MARIA L PEREZ          D21 9001 1980-09-30 CLERK     15 F1953-05-26     27380.00       500.00      2190.00
#000280        ETHEL R SCHNEIDER      E11 8997 1967-03-24 OPERATOR  17 F1936-03-28     26250.00       500.00      2100.00
#000290         JOHN R PARKER         E11 4502 1980-05-30 OPERATOR  12 M1946-07-09     15340.00       300.00      1227.00
#000300       PHILIP X SMITH          E11 2095 1972-06-19 OPERATOR  14 M1936-10-27     17750.00       400.00      1420.00
#000310        MAUDE F SETRIGHT       E11 3332 1964-09-12 OPERATOR  12 F1931-04-21     15900.00       300.00      1272.00
#000320       RAMLAL V MEHTA          E21 9990 1965-07-07 FIELDREP  16 M1932-08-11     19950.00       400.00      1596.00
#000330         WING   LEE            E21 2103 1976-02-23 FIELDREP  14 M1941-07-18     25370.00       500.00      2030.00
#000340        JASON R GOUNOT         E21 5698 1947-05-05 FIELDREP  16 M1926-05-17     23840.00       500.00      1907.00
#
#32 record(s) selected.
#__SYSTEMI_EXPECTED__
#000010    CHRISTINE I HAAS           A00 3978 1965-01-01 PRES      18 F1933-08-24     52750.00      1000.00      4220.00
#000020      MICHAEL L THOMPSON       B01 3476 1973-10-10 MANAGER   18 M1948-02-02     41250.00       800.00      3300.00
#000030        SALLY A KWAN           C01 4738 1975-04-05 MANAGER   20 F1941-05-11     38250.00       800.00      3060.00
#000050         JOHN B GEYER          E01 6789 1949-08-17 MANAGER   16 M1925-09-15     40175.00       800.00      3214.00
#000060       IRVING F STERN          D11 6423 1973-09-14 MANAGER   16 M1945-07-07     32250.00       500.00      2580.00
#000070          EVA D PULASKI        D21 7831 1980-09-30 MANAGER   16 F1953-05-26     36170.00       700.00      2893.00
#000090       EILEEN W HENDERSON      E11 5498 1970-08-15 MANAGER   16 F1941-05-15     29750.00       600.00      2380.00
#000100     THEODORE Q SPENSER        E21 0972 1980-06-19 MANAGER   14 M1956-12-18     26150.00       500.00      2092.00
#000110     VINCENZO G LUCCHESSI      A00 3490 1958-05-16 SALESREP  19 M1929-11-05     46500.00       900.00      3720.00
#000120         SEAN   OCONNELL       A00 2167 1963-12-05 CLERK     14 M1942-10-18     29250.00       600.00      2340.00
#000130      DOLORES M QUINTANA       C01 4578 1971-07-28 ANALYST   16 F1925-09-15     23800.00       500.00      1904.00
#000140      HEATHER A NICHOLLS       C01 1793 1976-12-15 ANALYST   18 F1946-01-19     28420.00       600.00      2274.00
#000150        BRUCE   ADAMSON        D11 4510 1972-02-12 DESIGNER  16 M1947-05-17     25280.00       500.00      2022.00
#000160    ELIZABETH R PIANKA         D11 3782 1977-10-11 DESIGNER  17 F1955-04-12     22250.00       400.00      1780.00
#000170    MASATOSHI J YOSHIMURA      D11 2890 1978-09-15 DESIGNER  16 M1951-01-05     24680.00       500.00      1974.00
#000180      MARILYN S SCOUTTEN       D11 1682 1973-07-07 DESIGNER  17 F1949-02-21     21340.00       500.00      1707.00
#000190        JAMES H WALKER         D11 2986 1974-07-26 DESIGNER  16 M1952-06-25     20450.00       400.00      1636.00
#000200        DAVID   BROWN          D11 4501 1966-03-03 DESIGNER  16 M1941-05-29     27740.00       600.00      2217.00
#000210      WILLIAM T JONES          D11 0942 1979-04-11 DESIGNER  17 M1953-02-23     18270.00       400.00      1462.00
#000220     JENNIFER K LUTZ           D11 0672 1968-08-29 DESIGNER  18 F1948-03-19     29840.00       600.00      2387.00
#000230        JAMES J JEFFERSON      D21 2094 1966-11-21 CLERK     14 M1935-05-30     22180.00       400.00      1774.00
#000240    SALVATORE M MARINO         D21 3780 1979-12-05 CLERK     17 M1954-03-31     28760.00       600.00      2301.00
#000250       DANIEL S SMITH          D21 0961 1969-10-30 CLERK     15 M1939-11-12     19180.00       400.00      1534.00
#000260        SYBIL P JOHNSON        D21 8953 1975-09-11 CLERK     16 F1936-10-05     17250.00       300.00      1380.00
#000270        MARIA L PEREZ          D21 9001 1980-09-30 CLERK     15 F1953-05-26     27380.00       500.00      2190.00
#000280        ETHEL R SCHNEIDER      E11 8997 1967-03-24 OPERATOR  17 F1936-03-28     26250.00       500.00      2100.00
#000290         JOHN R PARKER         E11 4502 1980-05-30 OPERATOR  12 M1946-07-09     15340.00       300.00      1227.00
#000300       PHILIP X SMITH          E11 2095 1972-06-19 OPERATOR  14 M1936-10-27     17750.00       400.00      1420.00
#000310        MAUDE F SETRIGHT       E11 3332 1964-09-12 OPERATOR  12 F1931-04-21     15900.00       300.00      1272.00
#000320       RAMLAL V MEHTA          E21 9990 1965-07-07 FIELDREP  16 M1932-08-11     19950.00       400.00      1596.00
#000330         WING   LEE            E21 2103 1976-02-23 FIELDREP  14 M1941-07-18     25370.00       500.00      2030.00
#000340        JASON R GOUNOT         E21 5698 1947-05-05 FIELDREP  16 M1926-05-17     23840.00       500.00      1907.00
#
#32 record(s) selected.
#__IDS_EXPECTED__
#000010    CHRISTINE I HAAS           A00 3978 1965-01-01 PRES      18 F1933-08-24     52750.00      1000.00      4220.00
#000020      MICHAEL L THOMPSON       B01 3476 1973-10-10 MANAGER   18 M1948-02-02     41250.00       800.00      3300.00
#000030        SALLY A KWAN           C01 4738 1975-04-05 MANAGER   20 F1941-05-11     38250.00       800.00      3060.00
#000050         JOHN B GEYER          E01 6789 1949-08-17 MANAGER   16 M1925-09-15     40175.00       800.00      3214.00
#000060       IRVING F STERN          D11 6423 1973-09-14 MANAGER   16 M1945-07-07     32250.00       500.00      2580.00
#000070          EVA D PULASKI        D21 7831 1980-09-30 MANAGER   16 F1953-05-26     36170.00       700.00      2893.00
#000090       EILEEN W HENDERSON      E11 5498 1970-08-15 MANAGER   16 F1941-05-15     29750.00       600.00      2380.00
#000100     THEODORE Q SPENSER        E21 0972 1980-06-19 MANAGER   14 M1956-12-18     26150.00       500.00      2092.00
#000110     VINCENZO G LUCCHESSI      A00 3490 1958-05-16 SALESREP  19 M1929-11-05     46500.00       900.00      3720.00
#000120         SEAN   OCONNELL       A00 2167 1963-12-05 CLERK     14 M1942-10-18     29250.00       600.00      2340.00
#000130      DOLORES M QUINTANA       C01 4578 1971-07-28 ANALYST   16 F1925-09-15     23800.00       500.00      1904.00
#000140      HEATHER A NICHOLLS       C01 1793 1976-12-15 ANALYST   18 F1946-01-19     28420.00       600.00      2274.00
#000150        BRUCE   ADAMSON        D11 4510 1972-02-12 DESIGNER  16 M1947-05-17     25280.00       500.00      2022.00
#000160    ELIZABETH R PIANKA         D11 3782 1977-10-11 DESIGNER  17 F1955-04-12     22250.00       400.00      1780.00
#000170    MASATOSHI J YOSHIMURA      D11 2890 1978-09-15 DESIGNER  16 M1951-01-05     24680.00       500.00      1974.00
#000180      MARILYN S SCOUTTEN       D11 1682 1973-07-07 DESIGNER  17 F1949-02-21     21340.00       500.00      1707.00
#000190        JAMES H WALKER         D11 2986 1974-07-26 DESIGNER  16 M1952-06-25     20450.00       400.00      1636.00
#000200        DAVID   BROWN          D11 4501 1966-03-03 DESIGNER  16 M1941-05-29     27740.00       600.00      2217.00
#000210      WILLIAM T JONES          D11 0942 1979-04-11 DESIGNER  17 M1953-02-23     18270.00       400.00      1462.00
#000220     JENNIFER K LUTZ           D11 0672 1968-08-29 DESIGNER  18 F1948-03-19     29840.00       600.00      2387.00
#000230        JAMES J JEFFERSON      D21 2094 1966-11-21 CLERK     14 M1935-05-30     22180.00       400.00      1774.00
#000240    SALVATORE M MARINO         D21 3780 1979-12-05 CLERK     17 M1954-03-31     28760.00       600.00      2301.00
#000250       DANIEL S SMITH          D21 0961 1969-10-30 CLERK     15 M1939-11-12     19180.00       400.00      1534.00
#000260        SYBIL P JOHNSON        D21 8953 1975-09-11 CLERK     16 F1936-10-05     17250.00       300.00      1380.00
#000270        MARIA L PEREZ          D21 9001 1980-09-30 CLERK     15 F1953-05-26     27380.00       500.00      2190.00
#000280        ETHEL R SCHNEIDER      E11 8997 1967-03-24 OPERATOR  17 F1936-03-28     26250.00       500.00      2100.00
#000290         JOHN R PARKER         E11 4502 1980-05-30 OPERATOR  12 M1946-07-09     15340.00       300.00      1227.00
#000300       PHILIP X SMITH          E11 2095 1972-06-19 OPERATOR  14 M1936-10-27     17750.00       400.00      1420.00
#000310        MAUDE F SETRIGHT       E11 3332 1964-09-12 OPERATOR  12 F1931-04-21     15900.00       300.00      1272.00
#000320       RAMLAL V MEHTA          E21 9990 1965-07-07 FIELDREP  16 M1932-08-11     19950.00       400.00      1596.00
#000330         WING   LEE            E21 2103 1976-02-23 FIELDREP  14 M1941-07-18     25370.00       500.00      2030.00
#000340        JASON R GOUNOT         E21 5698 1947-05-05 FIELDREP  16 M1926-05-17     23840.00       500.00      1907.00
#
#32 record(s) selected.
