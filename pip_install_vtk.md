# Installation of VTK in Blender 3.6 Python via Pip

Note: These instructions also likely work for other Blender and VTK
versions, but the versions applied below are the ones used as an example.

# On Windows

Run CMD.EXE as administrator and run commands
```
cd C:\Program Files\Blender Foundation\Blender\3.6\python\bin
.\python.exe -m ensurepip
.\python.exe -m pip install vtk==9.2.6
```
or if you need to install newest (possibly unsupported) version of vtk, replace last command with
```
.\python.exe -m pip install vtk
```

# On Linux

Run on normal terminal commands
```
cd /path/to/blender-3.6/3.6/python/bin
./python3.10 -m ensurepip
./python3.10 -m pip install vtk==9.2.6
```
or if you need to install newest (possibly unsupported) version of vtk, replace last command with
```
./python3.10 -m pip install vtk
```

# Testing

You can test if VTK is found in 
[Blender Python Console](https://docs.blender.org/manual/en/latest/editors/python_console.html)
(by default located in the Scripting 
[workspace](https://docs.blender.org/manual/en/latest/interface/window_system/workspaces.html)
) with commands

```
import vtk
vtk.vtkVersion().GetVTKVersion()
```

which should return VTK version number that was installed.


# Workaround for VTK Import Error on Linux

Blender 2.93 and newer has an issue on Linux, where running `import vtk` command in Blender Python Console raises error

```
ImportError: /path/to/blender/X.Y/python/lib/python3.Z/site-packages/vtkmodules/libvtkPythonInterpreter-9.0.so: undefined symbol: Py_Main
```

Workaround for this issue is to edit file
`/path/to/blender/X.Y/python/lib/pythonZ/site-packages/vtkmodules/all.py`
and disable import of `vtkRenderingMatplotlib` by commenting out the line like so:

```
# from .vtkRenderingMatplotlib import *
```

**Note!** Blender 3.3 and newer need the same modification of file
`/path/to/blender/X.Y/python/lib/pythonZ/site-packages/vtk.py`:

```
# from .vtkRenderingMatplotlib import *
```
