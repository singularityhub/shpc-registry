---
layout: container
name:  "quay.io/biocontainers/bioconductor-ptairms"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ptairms/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ptairms/container.yaml"
updated_at: "2022-10-29 05:35:42.700354"
latest: "1.2.0--r41hc247a5b_2"
container_url: "https://biocontainers.pro/tools/bioconductor-ptairms"
aliases:
 - "2to3-3.10"
 - "f2py3.10"
 - "gif2h5"
 - "gif2hdf"
 - "h4_ncdump"
 - "h4_ncgen"
 - "h4cc"
 - "h4redeploy"
 - "h52gif"
 - "h5c++"
versions:
 - "1.2.0--r41hc247a5b_2"
description: "shpc-registry automated BioContainers addition for bioconductor-ptairms"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ptairms", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ptairms", "latest": {"1.2.0--r41hc247a5b_2": "sha256:0d4d0a51f70e968c145f6adaa3c64dd5b5cc7134984e109480aca57c0632a6dc"}, "tags": {"1.2.0--r41hc247a5b_2": "sha256:0d4d0a51f70e968c145f6adaa3c64dd5b5cc7134984e109480aca57c0632a6dc"}, "docker": "quay.io/biocontainers/bioconductor-ptairms", "aliases": {"2to3-3.10": "/usr/local/bin/2to3-3.10", "f2py3.10": "/usr/local/bin/f2py3.10", "gif2h5": "/usr/local/bin/gif2h5", "gif2hdf": "/usr/local/bin/gif2hdf", "h4_ncdump": "/usr/local/bin/h4_ncdump", "h4_ncgen": "/usr/local/bin/h4_ncgen", "h4cc": "/usr/local/bin/h4cc", "h4redeploy": "/usr/local/bin/h4redeploy", "h52gif": "/usr/local/bin/h52gif", "h5c++": "/usr/local/bin/h5c++"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ptairms.
shpc-registry automated BioContainers addition for bioconductor-ptairms
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ptairms
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ptairms:1.2.0--r41hc247a5b_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ptairms/1.2.0--r41hc247a5b_2
$ module help quay.io/biocontainers/bioconductor-ptairms/1.2.0--r41hc247a5b_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ptairms-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ptairms-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ptairms-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ptairms-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ptairms-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ptairms-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.10

```bash
$ singularity exec <container> /usr/local/bin/f2py3.10
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gif2h5

```bash
$ singularity exec <container> /usr/local/bin/gif2h5
$ podman run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gif2h5   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### h52gif

```bash
$ singularity exec <container> /usr/local/bin/h52gif
$ podman run --it --rm --entrypoint /usr/local/bin/h52gif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h52gif   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5c++

```bash
$ singularity exec <container> /usr/local/bin/h5c++
$ podman run --it --rm --entrypoint /usr/local/bin/h5c++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5c++   -v ${PWD} -w ${PWD} <container> -c " $@"
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