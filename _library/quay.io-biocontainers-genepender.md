---
layout: container
name:  "quay.io/biocontainers/genepender"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/genepender/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/genepender/container.yaml"
updated_at: "2024-06-28 02:47:15.257887"
latest: "v2.6--h470a237_1"
container_url: "https://biocontainers.pro/tools/genepender"
aliases:
 - "genepender"
 - "qdoc3"
 - "qmlviewer"
 - "qt3to4"
 - "qtconfig"
 - "qttracereplay"
 - "qhelpconverter"
 - "qdbus"
 - "qdbuscpp2xml"
 - "qdbusviewer"
 - "qdbusxml2cpp"
 - "xmlpatterns"
 - "xmlpatternsvalidator"
 - "assistant"
 - "designer"
 - "lconvert"
versions:
 - "v2.6--h470a237_1"
description: "shpc-registry automated BioContainers addition for genepender"
config: {"url": "https://biocontainers.pro/tools/genepender", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for genepender", "latest": {"v2.6--h470a237_1": "sha256:5796152d7ed6e316942b444943fd52c25198c202fff403b648bae20c9c91844e"}, "tags": {"v2.6--h470a237_1": "sha256:5796152d7ed6e316942b444943fd52c25198c202fff403b648bae20c9c91844e"}, "docker": "quay.io/biocontainers/genepender", "aliases": {"genepender": "/usr/local/bin/genepender", "qdoc3": "/usr/local/bin/qdoc3", "qmlviewer": "/usr/local/bin/qmlviewer", "qt3to4": "/usr/local/bin/qt3to4", "qtconfig": "/usr/local/bin/qtconfig", "qttracereplay": "/usr/local/bin/qttracereplay", "qhelpconverter": "/usr/local/bin/qhelpconverter", "qdbus": "/usr/local/bin/qdbus", "qdbuscpp2xml": "/usr/local/bin/qdbuscpp2xml", "qdbusviewer": "/usr/local/bin/qdbusviewer", "qdbusxml2cpp": "/usr/local/bin/qdbusxml2cpp", "xmlpatterns": "/usr/local/bin/xmlpatterns", "xmlpatternsvalidator": "/usr/local/bin/xmlpatternsvalidator", "assistant": "/usr/local/bin/assistant", "designer": "/usr/local/bin/designer", "lconvert": "/usr/local/bin/lconvert"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/genepender.
shpc-registry automated BioContainers addition for genepender
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/genepender
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/genepender:v2.6--h470a237_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/genepender/v2.6--h470a237_1
$ module help quay.io/biocontainers/genepender/v2.6--h470a237_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### genepender-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### genepender-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### genepender-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### genepender-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### genepender-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### genepender-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### genepender

```bash
$ singularity exec <container> /usr/local/bin/genepender
$ podman run --it --rm --entrypoint /usr/local/bin/genepender   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genepender   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### qhelpconverter

```bash
$ singularity exec <container> /usr/local/bin/qhelpconverter
$ podman run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### xmlpatterns

```bash
$ singularity exec <container> /usr/local/bin/xmlpatterns
$ podman run --it --rm --entrypoint /usr/local/bin/xmlpatterns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xmlpatterns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xmlpatternsvalidator

```bash
$ singularity exec <container> /usr/local/bin/xmlpatternsvalidator
$ podman run --it --rm --entrypoint /usr/local/bin/xmlpatternsvalidator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xmlpatternsvalidator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### assistant

```bash
$ singularity exec <container> /usr/local/bin/assistant
$ podman run --it --rm --entrypoint /usr/local/bin/assistant   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/assistant   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### designer

```bash
$ singularity exec <container> /usr/local/bin/designer
$ podman run --it --rm --entrypoint /usr/local/bin/designer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/designer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lconvert

```bash
$ singularity exec <container> /usr/local/bin/lconvert
$ podman run --it --rm --entrypoint /usr/local/bin/lconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
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