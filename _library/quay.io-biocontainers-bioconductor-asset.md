---
layout: container
name:  "quay.io/biocontainers/bioconductor-asset"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-asset/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-asset/container.yaml"
updated_at: "2024-12-09 03:53:34.117486"
latest: "2.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-asset"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "2.8.0--r40hdfd78af_1"
 - "2.16.0--r42hdfd78af_0"
 - "2.12.0--r41hdfd78af_0"
 - "2.10.0--r41hdfd78af_0"
 - "2.18.0--r43hdfd78af_0"
 - "2.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-asset"
config: {"url": "https://biocontainers.pro/tools/bioconductor-asset", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-asset", "latest": {"2.20.0--r43hdfd78af_0": "sha256:841ef74654b3467330578ea1a4d9bfb77bb6d751cabfff112f81a61ae29927e8"}, "tags": {"2.8.0--r40hdfd78af_1": "sha256:e28e2e52d4827a1429f6ffe3cdf0bef2726ac23fab88eb116e121cf9990ce878", "2.16.0--r42hdfd78af_0": "sha256:6991d6250bce9068c320ac10ba618a993b5cd04a738e5e0da1a2f4fde498a8a8", "2.12.0--r41hdfd78af_0": "sha256:8d4ef8749b91d8147e13f5b45fb196eb8d40ae7cf640126b8f5c4d0dac343763", "2.10.0--r41hdfd78af_0": "sha256:d23c0b8baf16dd651d2623ce0ffafc8280d5f2b974637eb1d64eeac31aa398e9", "2.18.0--r43hdfd78af_0": "sha256:af4be3bf0da8c6f57b71b3a698dda821298ee98f810e351053bef7e5b183b646", "2.20.0--r43hdfd78af_0": "sha256:841ef74654b3467330578ea1a4d9bfb77bb6d751cabfff112f81a61ae29927e8"}, "docker": "quay.io/biocontainers/bioconductor-asset", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-asset.
shpc-registry automated BioContainers addition for bioconductor-asset
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-asset
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-asset:2.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-asset/2.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-asset/2.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-asset-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-asset-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-asset-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-asset-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-asset-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-asset-inspect-deffile:

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