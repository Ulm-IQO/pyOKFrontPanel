# -*- coding: utf-8 -*-
""" Classes
"""

import os
import sys
import struct


if sys.platform == 'win32':
    bits = struct.calcsize("P") * 8
    arch = 'x64' if bits == 64 else 'Win32'
    okpath = os.environ['OKFP_SDK']
    dllpath = os.path.join(okpath, 'lib', arch)
    os.environ['PATH'] = dllpath + ';' + os.environ['PATH']


from ._wrapper import ffi, lib


class PLL22150:
    def __init__(self):
        self._handle = lib.okPLL22150_Construct()

    def __del__(self):
        lib.okPLL22150_Destruct(self._handle)

    @property
    def h(self):
        return self._handle

    def SetCrystalLoad(self, capload):
        lib.okPLL22150_SetCrystalLoad(self._handle, float(capload))

    def SetReference(self, freq, extosc):
        lib.okPLL22150_SetReference(self._handle, float(freq), bool(extosc))

    def GetReference(self):
        return lib.okPLL22150_GetReference(self._handle)

    def SetVCOParameters(self, p, q):
        return lib.okPLL22150_SetVCOParameters(self._handle, p, q)

    def GetVCOP(self):
        return lib.okPLL22150_GetVCOP(self._handle)

    def GetVCOQ(self):
        return lib.okPLL22150_GetVCOQ(self._handle)

    def GetVCOFrequency(self):
        return lib.okPLL22150_GetVCOFrequency(self._handle)

    def SetDiv1(self, divsrc, n):
        lib.okPLL22150_SetDiv1(self._handle, divsrc, n)

    def SetDiv2(self, divsrc, n):
        lib.okPLL22150_SetDiv2(self._handle, divsrc, n)

    def GetDiv1Source(self):
        return lib.okPLL22150_GetDiv1Source(self._handle)

    def GetDiv2Source(self):
        return lib.okPLL22150_GetDiv2Source(self._handle)

    def GetDiv1Divider(self):
        return lib.okPLL22150_GetDiv1Divider(self._handle)

    def GetDiv2Divider(self):
        return lib.okPLL22150_GetDiv2Divider(self._handle)

    def SetOutputSource(self, output, clksrc):
        lib.okPLL22150_SetOutputSource(self._handle, output, clksrc)

    def SetOutputEnable(self, output, enable):
        lib.okPLL22150_SetOutputEnable(self._handle, output, enable)

    def GetOutputSource(self, output):
        lib.okPLL22150_GetOutputSource(self._handle, output)

    def GetOutputFrequency(self, output):
        lib.okPLL22150_GetOutputFrequency(self._handle, output)

    def IsOutputEnabled(self, output):
        return lib.okPLL22150_IsOutputEnabled(self._handle, output) == lib.TRUE

    def InitFromProgrammingInfo(self, info):
        buf = ffi.new('char[]', info)
        lib.okPLL22150_InitFromProgrammingInfo(self._handle, buf)

    def GetProgrammingInfo(self):
        buf = ffi.new('char[]', )
        lib.okPLL22150_GetProgrammingInfo(self._handle, buf)
        return ffi.string(buf).decode('ascii')


