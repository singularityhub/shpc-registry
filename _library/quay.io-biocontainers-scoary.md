---
layout: container
name:  "quay.io/biocontainers/scoary"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/scoary/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/scoary/container.yaml"
updated_at: "2026-01-07 04:03:59.464307"
latest: "1.6.16--py_2"
container_url: "https://biocontainers.pro/tools/scoary"
aliases:
 - "pylupdate4"
 - "pyrcc4"
 - "pyuic4"
 - "qdoc3"
 - "qmlviewer"
 - "qt3to4"
 - "qtconfig"
 - "qttracereplay"
 - "scoary"
 - "scoary_GUI"
 - "ete3"
 - "easy_install-3.6"
 - "qhelpconverter"
 - "sip"
 - "xslt-config"
 - "xsltproc"
 - "qdbus"
 - "qdbuscpp2xml"
 - "qdbusviewer"
 - "qdbusxml2cpp"
versions:
 - "1.6.9--py36_0"
 - "1.6.16--py_2"
description: "shpc-registry automated BioContainers addition for scoary"
config: {"url": "https://biocontainers.pro/tools/scoary", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for scoary", "latest": {"1.6.16--py_2": "sha256:e27a1c0be86c1556ae809fa94b7e73730a3e005a8c1c77558944441f81c90695"}, "tags": {"1.6.9--py36_0": "sha256:2d126df4e04eb4be1bbf246fa5ebfe6071bf2c52fcd23f0ae6f52ba926f14047", "1.6.16--py_2": "sha256:e27a1c0be86c1556ae809fa94b7e73730a3e005a8c1c77558944441f81c90695"}, "docker": "quay.io/biocontainers/scoary", "aliases": {"pylupdate4": "/usr/local/bin/pylupdate4", "pyrcc4": "/usr/local/bin/pyrcc4", "pyuic4": "/usr/local/bin/pyuic4", "qdoc3": "/usr/local/bin/qdoc3", "qmlviewer": "/usr/local/bin/qmlviewer", "qt3to4": "/usr/local/bin/qt3to4", "qtconfig": "/usr/local/bin/qtconfig", "qttracereplay": "/usr/local/bin/qttracereplay", "scoary": "/usr/local/bin/scoary", "scoary_GUI": "/usr/local/bin/scoary_GUI", "ete3": "/usr/local/bin/ete3", "easy_install-3.6": "/usr/local/bin/easy_install-3.6", "qhelpconverter": "/usr/local/bin/qhelpconverter", "sip": "/usr/local/bin/sip", "xslt-config": "/usr/local/bin/xslt-config", "xsltproc": "/usr/local/bin/xsltproc", "qdbus": "/usr/local/bin/qdbus", "qdbuscpp2xml": "/usr/local/bin/qdbuscpp2xml", "qdbusviewer": "/usr/local/bin/qdbusviewer", "qdbusxml2cpp": "/usr/local/bin/qdbusxml2cpp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/scoary.
shpc-registry automated BioContainers addition for scoary
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/scoary
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/scoary:1.6.16--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/scoary/1.6.16--py_2
$ module help quay.io/biocontainers/scoary/1.6.16--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scoary-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scoary-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scoary-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scoary-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scoary-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scoary-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pylupdate4

```bash
$ singularity exec <container> /usr/local/bin/pylupdate4
$ podman run --it --rm --entrypoint /usr/local/bin/pylupdate4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pylupdate4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrcc4

```bash
$ singularity exec <container> /usr/local/bin/pyrcc4
$ podman run --it --rm --entrypoint /usr/local/bin/pyrcc4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrcc4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyuic4

```bash
$ singularity exec <container> /usr/local/bin/pyuic4
$ podman run --it --rm --entrypoint /usr/local/bin/pyuic4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyuic4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdoc3

```bash
$ singularity exec <container> /usr/local/bin/qdoc3
$ podman run --it --rm --entrypoint /usr/local/bin/qdoc3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdoc3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qmlviewer

```bash
$ singularity exec <container> /usr/local/bin/qmlviewer
$ podman run --it --rm --entrypoint /usr/local/bin/qmlviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qmlviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qt3to4

```bash
$ singularity exec <container> /usr/local/bin/qt3to4
$ podman run --it --rm --entrypoint /usr/local/bin/qt3to4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qt3to4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qtconfig

```bash
$ singularity exec <container> /usr/local/bin/qtconfig
$ podman run --it --rm --entrypoint /usr/local/bin/qtconfig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qtconfig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qttracereplay

```bash
$ singularity exec <container> /usr/local/bin/qttracereplay
$ podman run --it --rm --entrypoint /usr/local/bin/qttracereplay   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qttracereplay   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scoary

```bash
$ singularity exec <container> /usr/local/bin/scoary
$ podman run --it --rm --entrypoint /usr/local/bin/scoary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scoary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scoary_GUI

```bash
$ singularity exec <container> /usr/local/bin/scoary_GUI
$ podman run --it --rm --entrypoint /usr/local/bin/scoary_GUI   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scoary_GUI   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ete3

```bash
$ singularity exec <container> /usr/local/bin/ete3
$ podman run --it --rm --entrypoint /usr/local/bin/ete3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ete3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easy_install-3.6

```bash
$ singularity exec <container> /usr/local/bin/easy_install-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/easy_install-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easy_install-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhelpconverter

```bash
$ singularity exec <container> /usr/local/bin/qhelpconverter
$ podman run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip

```bash
$ singularity exec <container> /usr/local/bin/sip
$ podman run --it --rm --entrypoint /usr/local/bin/sip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xslt-config

```bash
$ singularity exec <container> /usr/local/bin/xslt-config
$ podman run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xsltproc

```bash
$ singularity exec <container> /usr/local/bin/xsltproc
$ podman run --it --rm --entrypoint /usr/local/bin/xsltproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xsltproc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdbus

```bash
$ singularity exec <container> /usr/local/bin/qdbus
$ podman run --it --rm --entrypoint /usr/local/bin/qdbus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdbus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdbuscpp2xml

```bash
$ singularity exec <container> /usr/local/bin/qdbuscpp2xml
$ podman run --it --rm --entrypoint /usr/local/bin/qdbuscpp2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdbuscpp2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdbusviewer

```bash
$ singularity exec <container> /usr/local/bin/qdbusviewer
$ podman run --it --rm --entrypoint /usr/local/bin/qdbusviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdbusviewer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdbusxml2cpp

```bash
$ singularity exec <container> /usr/local/bin/qdbusxml2cpp
$ podman run --it --rm --entrypoint /usr/local/bin/qdbusxml2cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdbusxml2cpp   -v ${PWD} -w ${PWD} <container> -c " $@"
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