---
layout: container
name:  "quay.io/biocontainers/bioconductor-hicbricks"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hicbricks/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hicbricks/container.yaml"
updated_at: "2024-02-15 03:19:46.260384"
latest: "1.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-hicbricks"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.11.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r42hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-hicbricks"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hicbricks", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hicbricks", "latest": {"1.20.0--r43hdfd78af_0": "sha256:4febd9678917592162c76322186b2b44fdacb674bf4d0246d4ce9055324225c2"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:2fbeb2e4b144eaf77215f4e0e31ffa51192e4e25f1073fcbb47581d8b7923103", "1.11.0--r41hdfd78af_0": "sha256:5c03e1f339c2dc4f10d463f42aad5633d1ae90b94ebd4feb47fec30a8ed424ab", "1.10.0--r41hdfd78af_0": "sha256:3018e3e36cfcf336423cc728142ab2ab4dad49e1fa5a130d35b2d725521c9d99", "1.16.0--r42hdfd78af_0": "sha256:272d8db8e7d64cc5f1f9dca7f958d564071a9867df422a6707e8dd660a751e26", "1.18.0--r43hdfd78af_0": "sha256:a298926427b88febe25dc9049f95fb7175be5fb910f812973f13f2fe169c2da5", "1.20.0--r43hdfd78af_0": "sha256:4febd9678917592162c76322186b2b44fdacb674bf4d0246d4ce9055324225c2"}, "docker": "quay.io/biocontainers/bioconductor-hicbricks", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hicbricks.
shpc-registry automated BioContainers addition for bioconductor-hicbricks
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hicbricks
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hicbricks:1.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hicbricks/1.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-hicbricks/1.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hicbricks-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hicbricks-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hicbricks-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hicbricks-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hicbricks-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hicbricks-inspect-deffile:

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