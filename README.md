# vivado-boilerplate

This is an example project to demonstrate features of SCons-based build system for FPGA. Xilinx Vivado and Mentor Questa are supported for now.

## Features
* Unified configuration subsystem based on [YAML format](https://en.wikipedia.org/wiki/YAML).
* Arbitrary count of build variants (this example project offers three build variants for AC701, 7A35T and 7A50T evaluation boards).
* Fully customizable project layout and build scenarios with construction environment variables and reach set of builders.
* Many different targets such as:
    * IP Create Scripts.
    * IP Synthesize Scripts.
    * Create IPs.                                                  
    * Out-of-context synthesis of IPs.
    * Create IP simulation library scripts.
    * Compile IP simulation library.
    * Generate HDL headers files with specified parameters.
    * Generate Tcl scripts with specified parameters.
    * Compile work library.
    * Launch Questa GUI in destination dir with tool script loaded.
    * Launch simulation run in non-GUI mode (console run).
    * Create Vivado Project accoring to specified parameters.
    * Synthesize Vivado Project in non-GUI (console) mode.
    * Implement Vivado Project in non-GUI (console) mode.
    * Open Vivado Project in GUI mode.
* All targets are built by dependencies.
* Convenient help info (command line option `-h`)
* Comprehensive debug features (options --debug=exlplain, --tree=all, etc).

## Usage expamples

Commands can be invoked from any directory within project directory tree.

Display available targets:

```
scons -s -D -h
```

Create Vivado project:

```
scons -s -D prj
```

Synthesize Vivado project for variant 7A50T:

```
scons -s -D variant=7a50t prjsyn
```

Compile simulator work library (this is a default target):

```
scons -s -D
```

Changing any parameter file that is a dependency for some target[s] raises rebuild for all targes in dependency chain.
