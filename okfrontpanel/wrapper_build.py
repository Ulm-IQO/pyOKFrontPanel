# -*- coding: utf-8 -*-
""" Compile module.
"""

#
#   Find include and library directories
#
import sys
import os
import struct

extra_dirs = {}
include_dirs = []
library_dirs = []

bits = struct.calcsize("P") * 8

if sys.platform == 'win32':
    arch = 'x64' if bits == 64 else 'Win32'
    okpath = os.environ['OKFP_SDK']
    include_dirs.append(os.path.join(okpath, 'include'))
    library_dirs.append(os.path.join(okpath, 'lib', arch))
    extra_dirs.update({
        'include_dirs': include_dirs,
        'library_dirs': library_dirs
        })
#
#   CFFI
#

import cffi

ffibuilder = cffi.FFI()

ffibuilder.set_source(
    "okfrontpanel._wrapper",
    """
    #include <stdint.h>
    #include <okFrontPanelDLL.h>
    """,
    libraries=['okFrontPanel'],
    **extra_dirs
)

ffibuilder.cdef("""
    #define TRUE ...
    #define FALSE ...

    #define OK_MAX_DEVICEID_LENGTH              ...     // 32-byte content + NULL termination
    #define OK_MAX_SERIALNUMBER_LENGTH          ...     // 10-byte content + NULL termination
    #define OK_MAX_PRODUCT_NAME_LENGTH          ...    // 127-byte content + NULL termination
    #define OK_MAX_BOARD_MODEL_STRING_LENGTH    ...

    // ok_USBSpeed types
    #define OK_USBSPEED_UNKNOWN                 ...
    #define OK_USBSPEED_FULL                    ...
    #define OK_USBSPEED_HIGH                    ...
    #define OK_USBSPEED_SUPER                   ...

    // ok_Interface types
    #define OK_INTERFACE_UNKNOWN                ...
    #define OK_INTERFACE_USB2                   ...
    #define OK_INTERFACE_PCIE                   ...
    #define OK_INTERFACE_USB3                   ...
    #define OK_PRODUCT_OEM_START                ...

    typedef int Bool;
    typedef char okBool;
    typedef char const * okFP_dll_pchar;

    typedef enum {
        ok_FPGAConfigurationMethod_NVRAM = 0,
	    ok_FPGAConfigurationMethod_JTAG  = 1
    } ok_FPGAConfigurationMethod;

    typedef enum {
        ok_ClkSrc22150_Ref      = 0,
        ok_ClkSrc22150_Div1ByN  = 1,
        ok_ClkSrc22150_Div1By2  = 2,
        ok_ClkSrc22150_Div1By3  = 3,
        ok_ClkSrc22150_Div2ByN  = 4,
        ok_ClkSrc22150_Div2By2  = 5,
        ok_ClkSrc22150_Div2By4  = 6
    } ok_ClockSource_22150;

    typedef enum {
        ok_ClkSrc22393_Ref      = 0,
        ok_ClkSrc22393_PLL0_0   = 2,
        ok_ClkSrc22393_PLL0_180 = 3,
        ok_ClkSrc22393_PLL1_0   = 4,
        ok_ClkSrc22393_PLL1_180 = 5,
        ok_ClkSrc22393_PLL2_0   = 6,
        ok_ClkSrc22393_PLL2_180 = 7
    } ok_ClockSource_22393;

    typedef enum {
        ok_DivSrc_Ref = 0,
        ok_DivSrc_VCO = 1
    } ok_DividerSource;

    typedef enum {
        ok_brdUnknown           = 0,
        ok_brdXEM3001v1         = 1,
        ok_brdXEM3001v2         = 2,
        ok_brdXEM3010           = 3,
        ok_brdXEM3005           = 4,
        ok_brdXEM3001CL         = 5,
        ok_brdXEM3020           = 6,
        ok_brdXEM3050           = 7,
        ok_brdXEM9002           = 8,
        ok_brdXEM3001RB         = 9,
        ok_brdXEM5010           = 10,
        ok_brdXEM6110LX45       = 11,
        ok_brdXEM6110LX150      = 15,
        ok_brdXEM6001           = 12,
        ok_brdXEM6010LX45       = 13,
        ok_brdXEM6010LX150      = 14,
        ok_brdXEM6006LX9        = 16,
        ok_brdXEM6006LX16       = 17,
        ok_brdXEM6006LX25       = 18,
        ok_brdXEM5010LX110      = 19,
        ok_brdZEM4310           = 20,
        ok_brdXEM6310LX45       = 21,
        ok_brdXEM6310LX150      = 22,
        ok_brdXEM6110v2LX45     = 23,
        ok_brdXEM6110v2LX150    = 24,
        ok_brdXEM6002LX9        = 25,
        ok_brdXEM6310MTLX45T    = 26,
        ok_brdXEM6320LX130T     = 27,
        ok_brdXEM7350K70T       = 28,
        ok_brdXEM7350K160T      = 29,
        ok_brdXEM7350K410T      = 30,
        ok_brdXEM6310MTLX150T   = 31,
        ok_brdZEM5305A2         = 32,
        ok_brdZEM5305A7         = 33,
        ok_brdXEM7001A15        = 34,
        ok_brdXEM7001A35        = 35,
        ok_brdXEM7360K160T      = 36,
        ok_brdXEM7360K410T      = 37,
        ok_brdZEM5310A4         = 38,
        ok_brdZEM5310A7         = 39,
        ok_brdZEM5370A5         = 40,
        ok_brdXEM7010A50        = 41,
        ok_brdXEM7010A200       = 42,
        ok_brdXEM7310A75        = 43,
        ok_brdXEM7310A200       = 44
    } ok_BoardModel;


// Errors
    typedef enum {
        ok_NoError                = 0,
        ok_Failed                 = -1,
        ok_Timeout                = -2,
        ok_DoneNotHigh            = -3,
        ok_TransferError          = -4,
        ok_CommunicationError     = -5,
        ok_InvalidBitstream       = -6,
        ok_FileError              = -7,
        ok_DeviceNotOpen          = -8,
        ok_InvalidEndpoint        = -9,
        ok_InvalidBlockSize       = -10,
        ok_I2CRestrictedAddress   = -11,
        ok_I2CBitError            = -12,
        ok_I2CNack                = -13,
        ok_I2CUnknownStatus       = -14,
        ok_UnsupportedFeature     = -15,
        ok_FIFOUnderflow          = -16,
        ok_FIFOOverflow           = -17,
        ok_DataAlignmentError     = -18,
        ok_InvalidResetProfile    = -19,
        ok_InvalidParameter       = -20
    } ok_ErrorCode;


    typedef struct {...;} okTRegisterEntry;
    typedef struct {...;} okTTriggerEntry;
    typedef struct {...;} okTFPGAResetProfile;
    typedef struct {...;} okTFlashLayout;
    typedef struct {...;} okTDeviceInfo;
    typedef struct {...;} okTDeviceMatchInfo;
    typedef struct {...;} okTDeviceSensor;

    typedef void* okPLL22150_HANDLE;
    typedef void* okPLL22393_HANDLE;
    typedef void* okFrontPanel_HANDLE;
    typedef struct okDeviceSensorsHandle* okDeviceSensors_HANDLE;
    typedef struct okDeviceSettingsHandle* okDeviceSettings_HANDLE;
    typedef struct okFirmwareHandle* okFirmware_HANDLE;
    typedef struct okFirmwarePackageHandle* okFirmwarePackage_HANDLE;
    typedef struct okFrontPanelManagerHandle* okFrontPanelManager_HANDLE;
    typedef struct okCFrontPanelManagerHandle* okCFrontPanelManager_HANDLE;
    typedef struct okCFrontPanelDevicesHandle* okCFrontPanelDevices_HANDLE;

    typedef void (*okFirmware_PerformTasks_Callback)(void*, int, const char*);


// General
//
    void okFrontPanelDLL_GetVersion(char *date, char *time);

// okPLL22393
//
    okPLL22393_HANDLE okPLL22393_Construct();
    void okPLL22393_Destruct(okPLL22393_HANDLE pll);
    void okPLL22393_SetCrystalLoad(okPLL22393_HANDLE pll, double capload);
    void okPLL22393_SetReference(okPLL22393_HANDLE pll, double freq);
    double okPLL22393_GetReference(okPLL22393_HANDLE pll);
    Bool okPLL22393_SetPLLParameters(okPLL22393_HANDLE pll, int n, int p, int q, Bool enable);
    Bool okPLL22393_SetPLLLF(okPLL22393_HANDLE pll, int n, int lf);
    Bool okPLL22393_SetOutputDivider(okPLL22393_HANDLE pll, int n, int div);
    Bool okPLL22393_SetOutputSource(okPLL22393_HANDLE pll, int n, ok_ClockSource_22393 clksrc);
    void okPLL22393_SetOutputEnable(okPLL22393_HANDLE pll, int n, Bool enable);
    int okPLL22393_GetPLLP(okPLL22393_HANDLE pll, int n);
    int okPLL22393_GetPLLQ(okPLL22393_HANDLE pll, int n);
    double okPLL22393_GetPLLFrequency(okPLL22393_HANDLE pll, int n);
    int okPLL22393_GetOutputDivider(okPLL22393_HANDLE pll, int n);
    ok_ClockSource_22393 okPLL22393_GetOutputSource(okPLL22393_HANDLE pll, int n);
    double okPLL22393_GetOutputFrequency(okPLL22393_HANDLE pll, int n);
    Bool okPLL22393_IsOutputEnabled(okPLL22393_HANDLE pll, int n);
    Bool okPLL22393_IsPLLEnabled(okPLL22393_HANDLE pll, int n);
    void okPLL22393_InitFromProgrammingInfo(okPLL22393_HANDLE pll, unsigned char *buf);
    void okPLL22393_GetProgrammingInfo(okPLL22393_HANDLE pll, unsigned char *buf);

// okPLL22150
//
    okPLL22150_HANDLE okPLL22150_Construct();
    void okPLL22150_Destruct(okPLL22150_HANDLE pll);
    void okPLL22150_SetCrystalLoad(okPLL22150_HANDLE pll, double capload);
    void okPLL22150_SetReference(okPLL22150_HANDLE pll, double freq, Bool extosc);
    double okPLL22150_GetReference(okPLL22150_HANDLE pll);
    Bool okPLL22150_SetVCOParameters(okPLL22150_HANDLE pll, int p, int q);
    int okPLL22150_GetVCOP(okPLL22150_HANDLE pll);
    int okPLL22150_GetVCOQ(okPLL22150_HANDLE pll);
    double okPLL22150_GetVCOFrequency(okPLL22150_HANDLE pll);
    void okPLL22150_SetDiv1(okPLL22150_HANDLE pll, ok_DividerSource divsrc, int n);
    void okPLL22150_SetDiv2(okPLL22150_HANDLE pll, ok_DividerSource divsrc, int n);
    ok_DividerSource okPLL22150_GetDiv1Source(okPLL22150_HANDLE pll);
    ok_DividerSource okPLL22150_GetDiv2Source(okPLL22150_HANDLE pll);
    int okPLL22150_GetDiv1Divider(okPLL22150_HANDLE pll);
    int okPLL22150_GetDiv2Divider(okPLL22150_HANDLE pll);
    void okPLL22150_SetOutputSource(okPLL22150_HANDLE pll, int output, ok_ClockSource_22150 clksrc);
    void okPLL22150_SetOutputEnable(okPLL22150_HANDLE pll, int output, Bool enable);
    ok_ClockSource_22150 okPLL22150_GetOutputSource(okPLL22150_HANDLE pll, int output);
    double okPLL22150_GetOutputFrequency(okPLL22150_HANDLE pll, int output);
    Bool okPLL22150_IsOutputEnabled(okPLL22150_HANDLE pll, int output);
    void okPLL22150_InitFromProgrammingInfo(okPLL22150_HANDLE pll, unsigned char *buf);
    void okPLL22150_GetProgrammingInfo(okPLL22150_HANDLE pll, unsigned char *buf);

// okDeviceSensors
//
    okDeviceSensors_HANDLE okDeviceSensors_Construct();
    void okDeviceSensors_Destruct(okDeviceSensors_HANDLE hnd);
    int okDeviceSensors_GetSensorCount(okDeviceSensors_HANDLE hnd);
    okTDeviceSensor okDeviceSensors_GetSensor(okDeviceSensors_HANDLE hnd, int n);

// okDeviceSettings
//
    okDeviceSettings_HANDLE okDeviceSettings_Construct();
    void okDeviceSettings_Destruct(okDeviceSettings_HANDLE hnd);
    ok_ErrorCode okDeviceSettings_GetString(okDeviceSettings_HANDLE hnd, const char *key, int length, char *buf);
    ok_ErrorCode okDeviceSettings_SetString(okDeviceSettings_HANDLE hnd, const char *key, const char *buf);
    ok_ErrorCode okDeviceSettings_GetInt(okDeviceSettings_HANDLE hnd, const char *key, uint32_t *value);
    ok_ErrorCode okDeviceSettings_SetInt(okDeviceSettings_HANDLE hnd, const char *key, uint32_t value);
    ok_ErrorCode okDeviceSettings_Delete(okDeviceSettings_HANDLE hnd, const char *key);
    ok_ErrorCode okDeviceSettings_Save(okDeviceSettings_HANDLE hnd);

// okFirmware and okFirmwarePackage
//
    okFirmwarePackage_HANDLE okFirmwarePackage_Load(const char *filename);
    void okFirmwarePackage_Destruct(okFirmwarePackage_HANDLE hnd);
    int okFirmwarePackage_GetFirmwareCount(okFirmwarePackage_HANDLE hnd);
    okFirmware_HANDLE okFirmwarePackage_GetFirmware(okFirmwarePackage_HANDLE hnd, int num);

    ok_ErrorCode okFirmware_PerformTasks(okFirmware_HANDLE hnd, const char *serial, okFirmware_PerformTasks_Callback callback, void *arg);

// okFrontPanel
//
    okFrontPanel_HANDLE okFrontPanel_Construct();
    void okFrontPanel_Destruct(okFrontPanel_HANDLE hnd);
    int okFrontPanel_GetErrorString(int ec, char *buf, int length);
    ok_ErrorCode okFrontPanel_AddCustomDevice(const okTDeviceMatchInfo* matchInfo, const okTDeviceInfo* devInfo);
    ok_ErrorCode okFrontPanel_RemoveCustomDevice(int productID);
    ok_ErrorCode okFrontPanel_WriteI2C(okFrontPanel_HANDLE hnd, const int addr, int length, unsigned char *data);
    ok_ErrorCode okFrontPanel_ReadI2C(okFrontPanel_HANDLE hnd, const int addr, int length, unsigned char *data);
    ok_ErrorCode okFrontPanel_FlashEraseSector(okFrontPanel_HANDLE hnd, uint32_t address);
    ok_ErrorCode okFrontPanel_FlashWrite(okFrontPanel_HANDLE hnd, uint32_t address, uint32_t length, const uint8_t *buf);
    ok_ErrorCode okFrontPanel_FlashRead(okFrontPanel_HANDLE hnd, uint32_t address, uint32_t length, uint8_t *buf);
    ok_ErrorCode okFrontPanel_GetFPGAResetProfile(okFrontPanel_HANDLE hnd, ok_FPGAConfigurationMethod method, okTFPGAResetProfile *profile);
    ok_ErrorCode okFrontPanel_GetFPGAResetProfileWithSize(okFrontPanel_HANDLE hnd, ok_FPGAConfigurationMethod method, okTFPGAResetProfile *profile, unsigned size);
    ok_ErrorCode okFrontPanel_SetFPGAResetProfile(okFrontPanel_HANDLE hnd, ok_FPGAConfigurationMethod method, const okTFPGAResetProfile *profile);
    ok_ErrorCode okFrontPanel_SetFPGAResetProfileWithSize(okFrontPanel_HANDLE hnd, ok_FPGAConfigurationMethod method, const okTFPGAResetProfile *profile, unsigned size);
    ok_ErrorCode okFrontPanel_ReadRegister(okFrontPanel_HANDLE hnd, uint32_t addr, uint32_t *data);
    ok_ErrorCode okFrontPanel_ReadRegisters(okFrontPanel_HANDLE hnd, unsigned num, okTRegisterEntry* regs);
    ok_ErrorCode okFrontPanel_WriteRegister(okFrontPanel_HANDLE hnd, uint32_t addr, uint32_t data);
    ok_ErrorCode okFrontPanel_WriteRegisters(okFrontPanel_HANDLE hnd, unsigned num, const okTRegisterEntry* regs);
    int okFrontPanel_GetHostInterfaceWidth(okFrontPanel_HANDLE hnd);
    Bool okFrontPanel_IsHighSpeed(okFrontPanel_HANDLE hnd);
    ok_BoardModel okFrontPanel_GetBoardModel(okFrontPanel_HANDLE hnd);
    void okFrontPanel_GetBoardModelString(okFrontPanel_HANDLE hnd, ok_BoardModel m, char *buf);
    int okFrontPanel_GetDeviceCount(okFrontPanel_HANDLE hnd);
    ok_BoardModel okFrontPanel_GetDeviceListModel(okFrontPanel_HANDLE hnd, int num);
    void okFrontPanel_GetDeviceListSerial(okFrontPanel_HANDLE hnd, int num, char *buf);
    ok_ErrorCode okFrontPanel_OpenBySerial(okFrontPanel_HANDLE hnd, const char *serial);
    Bool okFrontPanel_IsOpen(okFrontPanel_HANDLE hnd);
    void okFrontPanel_EnableAsynchronousTransfers(okFrontPanel_HANDLE hnd, Bool enable);
    ok_ErrorCode okFrontPanel_SetBTPipePollingInterval(okFrontPanel_HANDLE hnd, int interval);
    void okFrontPanel_SetTimeout(okFrontPanel_HANDLE hnd, int timeout);
    int okFrontPanel_GetDeviceMajorVersion(okFrontPanel_HANDLE hnd);
    int okFrontPanel_GetDeviceMinorVersion(okFrontPanel_HANDLE hnd);
    ok_ErrorCode okFrontPanel_ResetFPGA(okFrontPanel_HANDLE hnd);
    void okFrontPanel_Close(okFrontPanel_HANDLE hnd);
    void okFrontPanel_GetSerialNumber(okFrontPanel_HANDLE hnd, char *buf);
    ok_ErrorCode okFrontPanel_GetDeviceSensors(okFrontPanel_HANDLE hnd, okDeviceSensors_HANDLE settings);
    ok_ErrorCode okFrontPanel_GetDeviceSettings(okFrontPanel_HANDLE hnd, okDeviceSettings_HANDLE settings);
    ok_ErrorCode okFrontPanel_GetDeviceInfo(okFrontPanel_HANDLE hnd, okTDeviceInfo *info);
    ok_ErrorCode okFrontPanel_GetDeviceInfoWithSize(okFrontPanel_HANDLE hnd, okTDeviceInfo *info, unsigned size);
    void okFrontPanel_GetDeviceID(okFrontPanel_HANDLE hnd, char *buf);
    void okFrontPanel_SetDeviceID(okFrontPanel_HANDLE hnd, const char *strID);
    ok_ErrorCode okFrontPanel_ConfigureFPGA(okFrontPanel_HANDLE hnd, const char *strFilename);
    ok_ErrorCode okFrontPanel_ConfigureFPGAWithReset(okFrontPanel_HANDLE hnd, const char *strFilename, const okTFPGAResetProfile *reset);
    ok_ErrorCode okFrontPanel_ConfigureFPGAFromMemory(okFrontPanel_HANDLE hnd, unsigned char *data, unsigned long length);
    ok_ErrorCode okFrontPanel_ConfigureFPGAFromMemoryWithReset(okFrontPanel_HANDLE hnd, unsigned char *data, unsigned long length, const okTFPGAResetProfile *reset);
    ok_ErrorCode okFrontPanel_ConfigureFPGAFromFlash(okFrontPanel_HANDLE hnd, unsigned long configIndex);
    ok_ErrorCode okFrontPanel_GetPLL22150Configuration(okFrontPanel_HANDLE hnd, okPLL22150_HANDLE pll);
    ok_ErrorCode okFrontPanel_SetPLL22150Configuration(okFrontPanel_HANDLE hnd, okPLL22150_HANDLE pll);
    ok_ErrorCode okFrontPanel_GetEepromPLL22150Configuration(okFrontPanel_HANDLE hnd, okPLL22150_HANDLE pll);
    ok_ErrorCode okFrontPanel_SetEepromPLL22150Configuration(okFrontPanel_HANDLE hnd, okPLL22150_HANDLE pll);
    ok_ErrorCode okFrontPanel_GetPLL22393Configuration(okFrontPanel_HANDLE hnd, okPLL22393_HANDLE pll);
    ok_ErrorCode okFrontPanel_SetPLL22393Configuration(okFrontPanel_HANDLE hnd, okPLL22393_HANDLE pll);
    ok_ErrorCode okFrontPanel_GetEepromPLL22393Configuration(okFrontPanel_HANDLE hnd, okPLL22393_HANDLE pll);
    ok_ErrorCode okFrontPanel_SetEepromPLL22393Configuration(okFrontPanel_HANDLE hnd, okPLL22393_HANDLE pll);
    ok_ErrorCode okFrontPanel_LoadDefaultPLLConfiguration(okFrontPanel_HANDLE hnd);
    Bool okFrontPanel_IsFrontPanelEnabled(okFrontPanel_HANDLE hnd);
    Bool okFrontPanel_IsFrontPanel3Supported(okFrontPanel_HANDLE hnd);
    void okFrontPanel_UpdateWireIns(okFrontPanel_HANDLE hnd);
    ok_ErrorCode okFrontPanel_GetWireInValue(okFrontPanel_HANDLE hnd, int epAddr, uint32_t *val);
    ok_ErrorCode okFrontPanel_SetWireInValue(okFrontPanel_HANDLE hnd, int ep, unsigned long val, unsigned long mask);
    void okFrontPanel_UpdateWireOuts(okFrontPanel_HANDLE hnd);
    unsigned long okFrontPanel_GetWireOutValue(okFrontPanel_HANDLE hnd, int epAddr);
    ok_ErrorCode okFrontPanel_ActivateTriggerIn(okFrontPanel_HANDLE hnd, int epAddr, int bit);
    void okFrontPanel_UpdateTriggerOuts(okFrontPanel_HANDLE hnd);
    Bool okFrontPanel_IsTriggered(okFrontPanel_HANDLE hnd, int epAddr, unsigned long mask);
    long okFrontPanel_GetLastTransferLength(okFrontPanel_HANDLE hnd);
    long okFrontPanel_WriteToPipeIn(okFrontPanel_HANDLE hnd, int epAddr, long length, unsigned char *data);
    long okFrontPanel_ReadFromPipeOut(okFrontPanel_HANDLE hnd, int epAddr, long length, unsigned char *data);
    long okFrontPanel_WriteToBlockPipeIn(okFrontPanel_HANDLE hnd, int epAddr, int blockSize, long length, unsigned char *data);
    long okFrontPanel_ReadFromBlockPipeOut(okFrontPanel_HANDLE hnd, int epAddr, int blockSize, long length, unsigned char *data);

// okFrontPanelManager
//
    okCFrontPanelManager_HANDLE okFrontPanelManager_Construct(okFrontPanelManager_HANDLE self, const char* realm);
    void okFrontPanelManager_Destruct(okCFrontPanelManager_HANDLE hnd);
    ok_ErrorCode okFrontPanelManager_StartMonitoring(okCFrontPanelManager_HANDLE hnd);
    okFrontPanel_HANDLE okFrontPanelManager_Open(okCFrontPanelManager_HANDLE hnd, const char *serial);

// FrontPanelDevices
//
    okCFrontPanelDevices_HANDLE okFrontPanelDevices_Construct(const char* realm);
    void okFrontPanelDevices_Destruct(okCFrontPanelDevices_HANDLE hnd);
    int okFrontPanelDevices_GetCount(okCFrontPanelDevices_HANDLE hnd);
    void okFrontPanelDevices_GetSerial(okCFrontPanelDevices_HANDLE hnd, int num, char* buf);
    okFrontPanel_HANDLE okFrontPanelDevices_Open(okCFrontPanelDevices_HANDLE hnd, const char* serial);

""")

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
