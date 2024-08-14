---
layout: container
name:  "quay.io/biocontainers/riboplot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/riboplot/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/riboplot/container.yaml"
updated_at: "2024-08-14 03:28:00.757393"
latest: "0.3.1--py27_2"
container_url: "https://biocontainers.pro/tools/riboplot"
aliases:
 - "assistant-qt4"
 - "designer-qt4"
 - "lconvert-qt4"
 - "linguist-qt4"
 - "lrelease-qt4"
 - "lupdate-qt4"
 - "moc-qt4"
 - "nosetests-2.7"
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
 - "ribocount"
 - "riboplot"
 - "uic-qt4"
 - "xmlpatterns-qt4"
 - "xmlpatternsvalidator-qt4"
 - "sip"
 - "annotateBed"
 - "bamToBed"
 - "bamToFastq"
 - "bed12ToBed6"
 - "bedToBam"
 - "bedToIgv"
 - "bedpeToBam"
 - "bedtools"
 - "closestBed"
versions:
 - "0.3.1--py27_2"
description: "shpc-registry automated BioContainers addition for riboplot"
config: {"url": "https://biocontainers.pro/tools/riboplot", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for riboplot", "latest": {"0.3.1--py27_2": "sha256:b7e813e95cbec8501227994015b1753176c53bed9c68602950b7a8ecf6c7e6f0"}, "tags": {"0.3.1--py27_2": "sha256:b7e813e95cbec8501227994015b1753176c53bed9c68602950b7a8ecf6c7e6f0"}, "docker": "quay.io/biocontainers/riboplot", "aliases": {"assistant-qt4": "/usr/local/bin/assistant-qt4", "designer-qt4": "/usr/local/bin/designer-qt4", "lconvert-qt4": "/usr/local/bin/lconvert-qt4", "linguist-qt4": "/usr/local/bin/linguist-qt4", "lrelease-qt4": "/usr/local/bin/lrelease-qt4", "lupdate-qt4": "/usr/local/bin/lupdate-qt4", "moc-qt4": "/usr/local/bin/moc-qt4", "nosetests-2.7": "/usr/local/bin/nosetests-2.7", "pixeltool-qt4": "/usr/local/bin/pixeltool-qt4", "pylupdate4": "/usr/local/bin/pylupdate4", "pyrcc4": "/usr/local/bin/pyrcc4", "pyuic4": "/usr/local/bin/pyuic4", "qcollectiongenerator-qt4": "/usr/local/bin/qcollectiongenerator-qt4", "qdbus-qt4": "/usr/local/bin/qdbus-qt4", "qdbuscpp2xml-qt4": "/usr/local/bin/qdbuscpp2xml-qt4", "qdbusviewer-qt4": "/usr/local/bin/qdbusviewer-qt4", "qdbusxml2cpp-qt4": "/usr/local/bin/qdbusxml2cpp-qt4", "qdoc3-qt4": "/usr/local/bin/qdoc3-qt4", "qhelpconverter-qt4": "/usr/local/bin/qhelpconverter-qt4", "qhelpgenerator-qt4": "/usr/local/bin/qhelpgenerator-qt4", "qmake-qt4": "/usr/local/bin/qmake-qt4", "qmlplugindump-qt4": "/usr/local/bin/qmlplugindump-qt4", "qmlviewer-qt4": "/usr/local/bin/qmlviewer-qt4", "qt3to4-qt4": "/usr/local/bin/qt3to4-qt4", "qtconfig-qt4": "/usr/local/bin/qtconfig-qt4", "qttracereplay-qt4": "/usr/local/bin/qttracereplay-qt4", "rcc-qt4": "/usr/local/bin/rcc-qt4", "ribocount": "/usr/local/bin/ribocount", "riboplot": "/usr/local/bin/riboplot", "uic-qt4": "/usr/local/bin/uic-qt4", "xmlpatterns-qt4": "/usr/local/bin/xmlpatterns-qt4", "xmlpatternsvalidator-qt4": "/usr/local/bin/xmlpatternsvalidator-qt4", "sip": "/usr/local/bin/sip", "annotateBed": "/usr/local/bin/annotateBed", "bamToBed": "/usr/local/bin/bamToBed", "bamToFastq": "/usr/local/bin/bamToFastq", "bed12ToBed6": "/usr/local/bin/bed12ToBed6", "bedToBam": "/usr/local/bin/bedToBam", "bedToIgv": "/usr/local/bin/bedToIgv", "bedpeToBam": "/usr/local/bin/bedpeToBam", "bedtools": "/usr/local/bin/bedtools", "closestBed": "/usr/local/bin/closestBed"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/riboplot.
shpc-registry automated BioContainers addition for riboplot
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/riboplot
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/riboplot:0.3.1--py27_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/riboplot/0.3.1--py27_2
$ module help quay.io/biocontainers/riboplot/0.3.1--py27_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### riboplot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### riboplot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### riboplot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### riboplot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### riboplot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### riboplot-inspect-deffile:

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


#### nosetests-2.7

```bash
$ singularity exec <container> /usr/local/bin/nosetests-2.7
$ podman run --it --rm --entrypoint /usr/local/bin/nosetests-2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nosetests-2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### ribocount

```bash
$ singularity exec <container> /usr/local/bin/ribocount
$ podman run --it --rm --entrypoint /usr/local/bin/ribocount   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ribocount   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### riboplot

```bash
$ singularity exec <container> /usr/local/bin/riboplot
$ podman run --it --rm --entrypoint /usr/local/bin/riboplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/riboplot   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### annotateBed

```bash
$ singularity exec <container> /usr/local/bin/annotateBed
$ podman run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToBed

```bash
$ singularity exec <container> /usr/local/bin/bamToBed
$ podman run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToFastq

```bash
$ singularity exec <container> /usr/local/bin/bamToFastq
$ podman run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed12ToBed6

```bash
$ singularity exec <container> /usr/local/bin/bed12ToBed6
$ podman run --it --rm --entrypoint /usr/local/bin/bed12ToBed6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed12ToBed6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedToBam

```bash
$ singularity exec <container> /usr/local/bin/bedToBam
$ podman run --it --rm --entrypoint /usr/local/bin/bedToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedToIgv

```bash
$ singularity exec <container> /usr/local/bin/bedToIgv
$ podman run --it --rm --entrypoint /usr/local/bin/bedToIgv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedToIgv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedpeToBam

```bash
$ singularity exec <container> /usr/local/bin/bedpeToBam
$ podman run --it --rm --entrypoint /usr/local/bin/bedpeToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedpeToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedtools

```bash
$ singularity exec <container> /usr/local/bin/bedtools
$ podman run --it --rm --entrypoint /usr/local/bin/bedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### closestBed

```bash
$ singularity exec <container> /usr/local/bin/closestBed
$ podman run --it --rm --entrypoint /usr/local/bin/closestBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/closestBed   -v ${PWD} -w ${PWD} <container> -c " $@"
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