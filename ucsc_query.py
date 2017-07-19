from ucscsdk.ucschandle import UcscHandle
import re

ucsc_ip = "10.1.212.46"
ucsc_user = "admin"
ucsc_pw = "NXos12345"

handle = UcscHandle(ucsc_ip,ucsc_user,ucsc_pw)

handle.login()

object_dict = handle.query_classid("LsServer")

for x in object_dict:
    #print x
    s_dn = ''.join(re.findall(r'dn                              :\D*(\d+)\D*(\d+)', str(x)))
    print s_dn
    #print re.findall(r'dn                              :\D*(\d+)\D*(\d+)', str(x))

handle.logout()

