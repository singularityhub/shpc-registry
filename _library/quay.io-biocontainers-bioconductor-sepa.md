---
layout: container
name:  "quay.io/biocontainers/bioconductor-sepa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sepa/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sepa/container.yaml"
updated_at: "2022-10-27 00:54:17.672789"
latest: "1.8.0--r3.4.1_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sepa"
aliases:
 - "GO.db_3.5.0_R_x86_64-pc-linux-gnu.tar.gz"
 - "org.Hs.eg.db_3.4.2_R_x86_64-pc-linux-gnu.tar.gz"
 - "org.Mm.eg.db_3.5.0_R_x86_64-pc-linux-gnu.tar.gz"
versions:
 - "1.8.0--r3.4.1_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sepa"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sepa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sepa", "latest": {"1.8.0--r3.4.1_0": "sha256:56e29c4a2e3ed957c0cc6e8fd6fc6c973ccb02ed057fd7ca8524f4d0f5275bfd"}, "tags": {"1.8.0--r3.4.1_0": "sha256:56e29c4a2e3ed957c0cc6e8fd6fc6c973ccb02ed057fd7ca8524f4d0f5275bfd"}, "docker": "quay.io/biocontainers/bioconductor-sepa", "aliases": {"GO.db_3.5.0_R_x86_64-pc-linux-gnu.tar.gz": "/usr/local/bin/GO.db_3.5.0_R_x86_64-pc-linux-gnu.tar.gz", "org.Hs.eg.db_3.4.2_R_x86_64-pc-linux-gnu.tar.gz": "/usr/local/bin/org.Hs.eg.db_3.4.2_R_x86_64-pc-linux-gnu.tar.gz", "org.Mm.eg.db_3.5.0_R_x86_64-pc-linux-gnu.tar.gz": "/usr/local/bin/org.Mm.eg.db_3.5.0_R_x86_64-pc-linux-gnu.tar.gz"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sepa.
shpc-registry automated BioContainers addition for bioconductor-sepa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sepa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sepa:1.8.0--r3.4.1_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sepa/1.8.0--r3.4.1_0
$ module help quay.io/biocontainers/bioconductor-sepa/1.8.0--r3.4.1_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sepa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sepa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sepa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sepa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sepa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sepa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GO.db_3.5.0_R_x86_64-pc-linux-gnu.tar.gz

```bash
$ singularity exec <container> /usr/local/bin/GO.db_3.5.0_R_x86_64-pc-linux-gnu.tar.gz
$ podman run --it --rm --entrypoint /usr/local/bin/GO.db_3.5.0_R_x86_64-pc-linux-gnu.tar.gz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GO.db_3.5.0_R_x86_64-pc-linux-gnu.tar.gz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### org.Hs.eg.db_3.4.2_R_x86_64-pc-linux-gnu.tar.gz

```bash
$ singularity exec <container> /usr/local/bin/org.Hs.eg.db_3.4.2_R_x86_64-pc-linux-gnu.tar.gz
$ podman run --it --rm --entrypoint /usr/local/bin/org.Hs.eg.db_3.4.2_R_x86_64-pc-linux-gnu.tar.gz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/org.Hs.eg.db_3.4.2_R_x86_64-pc-linux-gnu.tar.gz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### org.Mm.eg.db_3.5.0_R_x86_64-pc-linux-gnu.tar.gz

```bash
$ singularity exec <container> /usr/local/bin/org.Mm.eg.db_3.5.0_R_x86_64-pc-linux-gnu.tar.gz
$ podman run --it --rm --entrypoint /usr/local/bin/org.Mm.eg.db_3.5.0_R_x86_64-pc-linux-gnu.tar.gz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/org.Mm.eg.db_3.5.0_R_x86_64-pc-linux-gnu.tar.gz   -v ${PWD} -w ${PWD} <container> -c " $@"
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