class PLL22393:
    def __init__(self):
        self._handle = lib.okPLL22393_Construct()

    def __del__(self):
        lib.okPLL22393_Destruct(self._handle)

    @property
    def h(self):
        return self._handle

    def SetCrystalLoad(self, capload):
        lib.okPLL22393_SetCrystalLoad(self._handle, capload)

    def SetReference(self, freq):
        lib.okPLL22393_SetReference(self._handle, freq)

    def GetReference(self):
        return lib.okPLL22393_GetReference(self._handle)

    def SetPLLParameters(self, n, p, q, enable):
        return lib.okPLL22393_SetPLLParameters(self._handle, n, p, q, enable)

    def SetPLLLF(self, n, lf):
        return lib.okPLL22393_SetPLLLF(self._handle, n, lf)

    def SetOutputDivider(self, n, div):
        return lib.okPLL22393_SetOutputDivider(self._handle, n, div)

    def SetOutputSource(self, n, clksrc):
        return lib.okPLL22393_SetOutputSource(self._handle, n, clksrc)

    def SetOutputEnable(self, n, enable):
        lib.okPLL22393_SetOutputEnable(self._handle, n, enable)

    def GetPLLP(self, n):
        return lib.okPLL22393_GetPLLP(self._handle, n)

    def GetPLLQ(self, n):
        return lib.okPLL22393_GetPLLQ(self._handle, n)

    def GetPLLFrequency(self, n):
        return lib.okPLL22393_GetPLLFrequency(self._handle, n)

    def GetOutputDivider(self, n):
        return lib.okPLL22393_GetOutputDivider(self._handle, n)

    def GetOutputSource(self, n):
        return lib.okPLL22393_GetOutputSource(self._handle, n)

    def GetOutputFrequency(self, n):
        return lib.okPLL22393_GetOutputFrequency(self._handle, n)

    def IsOutputEnabled(self, n):
        return lib.okPLL22393_IsOutputEnabled(self._handle, n) == lib.TRUE

    def IsPLLEnabled(self, n):
        return lib.okPLL22393_IsPLLEnabled(self._handle, n) == lib.TRUE

    def InitFromProgrammingInfo(self, info):
        buf = ffi.from_buffer(info)
        lib.okPLL22393_InitFromProgrammingInfo(self._handle, buf)

    def GetProgrammingInfo(self, info):
        buf = ffi.new('char[]', info)
        lib.okPLL22393_GetProgrammingInfo(self._handle, buf)
        return ffi.string(buf).decode('ascii')


class DeviceSettings:
    def __init__(self):
        self._handle = lib.okDeviceSettings_Construct()

    def __del__(self):
        lib.okDeviceSettings_Destruct(self._handle)

    @property
    def h(self):
        return self._handle

    def GetString(self, key):
        length = 256
        buf = ffi.new('char[]', length)
        lib.okDeviceSettings_GetString(self._handle, key.encode(), length, buf)
        return ffi.string(buf).decode()

    def GetInt(self, key):
        value = ffi.new('uint32_t *')
        lib.okDeviceSettings_GetInt(self._handle, key.encode(), value)
        return int(value)

    def SetString(self, key, value):
        err = lib.okDeviceSettings_SetString(self._handle, key.encode(), value.encode())
        return check(err)

    def SetInt(self, key, value):
        err = lib.okDeviceSettings_SetInt(self._handle, key.encode(), value)
        return check(err)

    def Delete(self, key):
        err = lib.okDeviceSettings_Delete(self._handle, key.encode())
        return check(err)

    def Save(self):
        err = lib.okDeviceSettings_Save(self._handle)
        return check(err)


class DeviceSensors:
    def __init__(self):
        self._handle = lib.okDeviceSensors_Construct()

    def __del__(self):
        lib.okDeviceSensors_Destruct(self._handle)

    @property
    def h(self):
        return self._handle

    def GetSensorCount(self):
        return lib.okDeviceSensors_GetSensorCount(self._handle)

    def GetSensor(self, n):
        return lib.okDeviceSensors_GetSensor(self._handle, n)


class Firmware:
    def __init__(self, handle):
        self._handle = handle

    def PerformTasks(self, serial, callback, arg):
        return lib.okFirmware_PerformTasks(self._handle, serial.encode(), callback, arg)


class FirmwarePackage:
    def __init__(self, filename):
        self._handle = lib.okFirmwarePackage_Load(filename)

    def __del__(self):
        lib.okFirmwarePackage_Destruct(self._handle)

    def GetFirmwareCount(self):
        return lib.okFirmwarePackage_GetFirmwareCount(self._handle);

    def GetFirmware(self, num):
        fw = lib.okFirmwarePackage_GetFirmware(self._handle, num)
        return Firmware(fw)

