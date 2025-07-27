---
layout: container
name:  "quay.io/biocontainers/bioconductor-bgeedb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bgeedb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bgeedb/container.yaml"
updated_at: "2025-07-27 04:30:14.905577"
latest: "2.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bgeedb"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "2.8.0--r351_0"
 - "2.20.0--r41hdfd78af_0"
 - "2.18.0--r41hdfd78af_0"
 - "2.16.0--r40hdfd78af_1"
 - "2.14.0--r40_0"
 - "2.12.0--r36_0"
 - "2.24.0--r42hdfd78af_0"
 - "2.26.0--r43hdfd78af_0"
 - "2.28.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bgeedb"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bgeedb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bgeedb", "latest": {"2.28.0--r43hdfd78af_0": "sha256:43fca2ce18690fafff6858c17dd57de3c402e88a02b7981abac7b6530c5a4d06"}, "tags": {"2.8.0--r351_0": "sha256:ecb6c0a7e4b92ba7340ef89072b75f85fd9ba3bbb7578bd5cfa13bc8f74d0a5f", "2.20.0--r41hdfd78af_0": "sha256:0aa6d7c602b592cde9d4be843b6c8bc2a47fb3e80641c474c4750de005fbbca8", "2.18.0--r41hdfd78af_0": "sha256:708ecf7e4475c38aa4169dd91a93ae18bfdd6e41ed9216d278c2870e51f5fe0d", "2.16.0--r40hdfd78af_1": "sha256:9befd42b40a962a6de7bb85fb2f07b19eae1c59a40d1fdb5fd06f9fbe1d07075", "2.14.0--r40_0": "sha256:d2c25d00a26c8d24b01dc2c12117593b2adf68b5c9aaeeac3732fd678ac26389", "2.12.0--r36_0": "sha256:934f37bb6896df87abbd966ee34aaf3a253abfce32e5c08b61f1251832c28dc4", "2.24.0--r42hdfd78af_0": "sha256:6aedd0139528106866d1c0b3a67eac78fd24f8a5b2e20280f46b22e228c0d57c", "2.26.0--r43hdfd78af_0": "sha256:d4a4725e0c00f2ab639781a29399c0a8a30c61230018af038f8e440a57a40454", "2.28.0--r43hdfd78af_0": "sha256:43fca2ce18690fafff6858c17dd57de3c402e88a02b7981abac7b6530c5a4d06"}, "docker": "quay.io/biocontainers/bioconductor-bgeedb", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bgeedb.
shpc-registry automated BioContainers addition for bioconductor-bgeedb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bgeedb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bgeedb:2.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bgeedb/2.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-bgeedb/2.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bgeedb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bgeedb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bgeedb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bgeedb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bgeedb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bgeedb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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