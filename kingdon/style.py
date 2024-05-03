"""
contains colormaps for your convenience with graphing. 

Example::

    from kingdon.colormaps import colormaps
    cm = colormaps['Set2']

"""


"""
This file was generated with the following:

```
import matplotlib.pyplot as plt
from matplotlib.colors import to_hex
# Generate a list of colors from the colormap
def colors(name='Set2', N=None):
    cmap = plt.get_cmap(name)
    if N is None:
        N = cmap.N
    return [int(to_hex(cmap(i / N))[1:],16) for i in range(N)]

cmap_names = [name for name in plt.colormaps() if not name.endswith('_r')]
cmaps = {name:colors(name=name) for name in cmap_names if len(colors(name=name))<30 }
```


"""
colormaps = {'Accent': [8374655,
  12496596,
  16629894,
  16777113,
  3697840,
  15729279,
  12540695,
  6710886],
 'Dark2': [1810039,
  14245634,
  7696563,
  15149450,
  6727198,
  15117058,
  10909213,
  6710886],
 'Paired': [10931939,
  2062516,
  11722634,
  3383340,
  16489113,
  14883356,
  16629615,
  16744192,
  13284054,
  6962586,
  16777113,
  11622696],
 'Pastel1': [16495790,
  11783651,
  13429701,
  14601188,
  16701862,
  16777164,
  15063229,
  16636652,
  15921906],
 'Pastel2': [11789005,
  16633260,
  13358568,
  16042724,
  15136201,
  16773806,
  15852236,
  13421772],
 'Set1': [14948892,
  3636920,
  5091146,
  9981603,
  16744192,
  16777011,
  10901032,
  16220607,
  10066329],
 'Set2': [6734501,
  16551266,
  9281739,
  15174339,
  10934356,
  16767279,
  15058068,
  11776947],
 'Set3': [9294791,
  16777139,
  12499674,
  16482418,
  8434131,
  16626786,
  11787881,
  16567781,
  14277081,
  12353725,
  13429701,
  16772463],
 'tab10': [2062260,
  16744206,
  2924588,
  14034728,
  9725885,
  9197131,
  14907330,
  8355711,
  12369186,
  1556175],
 'tab20': [2062260,
  11454440,
  16744206,
  16759672,
  2924588,
  10018698,
  14034728,
  16750742,
  9725885,
  12955861,
  9197131,
  12885140,
  14907330,
  16234194,
  8355711,
  13092807,
  12369186,
  14408589,
  1556175,
  10410725],
 'tab20b': [3750777,
  5395619,
  7040719,
  10264286,
  6519097,
  9216594,
  11915115,
  13556636,
  9202993,
  12426809,
  15186514,
  15190932,
  8666169,
  11356490,
  14049643,
  15177372,
  8077683,
  10834324,
  13528509,
  14589654],
 'tab20c': [3244733,
  7057110,
  10406625,
  13032431,
  15095053,
  16616764,
  16625259,
  16634018,
  3253076,
  7652470,
  10607003,
  13101504,
  7695281,
  10394312,
  12369372,
  14342891,
  6513507,
  9868950,
  12434877,
  14277081]}
