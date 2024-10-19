---
layout: container
name:  "quay.io/biocontainers/kiwidist"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kiwidist/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kiwidist/container.yaml"
updated_at: "2024-10-19 03:32:59.531162"
latest: "0.3.6--py_3"
container_url: "https://biocontainers.pro/tools/kiwidist"
aliases:
 - "assistant-qt4"
 - "designer-qt4"
 - "lconvert-qt4"
 - "linguist-qt4"
 - "lrelease-qt4"
 - "lupdate-qt4"
 - "moc-qt4"
 - "pixeltool-qt4"
 - "pylupdate4"
 - "pyrcc4"
 - "pyuic4"
 - "qcollectiongenerator-qt4"
 - "qdbus-qt4"
 - "qdbuscpp2xml-qt4"
 - "qdbusviewer-qt4"
 - "qdbusxml2cpp-qt4"
 - "qdoc3-qt4"
 - "qhelpconverter-qt4"
 - "qhelpgenerator-qt4"
 - "qmake-qt4"
 - "qmlplugindump-qt4"
 - "qmlviewer-qt4"
 - "qt3to4-qt4"
 - "qtconfig-qt4"
 - "qttracereplay-qt4"
 - "rcc-qt4"
 - "uic-qt4"
 - "xmlpatterns-qt4"
 - "xmlpatternsvalidator-qt4"
 - "sip"
 - "chardetect"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
versions:
 - "0.3.6--py_3"
