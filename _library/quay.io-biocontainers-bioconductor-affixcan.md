---
layout: container
name:  "quay.io/biocontainers/bioconductor-affixcan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-affixcan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-affixcan/container.yaml"
updated_at: "2023-09-18 02:52:46.298488"
latest: "1.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-affixcan"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r42hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-affixcan"
config: {"url": "https://biocontainers.pro/tools/bioconductor-affixcan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-affixcan", "latest": {"1.18.0--r43hdfd78af_0": "sha256:b65598ecc1554613a64e14f918c71c1e0b56ba2f84daff248f4420e21faea1b3"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:9b97fb2c5e95086120e87c377952052fb26b816f66de09c27abfb1a3cbc75c83", "1.12.0--r41hdfd78af_0": "sha256:292e9c1db6c4d9e924291a679e4903027be74655314a1310f64dd73a7ea5e5aa", "1.10.0--r41hdfd78af_0": "sha256:4bbdcbdb6fc1e8cd2cb0a8571bdf00694ff985e996103a09706ebd1ca7d222b5", "1.16.0--r42hdfd78af_0": "sha256:1c6025ae03332280b2e077a3e6e998cbcbd09fccb25a77b1749cfcfcd198bb5a", "1.18.0--r43hdfd78af_0": "sha256:b65598ecc1554613a64e14f918c71c1e0b56ba2f84daff248f4420e21faea1b3"}, "docker": "quay.io/biocontainers/bioconductor-affixcan", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-affixcan.
shpc-registry automated BioContainers addition for bioconductor-affixcan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-affixcan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-affixcan:1.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-affixcan/1.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-affixcan/1.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-affixcan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-affixcan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-affixcan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-affixcan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-affixcan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-affixcan-inspect-deffile:

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