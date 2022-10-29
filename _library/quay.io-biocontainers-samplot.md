---
layout: container
name:  "quay.io/biocontainers/samplot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/samplot/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/samplot/container.yaml"
updated_at: "2022-10-29 05:41:47.060690"
latest: "1.3.0--pyh5e36f6f_1"
container_url: "https://biocontainers.pro/tools/samplot"
aliases:
 - "samplot"
 - "2to3-3.9"
 - "f2py3.9"
 - "idle3.9"
 - "idn2"
 - "jpgicc"
 - "linkicc"
 - "opj_compress"
 - "opj_decompress"
 - "opj_dump"
 - "psicc"
versions:
 - "1.3.0--pyh5e36f6f_1"
description: "shpc-registry automated BioContainers addition for samplot"
config: {"url": "https://biocontainers.pro/tools/samplot", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for samplot", "latest": {"1.3.0--pyh5e36f6f_1": "sha256:b7e4a9a52e1d908505398c6dc0fec1a4063841f7cfe701122bb417e204b1387a"}, "tags": {"1.3.0--pyh5e36f6f_1": "sha256:b7e4a9a52e1d908505398c6dc0fec1a4063841f7cfe701122bb417e204b1387a"}, "docker": "quay.io/biocontainers/samplot", "aliases": {"samplot": "/usr/local/bin/samplot", "2to3-3.9": "/usr/local/bin/2to3-3.9", "f2py3.9": "/usr/local/bin/f2py3.9", "idle3.9": "/usr/local/bin/idle3.9", "idn2": "/usr/local/bin/idn2", "jpgicc": "/usr/local/bin/jpgicc", "linkicc": "/usr/local/bin/linkicc", "opj_compress": "/usr/local/bin/opj_compress", "opj_decompress": "/usr/local/bin/opj_decompress", "opj_dump": "/usr/local/bin/opj_dump", "psicc": "/usr/local/bin/psicc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/samplot.
shpc-registry automated BioContainers addition for samplot
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/samplot
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/samplot:1.3.0--pyh5e36f6f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/samplot/1.3.0--pyh5e36f6f_1
$ module help quay.io/biocontainers/samplot/1.3.0--pyh5e36f6f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### samplot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### samplot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### samplot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### samplot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### samplot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### samplot-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### samplot

```bash
$ singularity exec <container> /usr/local/bin/samplot
$ podman run --it --rm --entrypoint /usr/local/bin/samplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idn2

```bash
$ singularity exec <container> /usr/local/bin/idn2
$ podman run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jpgicc

```bash
$ singularity exec <container> /usr/local/bin/jpgicc
$ podman run --it --rm --entrypoint /usr/local/bin/jpgicc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jpgicc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### linkicc

```bash
$ singularity exec <container> /usr/local/bin/linkicc
$ podman run --it --rm --entrypoint /usr/local/bin/linkicc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/linkicc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_compress

```bash
$ singularity exec <container> /usr/local/bin/opj_compress
$ podman run --it --rm --entrypoint /usr/local/bin/opj_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_compress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_decompress

```bash
$ singularity exec <container> /usr/local/bin/opj_decompress
$ podman run --it --rm --entrypoint /usr/local/bin/opj_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_decompress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opj_dump

```bash
$ singularity exec <container> /usr/local/bin/opj_dump
$ podman run --it --rm --entrypoint /usr/local/bin/opj_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opj_dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psicc

```bash
$ singularity exec <container> /usr/local/bin/psicc
$ podman run --it --rm --entrypoint /usr/local/bin/psicc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psicc   -v ${PWD} -w ${PWD} <container> -c " $@"
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