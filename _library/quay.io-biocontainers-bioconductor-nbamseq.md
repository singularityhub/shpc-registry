---
layout: container
name:  "quay.io/biocontainers/bioconductor-nbamseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-nbamseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-nbamseq/container.yaml"
updated_at: "2025-10-13 04:11:57.077858"
latest: "1.22.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-nbamseq"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.22.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-nbamseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-nbamseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-nbamseq", "latest": {"1.22.0--r44hdfd78af_0": "sha256:38d6df21e1c3d89c23d019dc5bcb431d73f796e9d2502b977d933a43cf1f9055"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:b81384b64857c72bbb4dd2840a884b84f455fc30e28542abad6b281d0894cfe8", "1.14.0--r42hdfd78af_0": "sha256:c7db7c72f96b633d326b65e7c0ca43fc6f3bc421fb7b5c5baa0b974d5f598486", "1.10.0--r41hdfd78af_0": "sha256:e1357ef8206dd4a6e693d729b244ad0bf1117a9721541259d74c8e8abfae365f", "1.16.0--r43hdfd78af_0": "sha256:56c27bdbab93acc42b77958408fe6d01b1fd401456c603595621e5b56e74b77a", "1.18.0--r43hdfd78af_0": "sha256:4392cd7eafa33e929e41e127c84d7be8ad8d6cee7173bd89b396634f5f5145e3", "1.22.0--r44hdfd78af_0": "sha256:38d6df21e1c3d89c23d019dc5bcb431d73f796e9d2502b977d933a43cf1f9055"}, "docker": "quay.io/biocontainers/bioconductor-nbamseq", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-nbamseq.
shpc-registry automated BioContainers addition for bioconductor-nbamseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-nbamseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-nbamseq:1.22.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-nbamseq/1.22.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-nbamseq/1.22.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-nbamseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nbamseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nbamseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-nbamseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-nbamseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-nbamseq-inspect-deffile:

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