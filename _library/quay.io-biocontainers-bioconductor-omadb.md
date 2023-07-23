---
layout: container
name:  "quay.io/biocontainers/bioconductor-omadb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-omadb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-omadb/container.yaml"
updated_at: "2023-07-23 02:57:10.691184"
latest: "2.14.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-omadb"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "2.8.0--r41hdfd78af_0"
 - "2.14.0--r42hdfd78af_0"
 - "2.10.0--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-omadb"
config: {"url": "https://biocontainers.pro/tools/bioconductor-omadb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-omadb", "latest": {"2.14.0--r42hdfd78af_0": "sha256:5e0dd5e0e4e1bd41a1e9887008be235e04397ef3f6ec2748843cbca8ca67fc2e"}, "tags": {"2.8.0--r41hdfd78af_0": "sha256:444daa83ed6f186265cd969fbc0e8a52209a837904e0539cad0f749acaeda2ae", "2.14.0--r42hdfd78af_0": "sha256:5e0dd5e0e4e1bd41a1e9887008be235e04397ef3f6ec2748843cbca8ca67fc2e", "2.10.0--r41hdfd78af_0": "sha256:630e2e4e629c043f81d79b4499ff376886b2c30c300faa78a7d5ef33c54e74d4"}, "docker": "quay.io/biocontainers/bioconductor-omadb", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-omadb.
shpc-registry automated BioContainers addition for bioconductor-omadb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-omadb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-omadb:2.14.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-omadb/2.14.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-omadb/2.14.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-omadb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-omadb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-omadb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-omadb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-omadb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-omadb-inspect-deffile:

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