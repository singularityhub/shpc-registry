---
layout: container
name:  "quay.io/biocontainers/bioconductor-mouse4302.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mouse4302.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mouse4302.db/container.yaml"
updated_at: "2025-11-20 03:43:38.325608"
latest: "3.13.0--r44hdfd78af_5"
container_url: "https://biocontainers.pro/tools/bioconductor-mouse4302.db"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.2.3--r41hdfd78af_7"
 - "3.13.0--r42hdfd78af_2"
 - "3.13.0--r43hdfd78af_3"
 - "3.13.0--r43hdfd78af_4"
 - "3.13.0--r44hdfd78af_5"
description: "shpc-registry automated BioContainers addition for bioconductor-mouse4302.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mouse4302.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mouse4302.db", "latest": {"3.13.0--r44hdfd78af_5": "sha256:798474c4b241374af3d4a26e7833d1c126bd213b7febe51a306d30be6e297778"}, "tags": {"3.2.3--r41hdfd78af_7": "sha256:78773372bc84d56d7d01f6faeaa9e522b692d4e09619305d300e6cb40f0a5e07", "3.13.0--r42hdfd78af_2": "sha256:a526fc7216bc6f56f6a8560d9bc3b9b81ef8efdf30a352901b8ac6cf19c582a3", "3.13.0--r43hdfd78af_3": "sha256:67b1ccd5849681bb79a112ca67c2216f9a730dfaf1547c1282ef3508629a224b", "3.13.0--r43hdfd78af_4": "sha256:b2e86b4b01644c5e8b22a5dbf1f096c1b831b27054eb6bfc6a97e9092f228757", "3.13.0--r44hdfd78af_5": "sha256:798474c4b241374af3d4a26e7833d1c126bd213b7febe51a306d30be6e297778"}, "docker": "quay.io/biocontainers/bioconductor-mouse4302.db", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mouse4302.db.
shpc-registry automated BioContainers addition for bioconductor-mouse4302.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mouse4302.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mouse4302.db:3.13.0--r44hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mouse4302.db/3.13.0--r44hdfd78af_5
$ module help quay.io/biocontainers/bioconductor-mouse4302.db/3.13.0--r44hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mouse4302.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mouse4302.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mouse4302.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mouse4302.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mouse4302.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mouse4302.db-inspect-deffile:

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