# pyOKFrontPanel
Python CFFI wrapper for the Opal Kelly FrontPanel FPGA interface.

## Prerequisites
To use this module, you need to have the Opal Kelly FrontPanel C interface installed correctly so your C compiler can find the okFrontPanel shared library and the `okFrontPanelDLL.h` header.

You have [to sign up](https://pins.opalkelly.com/users/sign_in) at OpalKelly to be able to download okFrontPanel.

### Windows
Get Opal Kelly FrontPanel, at least **v4.5.6** and install it.

Get the [Visual C compiler](http://landinghub.visualstudio.com/visual-cpp-build-tools) and install it.

pyOKFrontPanel should find your FrontPanel installation from the `OKFP_SDK` environment variable.

### Linux
FrontPanel for Linux is typically installed in `/usr/local/`, so make sure that your C compiler can find header files in `/usr/local/include` and that your linker can find dynamic libraries in `/usr/local/lib`.

Also make sure that you have installed the header files for the Python version that you are trying to use the FrontPanel with (in Debian-based distributions, this package is called python#.#-dev).


## Installation via pip

If the prerequisites are fulfilled for either Windows or Linux based systems, then you can install the OpalKelly Python Wrapper via

    pip install pyOKFrontPanel

which will trigger the compilation of OpalKelly Wrapper together with the header file (`okFrontPanelDLL.h`) of the front panel by using the mentioned C compiler above.

# API status


## PLL22150

|  Function                 |
|  -----------------------  |
|  SetCrystalLoad           |
|  SetReference             |
|  GetReference             |
|  SetVCOParameters         |
|  GetVCOP                  |
|  GetVCOQ                  |
|  GetVCOFrequency          |
|  SetDiv1                  |
|  SetDiv2                  |
|  GetDiv1Source            |
|  GetDiv2Source            |
|  GetDiv1Divider           |
|  GetDiv2Divider           |
|  SetOutputSource          |
|  SetOutputEnable          |
|  GetOutputSource          |
|  GetOutputFrequency       |
|  IsOutputEnabled          |
|  InitFromProgrammingInfo  |
|  GetProgrammingInfo       |

## PLL22393

|  Function                 |
|  -----------------------  |
|  SetCrystalLoad           |
|  SetReference             |
|  GetReference             |
|  SetPLLParameters         |
|  SetPLLLF                 |
|  SetOutputDivider         |
|  SetOutputSource          |
|  SetOutputEnable          |
|  GetPLLP                  |
|  GetPLLQ                  |
|  GetPLLFrequency          |
|  GetOutputDivider         |
|  GetOutputSource          |
|  GetOutputFrequency       |
|  IsOutputEnabled          |
|  IsPLLEnabled             |
|  InitFromProgrammingInfo  |
|  GetProgrammingInfo       |

## DeviceSettings

|  Function     |
|  -----------  |
|  GetString    |
|  GetInt       |
|  SetString    |
|  SetInt       |
|  Delete       |
|  Save         |

## DeviceSensors

|  Function         |
|  ---------------  |
|  GetSensorCount   |
|  GetSensor        |

## Firmware

|  Function     |
|  -----------  |
|  PerformTasks |


## FirmawarePackage

|  Function         |
|  ---------------  |
|  GetFirmwareCount |
|  GetFirmware      |

## FrontPanelManager

|  Function         |
|  ---------------  |
|  StartMonitoring  |
|  Open             |

## FrontPanelDevices

|  Function     |
|  -----------  |
|  GetCount     |
|  GetSerial    |
|  Open         |

## FrontPanel

|  Function                         |   status          |
|  -------------------------------  |  ---------------  |
|  GetErrorString                   |  probably works   |
|  AddCustomDevice                  |
|  RemoveCustomDevice               |
|  WriteI2C                         |
|  ReadI2C                          |
|  FlashEraseSector                 |
|  FlashWrite                       |
|  FlashRead                        |
|  GetFPGAResetProfile              |
|  SetFPGAResetProfile              |
|  ReadRegister                     |
|  ReadRegisters                    |
|  WriteRegister                    |
|  WriteRegisters                   |
|  GetHostInterfaceWidth            |
|  IsHighSpeed                      | works             |
|  GetBoardModel                    | works             |
|  GetBoardModelString              | works             |
|  GetDeviceCount                   | works             |
|  GetDeviceListModel               | works             |
|  GetDeviceListSerial              | works             |
|  OpenBySerial                     | works             |
|  IsOpen                           | works             |
|  EnableAsynchronousTransfers      |
|  SetBTPipePollingInterval         |
|  SetTimeout                       |
|  GetDeviceMajorVersion            |
|  GetDeviceMinorVersion            |
|  ResetFPGA                        |
|  Close                            |
|  GetSerialNumber                  | works             |
|  GetDeviceSensors                 | 
|  GetDeviceSettings                |
|  GetDeviceInfo                    |
|  GetDeviceID                      |
|  SetDeviceID                      |
|  ConfigureFPGA                    | works             |
|  ConfigureFPGAWithReset           |
|  ConfigureFPGAFromMemory          |
|  ConfigureFPGAFromMemoryWithReset |
|  ConfigureFPGAFromFlash           |
|  GetPLL22150Configuration         |
|  SetPLL22150Configuration         |
|  GetEepromPLL22150Configuration   |
|  SetEepromPLL22150Configuration   |
|  GetPLL22393Configuration         |
|  SetPLL22393Configuration         |
|  GetEepromPLL22393Configuration   |
|  SetEepromPLL22393Configuration   |
|  LoadDefaultPLLConfiguration      |
|  IsFrontPanelEnabled              | works             |
|  IsFrontPanel3Supported           | works probably    |
|  UpdateWireIns                    | works             |
|  GetWireInValue                   |
|  SetWireInValue                   | works             |
|  UpdateWireOuts                   | works             |
|  GetWireOutValue                  | works             |
|  ActivateTriggerIn                | works             |
|  UpdateTriggerOuts                |
|  IsTriggered                      |
|  GetLastTransferLength            |
|  WriteToPipeIn                    |
|  ReadFromPipeOut                  |
|  WriteToBlockPipeIn               | works             |
|  ReadFromBlockPipeOut             | works             |

