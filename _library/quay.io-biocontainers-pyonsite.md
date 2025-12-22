---
layout: container
name:  "quay.io/biocontainers/pyonsite"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pyonsite/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pyonsite/container.yaml"
updated_at: "2025-12-22 03:52:08.173309"
latest: "0.0.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/pyonsite"
aliases:
 - "androiddeployqt6"
 - "ascore"
 - "assistant6"
 - "designer6"
 - "linguist6"
 - "lucxor"
 - "onsite"
 - "phospho-scoring"
 - "phosphors"
 - "phosphors-scoring"
 - "pixeltool6"
 - "qdbus6"
 - "qdbusviewer6"
 - "qdistancefieldgenerator6"
 - "qdoc6"
 - "qmake6"
 - "qml6"
 - "qmleasing6"
 - "qmlls6"
 - "qmlpreview6"
 - "qmlscene6"
 - "qt6.conf"
 - "qtdiag6"
 - "qtplugininfo6"
 - "svm-predict"
 - "svm-scale"
 - "svm-train"
 - "ldapadd"
 - "ldapcompare"
 - "ldapdelete"
 - "ldapexop"
 - "ldapmodify"
 - "ldapmodrdn"
 - "ldappasswd"
 - "ldapsearch"
 - "ldapurl"
 - "ldapvc"
 - "ldapwhoami"
 - "wayland-scanner"
 - "CreateDOMDocument"
 - "DOMCount"
 - "DOMPrint"
 - "EnumVal"
 - "MemParse"
 - "PParse"
 - "PSVIWriter"
 - "Redirect"
 - "SAX2Count"
 - "SAX2Print"
versions:
 - "0.0.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for pyonsite"