class FrontPanelManager:
    def __init__(self, realm):
        self._handle = lib.okFrontPanelManager_Construct(self, realm)

    def __del__(self):
        lib.okFrontPanelManager_Destruct(self._handle)

    def StartMonitoring(self):
        lib.okFrontPanelManager_StartMonitoring(self._handle)

    def Open(self, serial):
        fp_handle = lib.okFrontPanelManager_Open(self._handle, serial.encode('ascii'))
        return FrontPanel(fp_handle)

class FrontPanelDevices:
    def __init__(self, realm):
        self._handle = lib.okFrontPanelDevices_Construct(realm.encode('ascii'))

    def __del__(self):
        lib.okFrontPanelDevices_Destruct(self._handle)

    def GetCount(self):
        return lib.okFrontPanelDevices_GetCount(self._handle)

    def GetSerial(self, num):
        buf = ffi.new('char[]', lib.OK_MAX_SERIALNUMBER_LENGTH)
        lib.okFrontPanelDevices_GetSerial(self._handle, num, buf)
        return ffi.string(buf).decode('ascii')

    def Open(self, serial):
        fp_handle = lib.okFrontPanelDevices_Open(self._handle, serial.encode('ascii'))
        return FrontPanel(fp_handle)

def check(error_code):
    """ Check routine for the received error codes.
    @param func_val int: return error code of the called function.
    @return int: pass the error code further so that other functions have
                 the possibility to use it.
    Each called function in the lib.has an 32-bit return integer, which
    indicates, whether the function was called and finished successfully
    (then func_val = 0) or if any error has occured (func_val < 0). The
    errorcode, which corresponds to the return value can be looked up in
    the class ok_ErrorCode.
    """
    if error_code < 0:
        msg = FrontPanel.GetErrorString(error_code)
        print(
            'Error in Opal Kelly okFrontPanel with errorcode {0}: '
            '{1}'.format(error_code, msg),
            file=sys.stderr)
    return error_code


