---
layout: container
name:  "quay.io/biocontainers/bioconductor-org.bt.eg.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-org.bt.eg.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-org.bt.eg.db/container.yaml"
updated_at: "2023-10-21 02:37:49.633905"
latest: "3.17.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-org.bt.eg.db"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.8.2--r36_1"
 - "3.14.0--r41hdfd78af_1"
 - "3.13.0--r41hdfd78af_0"
 - "3.12.0--r40hdfd78af_1"
 - "3.11.1--r40_0"
 - "3.10.0--r36_0"
 - "3.16.0--r42hdfd78af_0"
 - "3.17.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-org.bt.eg.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-org.bt.eg.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-org.bt.eg.db", "latest": {"3.17.0--r43hdfd78af_0": "sha256:5b9d9d42054299c80f497c610e916f739a1da1c636b711a19d2db76de169fa4a"}, "tags": {"3.8.2--r36_1": "sha256:606617bd5e55b60eed7145284b7c426003e31ff3c587288bcbff621b99042889", "3.14.0--r41hdfd78af_1": "sha256:df74b519cfc1265834a2e0cf32abf948035efbd34c74239dc18398d7e7f0403a", "3.13.0--r41hdfd78af_0": "sha256:b38dc49bce112c079faeb8b03c5902b062f75e19479bf4a02c3906ec8c4f55bc", "3.12.0--r40hdfd78af_1": "sha256:c30669a1bd1fec0b293c965354214c71b4f5721e8ff0009da0cebead0b4419f1", "3.11.1--r40_0": "sha256:81702990531f7b70da06f9418dd5c5afc5eefd2d37f60208af84b816aaf12115", "3.10.0--r36_0": "sha256:ac37ee2fc1437d1126eae4aaf19ce007cacb564a9af37a03ab669c0bac773d32", "3.16.0--r42hdfd78af_0": "sha256:b27eba59a9021f35e52a45d8d179638b74ccd72144f98095da95e69f9b470f54", "3.17.0--r43hdfd78af_0": "sha256:5b9d9d42054299c80f497c610e916f739a1da1c636b711a19d2db76de169fa4a"}, "docker": "quay.io/biocontainers/bioconductor-org.bt.eg.db", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-org.bt.eg.db.
shpc-registry automated BioContainers addition for bioconductor-org.bt.eg.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-org.bt.eg.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-org.bt.eg.db:3.17.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-org.bt.eg.db/3.17.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-org.bt.eg.db/3.17.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-org.bt.eg.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-org.bt.eg.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-org.bt.eg.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-org.bt.eg.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-org.bt.eg.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-org.bt.eg.db-inspect-deffile:

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