config: {"url": "https://biocontainers.pro/tools/pyonsite", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pyonsite", "latest": {"0.0.1--pyhdfd78af_0": "sha256:9b1b9e196eccd6aae8ffe3005b951f5471d464dd925a3a94c05b3b1de0eee810"}, "tags": {"0.0.1--pyhdfd78af_0": "sha256:9b1b9e196eccd6aae8ffe3005b951f5471d464dd925a3a94c05b3b1de0eee810"}, "docker": "quay.io/biocontainers/pyonsite", "aliases": {"androiddeployqt6": "/usr/local/bin/androiddeployqt6", "ascore": "/usr/local/bin/ascore", "assistant6": "/usr/local/bin/assistant6", "designer6": "/usr/local/bin/designer6", "linguist6": "/usr/local/bin/linguist6", "lucxor": "/usr/local/bin/lucxor", "onsite": "/usr/local/bin/onsite", "phospho-scoring": "/usr/local/bin/phospho-scoring", "phosphors": "/usr/local/bin/phosphors", "phosphors-scoring": "/usr/local/bin/phosphors-scoring", "pixeltool6": "/usr/local/bin/pixeltool6", "qdbus6": "/usr/local/bin/qdbus6", "qdbusviewer6": "/usr/local/bin/qdbusviewer6", "qdistancefieldgenerator6": "/usr/local/bin/qdistancefieldgenerator6", "qdoc6": "/usr/local/bin/qdoc6", "qmake6": "/usr/local/bin/qmake6", "qml6": "/usr/local/bin/qml6", "qmleasing6": "/usr/local/bin/qmleasing6", "qmlls6": "/usr/local/bin/qmlls6", "qmlpreview6": "/usr/local/bin/qmlpreview6", "qmlscene6": "/usr/local/bin/qmlscene6", "qt6.conf": "/usr/local/bin/qt6.conf", "qtdiag6": "/usr/local/bin/qtdiag6", "qtplugininfo6": "/usr/local/bin/qtplugininfo6", "svm-predict": "/usr/local/bin/svm-predict", "svm-scale": "/usr/local/bin/svm-scale", "svm-train": "/usr/local/bin/svm-train", "ldapadd": "/usr/local/bin/ldapadd", "ldapcompare": "/usr/local/bin/ldapcompare", "ldapdelete": "/usr/local/bin/ldapdelete", "ldapexop": "/usr/local/bin/ldapexop", "ldapmodify": "/usr/local/bin/ldapmodify", "ldapmodrdn": "/usr/local/bin/ldapmodrdn", "ldappasswd": "/usr/local/bin/ldappasswd", "ldapsearch": "/usr/local/bin/ldapsearch", "ldapurl": "/usr/local/bin/ldapurl", "ldapvc": "/usr/local/bin/ldapvc", "ldapwhoami": "/usr/local/bin/ldapwhoami", "wayland-scanner": "/usr/local/bin/wayland-scanner", "CreateDOMDocument": "/usr/local/bin/CreateDOMDocument", "DOMCount": "/usr/local/bin/DOMCount", "DOMPrint": "/usr/local/bin/DOMPrint", "EnumVal": "/usr/local/bin/EnumVal", "MemParse": "/usr/local/bin/MemParse", "PParse": "/usr/local/bin/PParse", "PSVIWriter": "/usr/local/bin/PSVIWriter", "Redirect": "/usr/local/bin/Redirect", "SAX2Count": "/usr/local/bin/SAX2Count", "SAX2Print": "/usr/local/bin/SAX2Print"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pyonsite.
singularity registry hpc automated addition for pyonsite
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pyonsite
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pyonsite:0.0.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pyonsite/0.0.1--pyhdfd78af_0
$ module help quay.io/biocontainers/pyonsite/0.0.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pyonsite-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pyonsite-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pyonsite-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pyonsite-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pyonsite-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pyonsite-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### androiddeployqt6

```bash
$ singularity exec <container> /usr/local/bin/androiddeployqt6
$ podman run --it --rm --entrypoint /usr/local/bin/androiddeployqt6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/androiddeployqt6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ascore

```bash
$ singularity exec <container> /usr/local/bin/ascore
$ podman run --it --rm --entrypoint /usr/local/bin/ascore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ascore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### assistant6

```bash
$ singularity exec <container> /usr/local/bin/assistant6
$ podman run --it --rm --entrypoint /usr/local/bin/assistant6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/assistant6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### designer6

```bash
$ singularity exec <container> /usr/local/bin/designer6
$ podman run --it --rm --entrypoint /usr/local/bin/designer6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/designer6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### linguist6

```bash
$ singularity exec <container> /usr/local/bin/linguist6
$ podman run --it --rm --entrypoint /usr/local/bin/linguist6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/linguist6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lucxor

```bash
$ singularity exec <container> /usr/local/bin/lucxor
$ podman run --it --rm --entrypoint /usr/local/bin/lucxor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lucxor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### onsite

```bash
$ singularity exec <container> /usr/local/bin/onsite
$ podman run --it --rm --entrypoint /usr/local/bin/onsite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/onsite   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phospho-scoring

```bash
$ singularity exec <container> /usr/local/bin/phospho-scoring
$ podman run --it --rm --entrypoint /usr/local/bin/phospho-scoring   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phospho-scoring   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phosphors

```bash
$ singularity exec <container> /usr/local/bin/phosphors
$ podman run --it --rm --entrypoint /usr/local/bin/phosphors   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phosphors   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phosphors-scoring

```bash
$ singularity exec <container> /usr/local/bin/phosphors-scoring
$ podman run --it --rm --entrypoint /usr/local/bin/phosphors-scoring   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phosphors-scoring   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pixeltool6

```bash
$ singularity exec <container> /usr/local/bin/pixeltool6
$ podman run --it --rm --entrypoint /usr/local/bin/pixeltool6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pixeltool6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdbus6

```bash
$ singularity exec <container> /usr/local/bin/qdbus6
$ podman run --it --rm --entrypoint /usr/local/bin/qdbus6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdbus6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdbusviewer6

```bash
$ singularity exec <container> /usr/local/bin/qdbusviewer6
$ podman run --it --rm --entrypoint /usr/local/bin/qdbusviewer6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdbusviewer6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdistancefieldgenerator6

```bash
$ singularity exec <container> /usr/local/bin/qdistancefieldgenerator6
$ podman run --it --rm --entrypoint /usr/local/bin/qdistancefieldgenerator6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdistancefieldgenerator6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdoc6

```bash
$ singularity exec <container> /usr/local/bin/qdoc6
$ podman run --it --rm --entrypoint /usr/local/bin/qdoc6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdoc6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qmake6

```bash
$ singularity exec <container> /usr/local/bin/qmake6
$ podman run --it --rm --entrypoint /usr/local/bin/qmake6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qmake6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qml6

```bash
$ singularity exec <container> /usr/local/bin/qml6
$ podman run --it --rm --entrypoint /usr/local/bin/qml6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qml6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qmleasing6

```bash
$ singularity exec <container> /usr/local/bin/qmleasing6
$ podman run --it --rm --entrypoint /usr/local/bin/qmleasing6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qmleasing6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qmlls6

```bash
$ singularity exec <container> /usr/local/bin/qmlls6
$ podman run --it --rm --entrypoint /usr/local/bin/qmlls6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qmlls6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qmlpreview6

```bash
$ singularity exec <container> /usr/local/bin/qmlpreview6
$ podman run --it --rm --entrypoint /usr/local/bin/qmlpreview6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qmlpreview6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qmlscene6

```bash
$ singularity exec <container> /usr/local/bin/qmlscene6
$ podman run --it --rm --entrypoint /usr/local/bin/qmlscene6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qmlscene6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qt6.conf

```bash
$ singularity exec <container> /usr/local/bin/qt6.conf
$ podman run --it --rm --entrypoint /usr/local/bin/qt6.conf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qt6.conf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qtdiag6

```bash
$ singularity exec <container> /usr/local/bin/qtdiag6
$ podman run --it --rm --entrypoint /usr/local/bin/qtdiag6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qtdiag6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qtplugininfo6

```bash
$ singularity exec <container> /usr/local/bin/qtplugininfo6
$ podman run --it --rm --entrypoint /usr/local/bin/qtplugininfo6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qtplugininfo6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svm-predict

```bash
$ singularity exec <container> /usr/local/bin/svm-predict
$ podman run --it --rm --entrypoint /usr/local/bin/svm-predict   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svm-predict   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svm-scale

```bash
$ singularity exec <container> /usr/local/bin/svm-scale
$ podman run --it --rm --entrypoint /usr/local/bin/svm-scale   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svm-scale   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svm-train

```bash
$ singularity exec <container> /usr/local/bin/svm-train
$ podman run --it --rm --entrypoint /usr/local/bin/svm-train   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svm-train   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapadd

```bash
$ singularity exec <container> /usr/local/bin/ldapadd
$ podman run --it --rm --entrypoint /usr/local/bin/ldapadd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapadd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapcompare

```bash
$ singularity exec <container> /usr/local/bin/ldapcompare
$ podman run --it --rm --entrypoint /usr/local/bin/ldapcompare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapcompare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapdelete

```bash
$ singularity exec <container> /usr/local/bin/ldapdelete
$ podman run --it --rm --entrypoint /usr/local/bin/ldapdelete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapdelete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapexop

```bash
$ singularity exec <container> /usr/local/bin/ldapexop
$ podman run --it --rm --entrypoint /usr/local/bin/ldapexop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapexop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapmodify

```bash
$ singularity exec <container> /usr/local/bin/ldapmodify
$ podman run --it --rm --entrypoint /usr/local/bin/ldapmodify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapmodify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapmodrdn

```bash
$ singularity exec <container> /usr/local/bin/ldapmodrdn
$ podman run --it --rm --entrypoint /usr/local/bin/ldapmodrdn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapmodrdn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldappasswd

```bash
$ singularity exec <container> /usr/local/bin/ldappasswd
$ podman run --it --rm --entrypoint /usr/local/bin/ldappasswd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldappasswd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapsearch

```bash
$ singularity exec <container> /usr/local/bin/ldapsearch
$ podman run --it --rm --entrypoint /usr/local/bin/ldapsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapurl

```bash
$ singularity exec <container> /usr/local/bin/ldapurl
$ podman run --it --rm --entrypoint /usr/local/bin/ldapurl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapurl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapvc

```bash
$ singularity exec <container> /usr/local/bin/ldapvc
$ podman run --it --rm --entrypoint /usr/local/bin/ldapvc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapvc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapwhoami

```bash
$ singularity exec <container> /usr/local/bin/ldapwhoami
$ podman run --it --rm --entrypoint /usr/local/bin/ldapwhoami   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapwhoami   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wayland-scanner

```bash
$ singularity exec <container> /usr/local/bin/wayland-scanner
$ podman run --it --rm --entrypoint /usr/local/bin/wayland-scanner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wayland-scanner   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CreateDOMDocument

```bash
$ singularity exec <container> /usr/local/bin/CreateDOMDocument
$ podman run --it --rm --entrypoint /usr/local/bin/CreateDOMDocument   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CreateDOMDocument   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DOMCount

```bash
$ singularity exec <container> /usr/local/bin/DOMCount
$ podman run --it --rm --entrypoint /usr/local/bin/DOMCount   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DOMCount   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### DOMPrint

```bash
$ singularity exec <container> /usr/local/bin/DOMPrint
$ podman run --it --rm --entrypoint /usr/local/bin/DOMPrint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DOMPrint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### EnumVal

```bash
$ singularity exec <container> /usr/local/bin/EnumVal
$ podman run --it --rm --entrypoint /usr/local/bin/EnumVal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/EnumVal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MemParse

```bash
$ singularity exec <container> /usr/local/bin/MemParse
$ podman run --it --rm --entrypoint /usr/local/bin/MemParse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MemParse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PParse

```bash
$ singularity exec <container> /usr/local/bin/PParse
$ podman run --it --rm --entrypoint /usr/local/bin/PParse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PParse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PSVIWriter

```bash
$ singularity exec <container> /usr/local/bin/PSVIWriter
$ podman run --it --rm --entrypoint /usr/local/bin/PSVIWriter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PSVIWriter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Redirect

```bash
$ singularity exec <container> /usr/local/bin/Redirect
$ podman run --it --rm --entrypoint /usr/local/bin/Redirect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Redirect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SAX2Count

```bash
$ singularity exec <container> /usr/local/bin/SAX2Count
$ podman run --it --rm --entrypoint /usr/local/bin/SAX2Count   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SAX2Count   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SAX2Print

```bash
$ singularity exec <container> /usr/local/bin/SAX2Print
$ podman run --it --rm --entrypoint /usr/local/bin/SAX2Print   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SAX2Print   -v ${PWD} -w ${PWD} <container> -c " $@"
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