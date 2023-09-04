---
layout: container
name:  "quay.io/biocontainers/pymix"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pymix/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pymix/container.yaml"
updated_at: "2023-09-04 02:39:51.708672"
latest: "0.8--py27hcb787e7_1"
container_url: "https://biocontainers.pro/tools/pymix"
aliases:
 - "assistant-qt4"
 - "ccache-swig"
 - "designer-qt4"
 - "ghmm-config"
 - "lconvert-qt4"
 - "linguist-qt4"
 - "lrelease-qt4"
 - "lupdate-qt4"
 - "moc-qt4"
 - "pixeltool-qt4"
 - "probdist"
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
 - "scluster"
 - "smix_hmm"
 - "swig"
 - "uic-qt4"
 - "xmlpatterns-qt4"
 - "xmlpatternsvalidator-qt4"
 - "cluster"
 - "sip"
 - "qt.conf"
 - "python2-config"
 - "python2.7-config"
 - "python2"
 - "python2.7"
 - "idle"
 - "python-config"
 - "smtpd.py"
versions:
 - "0.8--py27hcb787e7_1"
description: "shpc-registry automated BioContainers addition for pymix"
config: {"url": "https://biocontainers.pro/tools/pymix", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pymix", "latest": {"0.8--py27hcb787e7_1": "sha256:cbf7f71867a9644e5285be48a5e81546c0a3bb453ca3dc60a4aaf678acadab03"}, "tags": {"0.8--py27hcb787e7_1": "sha256:cbf7f71867a9644e5285be48a5e81546c0a3bb453ca3dc60a4aaf678acadab03"}, "docker": "quay.io/biocontainers/pymix", "aliases": {"assistant-qt4": "/usr/local/bin/assistant-qt4", "ccache-swig": "/usr/local/bin/ccache-swig", "designer-qt4": "/usr/local/bin/designer-qt4", "ghmm-config": "/usr/local/bin/ghmm-config", "lconvert-qt4": "/usr/local/bin/lconvert-qt4", "linguist-qt4": "/usr/local/bin/linguist-qt4", "lrelease-qt4": "/usr/local/bin/lrelease-qt4", "lupdate-qt4": "/usr/local/bin/lupdate-qt4", "moc-qt4": "/usr/local/bin/moc-qt4", "pixeltool-qt4": "/usr/local/bin/pixeltool-qt4", "probdist": "/usr/local/bin/probdist", "pylupdate4": "/usr/local/bin/pylupdate4", "pyrcc4": "/usr/local/bin/pyrcc4", "pyuic4": "/usr/local/bin/pyuic4", "qcollectiongenerator-qt4": "/usr/local/bin/qcollectiongenerator-qt4", "qdbus-qt4": "/usr/local/bin/qdbus-qt4", "qdbuscpp2xml-qt4": "/usr/local/bin/qdbuscpp2xml-qt4", "qdbusviewer-qt4": "/usr/local/bin/qdbusviewer-qt4", "qdbusxml2cpp-qt4": "/usr/local/bin/qdbusxml2cpp-qt4", "qdoc3-qt4": "/usr/local/bin/qdoc3-qt4", "qhelpconverter-qt4": "/usr/local/bin/qhelpconverter-qt4", "qhelpgenerator-qt4": "/usr/local/bin/qhelpgenerator-qt4", "qmake-qt4": "/usr/local/bin/qmake-qt4", "qmlplugindump-qt4": "/usr/local/bin/qmlplugindump-qt4", "qmlviewer-qt4": "/usr/local/bin/qmlviewer-qt4", "qt3to4-qt4": "/usr/local/bin/qt3to4-qt4", "qtconfig-qt4": "/usr/local/bin/qtconfig-qt4", "qttracereplay-qt4": "/usr/local/bin/qttracereplay-qt4", "rcc-qt4": "/usr/local/bin/rcc-qt4", "scluster": "/usr/local/bin/scluster", "smix_hmm": "/usr/local/bin/smix_hmm", "swig": "/usr/local/bin/swig", "uic-qt4": "/usr/local/bin/uic-qt4", "xmlpatterns-qt4": "/usr/local/bin/xmlpatterns-qt4", "xmlpatternsvalidator-qt4": "/usr/local/bin/xmlpatternsvalidator-qt4", "cluster": "/usr/local/bin/cluster", "sip": "/usr/local/bin/sip", "qt.conf": "/usr/local/bin/qt.conf", "python2-config": "/usr/local/bin/python2-config", "python2.7-config": "/usr/local/bin/python2.7-config", "python2": "/usr/local/bin/python2", "python2.7": "/usr/local/bin/python2.7", "idle": "/usr/local/bin/idle", "python-config": "/usr/local/bin/python-config", "smtpd.py": "/usr/local/bin/smtpd.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pymix.
shpc-registry automated BioContainers addition for pymix
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pymix
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pymix:0.8--py27hcb787e7_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pymix/0.8--py27hcb787e7_1
$ module help quay.io/biocontainers/pymix/0.8--py27hcb787e7_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pymix-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pymix-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pymix-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pymix-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pymix-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pymix-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### assistant-qt4

```bash
$ singularity exec <container> /usr/local/bin/assistant-qt4
$ podman run --it --rm --entrypoint /usr/local/bin/assistant-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/assistant-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ccache-swig

```bash
$ singularity exec <container> /usr/local/bin/ccache-swig
$ podman run --it --rm --entrypoint /usr/local/bin/ccache-swig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccache-swig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### designer-qt4

```bash
$ singularity exec <container> /usr/local/bin/designer-qt4
$ podman run --it --rm --entrypoint /usr/local/bin/designer-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/designer-qt4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ghmm-config

```bash
$ singularity exec <container> /usr/local/bin/ghmm-config
$ podman run --it --rm --entrypoint /usr/local/bin/ghmm-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ghmm-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### probdist

```bash
$ singularity exec <container> /usr/local/bin/probdist
$ podman run --it --rm --entrypoint /usr/local/bin/probdist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/probdist   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### scluster

```bash
$ singularity exec <container> /usr/local/bin/scluster
$ podman run --it --rm --entrypoint /usr/local/bin/scluster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scluster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smix_hmm

```bash
$ singularity exec <container> /usr/local/bin/smix_hmm
$ podman run --it --rm --entrypoint /usr/local/bin/smix_hmm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smix_hmm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### swig

```bash
$ singularity exec <container> /usr/local/bin/swig
$ podman run --it --rm --entrypoint /usr/local/bin/swig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/swig   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### cluster

```bash
$ singularity exec <container> /usr/local/bin/cluster
$ podman run --it --rm --entrypoint /usr/local/bin/cluster   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cluster   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sip

```bash
$ singularity exec <container> /usr/local/bin/sip
$ podman run --it --rm --entrypoint /usr/local/bin/sip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qt.conf

```bash
$ singularity exec <container> /usr/local/bin/qt.conf
$ podman run --it --rm --entrypoint /usr/local/bin/qt.conf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qt.conf   -v ${PWD} -w ${PWD} <container> -c " $@"
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