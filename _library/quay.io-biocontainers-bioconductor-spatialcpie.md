---
layout: container
name:  "quay.io/biocontainers/bioconductor-spatialcpie"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-spatialcpie/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-spatialcpie/container.yaml"
updated_at: "2025-02-01 03:21:34.958098"
latest: "1.22.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-spatialcpie"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.22.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-spatialcpie"
config: {"url": "https://biocontainers.pro/tools/bioconductor-spatialcpie", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-spatialcpie", "latest": {"1.22.0--r44hdfd78af_0": "sha256:265c428a0f049baf3e0cfd3ea572e22d1e958880a17a3ae93502fbc10da043e0"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:538f13f18a71140d0fb8597e655a2c8d3b832d549303cc47682e78fb6fe40891", "1.14.0--r42hdfd78af_0": "sha256:b40f2a67dd993f3043e6412a211e3d504b4efd40f253665e1d657b816d7640d5", "1.10.0--r41hdfd78af_0": "sha256:74a141cdfe4d4d784c294498b948c04d51fea1d5cd6fa9f65d8d393af36d3267", "1.16.0--r43hdfd78af_0": "sha256:4d9f4a7c26eb8fc3bfef7d34c48e7fc6810842c132b56bfd95f32097db9513cf", "1.18.0--r43hdfd78af_0": "sha256:0908729fbfea2c6d74e2167a9c1e609df01e7d159e7eefb40314aac643c16e28", "1.22.0--r44hdfd78af_0": "sha256:265c428a0f049baf3e0cfd3ea572e22d1e958880a17a3ae93502fbc10da043e0"}, "docker": "quay.io/biocontainers/bioconductor-spatialcpie", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-spatialcpie.
shpc-registry automated BioContainers addition for bioconductor-spatialcpie
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-spatialcpie
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-spatialcpie:1.22.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-spatialcpie/1.22.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-spatialcpie/1.22.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-spatialcpie-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spatialcpie-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spatialcpie-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-spatialcpie-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-spatialcpie-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-spatialcpie-inspect-deffile:

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