---
layout: container
name:  "quay.io/biocontainers/ddquint"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ddquint/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ddquint/container.yaml"
updated_at: "2026-01-01 07:34:15.868160"
latest: "0.1.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/ddquint"
aliases:
 - "ddquint"
 - "helpviewer"
 - "img2png"
 - "img2py"
 - "img2xpm"
 - "pycrust"
 - "pyshell"
 - "pyslices"
 - "pyslicesshell"
 - "pywxrc"
 - "spirv-as"
 - "spirv-cfg"
 - "spirv-dis"
 - "spirv-lesspipe.sh"
 - "spirv-link"
 - "spirv-lint"
 - "spirv-objdump"
 - "spirv-opt"
 - "spirv-reduce"
 - "spirv-val"
 - "wx-config"
 - "wxdemo"
 - "wxdocs"
 - "wxget"
 - "wxrc"
 - "wxrc-3.2"
 - "gtk-builder-tool"
 - "gtk-encode-symbolic-svg"
 - "gtk-launch"
 - "gtk-query-immodules-3.0"
 - "gtk-query-settings"
 - "send2trash"
 - "wayland-scanner"
 - "gi-compile-repository"
 - "gi-decompile-typelib"
 - "gi-inspect-typelib"
 - "xkbcli"
 - "qconvex"
 - "qdelaunay"
 - "qhalf"
 - "qhull"
 - "qvoronoi"
 - "rbox"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "rsvg-convert"
 - "gtk-update-icon-cache"
 - "gdk-pixbuf-thumbnailer"
 - "gdk-pixbuf-csource"
versions:
 - "0.1.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for ddquint"
