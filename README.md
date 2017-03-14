# pyOKFrontPanel
Python CFFI wrapper for the Opal Kelly FrontPanel FPGA interface.

## Prerequisites
To use this module, you need to have the Opal Kelly FrontPanel C interface installed correctly
so your C compiler can find the okFrontPanel shared library and the `okFrontPanelDLL.h` header.

### Windows
Get Opal Kelly FrontPanel, at least v4.5.6 and install it.

Get the visual C compiler from http://landinghub.visualstudio.com/visual-cpp-build-tools and install it.

pyOKFrontPanel should find your FrontPanel installation from the `OKFP_SDK` environment variable.

### Linux
FrontPanel for Linux is typically installed in `/usr/local/`, so make sure that your C compiler can find header files in `/usr/local/include` and that your linker can find dynamic libraries in `/usr/local/lib`.

Also make sure that you have installed the header files for the Python version that you are trying to use the FrontPanel with (in Debian-based distributions, this package is called python#.#-dev).

# API status


## PLL22150
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
|  -----------  |
|  GetString    |
|  GetInt       |
|  SetString    |
|  SetInt       |
|  Delete       |
|  Save         |

## DeviceSensors
|  ---------------  |
|  GetSensorCount   |
|  GetSensor        |

## Firmware
|  -----------  |
|  PerformTasks |


## FirmawarePackage
|  ---------------  |
|  GetFirmwareCount |
|  GetFirmware      |

## FrontPanelManager
|  ---------------  |
|  StartMonitoring  |
|  Open             |

## FrontPanelDevices
|  -----------  |
|  GetCount     |
|  GetSerial    |
|  Open         |

## FrontPanel
|  -------------------------------  |  ---------------  |
|  GetErrorString                   |       
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
|  GetBoardModel                    |
|  GetBoardModelString              |
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
|  UpdateWireOuts                   |
|  GetWireOutValue                  | works             |
|  ActivateTriggerIn                | works             |
|  UpdateTriggerOuts                |
|  IsTriggered                      |
|  GetLastTransferLength            |
|  WriteToPipeIn                    |
|  ReadFromPipeOut                  |
|  WriteToBlockPipeIn               |
|  ReadFromBlockPipeOut             | works             |

