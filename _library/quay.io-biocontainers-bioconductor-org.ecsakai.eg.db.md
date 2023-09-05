---
layout: container
name:  "quay.io/biocontainers/bioconductor-org.ecsakai.eg.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-org.ecsakai.eg.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-org.ecsakai.eg.db/container.yaml"
updated_at: "2023-09-05 03:08:37.028733"
latest: "3.16.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-org.ecsakai.eg.db"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.8.2--r36_1"
 - "3.16.0--r42hdfd78af_0"
 - "3.14.0--r41hdfd78af_1"
 - "3.13.0--r41hdfd78af_0"
 - "3.12.0--r40hdfd78af_1"
 - "3.11.1--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-org.ecsakai.eg.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-org.ecsakai.eg.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-org.ecsakai.eg.db", "latest": {"3.16.0--r42hdfd78af_0": "sha256:245313df9b0e48a66bcd12cd5e86bf3b33e3a8c04d843baaef85877125516165"}, "tags": {"3.8.2--r36_1": "sha256:45d2f46cf91d3a1c9728f272ce4dcfc3cba57d0b163f42fb508efb95a1bb079f", "3.16.0--r42hdfd78af_0": "sha256:245313df9b0e48a66bcd12cd5e86bf3b33e3a8c04d843baaef85877125516165", "3.14.0--r41hdfd78af_1": "sha256:3ebd8ef3b23336bbdf6b1e20b1b59a5cb0795f90e9fc9bf80fa4a5959a8f2c1d", "3.13.0--r41hdfd78af_0": "sha256:e285922a4c870e4ce7a57bd06f4a730e2a9844722cf401360e719f5ce5ea2d84", "3.12.0--r40hdfd78af_1": "sha256:7ae03e0c07118126902c144ac2728960473d0064138f4bc71d7d8b2ece627bd0", "3.11.1--r40_0": "sha256:6712d61579baf6ee6e2ed621eeb82777ed2692c6bbf8f183ee85512257763f14"}, "docker": "quay.io/biocontainers/bioconductor-org.ecsakai.eg.db", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-org.ecsakai.eg.db.
shpc-registry automated BioContainers addition for bioconductor-org.ecsakai.eg.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-org.ecsakai.eg.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-org.ecsakai.eg.db:3.16.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-org.ecsakai.eg.db/3.16.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-org.ecsakai.eg.db/3.16.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-org.ecsakai.eg.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-org.ecsakai.eg.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-org.ecsakai.eg.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-org.ecsakai.eg.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-org.ecsakai.eg.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-org.ecsakai.eg.db-inspect-deffile:

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