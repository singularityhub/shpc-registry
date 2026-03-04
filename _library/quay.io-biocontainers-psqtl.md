---
layout: container
name:  "quay.io/biocontainers/psqtl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/psqtl/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/psqtl/container.yaml"
updated_at: "2026-03-04 04:59:56.820630"
latest: "1.3.7--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/psqtl"
aliases:
 - "gff2gff"
 - "psQTL_post"
 - "psQTL_post.py"
 - "psQTL_prep"
 - "psQTL_prep.py"
 - "psQTL_proc"
 - "psQTL_proc.py"
 - "roh-viz"
 - "vrfs-variances"
 - "androiddeployqt6"
 - "assistant6"
 - "designer6"
 - "linguist6"
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
 - "vt"
 - "ldapadd"
 - "ldapcompare"
 - "ldapdelete"
 - "ldapexop"
 - "ldapmodify"
 - "ldapmodrdn"
versions:
 - "1.3.7--hdfd78af_0"
description: "singularity registry hpc automated addition for psqtl"
config: {"url": "https://biocontainers.pro/tools/psqtl", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for psqtl", "latest": {"1.3.7--hdfd78af_0": "sha256:8132a05f5140dafa70b220fb285731576371588831f409cfbc87e1e8ce17b6ac"}, "tags": {"1.3.7--hdfd78af_0": "sha256:8132a05f5140dafa70b220fb285731576371588831f409cfbc87e1e8ce17b6ac"}, "docker": "quay.io/biocontainers/psqtl", "aliases": {"gff2gff": "/usr/local/bin/gff2gff", "psQTL_post": "/usr/local/bin/psQTL_post", "psQTL_post.py": "/usr/local/bin/psQTL_post.py", "psQTL_prep": "/usr/local/bin/psQTL_prep", "psQTL_prep.py": "/usr/local/bin/psQTL_prep.py", "psQTL_proc": "/usr/local/bin/psQTL_proc", "psQTL_proc.py": "/usr/local/bin/psQTL_proc.py", "roh-viz": "/usr/local/bin/roh-viz", "vrfs-variances": "/usr/local/bin/vrfs-variances", "androiddeployqt6": "/usr/local/bin/androiddeployqt6", "assistant6": "/usr/local/bin/assistant6", "designer6": "/usr/local/bin/designer6", "linguist6": "/usr/local/bin/linguist6", "pixeltool6": "/usr/local/bin/pixeltool6", "qdbus6": "/usr/local/bin/qdbus6", "qdbusviewer6": "/usr/local/bin/qdbusviewer6", "qdistancefieldgenerator6": "/usr/local/bin/qdistancefieldgenerator6", "qdoc6": "/usr/local/bin/qdoc6", "qmake6": "/usr/local/bin/qmake6", "qml6": "/usr/local/bin/qml6", "qmleasing6": "/usr/local/bin/qmleasing6", "qmlls6": "/usr/local/bin/qmlls6", "qmlpreview6": "/usr/local/bin/qmlpreview6", "qmlscene6": "/usr/local/bin/qmlscene6", "qt6.conf": "/usr/local/bin/qt6.conf", "qtdiag6": "/usr/local/bin/qtdiag6", "qtplugininfo6": "/usr/local/bin/qtplugininfo6", "vt": "/usr/local/bin/vt", "ldapadd": "/usr/local/bin/ldapadd", "ldapcompare": "/usr/local/bin/ldapcompare", "ldapdelete": "/usr/local/bin/ldapdelete", "ldapexop": "/usr/local/bin/ldapexop", "ldapmodify": "/usr/local/bin/ldapmodify", "ldapmodrdn": "/usr/local/bin/ldapmodrdn"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/psqtl.
singularity registry hpc automated addition for psqtl
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/psqtl
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/psqtl:1.3.7--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/psqtl/1.3.7--hdfd78af_0
$ module help quay.io/biocontainers/psqtl/1.3.7--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### psqtl-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### psqtl-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### psqtl-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### psqtl-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### psqtl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### psqtl-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gff2gff

```bash
$ singularity exec <container> /usr/local/bin/gff2gff
$ podman run --it --rm --entrypoint /usr/local/bin/gff2gff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2gff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psQTL_post

```bash
$ singularity exec <container> /usr/local/bin/psQTL_post
$ podman run --it --rm --entrypoint /usr/local/bin/psQTL_post   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psQTL_post   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psQTL_post.py

```bash
$ singularity exec <container> /usr/local/bin/psQTL_post.py
$ podman run --it --rm --entrypoint /usr/local/bin/psQTL_post.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psQTL_post.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psQTL_prep

```bash
$ singularity exec <container> /usr/local/bin/psQTL_prep
$ podman run --it --rm --entrypoint /usr/local/bin/psQTL_prep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psQTL_prep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psQTL_prep.py

```bash
$ singularity exec <container> /usr/local/bin/psQTL_prep.py
$ podman run --it --rm --entrypoint /usr/local/bin/psQTL_prep.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psQTL_prep.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psQTL_proc

```bash
$ singularity exec <container> /usr/local/bin/psQTL_proc
$ podman run --it --rm --entrypoint /usr/local/bin/psQTL_proc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psQTL_proc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psQTL_proc.py

```bash
$ singularity exec <container> /usr/local/bin/psQTL_proc.py
$ podman run --it --rm --entrypoint /usr/local/bin/psQTL_proc.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psQTL_proc.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### roh-viz

```bash
$ singularity exec <container> /usr/local/bin/roh-viz
$ podman run --it --rm --entrypoint /usr/local/bin/roh-viz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/roh-viz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vrfs-variances

```bash
$ singularity exec <container> /usr/local/bin/vrfs-variances
$ podman run --it --rm --entrypoint /usr/local/bin/vrfs-variances   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vrfs-variances   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### vt

```bash
$ singularity exec <container> /usr/local/bin/vt
$ podman run --it --rm --entrypoint /usr/local/bin/vt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vt   -v ${PWD} -w ${PWD} <container> -c " $@"
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