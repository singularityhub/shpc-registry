---
layout: container
name:  "quay.io/biocontainers/secapr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/secapr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/secapr/container.yaml"
updated_at: "2023-07-12 03:26:37.698488"
latest: "2.2.8--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/secapr"
aliases:
 - "abyss-rresolver-short"
 - "abyss-stack-size"
 - "io_demo"
 - "scriptlive"
 - "secapr"
 - "ucx_info"
 - "ucx_perftest"
 - "ucx_read_profile"
 - "cal"
 - "chmem"
 - "choom"
 - "chrt"
 - "col"
 - "colcrt"
 - "colrm"
 - "column"
 - "dmesg"
 - "eject"
versions:
 - "2.2.8--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for secapr"
config: {"url": "https://biocontainers.pro/tools/secapr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for secapr", "latest": {"2.2.8--pyh5e36f6f_0": "sha256:26ee9b0ae61a1936a376569ced1d19e1af109ea45a813095a26ba04d794f9226"}, "tags": {"2.2.8--pyh5e36f6f_0": "sha256:26ee9b0ae61a1936a376569ced1d19e1af109ea45a813095a26ba04d794f9226"}, "docker": "quay.io/biocontainers/secapr", "aliases": {"abyss-rresolver-short": "/usr/local/bin/abyss-rresolver-short", "abyss-stack-size": "/usr/local/bin/abyss-stack-size", "io_demo": "/usr/local/bin/io_demo", "scriptlive": "/usr/local/bin/scriptlive", "secapr": "/usr/local/bin/secapr", "ucx_info": "/usr/local/bin/ucx_info", "ucx_perftest": "/usr/local/bin/ucx_perftest", "ucx_read_profile": "/usr/local/bin/ucx_read_profile", "cal": "/usr/local/bin/cal", "chmem": "/usr/local/bin/chmem", "choom": "/usr/local/bin/choom", "chrt": "/usr/local/bin/chrt", "col": "/usr/local/bin/col", "colcrt": "/usr/local/bin/colcrt", "colrm": "/usr/local/bin/colrm", "column": "/usr/local/bin/column", "dmesg": "/usr/local/bin/dmesg", "eject": "/usr/local/bin/eject"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/secapr.
shpc-registry automated BioContainers addition for secapr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/secapr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/secapr:2.2.8--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/secapr/2.2.8--pyh5e36f6f_0
$ module help quay.io/biocontainers/secapr/2.2.8--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### secapr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### secapr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### secapr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### secapr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### secapr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### secapr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### abyss-rresolver-short

```bash
$ singularity exec <container> /usr/local/bin/abyss-rresolver-short
$ podman run --it --rm --entrypoint /usr/local/bin/abyss-rresolver-short   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abyss-rresolver-short   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abyss-stack-size

```bash
$ singularity exec <container> /usr/local/bin/abyss-stack-size
$ podman run --it --rm --entrypoint /usr/local/bin/abyss-stack-size   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abyss-stack-size   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### io_demo

```bash
$ singularity exec <container> /usr/local/bin/io_demo
$ podman run --it --rm --entrypoint /usr/local/bin/io_demo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/io_demo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scriptlive

```bash
$ singularity exec <container> /usr/local/bin/scriptlive
$ podman run --it --rm --entrypoint /usr/local/bin/scriptlive   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scriptlive   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### secapr

```bash
$ singularity exec <container> /usr/local/bin/secapr
$ podman run --it --rm --entrypoint /usr/local/bin/secapr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/secapr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ucx_info

```bash
$ singularity exec <container> /usr/local/bin/ucx_info
$ podman run --it --rm --entrypoint /usr/local/bin/ucx_info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ucx_info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ucx_perftest

```bash
$ singularity exec <container> /usr/local/bin/ucx_perftest
$ podman run --it --rm --entrypoint /usr/local/bin/ucx_perftest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ucx_perftest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ucx_read_profile

```bash
$ singularity exec <container> /usr/local/bin/ucx_read_profile
$ podman run --it --rm --entrypoint /usr/local/bin/ucx_read_profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ucx_read_profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cal

```bash
$ singularity exec <container> /usr/local/bin/cal
$ podman run --it --rm --entrypoint /usr/local/bin/cal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chmem

```bash
$ singularity exec <container> /usr/local/bin/chmem
$ podman run --it --rm --entrypoint /usr/local/bin/chmem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chmem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### choom

```bash
$ singularity exec <container> /usr/local/bin/choom
$ podman run --it --rm --entrypoint /usr/local/bin/choom   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/choom   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chrt

```bash
$ singularity exec <container> /usr/local/bin/chrt
$ podman run --it --rm --entrypoint /usr/local/bin/chrt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chrt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### col

```bash
$ singularity exec <container> /usr/local/bin/col
$ podman run --it --rm --entrypoint /usr/local/bin/col   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/col   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### colcrt

```bash
$ singularity exec <container> /usr/local/bin/colcrt
$ podman run --it --rm --entrypoint /usr/local/bin/colcrt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/colcrt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### colrm

```bash
$ singularity exec <container> /usr/local/bin/colrm
$ podman run --it --rm --entrypoint /usr/local/bin/colrm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/colrm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### column

```bash
$ singularity exec <container> /usr/local/bin/column
$ podman run --it --rm --entrypoint /usr/local/bin/column   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/column   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dmesg

```bash
$ singularity exec <container> /usr/local/bin/dmesg
$ podman run --it --rm --entrypoint /usr/local/bin/dmesg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dmesg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eject

```bash
$ singularity exec <container> /usr/local/bin/eject
$ podman run --it --rm --entrypoint /usr/local/bin/eject   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eject   -v ${PWD} -w ${PWD} <container> -c " $@"
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