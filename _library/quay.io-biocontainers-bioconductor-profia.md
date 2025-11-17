---
layout: container
name:  "quay.io/biocontainers/bioconductor-profia"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-profia/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-profia/container.yaml"
updated_at: "2025-11-17 04:36:54.523742"
latest: "1.23.0--r42ha9d7317_1"
container_url: "https://biocontainers.pro/tools/bioconductor-profia"
aliases:
 - "gif2hdf"
 - "h4_ncdump"
 - "h4_ncgen"
 - "h4cc"
 - "h4redeploy"
 - "hdf24to8"
 - "hdf2gif"
 - "hdf2jpeg"
 - "hdf8to24"
 - "hdfcomp"
versions:
 - "1.8.1--r351h14c3975_0"
 - "1.20.0--r41hc0cfd56_2"
 - "1.18.0--r41hd029910_0"
 - "1.16.3--r40hd029910_0"
 - "1.15.0--r40h037d062_0"
 - "1.14.0--r40h037d062_0"
 - "1.23.0--r42hc0cfd56_0"
 - "1.23.0--r42ha9d7317_1"
description: "shpc-registry automated BioContainers addition for bioconductor-profia"
config: {"url": "https://biocontainers.pro/tools/bioconductor-profia", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-profia", "latest": {"1.23.0--r42ha9d7317_1": "sha256:e97fe5a2943db3d27f8a33992ed49380faa213b176bf4ac65cd85d36897b067f"}, "tags": {"1.8.1--r351h14c3975_0": "sha256:0604436c4628cdd4c1beeef15ce3b62ea415a5c5857dad832719e054e24fec29", "1.20.0--r41hc0cfd56_2": "sha256:35e344290c5c79874afafe9287d91884b6b165fd73e3459d78701c84d065dbe5", "1.18.0--r41hd029910_0": "sha256:5f5bbd2e84adf56ca4d7789a739a1964dae839bce6f253cd3f95b4669a87c69a", "1.16.3--r40hd029910_0": "sha256:cf153e4fd2e8e94f89dd3a0c9a3fbe1fb5e23f7b24325080a460de3104f8680d", "1.15.0--r40h037d062_0": "sha256:5dea3f4224a6182a4ebebd86a099dcd158554368ac9dc2d4867f0258be0da6db", "1.14.0--r40h037d062_0": "sha256:932d35b24caf31461f63b015891c7e3637192c07a6d7c8250c411e5cb2dc2bf6", "1.23.0--r42hc0cfd56_0": "sha256:bcbb14f2581178ccef50638879bf540667586688b267f52a1d10d0108255e542", "1.23.0--r42ha9d7317_1": "sha256:e97fe5a2943db3d27f8a33992ed49380faa213b176bf4ac65cd85d36897b067f"}, "docker": "quay.io/biocontainers/bioconductor-profia", "aliases": {"gif2hdf": "/usr/local/bin/gif2hdf", "h4_ncdump": "/usr/local/bin/h4_ncdump", "h4_ncgen": "/usr/local/bin/h4_ncgen", "h4cc": "/usr/local/bin/h4cc", "h4redeploy": "/usr/local/bin/h4redeploy", "hdf24to8": "/usr/local/bin/hdf24to8", "hdf2gif": "/usr/local/bin/hdf2gif", "hdf2jpeg": "/usr/local/bin/hdf2jpeg", "hdf8to24": "/usr/local/bin/hdf8to24", "hdfcomp": "/usr/local/bin/hdfcomp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-profia.
shpc-registry automated BioContainers addition for bioconductor-profia
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-profia
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-profia:1.23.0--r42ha9d7317_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-profia/1.23.0--r42ha9d7317_1
$ module help quay.io/biocontainers/bioconductor-profia/1.23.0--r42ha9d7317_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-profia-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-profia-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-profia-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-profia-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-profia-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-profia-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### hdf24to8

```bash
$ singularity exec <container> /usr/local/bin/hdf24to8
$ podman run --it --rm --entrypoint /usr/local/bin/hdf24to8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hdf24to8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hdf2gif

```bash
$ singularity exec <container> /usr/local/bin/hdf2gif
$ podman run --it --rm --entrypoint /usr/local/bin/hdf2gif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hdf2gif   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hdf2jpeg

```bash
$ singularity exec <container> /usr/local/bin/hdf2jpeg
$ podman run --it --rm --entrypoint /usr/local/bin/hdf2jpeg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hdf2jpeg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hdf8to24

```bash
$ singularity exec <container> /usr/local/bin/hdf8to24
$ podman run --it --rm --entrypoint /usr/local/bin/hdf8to24   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hdf8to24   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hdfcomp

```bash
$ singularity exec <container> /usr/local/bin/hdfcomp
$ podman run --it --rm --entrypoint /usr/local/bin/hdfcomp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hdfcomp   -v ${PWD} -w ${PWD} <container> -c " $@"
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