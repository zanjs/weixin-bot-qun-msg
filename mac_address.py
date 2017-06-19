# coding: utf-8
'''mac '''
from __future__ import unicode_literals

import sys
import uuid


reload(sys)

sys.setdefaultencoding('utf-8')

def get_mac_address():
    """
    mac address
    """


    mac = uuid.UUID(int = uuid.getnode()).hex[-12:]
    print mac.upper() # 转大写

    return "-".join([mac[e:e+2] for e in range(0,11,2)])


print get_mac_address().upper()
