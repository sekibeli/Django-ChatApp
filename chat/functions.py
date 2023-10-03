def pick_random_image():
    return 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAYAAABw4pVUAAAACXBIWXMAAAsTAAALEwEAmpwYAAASUklEQVR4nO1dd1BU2ZrvzbtVu1tbtX+8erv7tnar3u57I5KbprtBlDGgBJEk0A0IZoIBRBkxjgFFUUFlxQgGwDFgzoExcBuUmXEcZ0YxgMi9KNwLZlR0flvfxSY3dGMjoPdX9RVN09x7zvmd73zhfOe2TCZBggQJEiRIkCBBggQJEiRIkCBBggQJEiT0KuwB/qqompMzAjtLx7NHGIH9RcdzNTqefcvw3Gt6zQjszzqBO6AT2K911ZWDjqPk73q63Z8cdFUP/ofh2XRx8AUOJgnP1TI8t5GpYu16uh99HrqaB1Y02xmefWcyEe2Sw564XFth09P96nMoBv5Gx3PzxGXIHES0JKVeJ3Br8ktL/76n+9knoKut/C8dz31vdiJaCcNz12gp7On+9mroeO4LhufKu5uMZvZFKBAq1D3d716JgmrOgeE5/qOR0SjsM4avVPR0/3sViquqfs8IbOXHJKLubT3aQYnsc0c+8NcMz138+JrRevlirzPl5f8g+9yhE7ikj6gBbUCfa/X5ks/do3rV49rRpCVvP+s4Rcdz2R/LVrxopgntaEVn+PS1pkiotDAUgV94cAfbj+zH0uVLEBc9EWO8hkMzeCBGOdqLQq/pvbjoSViavBTbj+aJ/2MOAhme/a2gtsJW9rmB4bnlLUiouIsN2ZmIDAvGCEsLuFl8gUCVFWaOtEZqhA22RNkhN65BNkfaYU2EDeK9bBCotBQ/S/8TNSYYGTlZuMDeM1pz9NrSaunaIPucAOAvGJ4tpc6fu3cTSSuXiTN/uGU/zPCyweFEOe5vUaL+oJNRUrZFiUOJcsR52WB4/y/go5RjWcoy5JeVdNGWcDU3cONvZX0d1InC6sovGZ5dyfDcJZ3A3WYE9jkjcC90PHef3FvSDIZnpzPVFVi/bZNIhJetBdaPt0FFpspoEgxJRaZSvJanTX/4qhyQvn0L6F4mL1013EBZX0X+o0f/qBPYBB3PVhnT2VM3f8Qkjb84m1eE2aJql7rNwD7YpsKxuXKsHq/EDF81IgYroHGxh2aAPcYNUSDeV4m0CQocnycHm9WWyKqdKiSHkMb0w2TtaJy+9ZOJpLALZX0RBdXsKIbnqo3taPaZY/BRO0CjtsQPqYoWg1i7W41vZjpgwjBHBLkosTB+KrJ2bcfJgosounMTP1TcF0V36xecuHwB23ZkYUFcFEY7OWCimwL7E+SozW1JbvEqRwSrrOCnViD33HFTSMmT9bUIWyewq8krMbaTW/flwsPGEgne1hCym2b1sz1qbJmihL/SFl8nxOLMFR1K6+tQ9vaVUUKfPVNUgAUzYsRrZE1T4OmeJmL4HBVmeluL996at9tYb+uGrC8ZZZ3AbTVlCSAyRlhaIElji7q8phmsW6GE1kWOhbOm4/sHZUaTYEiK79/FwvgpCBloj6KVTRpYt98JS4JtxDYYQwppvayvQCdwa00hg5Ypmp1JGlu8OdAwQPRzU4wSGlcncXYbGuDvy0uxdl0qJoRoETzcDWEjvTBrWgxyD+zD3bpnBv+PljSNqxrbpiha3HNJkI3Ylk6XL557JesL0AmcuylkkAEnm0HLVF1e02xdHKLCtLBg3OAfGVyGiAhvlSPC42ciKisb04+cxLS8I5iYth5arRZBw4bg3HdFBkm5UV2JqVo/LNLIW9ybYhuyKZ0aep67zNRUeNGKIOuNKOT5fzZlA4nczUmaANGA623G6wNqfB2iwlfRE3Dn5VODZCz4ahaCA/wx4+xFJFy93q5EbcmCj7Maxy/lGySFtChhUjgWaRzw6j0p1dlqBKstRe+L4dnO+yFwpy7VsP8p621geDbRFO2gOINc2+beVHqUGrER2g6Xm8xd2xE4yhuzmGKDZOhlyu598BvghB8rKzokZUZEMNInNbWjeJVCdIn/b8dW4yaXwD4pqKn0lPWmmigK7owlgyJwipgpztAPwsVljggdOhC/Pq42OHi3ntXC11mNaYeOd0qGXqLnzMWyxQs7NPZ0zy0pM1u4xMu0NuJymn//tnGTjGfrGZ4bI+sN0AncCFO0g9IhFIHrgz6KDwKd5fj2WnGHA5d38ijCQkOMJoMk/swF+DqrcPf1i069sCfFCxsJebhDBU8bCyxfnWxSip7Gok9tJFGikFIilMLQdz5tkjOSlyzodMDWrF6JyYuXmkQIicZtKK7cudXp9Temr8KBuU0xytpxtmKKxZiEZOPyxbOPmUflf+xpQs4a22DK2lKiUJ+bqtyhgp/SHjeqH3Y6YIvmzkZM2jqTCRkfHCgGlJ1d/9vr3yFAZd8YOD7IVIp2LiN3u/Fa0mDoT390EsjdE5OFApeqE7iXxjaWUuiUtdXPwo1TnJGSvNSowG5hYgKi1643nRCtBqcLLxt1j2kRITg4pymbHOtpg6gxGpMIEUmpqfD6aGTQOikWk5nYyG/Lb4vRMKXQ9cFY8AAHFN7+1WhCotJMJ2SsJthoQo5fPI+Jw5sIOfiVPUb0/wKBrgOwYH4iztz52VjP61y3E0HV4mJhs4lE6IV2+mjDSL+f8WOaIyb6enQ6SHdfPceMKTEYYdUfkZszTSYkZNw4eCnk2L4nt9N7lb55iXEeQxqXrXubVWKbT+zdiR3rV8HfWYW9F88aY0t+K6qq+N9urallBO5QV8kgoW1X2unTz77MWDXWrErudJDOXi2E/wg3o2IPgzHJ3gPwGzjAKC0pf1WD+kMuje0MdLRE1toVePe2FteLLyBwkAtO/nLNGK9rarcRQluX7d20eWFAZxIbNUlMTeg7Ojt4EA6dOdnpAH3/oAw+LgO6TAZJTO5ejA/0N4oQ0sjrmb6N7ZzhaYMlsdEiISTbUpMxf95s7D5/CtGhGoyU24pCr2kVaLZs7e0eMgTO3ZRUuiGJGDlC3O/Wd3TMYKW4l9HpMlJfh2C3oZi6/3CXCZkwZ57oNhtDCLnItNGlb+fqcBtE+Xo2ElJ2+xrcbawwZsRQXDyZh2ePK/D8CYvLpw8i3N0NSclL9IT80j2E8NwPzTXCUEFZZxLo6oytUU3RuZedFUqePzZqkNatT0NYxNguLVuxR0/D18UFBTd/MupelHgMUNo1tpOKKMYMGdhISP0bHimJ8aipvtf4nl4eC/cR7Ooiakq3pOkZvmLIh2qGXnxVcuRMt2tMJJLHZexmU8nzx0iMnYqQoEDTyDhxDj5OKuzMzTbqPiT33ryAh5VFY2o+O9YeAWpFm8E3JBeO70dMmEZMp3wwAVT4ZWqZZXvFZe1pTXNCKLvqbmVh9CCVvR+o4KFDMGXvQeNjkNmJSElOMuk+JO6W/RozwKYSQkvYSAd7sUJFZm6Y84BM6yXL09YSt188MWmgduZmQ+vrY9TSRfsjfs5qk3cbKYnpZWtpcMnqSCpKb2D/9gx42FohUhtYN6xfv+FmIUKvKXX19W+7Umb5sh0NEY16eBMhIa6OuFp6x+TZOz8hHmFaLWbkFxgkY+qeA/Ab5IKDp0+YfP2iuyUIG+TQwqhH+3l1Sobu/FHs2ZqOJ7UPRPtyKi8bAWrli1FyuwUyc8GcZ/mo9DN+ZJOXNSvIFUfzz5o8YHdfv8DK5CR4D3AW3dnWZITP/xqjVI44dO6UydcmOXz+NGaPbiq0oFTP0riYTgnJyUhr8x4RE+Csej68/5/NU8vFCCzXOu4wxbNqLlRrS+Wd+o5unj4Qa9eu6dKgXX/EwdtZjQlr1iFs1leI3JSJiWvTERoXj/B5CzBt8oQuXZdk7ZoV4n5788Bw+7qVRtuQ1nL+yB74KR2LzUXIVXNpCBU+N0+dXE1RIDrIuGCt7L3cfFqDnLy9GDs6AJqxY0WNmFV0DVP3HRb31en3uHOXMFKtxPy5icj/oeM9lvYkyt8T369pIOTeJqXY5isXTnaZEP7hXXhYW5qnMILqq8xFCFWhk6t7aLZ9Y1GBv0oulueUdZJfoqRfwoxYjFTIERQaiskZm5FQdM2gDSFSwhcsgs+QwQhyH470jRs63MrVy3f372G0qqkc6UCCPTys++P5U67LhDx9/ICqWcxDCNWxmosQEqpCp8Jn/XKQGumK9evT2ieivg5ZObvgP9gVAaO8MW75yg4NuSGJztkDbVQMPB0dEDN+HI50YLfSUlOwblKz9LuHNWaPH9NlMkgomvdXKa6ahRAAf2lO15eOBNCmDxU+6+t0A5wUuPVEaDM4ycuXwtdtGKbuPfRBeSy9zCwoxoTU9eI1U1a1TaPcfMzDT9VUXU9to7aePfRNl8mgyF3jOuC5W/8/e8jMhUKeHWYOMi5VlmJx0tfwUcjhbt1fzBflxDlg8Zi2xp32SEYNcEL8hUKzkNFc4r/VYaRK1WYJS121HMkRTVu4aWNtxcny8vlDk4mg4JA0I3SI62tvB/sVMnODEbi0DyHjIleKCaP9MGfyePz6I4MXzypx66dCLIgcg2meDvBXtdyo2rxtM8Ji48xOhl60ERHYf+Jo4/2YWz+L27dUGa8vcvCw6ica9NYSPmJo48DT6/Y+M1JuJ6ZPMg/ve3m5uvqfuqeAmucOd5WQZSuTRDJaz6S3bwSRlJmj7BE0aAD8nFTwVtgjzGM4wufM6zZCQmOmYsfu7MY82TivYTi2oMl2LNXYwFetQH55Fw/2NJcaLsTshOhJeb+HbnKjtEMH49frTLvqffuXq/C0scSu9NWo4kpQxd1GdkZDqWjc6fxuISRsZgI2btkoenCJ0yJbLFVXUhTiLN+wa5u5nJnuPb7wPgP8XUeNuPyoHIsWzYevk1Lc9qRKwLoXhtfi5+24lbsyUhE6riHWMLdQNJ+SsgJL588WD/i83NdACNWKBaksERkaaFQpaa85vkDeV0EN58Lw7CqdwF7RCRz7vlBMbMTixQswJ3K8OOMfsbeQt30j3tbXmGQYq7jb8HSw7xZCxi5ZBq3bYMT7qvD0mwYyiBRKk/g7OeJ0iamnqjogRGCfyHoCwyws/jAjatJvlHqmbGd15Z0uu4tv62tQcPaw6I0Fa7WYfvyM2ciYdvA4fL4chBh3eaNm0N7HoiBreNpaYfe5k2Yjo0HYpz1Chpe9zePdm9eJM/vNa/6DgqnsDam4VpSPsjs/YuvqZfBxcfpgUuIvFiLiq9nwUTrg+MKm5CGRsiio4cDOtgPfmJkMUX796IT4OspP5GSk1n8ICe+ayb7MDS1+z8lIRZCXZ5dIiT12BhMS58Jb5YDl4wa2OEhKr2d4NmhGN5FBS9b+j06Iu7VlHWmGuQh5106CzseBam3l0IzywsQ588QM7/QjpxB/6UqTFly6Ir4XtSkTk+fMg9bbE35qOdZHOYuloc0r3MmbIgNONoMqSLqDjAajzoV9coRUcSXwlVuL26p0piQzbiBmBX8J7ZcqeNlZi14cCb0OGaxCQrArsuKc8MMax8at2OaV7RRnkGtL3pQ5DXgb4bna/NrSf/nohPg4yk9lb1hjtiXrXSvJ2bAKizSOBh8KQEZZX5RgSCg3RekQD2sLMeijOMNcrm0Hy9UsWU/AzfJPf/Kyt36cnZFab05NqeJKsCt9FUbaWSPazUqstS3dbPyjNagUNC9BjukepEVfiIdwklNXmicC71TYoh59wulwyz/+h49SfsxLbveuvfxO61zQnMljxZ9j3YeJ0l5uyFshR2zkBKSkpyI6XCtWqtD7ox0txZiB9rvpgTM5sQ1Cr+m9OE8bBCisxM+6W/VHdHgINubuFHNq3U+EaDfKL1ff/zdZbwAZse7q6IWKu9hx7CCSViQhLiYS4d7u4iOZ6IgcCb2OGOUh/o1Oau08fsikAzfm0oxeQ0azhx0bfebwkxGeqyWb0SufKc/w7LhPb8DZCxRT0OOjxKcYCewzCvooeUgHPnvEmzJxp5Hp8UEUzCN0dpAeWSvry6DDj5RY+wTI+I0RKgNknwIYoXK0OY4y6Lo2kO8Ygc1snoXuyjV0NVyU7FMCw3OxPURIDN2/sKbSo0uaynO1Op7zk32KIFI+lqYwpBk8O6X5/XUPH/5Ox7MZ77+SohMiSKPYrCtCxR9knzJo+aK9gW4lQ2Cf6HjO11AbKD7Q1XCRDM8eFb8WqcFTekmBHL1XKHDxDF/+77LPBfS9HPRoo+7RDO5SYW3lf/d0H/scxKfO8RUR+sfBfrDwbFmBwAb32mdX9RVQRF9YzYUyAnve5O+Som9fE9hz5I7SdXq6L58ciquqfk/1S+8N77c6gaugYKzJ22HLGIHN1wncOqaG1RY9qfjXnm6zBAkSJEiQIEGCBAkSJEiQIEGCBAkSJEiQIGuD/wed/6mIcx/gBQAAAABJRU5ErkJggg=='