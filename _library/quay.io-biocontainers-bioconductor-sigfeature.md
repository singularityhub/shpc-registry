---
layout: container
name:  "quay.io/biocontainers/bioconductor-sigfeature"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sigfeature/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sigfeature/container.yaml"
updated_at: "2023-09-14 03:11:34.527643"
latest: "1.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sigfeature"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sigfeature"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sigfeature", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sigfeature", "latest": {"1.18.0--r43hdfd78af_0": "sha256:f66cf8ca3eba0622f92213fbdce44ce6c8a4e48a691438de3c4531805d163105"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:cf19e911939096b313d9b9b63409cfbbfbd514098fac051f446c5c815f65414a", "1.16.0--r42hdfd78af_0": "sha256:a06b3899f176b2148892a196484feb5f0d4d0bd2fe0169dbfa93a582947bf9e9", "1.12.0--r41hdfd78af_0": "sha256:47396b5578843e609c6e8ca7e78e0d1b9ecdeebc5575bef3ceb4a26aa880dcbc", "1.10.0--r41hdfd78af_0": "sha256:e484057097e1efa0c337032c83e387851024308a09868d30c988d89f40bbe9a8", "1.18.0--r43hdfd78af_0": "sha256:f66cf8ca3eba0622f92213fbdce44ce6c8a4e48a691438de3c4531805d163105"}, "docker": "quay.io/biocontainers/bioconductor-sigfeature", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sigfeature.
shpc-registry automated BioContainers addition for bioconductor-sigfeature
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sigfeature
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sigfeature:1.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sigfeature/1.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-sigfeature/1.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sigfeature-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sigfeature-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sigfeature-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sigfeature-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sigfeature-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sigfeature-inspect-deffile:

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