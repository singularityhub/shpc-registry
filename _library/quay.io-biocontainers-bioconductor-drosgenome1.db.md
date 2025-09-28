---
layout: container
name:  "quay.io/biocontainers/bioconductor-drosgenome1.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-drosgenome1.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-drosgenome1.db/container.yaml"
updated_at: "2025-09-28 03:35:40.687494"
latest: "3.13.0--r44hdfd78af_5"
container_url: "https://biocontainers.pro/tools/bioconductor-drosgenome1.db"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.2.3--r41hdfd78af_7"
 - "3.13.0--r42hdfd78af_2"
 - "3.13.0--r43hdfd78af_3"
 - "3.13.0--r43hdfd78af_4"
 - "3.13.0--r44hdfd78af_5"
description: "shpc-registry automated BioContainers addition for bioconductor-drosgenome1.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-drosgenome1.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-drosgenome1.db", "latest": {"3.13.0--r44hdfd78af_5": "sha256:0b6b8ce8d56dcafec39b6a62697e465bebc8e58dbbd5e23566f423b73653fa60"}, "tags": {"3.2.3--r41hdfd78af_7": "sha256:93f8f2f51bdc952fa9f7db6bd4d7c0b4fb36f6eeebe1a19575321942ec014295", "3.13.0--r42hdfd78af_2": "sha256:60368517cdf004aec345e7d0947bed7fe6b8444e2eeb8a72765c58ae0c53ec82", "3.13.0--r43hdfd78af_3": "sha256:bd50e9cde50ba2b339c44f5344e13e8438bcc54825b13f7510ea618c480644d6", "3.13.0--r43hdfd78af_4": "sha256:a54379a7634f265167b918c867d4fc3777a1520b515d0e916ae51bc91ab7ada8", "3.13.0--r44hdfd78af_5": "sha256:0b6b8ce8d56dcafec39b6a62697e465bebc8e58dbbd5e23566f423b73653fa60"}, "docker": "quay.io/biocontainers/bioconductor-drosgenome1.db", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-drosgenome1.db.
shpc-registry automated BioContainers addition for bioconductor-drosgenome1.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-drosgenome1.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-drosgenome1.db:3.13.0--r44hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-drosgenome1.db/3.13.0--r44hdfd78af_5
$ module help quay.io/biocontainers/bioconductor-drosgenome1.db/3.13.0--r44hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-drosgenome1.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-drosgenome1.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-drosgenome1.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-drosgenome1.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-drosgenome1.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-drosgenome1.db-inspect-deffile:

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