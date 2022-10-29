---
layout: container
name:  "quay.io/biocontainers/sqt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sqt/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/sqt/container.yaml"
updated_at: "2022-10-29 05:39:27.090088"
latest: "0.8.0--py37h8902056_4"
container_url: "https://biocontainers.pro/tools/sqt"
aliases:
 - "sqt"
 - "2to3-3.7"
 - "aserver"
 - "assistant"
 - "attr"
 - "balsam"
 - "brotli"
 - "canbusutil"
 - "certutil"
 - "cups-config"
 - "cutadapt"
versions:
 - "0.8.0--py37h8902056_4"
description: "shpc-registry automated BioContainers addition for sqt"
config: {"url": "https://biocontainers.pro/tools/sqt", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sqt", "latest": {"0.8.0--py37h8902056_4": "sha256:5f7ab5a66822393ae7ad5798c623ed65d152131c65278acf32bc8db302ad1519"}, "tags": {"0.8.0--py37h8902056_4": "sha256:5f7ab5a66822393ae7ad5798c623ed65d152131c65278acf32bc8db302ad1519"}, "docker": "quay.io/biocontainers/sqt", "aliases": {"sqt": "/usr/local/bin/sqt", "2to3-3.7": "/usr/local/bin/2to3-3.7", "aserver": "/usr/local/bin/aserver", "assistant": "/usr/local/bin/assistant", "attr": "/usr/local/bin/attr", "balsam": "/usr/local/bin/balsam", "brotli": "/usr/local/bin/brotli", "canbusutil": "/usr/local/bin/canbusutil", "certutil": "/usr/local/bin/certutil", "cups-config": "/usr/local/bin/cups-config", "cutadapt": "/usr/local/bin/cutadapt"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sqt.
shpc-registry automated BioContainers addition for sqt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sqt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sqt:0.8.0--py37h8902056_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sqt/0.8.0--py37h8902056_4
$ module help quay.io/biocontainers/sqt/0.8.0--py37h8902056_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sqt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sqt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sqt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sqt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sqt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sqt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sqt

```bash
$ singularity exec <container> /usr/local/bin/sqt
$ podman run --it --rm --entrypoint /usr/local/bin/sqt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sqt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### assistant

```bash
$ singularity exec <container> /usr/local/bin/assistant
$ podman run --it --rm --entrypoint /usr/local/bin/assistant   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/assistant   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### attr

```bash
$ singularity exec <container> /usr/local/bin/attr
$ podman run --it --rm --entrypoint /usr/local/bin/attr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/attr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### balsam

```bash
$ singularity exec <container> /usr/local/bin/balsam
$ podman run --it --rm --entrypoint /usr/local/bin/balsam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/balsam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### brotli

```bash
$ singularity exec <container> /usr/local/bin/brotli
$ podman run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/brotli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### canbusutil

```bash
$ singularity exec <container> /usr/local/bin/canbusutil
$ podman run --it --rm --entrypoint /usr/local/bin/canbusutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/canbusutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### certutil

```bash
$ singularity exec <container> /usr/local/bin/certutil
$ podman run --it --rm --entrypoint /usr/local/bin/certutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/certutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cups-config

```bash
$ singularity exec <container> /usr/local/bin/cups-config
$ podman run --it --rm --entrypoint /usr/local/bin/cups-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cups-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cutadapt

```bash
$ singularity exec <container> /usr/local/bin/cutadapt
$ podman run --it --rm --entrypoint /usr/local/bin/cutadapt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cutadapt   -v ${PWD} -w ${PWD} <container> -c " $@"
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