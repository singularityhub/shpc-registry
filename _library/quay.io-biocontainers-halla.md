---
layout: container
name:  "quay.io/biocontainers/halla"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/halla/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/halla/container.yaml"
updated_at: "2023-05-22 03:01:11.150175"
latest: "0.8.17--py36_0"
container_url: "https://biocontainers.pro/tools/halla"
aliases:
 - "halla"
 - "halladata"
 - "hallagram"
 - "hallascatter"
 - "g-ir-doc-tool"
 - "g-ir-annotation-tool"
 - "g-ir-compiler"
 - "g-ir-generate"
 - "g-ir-inspect"
 - "g-ir-scanner"
 - "f2py3.6"
 - "qhelpconverter"
 - "gtk-builder-convert"
 - "gtk-demo"
versions:
 - "0.8.17--py36_0"
description: "shpc-registry automated BioContainers addition for halla"
config: {"url": "https://biocontainers.pro/tools/halla", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for halla", "latest": {"0.8.17--py36_0": "sha256:4c4ae4051f8db1e777892a856a89447478a610d6f9a58858e754ab40637f0848"}, "tags": {"0.8.17--py36_0": "sha256:4c4ae4051f8db1e777892a856a89447478a610d6f9a58858e754ab40637f0848"}, "docker": "quay.io/biocontainers/halla", "aliases": {"halla": "/usr/local/bin/halla", "halladata": "/usr/local/bin/halladata", "hallagram": "/usr/local/bin/hallagram", "hallascatter": "/usr/local/bin/hallascatter", "g-ir-doc-tool": "/usr/local/bin/g-ir-doc-tool", "g-ir-annotation-tool": "/usr/local/bin/g-ir-annotation-tool", "g-ir-compiler": "/usr/local/bin/g-ir-compiler", "g-ir-generate": "/usr/local/bin/g-ir-generate", "g-ir-inspect": "/usr/local/bin/g-ir-inspect", "g-ir-scanner": "/usr/local/bin/g-ir-scanner", "f2py3.6": "/usr/local/bin/f2py3.6", "qhelpconverter": "/usr/local/bin/qhelpconverter", "gtk-builder-convert": "/usr/local/bin/gtk-builder-convert", "gtk-demo": "/usr/local/bin/gtk-demo"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/halla.
shpc-registry automated BioContainers addition for halla
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/halla
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/halla:0.8.17--py36_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/halla/0.8.17--py36_0
$ module help quay.io/biocontainers/halla/0.8.17--py36_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### halla-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### halla-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### halla-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### halla-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### halla-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### halla-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### halla

```bash
$ singularity exec <container> /usr/local/bin/halla
$ podman run --it --rm --entrypoint /usr/local/bin/halla   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/halla   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### halladata

```bash
$ singularity exec <container> /usr/local/bin/halladata
$ podman run --it --rm --entrypoint /usr/local/bin/halladata   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/halladata   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hallagram

```bash
$ singularity exec <container> /usr/local/bin/hallagram
$ podman run --it --rm --entrypoint /usr/local/bin/hallagram   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hallagram   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hallascatter

```bash
$ singularity exec <container> /usr/local/bin/hallascatter
$ podman run --it --rm --entrypoint /usr/local/bin/hallascatter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hallascatter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### g-ir-doc-tool

```bash
$ singularity exec <container> /usr/local/bin/g-ir-doc-tool
$ podman run --it --rm --entrypoint /usr/local/bin/g-ir-doc-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/g-ir-doc-tool   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### f2py3.6

```bash
$ singularity exec <container> /usr/local/bin/f2py3.6
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhelpconverter

```bash
$ singularity exec <container> /usr/local/bin/qhelpconverter
$ podman run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhelpconverter   -v ${PWD} -w ${PWD} <container> -c " $@"
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