class FrontPanel:
    """Main wrapper class for controlling Opal Kelly FPGA boards."""

    def __init__(self, handle=None):
        if handle is None:
            self._handle = lib.okFrontPanel_Construct()
        else:
            self._handle = handle

    def __del__(self):
        lib.okFrontPanel_Destruct(self._handle)

    @staticmethod
    def GetErrorString(error_code):
        """int okFrontPanel_GetErrorString(int ec, char *buf, int length);"""
        actlen = lib.okFrontPanel_GetErrorString(error_code, ffi.NULL, 0)
        buf = ffi.new('char[]', int(actlen))
        lib.okFrontPanel_GetErrorString(error_code, buf, actlen + 1)
        msg = ffi.string(buf, actlen + 1).decode('ascii')
        return msg

    @staticmethod
    def AddCustomDevice(matchInfo, devInfo):
        err = lib.okFrontPanel_AddCustomDevice(matchInfo, devInfo)
        return check(err)

    @staticmethod
    def RemoveCustomDevice(self, productID):
        err = lib.okFrontPanel_RemoveCustomDevice(productID)
        return check(err)

    def WriteI2C(self, addr, data):
        length = len(data)
        err = lib.okFrontPanel_WriteI2C(self._handle, addr, length, data)
        return check(err)

    def ReadI2C(self, addr, length):
        data = ffi.new('unsigned char[]', length)
        err = lib.okFrontPanel_ReadI2C(self._handle, addr, length, data)
        return ffi.string(data)

    def FlashEraseSector(self, address):
        err = lib.okFrontPanel_FlashEraseSector(self._handle, address)
        return check(err)

    def FlashWrite(self, address, data):
        length = len(data)
        buf = ffi.from_buffer(data)
        err = lib.okFrontPanel_FlashWrite(self._handle, address, length, buf)
        return check(err)

    def FlashRead(self, address, length):
        buf = ffi.new('char[]', length)
        err = lib.okFrontPanel_FlashWrite(self._handle, address, length, buf)
        return ffi.string(buf)

    def GetFPGAResetProfile(self, method):
        profile = ffi.new('okTFPGAResetProfile *')
        size = ffi.sizeof(profile)
        err = lib.okFrontPanel_GetFPGAResetProfileWithSize(self._handle, method, profile, size)
        return profile

    def SetFPGAResetProfile(self, method, profile):
        assert ffi.typeof(profile) is ffi.typeof('okTFPGAResetProfile')
        size = ffi.sizeof(profile)
        err = lib.okFrontPanel_SetFPGAResetProfileWithSize(method, profile, size)
        return check(err)

    def ReadRegister(self, addr):
        data = ffi.new('uint32_t *')
        lib.okFrontPanel_ReadRegister(self._handle, addr, data)
        return int(data)

    def ReadRegisters(self, regs):
        num = len(regs)
        regbuf = ffi.new('okTRegisterEntry[]', num)
        lib.okFrontPanel_ReadRegisters(self._handle, num, regbuf)

    def WriteRegister(self, addr, data):
        err = lib.okFrontPanel_WriteRegister(self._handle, addr, data)
        return check(err)

    def WriteRegisters(self, regs):
        num = len(regs)
        err = lib.okFrontPanel_WriteRegisters(self._handle, num, regs)
        return check(err)

    def GetHostInterfaceWidth(self):
        return int(lib.okFrontPanel_GetHostInterfaceWidth(self._handle))

    def IsHighSpeed(self):
        return lib.okFrontPanel_IsHighSpeed(self._handle) == lib.TRUE

    def GetBoardModel(self):
        return lib.okFrontPanel_GetBoardModel(self._handle)

    def GetBoardModelString(self, model):
        buf = ffi.new('char[]', lib.OK_MAX_BOARD_MODEL_STRING_LENGTH)
        lib.okFrontPanel_GetBoardModelString(self._handle, model, buf)
        return ffi.string(buf).decode('ascii')

    def GetDeviceCount(self):
        """int okFrontPanel_GetDeviceCount(okFrontPanel_HANDLE hnd);"""
        return int(lib.okFrontPanel_GetDeviceCount(self._handle))

    def GetDeviceListModel(self, num):
        return lib.okFrontPanel_GetDeviceListModel(self._handle, num)

    def GetDeviceListSerial(self, num):
        buf = ffi.new('char[]', lib.OK_MAX_SERIALNUMBER_LENGTH)
        lib.okFrontPanel_GetDeviceListSerial(self._handle, num, buf)
        return ffi.string(buf).decode('ascii')

    def OpenBySerial(self, serial=""):
        err = lib.okFrontPanel_OpenBySerial(self._handle, serial.encode())
        return check(err)

    def IsOpen(self):
        return lib.okFrontPanel_IsOpen(self._handle) == lib.TRUE

    def EnableAsynchronousTransfers(self, enable):
        lib.okFrontPanel_EnableAsynchronousTransfers(
            self._handle,
            lib.TRUE if enable else lib.FALSE)

    def SetBTPipePollingInterval(self, interval):
        err = lib.okFrontPanel_SetBTPipePollingInterval(self._handle, interval)
        return check(err)

    def SetTimeout(self, timeout):
        lib.okFrontPanel_SetTimeout(self._handle, timeout)

    def GetDeviceMajorVersion(self):
        return int(lib.okFrontPanel_GetDeviceMajorVersion(self._handle))

    def GetDeviceMinorVersion(self):
        return int(lib.okFrontPanel_GetDeviceMinorVersion(self._handle))

    def ResetFPGA(self):
        err = lib.okFrontPanel_ResetFPGA(self._handle)
        return check(err)

    def Close(self):
        """void okFrontPanel_Close(okFrontPanel_HANDLE hnd);"""
        lib.okFrontPanel_Close(self._handle)

    def GetSerialNumber(self):
        buf = ffi.new('char[]', lib.OK_MAX_SERIALNUMBER_LENGTH)
        lib.okFrontPanel_GetSerialNumber(self._handle, buf)
        return ffi.string(buf).decode('ascii')

    def GetDeviceSensors(self):
        sensors = DeviceSensors()
        err = lib.okFrontPanel_GetDeviceSensors(self._handle, sensors.h)

    def GetDeviceSettings(self):
        settings = DeviceSettings()
        err = lib.okFrontPanel_GetDeviceSettings(self._handle, settings.h)

    def GetDeviceInfo(self):
        info = ffi.new('okTDeviceInfo *')
        size = ffi.sizeof(info)
        err = lib.okFrontPanel_GetDeviceInfoWithSize(self._handle, info, size)
        return info

    def GetDeviceID(self):
        buf = ffi.new('char[]', lib.OK_MAX_DEVICEID_LENGTH)
        lib.okFrontPanel_GetDeviceID(self._handle, buf)
        return ffi.string(buf).decode('ascii')

    def SetDeviceID(self, strID):
        return lib.okFrontPanel_SetDeviceID(self._handle, strID.encode())

    def ConfigureFPGA(self, strFilename):
        """ok_ErrorCode okFrontPanel_ConfigureFPGA(okFrontPanel_HANDLE hnd, const char *strFilename);"""
        err = lib.okFrontPanel_ConfigureFPGA(self._handle, strFilename.encode())
        return check(err)

    def ConfigureFPGAWithReset(self, strFilename, reset):
        err = lib.okFrontPanel_ConfigureFPGAWithReset(self._handle, strFilename, reset)
        return check(err)

    def ConfigureFPGAFromMemory(self, data):
        length = len(data)
        data_ref = ffi.from_buffer(data)
        err = lib.okFrontPanel_ConfigureFPGAFromMemory(self._handle, data_ref, length)
        return check(err)

    def ConfigureFPGAFromMemoryWithReset(self, data, reset):
        length = len(data)
        data_ref = ffi.from_buffer(data)
        err = lib.okFrontPanel_ConfigureFPGAFromMemoryWithReset(self._handle, data_ref, length, reset)
        return check(err)

    def ConfigureFPGAFromFlash(self, configIndex):
        err = lib.okFrontPanel_ConfigureFPGAFromFlash(self._handle, configIndex)
        return check(err)

    def GetPLL22150Configuration(self):
        pll = PLL22150()
        err = lib.okFrontPanel_GetPLL22150Configuration(self._handle, pll.h)
        return pll

    def SetPLL22150Configuration(self, pll):
        err = lib.okFrontPanel_SetPLL22150Configuration(self._handle, pll.h)
        return check(err)

    def GetEepromPLL22150Configuration(self):
        pll = PLL22150()
        err = lib.okFrontPanel_GetEepromPLL22150Configuration(self._handle, pll.h)
        return pll

    def SetEepromPLL22150Configuration(self, pll):
        err = lib.okFrontPanel_SetEepromPLL22150Configuration(self._handle, pll.h)
        return check(err)

    def GetPLL22393Configuration(self):
        pll = PLL22393()
        err = lib.okFrontPanel_GetPLL22393Configuration(self._handle, pll.h)
        return pll

    def SetPLL22393Configuration(self, pll):
        err = lib.okFrontPanel_SetPLL22393Configuration(self._handle, pll.h)
        return check(err)

    def GetEepromPLL22393Configuration(self):
        pll = PLL22393()
        err = lib.okFrontPanel_GetEepromPLL22393Configuration(self._handle, pll.h)
        return pll

    def SetEepromPLL22393Configuration(self, pll):
        err = lib.okFrontPanel_SetEepromPLL22393Configuration(self._handle, pll.h)
        return check(err)

    def LoadDefaultPLLConfiguration(self):
        return lib.okFrontPanel_LoadDefaultPLLConfiguration(self._handle)

    def IsFrontPanelEnabled(self):
        """Bool okFrontPanel_IsFrontPanelEnabled(okFrontPanel_HANDLE hnd);"""
        return lib.okFrontPanel_IsFrontPanelEnabled(self._handle) == lib.TRUE

    def IsFrontPanel3Supported(self):
        return lib.okFrontPanel_IsFrontPanel3Supported(self._handle) == lib.TRUE

    def UpdateWireIns(self):
        """void okFrontPanel_UpdateWireIns(okFrontPanel_HANDLE hnd);"""
        lib.okFrontPanel_UpdateWireIns(self._handle)

    def GetWireInValue(self, epAddr):
        """ok_ErrorCode okFrontPanel_GetWireInValue(okFrontPanel_HANDLE hnd, int epAddr, UINT32 *val);"""
        val = ffi.new('uint32_t *')
        lib.okFrontPanel_GetWireInValue(self._handle, epAddr, val)
        return val

    def SetWireInValue(self, ep, val, mask=0xffffffff):
        """ok_ErrorCode okFrontPanel_SetWireInValue(okFrontPanel_HANDLE hnd, int ep, unsigned long val, unsigned long mask);"""
        err = lib.okFrontPanel_SetWireInValue(self._handle, ep, val, mask)
        return check(err)

    def UpdateWireOuts(self):
        """void okFrontPanel_UpdateWireOuts(okFrontPanel_HANDLE hnd);"""
        lib.okFrontPanel_UpdateWireOuts(self._handle)

    def GetWireOutValue(self, epAddr):
        """unsigned long okFrontPanel_GetWireOutValue(okFrontPanel_HANDLE hnd, int epAddr);"""
        return lib.okFrontPanel_GetWireOutValue(self._handle, epAddr)

    def ActivateTriggerIn(self, epAddr, bit):
        err = lib.okFrontPanel_ActivateTriggerIn(self._handle, epAddr, bit)
        return check(err)

    def UpdateTriggerOuts(self):
        """void okFrontPanel_UpdateTriggerOuts(okFrontPanel_HANDLE hnd);"""
        lib.okFrontPanel_UpdateTriggerOuts(self._handle)

    def IsTriggered(self, epAddr, mask):
        return lib.okFrontPanel_IsTriggered(self._handle, epAddr, mask) == lib.TRUE

    def GetLastTransferLength(self):
        return lib.okFrontPanel_GetLastTransferLength(self._handle)

    def WriteToPipeIn(self, epAddr, data):
        length = len(data)
        data_ref = ffi.from_buffer(data)
        err = lib.okFrontPanel_WriteToPipeIn(self._handle, epAddr, length, data_ref)
        return check(err)

    def ReadFromPipeOut(self, epAddr, data):
        length = len(data)
        data_ref = ffi.from_buffer(data)
        err = lib.okFrontPanel_ReadFromPipeOut(self._handle, epAddr, length, data_ref)
        return check(err)

    def WriteToBlockPipeIn(self, epAddr, blockSize, data):
        length = len(data)
        data_ref = ffi.from_buffer(data)
        err = lib.okFrontPanel_WriteToBlockPipeIn(self._handle, epAddr, blockSize, length, data_ref)
        return check(err)

    def ReadFromBlockPipeOut(self, epAddr, blockSize, data):
        """ long DLL_ENTRY okFrontPanel_ReadFromBlockPipeOut(okFrontPanel_HANDLE hnd, int epAddr, int blockSize, long length, unsigned char *data);"""
        length = len(data)
        data_ref = ffi.from_buffer(data)
        err = lib.okFrontPanel_ReadFromBlockPipeOut(self._handle, epAddr, blockSize, length, data_ref)
        return check(err)
