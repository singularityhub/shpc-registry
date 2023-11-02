---
layout: container
name:  "quay.io/biocontainers/bioconductor-org.ss.eg.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-org.ss.eg.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-org.ss.eg.db/container.yaml"
updated_at: "2023-11-02 03:29:35.903457"
latest: "3.17.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-org.ss.eg.db"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.8.2--r36_1"
 - "3.16.0--r42hdfd78af_0"
 - "3.14.0--r41hdfd78af_1"
 - "3.12.0--r40hdfd78af_1"
 - "3.11.1--r40_0"
 - "3.10.0--r36_0"
 - "3.17.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-org.ss.eg.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-org.ss.eg.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-org.ss.eg.db", "latest": {"3.17.0--r43hdfd78af_0": "sha256:595b69ce1ea3c8ec3c8c91df00d5324d5e7eb8ae5656850571335e57c14e3169"}, "tags": {"3.8.2--r36_1": "sha256:418814e84b50cd5bc3335ef782e3840e60cef0874841cfb25da28ac67cb85454", "3.16.0--r42hdfd78af_0": "sha256:ad7ed35b9935177eded8c32ba70823f69ccbc8bde240448e147be6160785720b", "3.14.0--r41hdfd78af_1": "sha256:2569652f2f5b2c7dce3f584486f3520874f796b81813481616a08bb7f31e31a7", "3.12.0--r40hdfd78af_1": "sha256:0572dcb2c7cea15caaf4d58c97c6ec56fec6f3b8e782ef9b410f80ec1012f387", "3.11.1--r40_0": "sha256:c4ed02c20f116a67835e5284f9b8dcc7577cf693c3c48523ba9599be7ffced09", "3.10.0--r36_0": "sha256:b69f339d63797755dd054efdea77a127a25ad792f990ed0243a9b11037a87ede", "3.17.0--r43hdfd78af_0": "sha256:595b69ce1ea3c8ec3c8c91df00d5324d5e7eb8ae5656850571335e57c14e3169"}, "docker": "quay.io/biocontainers/bioconductor-org.ss.eg.db", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-org.ss.eg.db.
shpc-registry automated BioContainers addition for bioconductor-org.ss.eg.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-org.ss.eg.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-org.ss.eg.db:3.17.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-org.ss.eg.db/3.17.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-org.ss.eg.db/3.17.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-org.ss.eg.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-org.ss.eg.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-org.ss.eg.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-org.ss.eg.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-org.ss.eg.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-org.ss.eg.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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