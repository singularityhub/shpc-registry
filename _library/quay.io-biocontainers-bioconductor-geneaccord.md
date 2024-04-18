---
layout: container
name:  "quay.io/biocontainers/bioconductor-geneaccord"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-geneaccord/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-geneaccord/container.yaml"
updated_at: "2024-04-18 02:53:52.342796"
latest: "1.15.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-geneaccord"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.15.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-geneaccord"
config: {"url": "https://biocontainers.pro/tools/bioconductor-geneaccord", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-geneaccord", "latest": {"1.15.0--r42hdfd78af_0": "sha256:6f49f71ec44067387deb7b27bae147e2395cc33b4f00262409d1f605722acdf1"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:77ef800b8b666ac40a288506d91902940ecc7fc3448904c97d102b8dfeaf13c6", "1.15.0--r42hdfd78af_0": "sha256:6f49f71ec44067387deb7b27bae147e2395cc33b4f00262409d1f605722acdf1", "1.12.0--r41hdfd78af_0": "sha256:d608123c657f66b86b539fcbc8c1022c77a2a2ef20087201ad3f423e3004d8e9", "1.10.0--r41hdfd78af_0": "sha256:b6e873d557444fd3ae242a8944c6980ec04b1afa5094acc93eb4bbf69572316b"}, "docker": "quay.io/biocontainers/bioconductor-geneaccord", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-geneaccord.
shpc-registry automated BioContainers addition for bioconductor-geneaccord
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-geneaccord
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-geneaccord:1.15.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-geneaccord/1.15.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-geneaccord/1.15.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-geneaccord-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-geneaccord-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-geneaccord-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-geneaccord-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-geneaccord-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-geneaccord-inspect-deffile:

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