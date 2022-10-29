---
layout: container
name:  "quay.io/biocontainers/r-rtassel"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-rtassel/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/r-rtassel/container.yaml"
updated_at: "2022-10-29 05:53:22.547825"
latest: "0.1.2019.07.25--r41h9ee0642_3"
container_url: "https://biocontainers.pro/tools/r-rtassel"
aliases:
 - "aserver"
 - "gif2rgb"
 - "gifbuild"
 - "gifclrmp"
 - "giffix"
 - "giftext"
 - "giftool"
 - "jaotc"
 - "jar"
 - "jarsigner"
versions:
 - "0.1.2019.07.25--r41h9ee0642_3"
description: "shpc-registry automated BioContainers addition for r-rtassel"
config: {"url": "https://biocontainers.pro/tools/r-rtassel", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-rtassel", "latest": {"0.1.2019.07.25--r41h9ee0642_3": "sha256:57f4ff458e5970d0b518d8f4ee765542f89fba3dae8fa0b3865b2aaf81043332"}, "tags": {"0.1.2019.07.25--r41h9ee0642_3": "sha256:57f4ff458e5970d0b518d8f4ee765542f89fba3dae8fa0b3865b2aaf81043332"}, "docker": "quay.io/biocontainers/r-rtassel", "aliases": {"aserver": "/usr/local/bin/aserver", "gif2rgb": "/usr/local/bin/gif2rgb", "gifbuild": "/usr/local/bin/gifbuild", "gifclrmp": "/usr/local/bin/gifclrmp", "giffix": "/usr/local/bin/giffix", "giftext": "/usr/local/bin/giftext", "giftool": "/usr/local/bin/giftool", "jaotc": "/usr/local/bin/jaotc", "jar": "/usr/local/bin/jar", "jarsigner": "/usr/local/bin/jarsigner"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-rtassel.
shpc-registry automated BioContainers addition for r-rtassel
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-rtassel
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-rtassel:0.1.2019.07.25--r41h9ee0642_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-rtassel/0.1.2019.07.25--r41h9ee0642_3
$ module help quay.io/biocontainers/r-rtassel/0.1.2019.07.25--r41h9ee0642_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-rtassel-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-rtassel-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-rtassel-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-rtassel-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-rtassel-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-rtassel-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2rgb

```bash
$ singularity exec <container> /usr/local/bin/gif2rgb
$ podman run --it --rm --entrypoint /usr/local/bin/gif2rgb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2rgb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifbuild

```bash
$ singularity exec <container> /usr/local/bin/gifbuild
$ podman run --it --rm --entrypoint /usr/local/bin/gifbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gifclrmp

```bash
$ singularity exec <container> /usr/local/bin/gifclrmp
$ podman run --it --rm --entrypoint /usr/local/bin/gifclrmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gifclrmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### giffix

```bash
$ singularity exec <container> /usr/local/bin/giffix
$ podman run --it --rm --entrypoint /usr/local/bin/giffix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/giffix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### giftext

```bash
$ singularity exec <container> /usr/local/bin/giftext
$ podman run --it --rm --entrypoint /usr/local/bin/giftext   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/giftext   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### giftool

```bash
$ singularity exec <container> /usr/local/bin/giftool
$ podman run --it --rm --entrypoint /usr/local/bin/giftool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/giftool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jaotc

```bash
$ singularity exec <container> /usr/local/bin/jaotc
$ podman run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jar

```bash
$ singularity exec <container> /usr/local/bin/jar
$ podman run --it --rm --entrypoint /usr/local/bin/jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jarsigner

```bash
$ singularity exec <container> /usr/local/bin/jarsigner
$ podman run --it --rm --entrypoint /usr/local/bin/jarsigner   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jarsigner   -v ${PWD} -w ${PWD} <container> -c " $@"
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