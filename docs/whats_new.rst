.. _whats_new:

What's New
==========

This information applies to the
`tkeskita/bvtknodes <https://github.com/tkeskita/BVtkNodes>`_ version.

Version 0.11
------------

- 2024-07-19: BVTKNodes upgrade to Blender LTS version 4.2
  (Python 3.11) required no class or VTK changes.

- 2023-12-31: Motion Blur is available in VTK To Blender Mesh
  Node. Mesh motion blur is implemented using Blender Shape
  Keys, based on mesh point transformation by a vector point field.

Version 0.10
------------

- 2023-08-19: Resurrected VTK To Blender Volume Node. This was possible since
  pyopenvdb is now included in Blender 3.6 by default.

- 2023-08-18: Upgrade to Blender LTS version 3.6 (Python 3.10) and VTK 9.2.6.
  The previous Blender LTS version 3.3 (Python 3.10) still works as well
  with VTK 9.2.6. This upgrade required no class changes.

- 2023-06-09: Fixed a bug where negative scalar values were colored incorrectly
  with Color Mapper node (absolute values of data was shown).

- 2023-01-21: Upgrade to Blender LTS version 3.3 (Python 3.10) and VTK 9.2.2.
  The previous Blender LTS version 2.93 (Python 3.9) still works as well
  with VTK 9.2.2.

Version 0.9
-----------

- 2022-07-28: Color Mapper Node now supports vector arrays as well as
  scalar arrays as input. For vectors, magnitude of the vector is used
  for the color scale.

- 2022-06-12: Changed Custom Filter to fix it's tree import/export.

- 2022-06-05: Fixed importing of colors for Color Ramp node.

- 2022-05-28: Fixed Property listing bug for Blender 2.93 (properties were not
  shown in the Properties tab).

- 2022-05-28: Added VTK To Blender Image Node to convert vtkImageData
  to a Blender Image.

Version 0.8 (2022-01-16)
------------------------

- Upgrade to Blender LTS version 2.93 and VTK 9.1.0. The previous
  Blender LTS version 2.83 still works as well with VTK 9.1.0.

Version 0.7 (2021-09-18)
------------------------

- Supported Blender LTS version 2.83 and VTK 9.0.1.
- New node update system, where VTK updates are independent of node
  editing actions. User has now option to change **Update Mode** in
  the Inspect Panel, which determines when changes in nodes are
  updated to VTK objects. Most useful options include *No Automatic
  Updates* and *Update All Automatically*.

- Nodes have now :ref:`node_status` information, which is shown by node colors.

- Values of dynamic enumeration lists are stored in string properties,
  so that it is possible to pre-define whole node trees without need to
  run updates on nodes. This allows full pre-definition of node trees
  e.g. for JSON imports.

- several new *cubeflow* node tree examples (in
  :ref:`json_importexport` Tab) available for :ref:`ug_nodes`.

- Development for this release was made in 
  `pull request #46 <https://github.com/tkeskita/BVtkNodes/pull/46>`_.


Previous versions
-----------------

- A testing framework helps developers catch regression bugs.

- :ref:`global_time_keeper` node allows animation of many node properties
  by Blender's Keyframes feature.

- Improved Custom Code editing.

- Matplotlib color maps are available as presets in Color Ramp node.

- Several bug fixes and small usability improvements.

- More information in `pull requests at github <https://github.com/tkeskita/BVtkNodes/pulls?q=is%3Apr>`_.