description: "shpc-registry automated BioContainers addition for kiwidist"
config: {"url": "https://biocontainers.pro/tools/kiwidist", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kiwidist", "latest": {"0.3.6--py_3": "sha256:51f4b5d1f04a1b5f488826966b198c99de043e01491bfc9205cda9dc4f49b478"}, "tags": {"0.3.6--py_3": "sha256:51f4b5d1f04a1b5f488826966b198c99de043e01491bfc9205cda9dc4f49b478"}, "docker": "quay.io/biocontainers/kiwidist", "aliases": {"assistant-qt4": "/usr/local/bin/assistant-qt4", "designer-qt4": "/usr/local/bin/designer-qt4", "lconvert-qt4": "/usr/local/bin/lconvert-qt4", "linguist-qt4": "/usr/local/bin/linguist-qt4", "lrelease-qt4": "/usr/local/bin/lrelease-qt4", "lupdate-qt4": "/usr/local/bin/lupdate-qt4", "moc-qt4": "/usr/local/bin/moc-qt4", "pixeltool-qt4": "/usr/local/bin/pixeltool-qt4", "pylupdate4": "/usr/local/bin/pylupdate4", "pyrcc4": "/usr/local/bin/pyrcc4", "pyuic4": "/usr/local/bin/pyuic4", "qcollectiongenerator-qt4": "/usr/local/bin/qcollectiongenerator-qt4", "qdbus-qt4": "/usr/local/bin/qdbus-qt4", "qdbuscpp2xml-qt4": "/usr/local/bin/qdbuscpp2xml-qt4", "qdbusviewer-qt4": "/usr/local/bin/qdbusviewer-qt4", "qdbusxml2cpp-qt4": "/usr/local/bin/qdbusxml2cpp-qt4", "qdoc3-qt4": "/usr/local/bin/qdoc3-qt4", "qhelpconverter-qt4": "/usr/local/bin/qhelpconverter-qt4", "qhelpgenerator-qt4": "/usr/local/bin/qhelpgenerator-qt4", "qmake-qt4": "/usr/local/bin/qmake-qt4", "qmlplugindump-qt4": "/usr/local/bin/qmlplugindump-qt4", "qmlviewer-qt4": "/usr/local/bin/qmlviewer-qt4", "qt3to4-qt4": "/usr/local/bin/qt3to4-qt4", "qtconfig-qt4": "/usr/local/bin/qtconfig-qt4", "qttracereplay-qt4": "/usr/local/bin/qttracereplay-qt4", "rcc-qt4": "/usr/local/bin/rcc-qt4", "uic-qt4": "/usr/local/bin/uic-qt4", "xmlpatterns-qt4": "/usr/local/bin/xmlpatterns-qt4", "xmlpatternsvalidator-qt4": "/usr/local/bin/xmlpatternsvalidator-qt4", "sip": "/usr/local/bin/sip", "chardetect": "/usr/local/bin/chardetect", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kiwidist.
shpc-registry automated BioContainers addition for kiwidist
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kiwidist
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kiwidist:0.3.6--py_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kiwidist/0.3.6--py_3
$ module help quay.io/biocontainers/kiwidist/0.3.6--py_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kiwidist-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kiwidist-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kiwidist-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kiwidist-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kiwidist-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kiwidist-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### assistant-qt4

```bash
$ singularity exec <container> /usr/local/bin/assistant-qt4
$ podman run --it --rm --entrypoint /usr/local/bin/assistant-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/assistant-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### designer-qt4

```bash
$ singularity exec <container> /usr/local/bin/designer-qt4
$ podman run --it --rm --entrypoint /usr/local/bin/designer-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/designer-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lconvert-qt4

```bash
$ singularity exec <container> /usr/local/bin/lconvert-qt4
$ podman run --it --rm --entrypoint /usr/local/bin/lconvert-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lconvert-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### linguist-qt4

```bash
$ singularity exec <container> /usr/local/bin/linguist-qt4
$ podman run --it --rm --entrypoint /usr/local/bin/linguist-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/linguist-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrelease-qt4

```bash
$ singularity exec <container> /usr/local/bin/lrelease-qt4
$ podman run --it --rm --entrypoint /usr/local/bin/lrelease-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrelease-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lupdate-qt4

```bash
$ singularity exec <container> /usr/local/bin/lupdate-qt4
$ podman run --it --rm --entrypoint /usr/local/bin/lupdate-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lupdate-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### moc-qt4

```bash
$ singularity exec <container> /usr/local/bin/moc-qt4
$ podman run --it --rm --entrypoint /usr/local/bin/moc-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/moc-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pixeltool-qt4

```bash
$ singularity exec <container> /usr/local/bin/pixeltool-qt4
$ podman run --it --rm --entrypoint /usr/local/bin/pixeltool-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pixeltool-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### qcollectiongenerator-qt4

```bash
$ singularity exec <container> /usr/local/bin/qcollectiongenerator-qt4
$ podman run --it --rm --entrypoint /usr/local/bin/qcollectiongenerator-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qcollectiongenerator-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdbus-qt4

```bash
$ singularity exec <container> /usr/local/bin/qdbus-qt4
$ podman run --it --rm --entrypoint /usr/local/bin/qdbus-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdbus-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdbuscpp2xml-qt4

```bash
$ singularity exec <container> /usr/local/bin/qdbuscpp2xml-qt4
$ podman run --it --rm --entrypoint /usr/local/bin/qdbuscpp2xml-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdbuscpp2xml-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdbusviewer-qt4

```bash
$ singularity exec <container> /usr/local/bin/qdbusviewer-qt4
$ podman run --it --rm --entrypoint /usr/local/bin/qdbusviewer-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdbusviewer-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdbusxml2cpp-qt4

```bash
$ singularity exec <container> /usr/local/bin/qdbusxml2cpp-qt4
$ podman run --it --rm --entrypoint /usr/local/bin/qdbusxml2cpp-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdbusxml2cpp-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdoc3-qt4

```bash
$ singularity exec <container> /usr/local/bin/qdoc3-qt4
$ podman run --it --rm --entrypoint /usr/local/bin/qdoc3-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdoc3-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhelpconverter-qt4

```bash
$ singularity exec <container> /usr/local/bin/qhelpconverter-qt4
$ podman run --it --rm --entrypoint /usr/local/bin/qhelpconverter-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhelpconverter-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhelpgenerator-qt4

```bash
$ singularity exec <container> /usr/local/bin/qhelpgenerator-qt4
$ podman run --it --rm --entrypoint /usr/local/bin/qhelpgenerator-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhelpgenerator-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qmake-qt4

```bash
$ singularity exec <container> /usr/local/bin/qmake-qt4
$ podman run --it --rm --entrypoint /usr/local/bin/qmake-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qmake-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qmlplugindump-qt4

```bash
$ singularity exec <container> /usr/local/bin/qmlplugindump-qt4
$ podman run --it --rm --entrypoint /usr/local/bin/qmlplugindump-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qmlplugindump-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qmlviewer-qt4

```bash
$ singularity exec <container> /usr/local/bin/qmlviewer-qt4
$ podman run --it --rm --entrypoint /usr/local/bin/qmlviewer-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qmlviewer-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qt3to4-qt4

```bash
$ singularity exec <container> /usr/local/bin/qt3to4-qt4
$ podman run --it --rm --entrypoint /usr/local/bin/qt3to4-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qt3to4-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qtconfig-qt4

```bash
$ singularity exec <container> /usr/local/bin/qtconfig-qt4
$ podman run --it --rm --entrypoint /usr/local/bin/qtconfig-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qtconfig-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qttracereplay-qt4

```bash
$ singularity exec <container> /usr/local/bin/qttracereplay-qt4
$ podman run --it --rm --entrypoint /usr/local/bin/qttracereplay-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qttracereplay-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rcc-qt4

```bash
$ singularity exec <container> /usr/local/bin/rcc-qt4
$ podman run --it --rm --entrypoint /usr/local/bin/rcc-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rcc-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uic-qt4

```bash
$ singularity exec <container> /usr/local/bin/uic-qt4
$ podman run --it --rm --entrypoint /usr/local/bin/uic-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uic-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xmlpatterns-qt4

```bash
$ singularity exec <container> /usr/local/bin/xmlpatterns-qt4
$ podman run --it --rm --entrypoint /usr/local/bin/xmlpatterns-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xmlpatterns-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xmlpatternsvalidator-qt4

```bash
$ singularity exec <container> /usr/local/bin/xmlpatternsvalidator-qt4
$ podman run --it --rm --entrypoint /usr/local/bin/xmlpatternsvalidator-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xmlpatternsvalidator-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip

```bash
$ singularity exec <container> /usr/local/bin/sip
$ podman run --it --rm --entrypoint /usr/local/bin/sip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2-config

```bash
$ singularity exec <container> /usr/local/bin/python2-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7-config

```bash
$ singularity exec <container> /usr/local/bin/python2.7-config
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2

```bash
$ singularity exec <container> /usr/local/bin/python2
$ podman run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python2.7

```bash
$ singularity exec <container> /usr/local/bin/python2.7
$ podman run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle

```bash
$ singularity exec <container> /usr/local/bin/idle
$ podman run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-config

```bash
$ singularity exec <container> /usr/local/bin/python-config
$ podman run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smtpd.py

```bash
$ singularity exec <container> /usr/local/bin/smtpd.py
$ podman run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smtpd.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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