---
layout: container
name:  "quay.io/biocontainers/bioconductor-mu11ksuba.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mu11ksuba.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mu11ksuba.db/container.yaml"
updated_at: "2022-11-22 01:25:27.861911"
latest: "3.13.0--r42hdfd78af_2"
container_url: "https://biocontainers.pro/tools/bioconductor-mu11ksuba.db"
aliases:
 - ".bioconductor-mu11ksuba.db-post-link.sh"
 - ".bioconductor-mu11ksuba.db-pre-unlink.sh"
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.2.3--r41hdfd78af_7"
 - "3.13.0--r42hdfd78af_2"
description: "shpc-registry automated BioContainers addition for bioconductor-mu11ksuba.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mu11ksuba.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mu11ksuba.db", "latest": {"3.13.0--r42hdfd78af_2": "sha256:5c7e215ed2c5222951b460366c441a74e55c69918a5b0359bdd0e5ebc85d31e0"}, "tags": {"3.2.3--r41hdfd78af_7": "sha256:447782cffdb5d413c382696417272f4a5998e27fb15095bc291f236e5f4fb41e", "3.13.0--r42hdfd78af_2": "sha256:5c7e215ed2c5222951b460366c441a74e55c69918a5b0359bdd0e5ebc85d31e0"}, "docker": "quay.io/biocontainers/bioconductor-mu11ksuba.db", "aliases": {".bioconductor-mu11ksuba.db-post-link.sh": "/usr/local/bin/.bioconductor-mu11ksuba.db-post-link.sh", ".bioconductor-mu11ksuba.db-pre-unlink.sh": "/usr/local/bin/.bioconductor-mu11ksuba.db-pre-unlink.sh", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mu11ksuba.db.
shpc-registry automated BioContainers addition for bioconductor-mu11ksuba.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mu11ksuba.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mu11ksuba.db:3.13.0--r42hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mu11ksuba.db/3.13.0--r42hdfd78af_2
$ module help quay.io/biocontainers/bioconductor-mu11ksuba.db/3.13.0--r42hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mu11ksuba.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mu11ksuba.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mu11ksuba.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mu11ksuba.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mu11ksuba.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mu11ksuba.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .bioconductor-mu11ksuba.db-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-mu11ksuba.db-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-mu11ksuba.db-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-mu11ksuba.db-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-mu11ksuba.db-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-mu11ksuba.db-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-mu11ksuba.db-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-mu11ksuba.db-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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