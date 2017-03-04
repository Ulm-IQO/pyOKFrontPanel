# pyOKFrontPanel
Python CFFI wrapper for the Opal Kelly FrontPanel FPGA interface.

## Prerequisites
To use this module, you need to have the Opal Kelly FrontPanel C interface installed correctly
so your C compiler can find the okFrontPanel shared library and the `okFrontPanelDLL.h` header.

### Windows
Get Opal Kelly FrontPanel, at least v4.5.6 and install it.

Get the visual C compiler from http://landinghub.visualstudio.com/visual-cpp-build-tools and install it.

From the FrontPanel installation folder, copy `API\include\okFrontPanelDLL.h` to (please fill in)
and copy `API\lib\okFrontPanel.lib` to (please fill in).

### Linux
FrontPanel for Linux is typically installed in `/usr/local/`, so make sure that your C compiler can find header files in `/usr/local/include` and that your linker can find dynamic libraries in `/usr/local/lib`.

Also make sure that you have installed the header files for the Python version that you are trying to use the FrontPanel with (in Debian-based distributions, this package is called python#.#-dev).
