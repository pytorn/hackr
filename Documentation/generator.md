# `hackr.generator`

`hackr.generator` exposes functions that create data. It is structured as an `__init__.py` file and other modules.

Any method you would like to expose in the `hackr.generator` namespace can be added to `hackr/generator/__init__.py`. Any grouping can be added by making a new `.py` file (like `hackr/generator/networking.py`) and importing it into `__init__.py` with:

```python
from internet import *
```

After importing the namespace, you can use it's methods with `hackr.generator.internet.<your method here>`.
