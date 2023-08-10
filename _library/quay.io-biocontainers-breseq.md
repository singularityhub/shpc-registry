---
layout: container
name:  "quay.io/biocontainers/breseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/breseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/breseq/container.yaml"
updated_at: "2023-08-10 03:12:59.702167"
latest: "0.38.1--h43eeafb_1"
container_url: "https://biocontainers.pro/tools/breseq"
aliases:
 - "breseq"
 - "gdtools"
 - "bowtie2"
 - "bowtie2-align-l"
 - "bowtie2-align-s"
 - "bowtie2-build"
 - "bowtie2-build-l"
 - "bowtie2-build-s"
 - "bowtie2-inspect"
 - "bowtie2-inspect-l"
 - "bowtie2-inspect-s"
 - "2to3-3.10"
versions:
 - "0.37.1--h5b5514e_0"
 - "0.37.1--h5b5514e_1"
 - "0.38.1--h5b5514e_0"
 - "0.38.1--h43eeafb_1"
description: "shpc-registry automated BioContainers addition for breseq"
config: {"url": "https://biocontainers.pro/tools/breseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for breseq", "latest": {"0.38.1--h43eeafb_1": "sha256:b51fb9df6e916cd45255e373760bbad0335a2020eb83d35fc72926be6706255e"}, "tags": {"0.37.1--h5b5514e_0": "sha256:a6200568daae92ababf6a575aba17899f2d0b355edf233a8c1644fdc81d07eb0", "0.37.1--h5b5514e_1": "sha256:22d2b0d6210d7e0cea68b521528fbfa06c335d26875bfc48c3445d31d2a38045", "0.38.1--h5b5514e_0": "sha256:17622715538290ed28c210327ec9e8027c7ba107803e1619808b5243e28257c0", "0.38.1--h43eeafb_1": "sha256:b51fb9df6e916cd45255e373760bbad0335a2020eb83d35fc72926be6706255e"}, "docker": "quay.io/biocontainers/breseq", "aliases": {"breseq": "/usr/local/bin/breseq", "gdtools": "/usr/local/bin/gdtools", "bowtie2": "/usr/local/bin/bowtie2", "bowtie2-align-l": "/usr/local/bin/bowtie2-align-l", "bowtie2-align-s": "/usr/local/bin/bowtie2-align-s", "bowtie2-build": "/usr/local/bin/bowtie2-build", "bowtie2-build-l": "/usr/local/bin/bowtie2-build-l", "bowtie2-build-s": "/usr/local/bin/bowtie2-build-s", "bowtie2-inspect": "/usr/local/bin/bowtie2-inspect", "bowtie2-inspect-l": "/usr/local/bin/bowtie2-inspect-l", "bowtie2-inspect-s": "/usr/local/bin/bowtie2-inspect-s", "2to3-3.10": "/usr/local/bin/2to3-3.10"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/breseq.
shpc-registry automated BioContainers addition for breseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/breseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/breseq:0.38.1--h43eeafb_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/breseq/0.38.1--h43eeafb_1
$ module help quay.io/biocontainers/breseq/0.38.1--h43eeafb_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### breseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### breseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### breseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### breseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### breseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### breseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### breseq

```bash
$ singularity exec <container> /usr/local/bin/breseq
$ podman run --it --rm --entrypoint /usr/local/bin/breseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/breseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdtools

```bash
$ singularity exec <container> /usr/local/bin/gdtools
$ podman run --it --rm --entrypoint /usr/local/bin/gdtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2

```bash
$ singularity exec <container> /usr/local/bin/bowtie2
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-align-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-align-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-align-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-align-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-build
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-build-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-build-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-inspect

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-inspect-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-inspect-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-inspect-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-inspect-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
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