# -*- coding: utf-8 -*-
""" Compile module.
"""

import cffi

ffibuilder = cffi.FFI()

ffibuilder.set_source(
    "okfrontpanel._wrapper",
    """
    #include <okFrontPanelDLL.h>
    """,
    libraries=['okFrontPanel']
)

ffibuilder.cdef("""
    typedef void* okFrontPanel_HANDLE;

    typedef enum {
        ok_brdUnknown = 0,
        ok_brdXEM3001v1 = 1,
        ok_brdXEM3001v2 = 2,
        ok_brdXEM3010 = 3,
        ok_brdXEM3005 = 4,
        ok_brdXEM3001CL = 5,
        ok_brdXEM3020 = 6,
        ok_brdXEM3050 = 7,
        ok_brdXEM9002 = 8,
        ok_brdXEM3001RB = 9,
        ok_brdXEM5010 = 10,
        ok_brdXEM6110LX45 = 11,
        ok_brdXEM6110LX150 = 15,
        ok_brdXEM6001 = 12,
        ok_brdXEM6010LX45 = 13,
        ok_brdXEM6010LX150 = 14,
        ok_brdXEM6006LX9 = 16,
        ok_brdXEM6006LX16 = 17,
        ok_brdXEM6006LX25 = 18,
        ok_brdXEM5010LX110 = 19,
        ok_brdZEM4310=20,
        ok_brdXEM6310LX45=21,
        ok_brdXEM6310LX150=22,
        ok_brdXEM6110v2LX45=23,
        ok_brdXEM6110v2LX150=24,
        ok_brdXEM6002LX9=25,
        ok_brdXEM6310MTLX45T=26,
        ok_brdXEM6320LX130T=27,
        ok_brdXEM7350K70T=28,
        ok_brdXEM7350K160T=29,
        ok_brdXEM7350K410T=30,
        ok_brdXEM6310MTLX150T=31
    } ok_BoardModel;
    

    okFrontPanel_HANDLE okFrontPanel_Construct();
    void okFrontPanel_Destruct(okFrontPanel_HANDLE hnd);
    int okFrontPanel_GetDeviceCount(okFrontPanel_HANDLE hnd);
    ok_BoardModel okFrontPanel_GetDeviceListModel(okFrontPanel_HANDLE hnd, int num);
    void okFrontPanel_GetDeviceListSerial(okFrontPanel_HANDLE hnd, int num, char *buf);
    void okFrontPanel_GetBoardModelString(okFrontPanel_HANDLE hnd, ok_BoardModel m, char *buf);
""")

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
