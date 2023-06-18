---
layout: container
name:  "quay.io/biocontainers/mcl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mcl/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mcl/container.yaml"
updated_at: "2023-06-18 03:26:21.914190"
latest: "14.137--pl5321h031d066_9"
container_url: "https://biocontainers.pro/tools/mcl"
aliases:
 - "mcl"
 - "mclblastline"
 - "mclcm"
 - "mclpipeline"
 - "clm"
 - "clmformat"
 - "clxdo"
 - "mcx"
 - "mcxarray"
 - "mcxassemble"
 - "mcxdeblast"
 - "mcxdump"
 - "mcxi"
 - "mcxload"
versions:
 - "14.137--pl5321hec16e2b_8"
 - "14.137--pl5321h031d066_9"
description: "shpc-registry automated BioContainers addition for mcl"
config: {"url": "https://biocontainers.pro/tools/mcl", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mcl", "latest": {"14.137--pl5321h031d066_9": "sha256:576283dc19b0880e40e47a803c1c1f66b1d095066fdbbef70fb9fd4a35fa9c77"}, "tags": {"14.137--pl5321hec16e2b_8": "sha256:18327f4fcf1427fa7fcd08b852dfc7597581871ae23d86603333aa28593c94ac", "14.137--pl5321h031d066_9": "sha256:576283dc19b0880e40e47a803c1c1f66b1d095066fdbbef70fb9fd4a35fa9c77"}, "docker": "quay.io/biocontainers/mcl", "aliases": {"mcl": "/usr/local/bin/mcl", "mclblastline": "/usr/local/bin/mclblastline", "mclcm": "/usr/local/bin/mclcm", "mclpipeline": "/usr/local/bin/mclpipeline", "clm": "/usr/local/bin/clm", "clmformat": "/usr/local/bin/clmformat", "clxdo": "/usr/local/bin/clxdo", "mcx": "/usr/local/bin/mcx", "mcxarray": "/usr/local/bin/mcxarray", "mcxassemble": "/usr/local/bin/mcxassemble", "mcxdeblast": "/usr/local/bin/mcxdeblast", "mcxdump": "/usr/local/bin/mcxdump", "mcxi": "/usr/local/bin/mcxi", "mcxload": "/usr/local/bin/mcxload"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mcl.
shpc-registry automated BioContainers addition for mcl
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mcl
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mcl:14.137--pl5321h031d066_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mcl/14.137--pl5321h031d066_9
$ module help quay.io/biocontainers/mcl/14.137--pl5321h031d066_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mcl-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mcl-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mcl-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mcl-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mcl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mcl-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### mcxdeblast

```bash
$ singularity exec <container> /usr/local/bin/mcxdeblast
$ podman run --it --rm --entrypoint /usr/local/bin/mcxdeblast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcxdeblast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcxdump

```bash
$ singularity exec <container> /usr/local/bin/mcxdump
$ podman run --it --rm --entrypoint /usr/local/bin/mcxdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcxdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcxi

```bash
$ singularity exec <container> /usr/local/bin/mcxi
$ podman run --it --rm --entrypoint /usr/local/bin/mcxi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcxi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mcxload

```bash
$ singularity exec <container> /usr/local/bin/mcxload
$ podman run --it --rm --entrypoint /usr/local/bin/mcxload   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mcxload   -v ${PWD} -w ${PWD} <container> -c " $@"
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