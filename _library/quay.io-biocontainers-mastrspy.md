---
layout: container
name:  "quay.io/biocontainers/mastrspy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mastrspy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mastrspy/container.yaml"
updated_at: "2026-06-17 07:14:48.594048"
latest: "1.1.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/mastrspy"
aliases:
 - "android_deploy.py"
 - "deploy.py"
 - "kmap2qmap6"
 - "lcheck6"
 - "lconvert6"
 - "lrelease-pro6"
 - "lrelease6"
 - "ltext2id6"
 - "lupdate-pro6"
 - "lupdate6"
 - "mastrspy"
 - "metaobjectdump.py"
 - "project.py"
 - "pyside6-rcc"
 - "pyside6-uic"
 - "qml.py"
 - "qtpy2cpp.py"
 - "requirements-android.txt"
 - "shiboken6"
 - "shiboken_tool.py"
 - "wasmdeployqt6"
 - "androiddeployqt6"
 - "assistant6"
 - "designer6"
 - "linguist6"
 - "pixeltool6"
 - "qdbus6"
 - "qdbusviewer6"
 - "qdistancefieldgenerator6"
 - "qmake6"
 - "qml6"
 - "qmleasing6"
 - "qmlls6"
 - "qmlpreview6"
 - "qmlscene6"
 - "qt6.conf"
 - "qtdiag6"
 - "qtplugininfo6"
 - "ldapadd"
 - "ldapcompare"
 - "ldapdelete"
 - "ldapexop"
 - "ldapmodify"
 - "ldapmodrdn"
 - "ldappasswd"
 - "ldapsearch"
versions:
 - "1.1.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for mastrspy"
