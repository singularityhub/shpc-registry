---
layout: container
name:  "quay.io/biocontainers/easy45"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/easy45/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/easy45/container.yaml"
updated_at: "2026-08-02 06:03:52.747628"
latest: "0.1.0--pyh106432d_0"
container_url: "https://biocontainers.pro/tools/easy45"
aliases:
 - "ITSx"
 - "abpoa"
 - "easy45"
 - "barrnap"
 - "vsearch"
 - "seqkit"
 - "cmalign"
 - "cmbuild"
 - "cmcalibrate"
 - "cmconvert"
 - "cmemit"
 - "cmfetch"
 - "cmpress"
 - "cmscan"
 - "cmsearch"
 - "cmstat"
 - "shmemrun"
 - "oshCC"
 - "oshc++"
 - "oshcxx"
 - "shmemCC"
 - "shmemc++"
 - "shmemcxx"
 - "oshcc"
 - "oshfort"
 - "oshmem_info"
 - "oshrun"
 - "shmemcc"
versions:
 - "0.1.0--pyh106432d_0"
description: "singularity registry hpc automated addition for easy45"
config: {"url": "https://biocontainers.pro/tools/easy45", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for easy45", "latest": {"0.1.0--pyh106432d_0": "sha256:0f3fc895bbd4316d9c760099be0b7fe7d8fbfbe5b69a5d110adb976d931d94df"}, "tags": {"0.1.0--pyh106432d_0": "sha256:0f3fc895bbd4316d9c760099be0b7fe7d8fbfbe5b69a5d110adb976d931d94df"}, "docker": "quay.io/biocontainers/easy45", "aliases": {"ITSx": "/usr/local/bin/ITSx", "abpoa": "/usr/local/bin/abpoa", "easy45": "/usr/local/bin/easy45", "barrnap": "/usr/local/bin/barrnap", "vsearch": "/usr/local/bin/vsearch", "seqkit": "/usr/local/bin/seqkit", "cmalign": "/usr/local/bin/cmalign", "cmbuild": "/usr/local/bin/cmbuild", "cmcalibrate": "/usr/local/bin/cmcalibrate", "cmconvert": "/usr/local/bin/cmconvert", "cmemit": "/usr/local/bin/cmemit", "cmfetch": "/usr/local/bin/cmfetch", "cmpress": "/usr/local/bin/cmpress", "cmscan": "/usr/local/bin/cmscan", "cmsearch": "/usr/local/bin/cmsearch", "cmstat": "/usr/local/bin/cmstat", "shmemrun": "/usr/local/bin/shmemrun", "oshCC": "/usr/local/bin/oshCC", "oshc++": "/usr/local/bin/oshc++", "oshcxx": "/usr/local/bin/oshcxx", "shmemCC": "/usr/local/bin/shmemCC", "shmemc++": "/usr/local/bin/shmemc++", "shmemcxx": "/usr/local/bin/shmemcxx", "oshcc": "/usr/local/bin/oshcc", "oshfort": "/usr/local/bin/oshfort", "oshmem_info": "/usr/local/bin/oshmem_info", "oshrun": "/usr/local/bin/oshrun", "shmemcc": "/usr/local/bin/shmemcc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/easy45.
singularity registry hpc automated addition for easy45
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/easy45
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/easy45:0.1.0--pyh106432d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/easy45/0.1.0--pyh106432d_0
$ module help quay.io/biocontainers/easy45/0.1.0--pyh106432d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### easy45-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### easy45-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### easy45-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### easy45-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### easy45-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### easy45-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ITSx

```bash
$ singularity exec <container> /usr/local/bin/ITSx
$ podman run --it --rm --entrypoint /usr/local/bin/ITSx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ITSx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### abpoa

```bash
$ singularity exec <container> /usr/local/bin/abpoa
$ podman run --it --rm --entrypoint /usr/local/bin/abpoa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/abpoa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easy45

```bash
$ singularity exec <container> /usr/local/bin/easy45
$ podman run --it --rm --entrypoint /usr/local/bin/easy45   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easy45   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### barrnap

```bash
$ singularity exec <container> /usr/local/bin/barrnap
$ podman run --it --rm --entrypoint /usr/local/bin/barrnap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/barrnap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vsearch

```bash
$ singularity exec <container> /usr/local/bin/vsearch
$ podman run --it --rm --entrypoint /usr/local/bin/vsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqkit

```bash
$ singularity exec <container> /usr/local/bin/seqkit
$ podman run --it --rm --entrypoint /usr/local/bin/seqkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqkit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmalign

```bash
$ singularity exec <container> /usr/local/bin/cmalign
$ podman run --it --rm --entrypoint /usr/local/bin/cmalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmbuild

```bash
$ singularity exec <container> /usr/local/bin/cmbuild
$ podman run --it --rm --entrypoint /usr/local/bin/cmbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmbuild   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmcalibrate

```bash
$ singularity exec <container> /usr/local/bin/cmcalibrate
$ podman run --it --rm --entrypoint /usr/local/bin/cmcalibrate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmcalibrate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmconvert

```bash
$ singularity exec <container> /usr/local/bin/cmconvert
$ podman run --it --rm --entrypoint /usr/local/bin/cmconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmemit

```bash
$ singularity exec <container> /usr/local/bin/cmemit
$ podman run --it --rm --entrypoint /usr/local/bin/cmemit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmemit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmfetch

```bash
$ singularity exec <container> /usr/local/bin/cmfetch
$ podman run --it --rm --entrypoint /usr/local/bin/cmfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmpress

```bash
$ singularity exec <container> /usr/local/bin/cmpress
$ podman run --it --rm --entrypoint /usr/local/bin/cmpress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmpress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmscan

```bash
$ singularity exec <container> /usr/local/bin/cmscan
$ podman run --it --rm --entrypoint /usr/local/bin/cmscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmsearch

```bash
$ singularity exec <container> /usr/local/bin/cmsearch
$ podman run --it --rm --entrypoint /usr/local/bin/cmsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmstat

```bash
$ singularity exec <container> /usr/local/bin/cmstat
$ podman run --it --rm --entrypoint /usr/local/bin/cmstat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmstat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shmemrun

```bash
$ singularity exec <container> /usr/local/bin/shmemrun
$ podman run --it --rm --entrypoint /usr/local/bin/shmemrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shmemrun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshCC

```bash
$ singularity exec <container> /usr/local/bin/oshCC
$ podman run --it --rm --entrypoint /usr/local/bin/oshCC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshCC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshc++

```bash
$ singularity exec <container> /usr/local/bin/oshc++
$ podman run --it --rm --entrypoint /usr/local/bin/oshc++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshc++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshcxx

```bash
$ singularity exec <container> /usr/local/bin/oshcxx
$ podman run --it --rm --entrypoint /usr/local/bin/oshcxx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshcxx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shmemCC

```bash
$ singularity exec <container> /usr/local/bin/shmemCC
$ podman run --it --rm --entrypoint /usr/local/bin/shmemCC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shmemCC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shmemc++

```bash
$ singularity exec <container> /usr/local/bin/shmemc++
$ podman run --it --rm --entrypoint /usr/local/bin/shmemc++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shmemc++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shmemcxx

```bash
$ singularity exec <container> /usr/local/bin/shmemcxx
$ podman run --it --rm --entrypoint /usr/local/bin/shmemcxx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shmemcxx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshcc

```bash
$ singularity exec <container> /usr/local/bin/oshcc
$ podman run --it --rm --entrypoint /usr/local/bin/oshcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshcc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshfort

```bash
$ singularity exec <container> /usr/local/bin/oshfort
$ podman run --it --rm --entrypoint /usr/local/bin/oshfort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshfort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshmem_info

```bash
$ singularity exec <container> /usr/local/bin/oshmem_info
$ podman run --it --rm --entrypoint /usr/local/bin/oshmem_info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshmem_info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshrun

```bash
$ singularity exec <container> /usr/local/bin/oshrun
$ podman run --it --rm --entrypoint /usr/local/bin/oshrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshrun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shmemcc

```bash
$ singularity exec <container> /usr/local/bin/shmemcc
$ podman run --it --rm --entrypoint /usr/local/bin/shmemcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shmemcc   -v ${PWD} -w ${PWD} <container> -c " $@"
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