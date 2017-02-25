# -*- coding: utf-8 -*-
""" Defined constants and structures for FrontPanel
"""

import ctypes
from enum import Enum, IntEnum

MODE_HIST = 0

MAX_DEVICEID_LENGTH = 33            # 32-byte content + NULL termination
MAX_SERIALNUMBER_LENGTH = 11        # 10-byte content + NULL termination
MAX_PRODUCT_NAME_LENGTH = 128       # 127-byte content + NULL termination
MAX_BOARD_MODEL_STRING_LENGTH = 128
MAX_ERROR_NAME_LENGTH = 128

# ok_USBSpeed types
USBSPEED_UNKNOWN = 0
USBSPEED_FULL = 1
USBSPEED_HIGH = 2
USBSPEED_SUPER = 3

# ok_Interface types
OK_INTERFACE_UNKNOWN = 0
OK_INTERFACE_USB2 = 1
OK_INTERFACE_PCIE = 2
OK_INTERFACE_USB3 = 3

# ok_Product types
PRODUCT_OEM_START = 11000

# ok_FPGAConfigurationMethod types
FPGACONFIGURATIONMETHOD_NVRAM = 0
FPGACONFIGURATIONMETHOD_JTAG = 1

# device sensor
MAX_DEVICE_SENSOR_NAME_LENGTH = 64              # including NULL termination
MAX_DEVICE_SENSOR_DESCRIPTION_LENGTH = 256      # including NULL termination

REGISTER_SET_ENTRIES = 64

# =============================================================================
# predefined Enum types
# =============================================================================


class ClockSource_22150(Enum):
    Ref = 0
    Div1ByN = 1
    Div1By2 = 2
    Div1By3 = 3
    Div2ByN = 4
    Div2By2 = 5
    Div2By4 = 6


class ClockSource_22393(Enum):
    Ref         = 0
    PLL0_0      = 2
    PLL0_180    = 3
    PLL1_0      = 4
    PLL1_180    = 5
    PLL2_0      = 6
    PLL2_180    = 7


class DividerSource(Enum):
    Ref = 0
    VCO = 1


class BoardModel(Enum):
    Unknown         = 0
    XEM3001v1       = 1
    XEM3001v2       = 2
    XEM3010         = 3
    XEM3005         = 4
    XEM3001CL       = 5
    XEM3020         = 6
    XEM3050         = 7
    XEM9002         = 8
    XEM3001RB       = 9
    XEM5010         = 10
    XEM6110LX45     = 11
    XEM6110LX150    = 15
    XEM6001         = 12
    XEM6010LX45     = 13
    XEM6010LX150    = 14
    XEM6006LX9      = 16
    XEM6006LX16     = 17
    XEM6006LX25     = 18
    XEM5010LX110    = 19
    ZEM4310         = 20
    XEM6310LX45     = 21
    XEM6310LX150    = 22
    XEM6110v2LX45   = 23
    XEM6110v2LX150  = 24
    XEM6002LX9      = 25
    XEM6310MTLX45T  = 26
    XEM6320LX130T   = 27
    XEM7350K70T     = 28
    XEM7350K160T    = 29
    XEM7350K410T    = 30
    XEM6310MTLX150T = 31
    ZEM5305A2       = 32
    ZEM5305A7       = 33
    XEM7001A15      = 34
    XEM7001A35      = 35
    XEM7360K160T    = 36
    XEM7360K410T    = 37
    ZEM5310A4       = 38
    ZEM5310A7       = 39
    ZEM5370A5       = 40
    XEM7010A50      = 41
    XEM7010A200     = 42
    XEM7310A75      = 43
    XEM7310A200     = 44


class ErrorCode(Enum):
    NoError             = 0
    Failed              = -1
    Timeout             = -2
    DoneNotHigh         = -3
    TransferError       = -4
    CommunicationError  = -5
    InvalidBitstream    = -6
    FileError           = -7
    DeviceNotOpen       = -8
    InvalidEndpoint     = -9
    InvalidBlockSize    = -10
    I2CRestrictedAddress = -11
    I2CBitError         = -12
    I2CNack             = -13
    I2CUnknownStatus    = -14
    UnsupportedFeature  = -15
    FIFOUnderflow       = -16
    FIFOOverflow        = -17
    DataAlignmentError  = -18
    InvalidResetProfile = -19
    InvalidParameter    = -20