config: {"url": "https://biocontainers.pro/tools/ddquint", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ddquint", "latest": {"0.1.0--pyhdfd78af_0": "sha256:4fda719b4d88f86dfd8f51278cffe52f11d4a50f16604f22b5255dfc184a06ae"}, "tags": {"0.1.0--pyhdfd78af_0": "sha256:4fda719b4d88f86dfd8f51278cffe52f11d4a50f16604f22b5255dfc184a06ae"}, "docker": "quay.io/biocontainers/ddquint", "aliases": {"ddquint": "/usr/local/bin/ddquint", "helpviewer": "/usr/local/bin/helpviewer", "img2png": "/usr/local/bin/img2png", "img2py": "/usr/local/bin/img2py", "img2xpm": "/usr/local/bin/img2xpm", "pycrust": "/usr/local/bin/pycrust", "pyshell": "/usr/local/bin/pyshell", "pyslices": "/usr/local/bin/pyslices", "pyslicesshell": "/usr/local/bin/pyslicesshell", "pywxrc": "/usr/local/bin/pywxrc", "spirv-as": "/usr/local/bin/spirv-as", "spirv-cfg": "/usr/local/bin/spirv-cfg", "spirv-dis": "/usr/local/bin/spirv-dis", "spirv-lesspipe.sh": "/usr/local/bin/spirv-lesspipe.sh", "spirv-link": "/usr/local/bin/spirv-link", "spirv-lint": "/usr/local/bin/spirv-lint", "spirv-objdump": "/usr/local/bin/spirv-objdump", "spirv-opt": "/usr/local/bin/spirv-opt", "spirv-reduce": "/usr/local/bin/spirv-reduce", "spirv-val": "/usr/local/bin/spirv-val", "wx-config": "/usr/local/bin/wx-config", "wxdemo": "/usr/local/bin/wxdemo", "wxdocs": "/usr/local/bin/wxdocs", "wxget": "/usr/local/bin/wxget", "wxrc": "/usr/local/bin/wxrc", "wxrc-3.2": "/usr/local/bin/wxrc-3.2", "gtk-builder-tool": "/usr/local/bin/gtk-builder-tool", "gtk-encode-symbolic-svg": "/usr/local/bin/gtk-encode-symbolic-svg", "gtk-launch": "/usr/local/bin/gtk-launch", "gtk-query-immodules-3.0": "/usr/local/bin/gtk-query-immodules-3.0", "gtk-query-settings": "/usr/local/bin/gtk-query-settings", "send2trash": "/usr/local/bin/send2trash", "wayland-scanner": "/usr/local/bin/wayland-scanner", "gi-compile-repository": "/usr/local/bin/gi-compile-repository", "gi-decompile-typelib": "/usr/local/bin/gi-decompile-typelib", "gi-inspect-typelib": "/usr/local/bin/gi-inspect-typelib", "xkbcli": "/usr/local/bin/xkbcli", "qconvex": "/usr/local/bin/qconvex", "qdelaunay": "/usr/local/bin/qdelaunay", "qhalf": "/usr/local/bin/qhalf", "qhull": "/usr/local/bin/qhull", "qvoronoi": "/usr/local/bin/qvoronoi", "rbox": "/usr/local/bin/rbox", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "rsvg-convert": "/usr/local/bin/rsvg-convert", "gtk-update-icon-cache": "/usr/local/bin/gtk-update-icon-cache", "gdk-pixbuf-thumbnailer": "/usr/local/bin/gdk-pixbuf-thumbnailer", "gdk-pixbuf-csource": "/usr/local/bin/gdk-pixbuf-csource"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ddquint.
singularity registry hpc automated addition for ddquint
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ddquint
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ddquint:0.1.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ddquint/0.1.0--pyhdfd78af_0
$ module help quay.io/biocontainers/ddquint/0.1.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ddquint-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ddquint-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ddquint-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ddquint-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ddquint-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ddquint-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ddquint

```bash
$ singularity exec <container> /usr/local/bin/ddquint
$ podman run --it --rm --entrypoint /usr/local/bin/ddquint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ddquint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### helpviewer

```bash
$ singularity exec <container> /usr/local/bin/helpviewer
$ podman run --it --rm --entrypoint /usr/local/bin/helpviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/helpviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### img2png

```bash
$ singularity exec <container> /usr/local/bin/img2png
$ podman run --it --rm --entrypoint /usr/local/bin/img2png   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/img2png   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### img2py

```bash
$ singularity exec <container> /usr/local/bin/img2py
$ podman run --it --rm --entrypoint /usr/local/bin/img2py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/img2py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### img2xpm

```bash
$ singularity exec <container> /usr/local/bin/img2xpm
$ podman run --it --rm --entrypoint /usr/local/bin/img2xpm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/img2xpm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pycrust

```bash
$ singularity exec <container> /usr/local/bin/pycrust
$ podman run --it --rm --entrypoint /usr/local/bin/pycrust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pycrust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyshell

```bash
$ singularity exec <container> /usr/local/bin/pyshell
$ podman run --it --rm --entrypoint /usr/local/bin/pyshell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyshell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyslices

```bash
$ singularity exec <container> /usr/local/bin/pyslices
$ podman run --it --rm --entrypoint /usr/local/bin/pyslices   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyslices   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyslicesshell

```bash
$ singularity exec <container> /usr/local/bin/pyslicesshell
$ podman run --it --rm --entrypoint /usr/local/bin/pyslicesshell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyslicesshell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pywxrc

```bash
$ singularity exec <container> /usr/local/bin/pywxrc
$ podman run --it --rm --entrypoint /usr/local/bin/pywxrc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pywxrc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spirv-as

```bash
$ singularity exec <container> /usr/local/bin/spirv-as
$ podman run --it --rm --entrypoint /usr/local/bin/spirv-as   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spirv-as   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spirv-cfg

```bash
$ singularity exec <container> /usr/local/bin/spirv-cfg
$ podman run --it --rm --entrypoint /usr/local/bin/spirv-cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spirv-cfg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spirv-dis

```bash
$ singularity exec <container> /usr/local/bin/spirv-dis
$ podman run --it --rm --entrypoint /usr/local/bin/spirv-dis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spirv-dis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spirv-lesspipe.sh

```bash
$ singularity exec <container> /usr/local/bin/spirv-lesspipe.sh
$ podman run --it --rm --entrypoint /usr/local/bin/spirv-lesspipe.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spirv-lesspipe.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spirv-link

```bash
$ singularity exec <container> /usr/local/bin/spirv-link
$ podman run --it --rm --entrypoint /usr/local/bin/spirv-link   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spirv-link   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spirv-lint

```bash
$ singularity exec <container> /usr/local/bin/spirv-lint
$ podman run --it --rm --entrypoint /usr/local/bin/spirv-lint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spirv-lint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spirv-objdump

```bash
$ singularity exec <container> /usr/local/bin/spirv-objdump
$ podman run --it --rm --entrypoint /usr/local/bin/spirv-objdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spirv-objdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spirv-opt

```bash
$ singularity exec <container> /usr/local/bin/spirv-opt
$ podman run --it --rm --entrypoint /usr/local/bin/spirv-opt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spirv-opt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spirv-reduce

```bash
$ singularity exec <container> /usr/local/bin/spirv-reduce
$ podman run --it --rm --entrypoint /usr/local/bin/spirv-reduce   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spirv-reduce   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spirv-val

```bash
$ singularity exec <container> /usr/local/bin/spirv-val
$ podman run --it --rm --entrypoint /usr/local/bin/spirv-val   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spirv-val   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wx-config

```bash
$ singularity exec <container> /usr/local/bin/wx-config
$ podman run --it --rm --entrypoint /usr/local/bin/wx-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wx-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wxdemo

```bash
$ singularity exec <container> /usr/local/bin/wxdemo
$ podman run --it --rm --entrypoint /usr/local/bin/wxdemo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wxdemo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wxdocs

```bash
$ singularity exec <container> /usr/local/bin/wxdocs
$ podman run --it --rm --entrypoint /usr/local/bin/wxdocs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wxdocs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wxget

```bash
$ singularity exec <container> /usr/local/bin/wxget
$ podman run --it --rm --entrypoint /usr/local/bin/wxget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wxget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wxrc

```bash
$ singularity exec <container> /usr/local/bin/wxrc
$ podman run --it --rm --entrypoint /usr/local/bin/wxrc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wxrc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wxrc-3.2

```bash
$ singularity exec <container> /usr/local/bin/wxrc-3.2
$ podman run --it --rm --entrypoint /usr/local/bin/wxrc-3.2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wxrc-3.2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-builder-tool

```bash
$ singularity exec <container> /usr/local/bin/gtk-builder-tool
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-builder-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-builder-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-encode-symbolic-svg

```bash
$ singularity exec <container> /usr/local/bin/gtk-encode-symbolic-svg
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-encode-symbolic-svg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-encode-symbolic-svg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-launch

```bash
$ singularity exec <container> /usr/local/bin/gtk-launch
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-launch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-launch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-query-immodules-3.0

```bash
$ singularity exec <container> /usr/local/bin/gtk-query-immodules-3.0
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-query-immodules-3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-query-immodules-3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-query-settings

```bash
$ singularity exec <container> /usr/local/bin/gtk-query-settings
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-query-settings   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-query-settings   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### send2trash

```bash
$ singularity exec <container> /usr/local/bin/send2trash
$ podman run --it --rm --entrypoint /usr/local/bin/send2trash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/send2trash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wayland-scanner

```bash
$ singularity exec <container> /usr/local/bin/wayland-scanner
$ podman run --it --rm --entrypoint /usr/local/bin/wayland-scanner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wayland-scanner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gi-compile-repository

```bash
$ singularity exec <container> /usr/local/bin/gi-compile-repository
$ podman run --it --rm --entrypoint /usr/local/bin/gi-compile-repository   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gi-compile-repository   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gi-decompile-typelib

```bash
$ singularity exec <container> /usr/local/bin/gi-decompile-typelib
$ podman run --it --rm --entrypoint /usr/local/bin/gi-decompile-typelib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gi-decompile-typelib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gi-inspect-typelib

```bash
$ singularity exec <container> /usr/local/bin/gi-inspect-typelib
$ podman run --it --rm --entrypoint /usr/local/bin/gi-inspect-typelib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gi-inspect-typelib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xkbcli

```bash
$ singularity exec <container> /usr/local/bin/xkbcli
$ podman run --it --rm --entrypoint /usr/local/bin/xkbcli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xkbcli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qconvex

```bash
$ singularity exec <container> /usr/local/bin/qconvex
$ podman run --it --rm --entrypoint /usr/local/bin/qconvex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qconvex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdelaunay

```bash
$ singularity exec <container> /usr/local/bin/qdelaunay
$ podman run --it --rm --entrypoint /usr/local/bin/qdelaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdelaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhalf

```bash
$ singularity exec <container> /usr/local/bin/qhalf
$ podman run --it --rm --entrypoint /usr/local/bin/qhalf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhalf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhull

```bash
$ singularity exec <container> /usr/local/bin/qhull
$ podman run --it --rm --entrypoint /usr/local/bin/qhull   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhull   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qvoronoi

```bash
$ singularity exec <container> /usr/local/bin/qvoronoi
$ podman run --it --rm --entrypoint /usr/local/bin/qvoronoi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qvoronoi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rbox

```bash
$ singularity exec <container> /usr/local/bin/rbox
$ podman run --it --rm --entrypoint /usr/local/bin/rbox   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rbox   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.13

```bash
$ singularity exec <container> /usr/local/bin/idle3.13
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.13

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.13
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13

```bash
$ singularity exec <container> /usr/local/bin/python3.13
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13-config

```bash
$ singularity exec <container> /usr/local/bin/python3.13-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rsvg-convert

```bash
$ singularity exec <container> /usr/local/bin/rsvg-convert
$ podman run --it --rm --entrypoint /usr/local/bin/rsvg-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rsvg-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-update-icon-cache

```bash
$ singularity exec <container> /usr/local/bin/gtk-update-icon-cache
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-update-icon-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-update-icon-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdk-pixbuf-thumbnailer

```bash
$ singularity exec <container> /usr/local/bin/gdk-pixbuf-thumbnailer
$ podman run --it --rm --entrypoint /usr/local/bin/gdk-pixbuf-thumbnailer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdk-pixbuf-thumbnailer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdk-pixbuf-csource

```bash
$ singularity exec <container> /usr/local/bin/gdk-pixbuf-csource
$ podman run --it --rm --entrypoint /usr/local/bin/gdk-pixbuf-csource   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdk-pixbuf-csource   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)