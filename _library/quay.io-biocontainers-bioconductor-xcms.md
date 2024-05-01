---
layout: container
name:  "quay.io/biocontainers/bioconductor-xcms"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-xcms/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-xcms/container.yaml"
updated_at: "2024-05-01 02:56:15.640481"
latest: "4.0.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-xcms"
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
 - "3.8.0--r36he1b5a44_0"
 - "3.20.0--r42hc247a5b_0"
 - "3.16.1--r41hc247a5b_1"
 - "3.14.0--r41h399db7b_0"
 - "3.12.0--r40h399db7b_1"
 - "3.10.0--r40h5f743cb_0"
 - "3.20.0--r42hf17093f_1"
 - "3.22.0--r43hf17093f_0"
 - "4.0.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-xcms"
config: {"url": "https://biocontainers.pro/tools/bioconductor-xcms", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-xcms", "latest": {"4.0.0--r43hf17093f_0": "sha256:8bf3b23ee17db80de79c742c4e491420138c58f75d4d49e13fa95f1762add9c3"}, "tags": {"3.8.0--r36he1b5a44_0": "sha256:dcab40228cb284c5727912c49d31af6a1f86076f7a1461b454affdaaabf78cc4", "3.20.0--r42hc247a5b_0": "sha256:48a30d0d10affe8a2db4c9e22d72b0beae05f81911a19eec6f3a2b73efb59e03", "3.16.1--r41hc247a5b_1": "sha256:06118716fcc368269a5778c95faaefeedc1b120991eabe57f0df56b09ac5d8eb", "3.14.0--r41h399db7b_0": "sha256:413d59b9fb7d39165cf4867b9effb63b389ed2624c001d0a2d0d65f20a4b87c3", "3.12.0--r40h399db7b_1": "sha256:2ce8bb8a4be82eca2bf201bda24f70c0ce52e597e7ca5077ffab7f4483160282", "3.10.0--r40h5f743cb_0": "sha256:9c6c2ac82601d074d94f430c9fe2575410bb0f30eee19435957785db90e971a9", "3.20.0--r42hf17093f_1": "sha256:182600dbef352ecc78cedc17c44640a7c128b87ffb3323b32c64c6baf854bbee", "3.22.0--r43hf17093f_0": "sha256:71bf83b73597a7d9776b7cf27a630bbf5b0109c0b152909e190ef3320a21cc2e", "4.0.0--r43hf17093f_0": "sha256:8bf3b23ee17db80de79c742c4e491420138c58f75d4d49e13fa95f1762add9c3"}, "docker": "quay.io/biocontainers/bioconductor-xcms", "aliases": {"gif2hdf": "/usr/local/bin/gif2hdf", "h4_ncdump": "/usr/local/bin/h4_ncdump", "h4_ncgen": "/usr/local/bin/h4_ncgen", "h4cc": "/usr/local/bin/h4cc", "h4redeploy": "/usr/local/bin/h4redeploy", "hdf24to8": "/usr/local/bin/hdf24to8", "hdf2gif": "/usr/local/bin/hdf2gif", "hdf2jpeg": "/usr/local/bin/hdf2jpeg", "hdf8to24": "/usr/local/bin/hdf8to24", "hdfcomp": "/usr/local/bin/hdfcomp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-xcms.
shpc-registry automated BioContainers addition for bioconductor-xcms
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-xcms
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-xcms:4.0.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-xcms/4.0.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-xcms/4.0.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-xcms-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-xcms-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-xcms-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-xcms-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-xcms-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-xcms-inspect-deffile:

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