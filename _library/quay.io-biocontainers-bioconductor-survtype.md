---
layout: container
name:  "quay.io/biocontainers/bioconductor-survtype"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-survtype/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-survtype/container.yaml"
updated_at: "2024-05-06 04:49:21.527343"
latest: "1.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-survtype"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-survtype"
config: {"url": "https://biocontainers.pro/tools/bioconductor-survtype", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-survtype", "latest": {"1.18.0--r43hdfd78af_0": "sha256:61d637c7843f16ce7aadda93c6752e8d79ddfe01751ac54a55dd8958539104aa"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:5181806557a6f8aa982f8c2099615509582c60dfe6b1d13007e2424be2a992c2", "1.14.0--r42hdfd78af_0": "sha256:25d4594998b28d476fc61e076c42d8245f9c2eaa1e3ade21628f0416aa81e485", "1.10.0--r41hdfd78af_0": "sha256:46f0f6b292244df9017a13b390dc0c9de5319acbd553f99ae2be645a52d16cfe", "1.16.0--r43hdfd78af_0": "sha256:ae6f390a54ed76f58f4b2ace449c4edbf0fc3077aeec8bb73bad1b958193f3cb", "1.18.0--r43hdfd78af_0": "sha256:61d637c7843f16ce7aadda93c6752e8d79ddfe01751ac54a55dd8958539104aa"}, "docker": "quay.io/biocontainers/bioconductor-survtype", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-survtype.
shpc-registry automated BioContainers addition for bioconductor-survtype
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-survtype
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-survtype:1.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-survtype/1.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-survtype/1.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-survtype-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-survtype-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-survtype-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-survtype-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-survtype-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-survtype-inspect-deffile:

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