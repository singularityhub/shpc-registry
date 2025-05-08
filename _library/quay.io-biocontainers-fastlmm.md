---
layout: container
name:  "quay.io/biocontainers/fastlmm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastlmm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastlmm/container.yaml"
updated_at: "2025-05-08 05:41:02.834760"
latest: "0.2.32--py27h95a95ce_5"
container_url: "https://biocontainers.pro/tools/fastlmm"
aliases:
 - "get_objgraph"
 - "undill"
 - "qhelpconverter"
 - "f2py2"
 - "f2py2.7"
 - "qwebengine_convert_dict"
 - "canbusutil"
 - "qgltf"
 - "qmlcachegen"
 - "qscxmlc"
versions:
 - "0.2.32--py27h95a95ce_5"
description: "shpc-registry automated BioContainers addition for fastlmm"
config: {"url": "https://biocontainers.pro/tools/fastlmm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fastlmm", "latest": {"0.2.32--py27h95a95ce_5": "sha256:b060d9d2dedcf02b770fb469645b4dc68b488173caa9669fac9bdcfc3e0a78a0"}, "tags": {"0.2.32--py27h95a95ce_5": "sha256:b060d9d2dedcf02b770fb469645b4dc68b488173caa9669fac9bdcfc3e0a78a0"}, "docker": "quay.io/biocontainers/fastlmm", "aliases": {"get_objgraph": "/usr/local/bin/get_objgraph", "undill": "/usr/local/bin/undill", "qhelpconverter": "/usr/local/bin/qhelpconverter", "f2py2": "/usr/local/bin/f2py2", "f2py2.7": "/usr/local/bin/f2py2.7", "qwebengine_convert_dict": "/usr/local/bin/qwebengine_convert_dict", "canbusutil": "/usr/local/bin/canbusutil", "qgltf": "/usr/local/bin/qgltf", "qmlcachegen": "/usr/local/bin/qmlcachegen", "qscxmlc": "/usr/local/bin/qscxmlc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastlmm.
shpc-registry automated BioContainers addition for fastlmm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastlmm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastlmm:0.2.32--py27h95a95ce_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastlmm/0.2.32--py27h95a95ce_5
$ module help quay.io/biocontainers/fastlmm/0.2.32--py27h95a95ce_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastlmm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastlmm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastlmm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastlmm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastlmm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastlmm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### get_objgraph

```bash
$ singularity exec <container> /usr/local/bin/get_objgraph
$ podman run --it --rm --entrypoint /usr/local/bin/get_objgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get_objgraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### undill

```bash
$ singularity exec <container> /usr/local/bin/undill
$ podman run --it --rm --entrypoint /usr/local/bin/undill   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/undill   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhelpconverter

```bash
$ singularity exec <container> /usr/local/bin/qhelpconverter
$ podman run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2

```bash
$ singularity exec <container> /usr/local/bin/f2py2
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py2.7

```bash
$ singularity exec <container> /usr/local/bin/f2py2.7
$ podman run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py2.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qwebengine_convert_dict

```bash
$ singularity exec <container> /usr/local/bin/qwebengine_convert_dict
$ podman run --it --rm --entrypoint /usr/local/bin/qwebengine_convert_dict   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qwebengine_convert_dict   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### canbusutil

```bash
$ singularity exec <container> /usr/local/bin/canbusutil
$ podman run --it --rm --entrypoint /usr/local/bin/canbusutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/canbusutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qgltf

```bash
$ singularity exec <container> /usr/local/bin/qgltf
$ podman run --it --rm --entrypoint /usr/local/bin/qgltf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qgltf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qmlcachegen

```bash
$ singularity exec <container> /usr/local/bin/qmlcachegen
$ podman run --it --rm --entrypoint /usr/local/bin/qmlcachegen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qmlcachegen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qscxmlc

```bash
$ singularity exec <container> /usr/local/bin/qscxmlc
$ podman run --it --rm --entrypoint /usr/local/bin/qscxmlc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qscxmlc   -v ${PWD} -w ${PWD} <container> -c " $@"
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