config: {"url": "https://biocontainers.pro/tools/mastrspy", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mastrspy", "latest": {"1.1.0--pyhdfd78af_0": "sha256:7cc9a011d1b6885f1de74e374d320c26be856ab48be0309996809ad1ed289da8"}, "tags": {"1.1.0--pyhdfd78af_0": "sha256:7cc9a011d1b6885f1de74e374d320c26be856ab48be0309996809ad1ed289da8"}, "docker": "quay.io/biocontainers/mastrspy", "aliases": {"android_deploy.py": "/usr/local/bin/android_deploy.py", "deploy.py": "/usr/local/bin/deploy.py", "kmap2qmap6": "/usr/local/bin/kmap2qmap6", "lcheck6": "/usr/local/bin/lcheck6", "lconvert6": "/usr/local/bin/lconvert6", "lrelease-pro6": "/usr/local/bin/lrelease-pro6", "lrelease6": "/usr/local/bin/lrelease6", "ltext2id6": "/usr/local/bin/ltext2id6", "lupdate-pro6": "/usr/local/bin/lupdate-pro6", "lupdate6": "/usr/local/bin/lupdate6", "mastrspy": "/usr/local/bin/mastrspy", "metaobjectdump.py": "/usr/local/bin/metaobjectdump.py", "project.py": "/usr/local/bin/project.py", "pyside6-rcc": "/usr/local/bin/pyside6-rcc", "pyside6-uic": "/usr/local/bin/pyside6-uic", "qml.py": "/usr/local/bin/qml.py", "qtpy2cpp.py": "/usr/local/bin/qtpy2cpp.py", "requirements-android.txt": "/usr/local/bin/requirements-android.txt", "shiboken6": "/usr/local/bin/shiboken6", "shiboken_tool.py": "/usr/local/bin/shiboken_tool.py", "wasmdeployqt6": "/usr/local/bin/wasmdeployqt6", "androiddeployqt6": "/usr/local/bin/androiddeployqt6", "assistant6": "/usr/local/bin/assistant6", "designer6": "/usr/local/bin/designer6", "linguist6": "/usr/local/bin/linguist6", "pixeltool6": "/usr/local/bin/pixeltool6", "qdbus6": "/usr/local/bin/qdbus6", "qdbusviewer6": "/usr/local/bin/qdbusviewer6", "qdistancefieldgenerator6": "/usr/local/bin/qdistancefieldgenerator6", "qmake6": "/usr/local/bin/qmake6", "qml6": "/usr/local/bin/qml6", "qmleasing6": "/usr/local/bin/qmleasing6", "qmlls6": "/usr/local/bin/qmlls6", "qmlpreview6": "/usr/local/bin/qmlpreview6", "qmlscene6": "/usr/local/bin/qmlscene6", "qt6.conf": "/usr/local/bin/qt6.conf", "qtdiag6": "/usr/local/bin/qtdiag6", "qtplugininfo6": "/usr/local/bin/qtplugininfo6", "ldapadd": "/usr/local/bin/ldapadd", "ldapcompare": "/usr/local/bin/ldapcompare", "ldapdelete": "/usr/local/bin/ldapdelete", "ldapexop": "/usr/local/bin/ldapexop", "ldapmodify": "/usr/local/bin/ldapmodify", "ldapmodrdn": "/usr/local/bin/ldapmodrdn", "ldappasswd": "/usr/local/bin/ldappasswd", "ldapsearch": "/usr/local/bin/ldapsearch"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mastrspy.
singularity registry hpc automated addition for mastrspy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mastrspy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mastrspy:1.1.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mastrspy/1.1.0--pyhdfd78af_0
$ module help quay.io/biocontainers/mastrspy/1.1.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mastrspy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mastrspy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mastrspy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mastrspy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mastrspy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mastrspy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### android_deploy.py

```bash
$ singularity exec <container> /usr/local/bin/android_deploy.py
$ podman run --it --rm --entrypoint /usr/local/bin/android_deploy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/android_deploy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### deploy.py

```bash
$ singularity exec <container> /usr/local/bin/deploy.py
$ podman run --it --rm --entrypoint /usr/local/bin/deploy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deploy.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kmap2qmap6

```bash
$ singularity exec <container> /usr/local/bin/kmap2qmap6
$ podman run --it --rm --entrypoint /usr/local/bin/kmap2qmap6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kmap2qmap6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lcheck6

```bash
$ singularity exec <container> /usr/local/bin/lcheck6
$ podman run --it --rm --entrypoint /usr/local/bin/lcheck6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lcheck6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lconvert6

```bash
$ singularity exec <container> /usr/local/bin/lconvert6
$ podman run --it --rm --entrypoint /usr/local/bin/lconvert6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lconvert6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrelease-pro6

```bash
$ singularity exec <container> /usr/local/bin/lrelease-pro6
$ podman run --it --rm --entrypoint /usr/local/bin/lrelease-pro6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrelease-pro6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrelease6

```bash
$ singularity exec <container> /usr/local/bin/lrelease6
$ podman run --it --rm --entrypoint /usr/local/bin/lrelease6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrelease6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ltext2id6

```bash
$ singularity exec <container> /usr/local/bin/ltext2id6
$ podman run --it --rm --entrypoint /usr/local/bin/ltext2id6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ltext2id6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lupdate-pro6

```bash
$ singularity exec <container> /usr/local/bin/lupdate-pro6
$ podman run --it --rm --entrypoint /usr/local/bin/lupdate-pro6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lupdate-pro6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lupdate6

```bash
$ singularity exec <container> /usr/local/bin/lupdate6
$ podman run --it --rm --entrypoint /usr/local/bin/lupdate6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lupdate6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mastrspy

```bash
$ singularity exec <container> /usr/local/bin/mastrspy
$ podman run --it --rm --entrypoint /usr/local/bin/mastrspy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mastrspy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metaobjectdump.py

```bash
$ singularity exec <container> /usr/local/bin/metaobjectdump.py
$ podman run --it --rm --entrypoint /usr/local/bin/metaobjectdump.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaobjectdump.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### project.py

```bash
$ singularity exec <container> /usr/local/bin/project.py
$ podman run --it --rm --entrypoint /usr/local/bin/project.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/project.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyside6-rcc

```bash
$ singularity exec <container> /usr/local/bin/pyside6-rcc
$ podman run --it --rm --entrypoint /usr/local/bin/pyside6-rcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyside6-rcc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyside6-uic

```bash
$ singularity exec <container> /usr/local/bin/pyside6-uic
$ podman run --it --rm --entrypoint /usr/local/bin/pyside6-uic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyside6-uic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qml.py

```bash
$ singularity exec <container> /usr/local/bin/qml.py
$ podman run --it --rm --entrypoint /usr/local/bin/qml.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qml.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qtpy2cpp.py

```bash
$ singularity exec <container> /usr/local/bin/qtpy2cpp.py
$ podman run --it --rm --entrypoint /usr/local/bin/qtpy2cpp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qtpy2cpp.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### requirements-android.txt

```bash
$ singularity exec <container> /usr/local/bin/requirements-android.txt
$ podman run --it --rm --entrypoint /usr/local/bin/requirements-android.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/requirements-android.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiboken6

```bash
$ singularity exec <container> /usr/local/bin/shiboken6
$ podman run --it --rm --entrypoint /usr/local/bin/shiboken6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiboken6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiboken_tool.py

```bash
$ singularity exec <container> /usr/local/bin/shiboken_tool.py
$ podman run --it --rm --entrypoint /usr/local/bin/shiboken_tool.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiboken_tool.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wasmdeployqt6

```bash
$ singularity exec <container> /usr/local/bin/wasmdeployqt6
$ podman run --it --rm --entrypoint /usr/local/bin/wasmdeployqt6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wasmdeployqt6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### androiddeployqt6

```bash
$ singularity exec <container> /usr/local/bin/androiddeployqt6
$ podman run --it --rm --entrypoint /usr/local/bin/androiddeployqt6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/androiddeployqt6   -v ${PWD} -w ${PWD} <container> -c " $@"
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