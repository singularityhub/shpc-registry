---
layout: container
name:  "quay.io/biocontainers/blockclust"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/blockclust/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/blockclust/container.yaml"
updated_at: "2026-01-22 03:57:37.637581"
latest: "1.1.1--py311r44he264feb_2"
container_url: "https://biocontainers.pro/tools/blockclust"
aliases:
 - "EDeN"
 - "blockclust"
 - "blockclust.py"
 - "blockclust_plot.r"
 - "clm"
 - "clmformat"
 - "clxdo"
 - "mcl"
 - "mclblastline"
 - "mclcm"
 - "mclpipeline"
 - "mcx"
 - "mcxarray"
 - "mcxassemble"
versions:
 - "1.1.0--py36r41h2ad2d48_7"
 - "1.1.0--py37r42h96cfd12_8"
 - "1.1.0--py38r42h2494328_9"
 - "1.1.1--py39r43h1f90b4d_0"
 - "1.1.1--py310r43h0dbaff4_0"
 - "1.1.1--py311r43h2a4ad6c_1"
 - "1.1.1--py311r44he264feb_2"
description: "shpc-registry automated BioContainers addition for blockclust"
config: {"url": "https://biocontainers.pro/tools/blockclust", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for blockclust", "latest": {"1.1.1--py311r44he264feb_2": "sha256:d0dee103e3cb070bd17110669d109117de9b746734d4f658d9d8da28c3465ccd"}, "tags": {"1.1.0--py36r41h2ad2d48_7": "sha256:2216d30f270c5e8df9ff3e8d17f2581e5814e69ce1039033c46411093f67e7e4", "1.1.0--py37r42h96cfd12_8": "sha256:9fab3b8bd584a044d5c9a40d9181852af1ffeefebcc50ba81a3dbec68c19cc0e", "1.1.0--py38r42h2494328_9": "sha256:e9e8c742fa3cc348b4f1eece4679760f6844f8cf3d2b79447402144ee624fe9e", "1.1.1--py39r43h1f90b4d_0": "sha256:70c3271a0c60e4df91ea7232ae23918f594dc2cf76f94b2fa7dd284eca7382f4", "1.1.1--py310r43h0dbaff4_0": "sha256:7581d2fee96f7fb67fef7fc6e4146cd6b42c6953a0b22024fa21d2e97d33820a", "1.1.1--py311r43h2a4ad6c_1": "sha256:a848bf48f0eb35bd383b8d9344d43fb586de675ee34322f23d6520984fa224e0", "1.1.1--py311r44he264feb_2": "sha256:d0dee103e3cb070bd17110669d109117de9b746734d4f658d9d8da28c3465ccd"}, "docker": "quay.io/biocontainers/blockclust", "aliases": {"EDeN": "/usr/local/bin/EDeN", "blockclust": "/usr/local/bin/blockclust", "blockclust.py": "/usr/local/bin/blockclust.py", "blockclust_plot.r": "/usr/local/bin/blockclust_plot.r", "clm": "/usr/local/bin/clm", "clmformat": "/usr/local/bin/clmformat", "clxdo": "/usr/local/bin/clxdo", "mcl": "/usr/local/bin/mcl", "mclblastline": "/usr/local/bin/mclblastline", "mclcm": "/usr/local/bin/mclcm", "mclpipeline": "/usr/local/bin/mclpipeline", "mcx": "/usr/local/bin/mcx", "mcxarray": "/usr/local/bin/mcxarray", "mcxassemble": "/usr/local/bin/mcxassemble"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/blockclust.
shpc-registry automated BioContainers addition for blockclust
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/blockclust
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/blockclust:1.1.1--py311r44he264feb_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/blockclust/1.1.1--py311r44he264feb_2
$ module help quay.io/biocontainers/blockclust/1.1.1--py311r44he264feb_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### blockclust-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### blockclust-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### blockclust-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### blockclust-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### blockclust-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### blockclust-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### EDeN

```bash
$ singularity exec <container> /usr/local/bin/EDeN
$ podman run --it --rm --entrypoint /usr/local/bin/EDeN   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/EDeN   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blockclust

```bash
$ singularity exec <container> /usr/local/bin/blockclust
$ podman run --it --rm --entrypoint /usr/local/bin/blockclust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blockclust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blockclust.py

```bash
$ singularity exec <container> /usr/local/bin/blockclust.py
$ podman run --it --rm --entrypoint /usr/local/bin/blockclust.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blockclust.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blockclust_plot.r

```bash
$ singularity exec <container> /usr/local/bin/blockclust_plot.r
$ podman run --it --rm --entrypoint /usr/local/bin/blockclust_plot.r   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blockclust_plot.r   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clm

```bash
$ singularity exec <container> /usr/local/bin/clm
$ podman run --it --rm --entrypoint /usr/local/bin/clm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clmformat

```bash
$ singularity exec <container> /usr/local/bin/clmformat
$ podman run --it --rm --entrypoint /usr/local/bin/clmformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clmformat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clxdo

```bash
$ singularity exec <container> /usr/local/bin/clxdo
$ podman run --it --rm --entrypoint /usr/local/bin/clxdo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clxdo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcl

```bash
$ singularity exec <container> /usr/local/bin/mcl
$ podman run --it --rm --entrypoint /usr/local/bin/mcl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mclblastline

```bash
$ singularity exec <container> /usr/local/bin/mclblastline
$ podman run --it --rm --entrypoint /usr/local/bin/mclblastline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mclblastline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mclcm

```bash
$ singularity exec <container> /usr/local/bin/mclcm
$ podman run --it --rm --entrypoint /usr/local/bin/mclcm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mclcm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mclpipeline

```bash
$ singularity exec <container> /usr/local/bin/mclpipeline
$ podman run --it --rm --entrypoint /usr/local/bin/mclpipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mclpipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcx

```bash
$ singularity exec <container> /usr/local/bin/mcx
$ podman run --it --rm --entrypoint /usr/local/bin/mcx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcxarray

```bash
$ singularity exec <container> /usr/local/bin/mcxarray
$ podman run --it --rm --entrypoint /usr/local/bin/mcxarray   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcxarray   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcxassemble

```bash
$ singularity exec <container> /usr/local/bin/mcxassemble
$ podman run --it --rm --entrypoint /usr/local/bin/mcxassemble   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcxassemble   -v ${PWD} -w ${PWD} <container> -c " $@"
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