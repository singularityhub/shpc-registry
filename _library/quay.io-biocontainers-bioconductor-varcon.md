---
layout: container
name:  "quay.io/biocontainers/bioconductor-varcon"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-varcon/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-varcon/container.yaml"
updated_at: "2024-01-01 03:13:19.197448"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-varcon"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-varcon"
config: {"url": "https://biocontainers.pro/tools/bioconductor-varcon", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-varcon", "latest": {"1.10.0--r43hdfd78af_0": "sha256:bd69682edbc4d4d7233026cfe56368a5bd43d29d9d8d481798741b079a647f85"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:95d09e3a6a61795afbacea6adfb1a25f97a866fae61e196fd2587be17354fff1", "1.6.0--r42hdfd78af_0": "sha256:d587ff80837e4c4315f5c1e33d64ccb85fb5e47fde3ed91599703731b8aa646c", "1.8.0--r43hdfd78af_0": "sha256:ce04075d033ac6d8999afe23bfc465b055c59d0b14349720b1ce235627973fdc", "1.10.0--r43hdfd78af_0": "sha256:bd69682edbc4d4d7233026cfe56368a5bd43d29d9d8d481798741b079a647f85"}, "docker": "quay.io/biocontainers/bioconductor-varcon"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-varcon.
shpc-registry automated BioContainers addition for bioconductor-varcon
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-varcon
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-varcon:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-varcon/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-varcon/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-varcon-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-varcon-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-varcon-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-varcon-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-varcon-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-varcon-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-varcon

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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