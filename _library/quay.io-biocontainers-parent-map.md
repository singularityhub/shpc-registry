---
layout: container
name:  "quay.io/biocontainers/parent-map"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/parent-map/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/parent-map/container.yaml"
updated_at: "2025-10-29 03:57:11.905603"
latest: "1.1.2--pyhdfd78af_3"
container_url: "https://biocontainers.pro/tools/parent-map"
aliases:
 - "helpviewer"
 - "img2png"
 - "img2py"
 - "img2xpm"
 - "pycrust"
 - "pyshell"
 - "pyslices"
 - "pyslicesshell"
 - "pywxrc"
 - "wx-config"
 - "wxdemo"
 - "wxdocs"
 - "wxget"
 - "wxrc"
 - "wxrc-3.0"
 - "g-ir-annotation-tool"
 - "g-ir-compiler"
 - "g-ir-generate"
 - "g-ir-inspect"
 - "g-ir-scanner"
 - "gtk-builder-convert"
 - "gtk-demo"
 - "gtk-query-immodules-2.0"
 - "gtk-update-icon-cache"
 - "gdk-pixbuf-thumbnailer"
versions:
 - "1.1.2--py_0"
 - "1.1.2--pyhdfd78af_3"
description: "shpc-registry automated BioContainers addition for parent-map"
config: {"url": "https://biocontainers.pro/tools/parent-map", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for parent-map", "latest": {"1.1.2--pyhdfd78af_3": "sha256:791a26019648b9bceba5c5f0dfa3de0ab7f0a69cce46f0e41bedbd40b0a7ddcf"}, "tags": {"1.1.2--py_0": "sha256:2879f44f51fac2ad7d88c393bb8be879e14ad9611af8da8c736605c96006de84", "1.1.2--pyhdfd78af_3": "sha256:791a26019648b9bceba5c5f0dfa3de0ab7f0a69cce46f0e41bedbd40b0a7ddcf"}, "docker": "quay.io/biocontainers/parent-map", "aliases": {"helpviewer": "/usr/local/bin/helpviewer", "img2png": "/usr/local/bin/img2png", "img2py": "/usr/local/bin/img2py", "img2xpm": "/usr/local/bin/img2xpm", "pycrust": "/usr/local/bin/pycrust", "pyshell": "/usr/local/bin/pyshell", "pyslices": "/usr/local/bin/pyslices", "pyslicesshell": "/usr/local/bin/pyslicesshell", "pywxrc": "/usr/local/bin/pywxrc", "wx-config": "/usr/local/bin/wx-config", "wxdemo": "/usr/local/bin/wxdemo", "wxdocs": "/usr/local/bin/wxdocs", "wxget": "/usr/local/bin/wxget", "wxrc": "/usr/local/bin/wxrc", "wxrc-3.0": "/usr/local/bin/wxrc-3.0", "g-ir-annotation-tool": "/usr/local/bin/g-ir-annotation-tool", "g-ir-compiler": "/usr/local/bin/g-ir-compiler", "g-ir-generate": "/usr/local/bin/g-ir-generate", "g-ir-inspect": "/usr/local/bin/g-ir-inspect", "g-ir-scanner": "/usr/local/bin/g-ir-scanner", "gtk-builder-convert": "/usr/local/bin/gtk-builder-convert", "gtk-demo": "/usr/local/bin/gtk-demo", "gtk-query-immodules-2.0": "/usr/local/bin/gtk-query-immodules-2.0", "gtk-update-icon-cache": "/usr/local/bin/gtk-update-icon-cache", "gdk-pixbuf-thumbnailer": "/usr/local/bin/gdk-pixbuf-thumbnailer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/parent-map.
shpc-registry automated BioContainers addition for parent-map
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/parent-map
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/parent-map:1.1.2--pyhdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/parent-map/1.1.2--pyhdfd78af_3
$ module help quay.io/biocontainers/parent-map/1.1.2--pyhdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### parent-map-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### parent-map-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### parent-map-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### parent-map-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### parent-map-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### parent-map-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### wxrc-3.0

```bash
$ singularity exec <container> /usr/local/bin/wxrc-3.0
$ podman run --it --rm --entrypoint /usr/local/bin/wxrc-3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wxrc-3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-annotation-tool

```bash
$ singularity exec <container> /usr/local/bin/g-ir-annotation-tool
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-annotation-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-annotation-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-compiler

```bash
$ singularity exec <container> /usr/local/bin/g-ir-compiler
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-compiler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-compiler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-generate

```bash
$ singularity exec <container> /usr/local/bin/g-ir-generate
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-generate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-generate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-inspect

```bash
$ singularity exec <container> /usr/local/bin/g-ir-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-scanner

```bash
$ singularity exec <container> /usr/local/bin/g-ir-scanner
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-scanner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-scanner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-builder-convert

```bash
$ singularity exec <container> /usr/local/bin/gtk-builder-convert
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-builder-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-builder-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-demo

```bash
$ singularity exec <container> /usr/local/bin/gtk-demo
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-demo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-demo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtk-query-immodules-2.0

```bash
$ singularity exec <container> /usr/local/bin/gtk-query-immodules-2.0
$ podman run --it --rm --entrypoint /usr/local/bin/gtk-query-immodules-2.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtk-query-immodules-2.0   -v ${PWD} -w ${PWD} <container> -c " $@"
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