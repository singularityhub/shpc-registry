---
layout: container
name:  "quay.io/biocontainers/correlationplus"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/correlationplus/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/correlationplus/container.yaml"
updated_at: "2024-03-29 02:59:45.532347"
latest: "0.2.1--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/correlationplus"
aliases:
 - "correlationplus"
 - "evol"
 - "gsd"
 - "nc3tonc4"
 - "nc4tonc3"
 - "ncinfo"
 - "prody"
 - "numba"
 - "pycc"
 - "zipcmp"
 - "zipmerge"
 - "ziptool"
 - "gif2hdf"
 - "h4_ncdump"
 - "h4_ncgen"
 - "h4cc"
 - "h4redeploy"
versions:
 - "0.2.1--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for correlationplus"
config: {"url": "https://biocontainers.pro/tools/correlationplus", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for correlationplus", "latest": {"0.2.1--pyh5e36f6f_0": "sha256:77e2f3c9e1eecc8d98b5689fe20d416eb72a01be22c3ca864dce544572913d96"}, "tags": {"0.2.1--pyh5e36f6f_0": "sha256:77e2f3c9e1eecc8d98b5689fe20d416eb72a01be22c3ca864dce544572913d96"}, "docker": "quay.io/biocontainers/correlationplus", "aliases": {"correlationplus": "/usr/local/bin/correlationplus", "evol": "/usr/local/bin/evol", "gsd": "/usr/local/bin/gsd", "nc3tonc4": "/usr/local/bin/nc3tonc4", "nc4tonc3": "/usr/local/bin/nc4tonc3", "ncinfo": "/usr/local/bin/ncinfo", "prody": "/usr/local/bin/prody", "numba": "/usr/local/bin/numba", "pycc": "/usr/local/bin/pycc", "zipcmp": "/usr/local/bin/zipcmp", "zipmerge": "/usr/local/bin/zipmerge", "ziptool": "/usr/local/bin/ziptool", "gif2hdf": "/usr/local/bin/gif2hdf", "h4_ncdump": "/usr/local/bin/h4_ncdump", "h4_ncgen": "/usr/local/bin/h4_ncgen", "h4cc": "/usr/local/bin/h4cc", "h4redeploy": "/usr/local/bin/h4redeploy"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/correlationplus.
shpc-registry automated BioContainers addition for correlationplus
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/correlationplus
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/correlationplus:0.2.1--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/correlationplus/0.2.1--pyh5e36f6f_0
$ module help quay.io/biocontainers/correlationplus/0.2.1--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### correlationplus-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### correlationplus-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### correlationplus-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### correlationplus-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### correlationplus-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### correlationplus-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### correlationplus

```bash
$ singularity exec <container> /usr/local/bin/correlationplus
$ podman run --it --rm --entrypoint /usr/local/bin/correlationplus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/correlationplus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### evol

```bash
$ singularity exec <container> /usr/local/bin/evol
$ podman run --it --rm --entrypoint /usr/local/bin/evol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/evol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsd

```bash
$ singularity exec <container> /usr/local/bin/gsd
$ podman run --it --rm --entrypoint /usr/local/bin/gsd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nc3tonc4

```bash
$ singularity exec <container> /usr/local/bin/nc3tonc4
$ podman run --it --rm --entrypoint /usr/local/bin/nc3tonc4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nc3tonc4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nc4tonc3

```bash
$ singularity exec <container> /usr/local/bin/nc4tonc3
$ podman run --it --rm --entrypoint /usr/local/bin/nc4tonc3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nc4tonc3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncinfo

```bash
$ singularity exec <container> /usr/local/bin/ncinfo
$ podman run --it --rm --entrypoint /usr/local/bin/ncinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prody

```bash
$ singularity exec <container> /usr/local/bin/prody
$ podman run --it --rm --entrypoint /usr/local/bin/prody   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prody   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numba

```bash
$ singularity exec <container> /usr/local/bin/numba
$ podman run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pycc

```bash
$ singularity exec <container> /usr/local/bin/pycc
$ podman run --it --rm --entrypoint /usr/local/bin/pycc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pycc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zipcmp

```bash
$ singularity exec <container> /usr/local/bin/zipcmp
$ podman run --it --rm --entrypoint /usr/local/bin/zipcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zipcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zipmerge

```bash
$ singularity exec <container> /usr/local/bin/zipmerge
$ podman run --it --rm --entrypoint /usr/local/bin/zipmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zipmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ziptool

```bash
$ singularity exec <container> /usr/local/bin/ziptool
$ podman run --it --rm --entrypoint /usr/local/bin/ziptool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ziptool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2hdf

```bash
$ singularity exec <container> /usr/local/bin/gif2hdf
$ podman run --it --rm --entrypoint /usr/local/bin/gif2hdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2hdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h4_ncdump

```bash
$ singularity exec <container> /usr/local/bin/h4_ncdump
$ podman run --it --rm --entrypoint /usr/local/bin/h4_ncdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h4_ncdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h4_ncgen

```bash
$ singularity exec <container> /usr/local/bin/h4_ncgen
$ podman run --it --rm --entrypoint /usr/local/bin/h4_ncgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h4_ncgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h4cc

```bash
$ singularity exec <container> /usr/local/bin/h4cc
$ podman run --it --rm --entrypoint /usr/local/bin/h4cc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h4cc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h4redeploy

```bash
$ singularity exec <container> /usr/local/bin/h4redeploy
$ podman run --it --rm --entrypoint /usr/local/bin/h4redeploy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h4redeploy   -v ${PWD} -w ${PWD} <container> -c " $@"
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