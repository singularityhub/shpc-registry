---
layout: container
name:  "quay.io/biocontainers/fastk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastk/container.yaml"
updated_at: "2023-12-19 03:04:39.459085"
latest: "1.0--h4ef89c6_4"
container_url: "https://biocontainers.pro/tools/fastk"
aliases:
 - "FastK"
 - "Fastcp"
 - "Fastmerge"
 - "Fastmv"
 - "Fastrm"
 - "Haplex"
 - "Histex"
 - "Homex"
 - "Logex"
 - "Profex"
 - "Symmex"
 - "Tabex"
 - "Vennex"
versions:
 - "1.0--h3e8787d_1"
 - "1.0--h3e8787d_2"
 - "1.0--h4ef89c6_4"
description: "singularity registry hpc automated addition for fastk"
config: {"url": "https://biocontainers.pro/tools/fastk", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for fastk", "latest": {"1.0--h4ef89c6_4": "sha256:0503e48703d45e062b2b6875476241d7e95829f6b097b010e0c3476fa058f38a"}, "tags": {"1.0--h3e8787d_1": "sha256:4b7bfa967244033afaf0a70097d2951df519979cff99a6c6d56fc5c50356705b", "1.0--h3e8787d_2": "sha256:83fe636b9865e427afee92d748fb37c1b18eb3f4a4a641b585b050f53a1274d1", "1.0--h4ef89c6_4": "sha256:0503e48703d45e062b2b6875476241d7e95829f6b097b010e0c3476fa058f38a"}, "docker": "quay.io/biocontainers/fastk", "aliases": {"FastK": "/usr/local/bin/FastK", "Fastcp": "/usr/local/bin/Fastcp", "Fastmerge": "/usr/local/bin/Fastmerge", "Fastmv": "/usr/local/bin/Fastmv", "Fastrm": "/usr/local/bin/Fastrm", "Haplex": "/usr/local/bin/Haplex", "Histex": "/usr/local/bin/Histex", "Homex": "/usr/local/bin/Homex", "Logex": "/usr/local/bin/Logex", "Profex": "/usr/local/bin/Profex", "Symmex": "/usr/local/bin/Symmex", "Tabex": "/usr/local/bin/Tabex", "Vennex": "/usr/local/bin/Vennex"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastk.
singularity registry hpc automated addition for fastk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastk:1.0--h4ef89c6_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastk/1.0--h4ef89c6_4
$ module help quay.io/biocontainers/fastk/1.0--h4ef89c6_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### FastK

```bash
$ singularity exec <container> /usr/local/bin/FastK
$ podman run --it --rm --entrypoint /usr/local/bin/FastK   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FastK   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Fastcp

```bash
$ singularity exec <container> /usr/local/bin/Fastcp
$ podman run --it --rm --entrypoint /usr/local/bin/Fastcp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Fastcp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Fastmerge

```bash
$ singularity exec <container> /usr/local/bin/Fastmerge
$ podman run --it --rm --entrypoint /usr/local/bin/Fastmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Fastmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Fastmv

```bash
$ singularity exec <container> /usr/local/bin/Fastmv
$ podman run --it --rm --entrypoint /usr/local/bin/Fastmv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Fastmv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Fastrm

```bash
$ singularity exec <container> /usr/local/bin/Fastrm
$ podman run --it --rm --entrypoint /usr/local/bin/Fastrm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Fastrm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Haplex

```bash
$ singularity exec <container> /usr/local/bin/Haplex
$ podman run --it --rm --entrypoint /usr/local/bin/Haplex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Haplex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Histex

```bash
$ singularity exec <container> /usr/local/bin/Histex
$ podman run --it --rm --entrypoint /usr/local/bin/Histex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Histex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Homex

```bash
$ singularity exec <container> /usr/local/bin/Homex
$ podman run --it --rm --entrypoint /usr/local/bin/Homex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Homex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Logex

```bash
$ singularity exec <container> /usr/local/bin/Logex
$ podman run --it --rm --entrypoint /usr/local/bin/Logex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Logex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Profex

```bash
$ singularity exec <container> /usr/local/bin/Profex
$ podman run --it --rm --entrypoint /usr/local/bin/Profex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Profex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Symmex

```bash
$ singularity exec <container> /usr/local/bin/Symmex
$ podman run --it --rm --entrypoint /usr/local/bin/Symmex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Symmex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Tabex

```bash
$ singularity exec <container> /usr/local/bin/Tabex
$ podman run --it --rm --entrypoint /usr/local/bin/Tabex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Tabex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Vennex

```bash
$ singularity exec <container> /usr/local/bin/Vennex
$ podman run --it --rm --entrypoint /usr/local/bin/Vennex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Vennex   -v ${PWD} -w ${PWD} <container> -c " $@"
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