class RegisterEntry(ctypes.Structure):
    _fields_ = [
        ('address', ctypes.c_uint32),
        ('data', ctypes.c_uint32)
    ]


class RegisterSet(ctypes.Structure):
    _fields_ = [
        ('count', ctypes.c_uint32),
        ('entries', RegisterEntry * REGISTER_SET_ENTRIES)
    ]


class TriggerEntry(ctypes.Structure):
    _fields_ = [
        ('address', ctypes.c_uint32),
        ('mask', ctypes.c_uint32)
    ]


class ResetProfile(ctypes.Structure):
    _fields_ = [
        ('magic',               ctypes.c_uint32),
        ('configFileLocation',  ctypes.c_uint32),
        ('configFileLength',    ctypes.c_uint32),
        ('doneWaitUS',          ctypes.c_uint32),
        ('resetWaitUS',         ctypes.c_uint32),
        ('registerWaitUS',      ctypes.c_uint32),
        ('padBytes1',           ctypes.c_uint32 * 28),
        ('wireInValues',        ctypes.c_uint32 * 32),
        ('registerEntryCount',  ctypes.c_uint32),
        ('registerEntries',     RegisterEntry * 256),
        ('triggerEntryCount',   ctypes.c_uint32),
        ('triggerEntries',      TriggerEntry * 32),
        ('padBytes2',           ctypes.c_uint8 * 1520)
    ]


class FlashLayout(ctypes.Structure):
    _fields_ = [
        ('sectorCount',     ctypes.c_uint32),
        ('sectorSize',      ctypes.c_uint32),
        ('pageSize',        ctypes.c_uint32),
        ('minUserSector',   ctypes.c_uint32),
        ('maxUserSector',   ctypes.c_uint32)
    ]

class DeviceInfo(ctypes.Structure):
    _fields_ = [
        ('deviceID',                    ctypes.c_char * MAX_DEVICEID_LENGTH),
        ('serialNumber',                ctypes.c_char * MAX_SERIALNUMBER_LENGTH),
        ('productName',                 ctypes.c_char * MAX_BOARD_MODEL_STRING_LENGTH),
        ('productID',                   ctypes.c_int),
        ('deviceInterface',             ctypes.c_int),
        ('usbSpeed',                    ctypes.c_int),
        ('deviceMajorVersion',          ctypes.c_int),
        ('deviceMinorVersion',          ctypes.c_int),
        ('hostInterfaceMajorVersion',   ctypes.c_int),
        ('hostInterfaceMinorVersion',   ctypes.c_int),
        ('isPLL22150Supported',         ctypes.c_bool),
        ('isPLL22393Supported',         ctypes.c_bool),
        ('isFrontPanelEnabled',         ctypes.c_bool),
        ('wireWidth',                   ctypes.c_int),
        ('triggerWidth',                ctypes.c_int),
        ('pipeWidth',                   ctypes.c_int),
        ('registerAddressWidth',        ctypes.c_int),
        ('registerDataWidth',           ctypes.c_int),
        ('flashSystem',                 FlashLayout),
        ('flashFPGA',                   FlashLayout),
        ('hasFMCEEPROM',                ctypes.c_bool),
    ]

class DeviceMatchInfo(ctypes.Structure):
    _fields_ = [
        ('productName',     ctypes.c_char * MAX_PRODUCT_NAME_LENGTH),
        ('productBaseID',   ctypes.c_int),
        ('productID',       ctypes.c_int),
        ('usbVID',          ctypes.c_uint32),
        ('usbPID',          ctypes.c_uint32),
        ('pciDID',          ctypes.c_uint32)
    ]

DeviceSensorType_t = ctypes.c_int


class DeviceSensorType(IntEnum):
    INVALID     = 0
    BOOL        = 1
    INTEGER     = 2
    FLOAT       = 3
    VOLTAGE     = 4
    CURRENT     = 5
    TEMPERATURE = 6
    FAN_RPM     = 7


class DeviceSensor(ctypes.Structure):
    _fields_ = [
        ('id',          ctypes.c_int),
        ('type',        DeviceSensorType_t),
        ('name',        ctypes.c_char * MAX_DEVICE_SENSOR_NAME_LENGTH),
        ('description', ctypes.c_char * MAX_DEVICE_SENSOR_DESCRIPTION_LENGTH),
        ('min',         ctypes.c_double),
        ('max',         ctypes.c_double),
        ('step',        ctypes.c_double),
        ('value',       ctypes.c_double)
    ]


