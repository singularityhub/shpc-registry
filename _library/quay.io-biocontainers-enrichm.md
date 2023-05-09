---
layout: container
name:  "quay.io/biocontainers/enrichm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/enrichm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/enrichm/container.yaml"
updated_at: "2023-05-09 03:02:42.735020"
latest: "0.6.5--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/enrichm"
aliases:
 - "chronic"
 - "combine"
 - "enrichm"
 - "errno"
 - "ifdata"
 - "ifne"
 - "isutf8"
 - "lckdo"
 - "mispipe"
 - "pee"
 - "seqmagick"
 - "sponge"
 - "ts"
 - "vidir"
 - "vipe"
 - "zrun"
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
 - "0.6.4--pyhdfd78af_0"
 - "0.6.5--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for enrichm"
config: {"url": "https://biocontainers.pro/tools/enrichm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for enrichm", "latest": {"0.6.5--pyhdfd78af_0": "sha256:e97f9c0e571ae3c3f4c0e007f7d7af7ea2abec92affdd4fc4684266073f24eb7"}, "tags": {"0.6.4--pyhdfd78af_0": "sha256:0c6eeaf823e60524784724dfb740ee6ee0ec01406ac02a737351a1684bea9c09", "0.6.5--pyhdfd78af_0": "sha256:e97f9c0e571ae3c3f4c0e007f7d7af7ea2abec92affdd4fc4684266073f24eb7"}, "docker": "quay.io/biocontainers/enrichm", "aliases": {"chronic": "/usr/local/bin/chronic", "combine": "/usr/local/bin/combine", "enrichm": "/usr/local/bin/enrichm", "errno": "/usr/local/bin/errno", "ifdata": "/usr/local/bin/ifdata", "ifne": "/usr/local/bin/ifne", "isutf8": "/usr/local/bin/isutf8", "lckdo": "/usr/local/bin/lckdo", "mispipe": "/usr/local/bin/mispipe", "pee": "/usr/local/bin/pee", "seqmagick": "/usr/local/bin/seqmagick", "sponge": "/usr/local/bin/sponge", "ts": "/usr/local/bin/ts", "vidir": "/usr/local/bin/vidir", "vipe": "/usr/local/bin/vipe", "zrun": "/usr/local/bin/zrun", "clm": "/usr/local/bin/clm", "clmformat": "/usr/local/bin/clmformat", "clxdo": "/usr/local/bin/clxdo", "mcl": "/usr/local/bin/mcl", "mclblastline": "/usr/local/bin/mclblastline", "mclcm": "/usr/local/bin/mclcm", "mclpipeline": "/usr/local/bin/mclpipeline", "mcx": "/usr/local/bin/mcx", "mcxarray": "/usr/local/bin/mcxarray", "mcxassemble": "/usr/local/bin/mcxassemble"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/enrichm.
shpc-registry automated BioContainers addition for enrichm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/enrichm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/enrichm:0.6.5--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/enrichm/0.6.5--pyhdfd78af_0
$ module help quay.io/biocontainers/enrichm/0.6.5--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### enrichm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### enrichm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### enrichm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### enrichm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### enrichm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### enrichm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### chronic

```bash
$ singularity exec <container> /usr/local/bin/chronic
$ podman run --it --rm --entrypoint /usr/local/bin/chronic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chronic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### combine

```bash
$ singularity exec <container> /usr/local/bin/combine
$ podman run --it --rm --entrypoint /usr/local/bin/combine   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/combine   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### enrichm

```bash
$ singularity exec <container> /usr/local/bin/enrichm
$ podman run --it --rm --entrypoint /usr/local/bin/enrichm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/enrichm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### errno

```bash
$ singularity exec <container> /usr/local/bin/errno
$ podman run --it --rm --entrypoint /usr/local/bin/errno   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/errno   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ifdata

```bash
$ singularity exec <container> /usr/local/bin/ifdata
$ podman run --it --rm --entrypoint /usr/local/bin/ifdata   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ifdata   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ifne

```bash
$ singularity exec <container> /usr/local/bin/ifne
$ podman run --it --rm --entrypoint /usr/local/bin/ifne   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ifne   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isutf8

```bash
$ singularity exec <container> /usr/local/bin/isutf8
$ podman run --it --rm --entrypoint /usr/local/bin/isutf8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isutf8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lckdo

```bash
$ singularity exec <container> /usr/local/bin/lckdo
$ podman run --it --rm --entrypoint /usr/local/bin/lckdo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lckdo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mispipe

```bash
$ singularity exec <container> /usr/local/bin/mispipe
$ podman run --it --rm --entrypoint /usr/local/bin/mispipe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mispipe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pee

```bash
$ singularity exec <container> /usr/local/bin/pee
$ podman run --it --rm --entrypoint /usr/local/bin/pee   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pee   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqmagick

```bash
$ singularity exec <container> /usr/local/bin/seqmagick
$ podman run --it --rm --entrypoint /usr/local/bin/seqmagick   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqmagick   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sponge

```bash
$ singularity exec <container> /usr/local/bin/sponge
$ podman run --it --rm --entrypoint /usr/local/bin/sponge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sponge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ts

```bash
$ singularity exec <container> /usr/local/bin/ts
$ podman run --it --rm --entrypoint /usr/local/bin/ts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vidir

```bash
$ singularity exec <container> /usr/local/bin/vidir
$ podman run --it --rm --entrypoint /usr/local/bin/vidir   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vidir   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vipe

```bash
$ singularity exec <container> /usr/local/bin/vipe
$ podman run --it --rm --entrypoint /usr/local/bin/vipe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vipe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zrun

```bash
$ singularity exec <container> /usr/local/bin/zrun
$ podman run --it --rm --entrypoint /usr/local/bin/zrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zrun   -v ${PWD} -w ${PWD} <container> -c " $@"
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