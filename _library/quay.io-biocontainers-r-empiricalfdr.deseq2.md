---
layout: container
name:  "quay.io/biocontainers/r-empiricalfdr.deseq2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-empiricalfdr.deseq2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-empiricalfdr.deseq2/container.yaml"
updated_at: "2025-10-21 03:44:10.763047"
latest: "1.0.3--r44h3121a25_11"
container_url: "https://biocontainers.pro/tools/r-empiricalfdr.deseq2"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.0.3--r41h3121a25_8"
 - "1.0.3--r42h3121a25_9"
 - "1.0.3--r43h3121a25_10"
 - "1.0.3--r44h3121a25_11"
description: "shpc-registry automated BioContainers addition for r-empiricalfdr.deseq2"
config: {"url": "https://biocontainers.pro/tools/r-empiricalfdr.deseq2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-empiricalfdr.deseq2", "latest": {"1.0.3--r44h3121a25_11": "sha256:bb1d4d699ea5126ba077d310c2ff8aa931b0f4ce0941e943ca32ba377e3969d7"}, "tags": {"1.0.3--r41h3121a25_8": "sha256:fceeedc1f2d94f63e5f1a9a12a03ed0ca5c3e3875c25060716b8d2b61dd9fadc", "1.0.3--r42h3121a25_9": "sha256:f366efd35a62738a2b6168e17b2975c96fdd49ca565f25d65cc9c3fca5ea6eee", "1.0.3--r43h3121a25_10": "sha256:b523e5344095bc8f7d28e9915febd8a40f83931b9eb1d2e4a789a3ca280b445f", "1.0.3--r44h3121a25_11": "sha256:bb1d4d699ea5126ba077d310c2ff8aa931b0f4ce0941e943ca32ba377e3969d7"}, "docker": "quay.io/biocontainers/r-empiricalfdr.deseq2", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-empiricalfdr.deseq2.
shpc-registry automated BioContainers addition for r-empiricalfdr.deseq2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-empiricalfdr.deseq2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-empiricalfdr.deseq2:1.0.3--r44h3121a25_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-empiricalfdr.deseq2/1.0.3--r44h3121a25_11
$ module help quay.io/biocontainers/r-empiricalfdr.deseq2/1.0.3--r44h3121a25_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-empiricalfdr.deseq2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-empiricalfdr.deseq2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-empiricalfdr.deseq2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-empiricalfdr.deseq2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-empiricalfdr.deseq2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-empiricalfdr.deseq2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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