---
layout: container
name:  "quay.io/biocontainers/bioconductor-tpp2d"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tpp2d/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tpp2d/container.yaml"
updated_at: "2024-01-25 03:06:42.975680"
latest: "1.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tpp2d"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tpp2d"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tpp2d", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tpp2d", "latest": {"1.18.0--r43hdfd78af_0": "sha256:247ef4dbcdf6d4dccc67ce24ef0c26c64c50fb6805a04dc3503f788f3f34a1f2"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:15dd708a4d92bbf7632d953a33f2c3471bd4cd46006d1228aa7275a5b8e67cfd", "1.14.0--r42hdfd78af_0": "sha256:54cc115a9edb98fc0d332d7eb56b1932c27e8e49a9037c68f96c28990221691a", "1.10.0--r41hdfd78af_0": "sha256:f8953b850738345ef105d52fe6a86bc6f318bda405138ded6d261e9ec120dacd", "1.16.0--r43hdfd78af_0": "sha256:7f3245ad1f6d566408169eed955dc8e037a4a411845a9cbe3c5c028ebbe34ec3", "1.18.0--r43hdfd78af_0": "sha256:247ef4dbcdf6d4dccc67ce24ef0c26c64c50fb6805a04dc3503f788f3f34a1f2"}, "docker": "quay.io/biocontainers/bioconductor-tpp2d", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tpp2d.
shpc-registry automated BioContainers addition for bioconductor-tpp2d
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tpp2d
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tpp2d:1.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tpp2d/1.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tpp2d/1.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tpp2d-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tpp2d-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tpp2d-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tpp2d-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tpp2d-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tpp2d-inspect-deffile:

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