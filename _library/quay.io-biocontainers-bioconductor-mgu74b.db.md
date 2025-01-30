---
layout: container
name:  "quay.io/biocontainers/bioconductor-mgu74b.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mgu74b.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mgu74b.db/container.yaml"
updated_at: "2025-01-30 03:42:25.423912"
latest: "3.13.0--r44hdfd78af_5"
container_url: "https://biocontainers.pro/tools/bioconductor-mgu74b.db"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.2.3--r41hdfd78af_7"
 - "3.13.0--r42hdfd78af_2"
 - "3.13.0--r43hdfd78af_3"
 - "3.13.0--r43hdfd78af_4"
 - "3.13.0--r44hdfd78af_5"
description: "shpc-registry automated BioContainers addition for bioconductor-mgu74b.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mgu74b.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mgu74b.db", "latest": {"3.13.0--r44hdfd78af_5": "sha256:4b192e106d2ca3619bc5339e9fc8c1d7b525cea243308792bddd49e94f1811e8"}, "tags": {"3.2.3--r41hdfd78af_7": "sha256:1e5105a17b007a7ba0ddf78dc3af9ed99708a419de7752d4963296ff9c6cdc57", "3.13.0--r42hdfd78af_2": "sha256:19d66ee6c20e0c45dfeaaee3529e7a81d4a09eaa3a57b44caf4db13c2613ff79", "3.13.0--r43hdfd78af_3": "sha256:3e39e72b78ea7634116be030b584679cede45460ae9c5ced22d27d924731ea68", "3.13.0--r43hdfd78af_4": "sha256:ad22ba6cdebfb579fb117c20b17724de802e50d6fbf92f59b8a77693d49cfb95", "3.13.0--r44hdfd78af_5": "sha256:4b192e106d2ca3619bc5339e9fc8c1d7b525cea243308792bddd49e94f1811e8"}, "docker": "quay.io/biocontainers/bioconductor-mgu74b.db", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mgu74b.db.
shpc-registry automated BioContainers addition for bioconductor-mgu74b.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mgu74b.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mgu74b.db:3.13.0--r44hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mgu74b.db/3.13.0--r44hdfd78af_5
$ module help quay.io/biocontainers/bioconductor-mgu74b.db/3.13.0--r44hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mgu74b.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgu74b.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgu74b.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mgu74b.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mgu74b.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mgu74b.db-inspect-deffile:

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