---
layout: container
name:  "quay.io/biocontainers/bioconductor-metabosignal"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-metabosignal/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-metabosignal/container.yaml"
updated_at: "2023-05-05 03:10:42.555748"
latest: "1.28.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-metabosignal"
aliases:
 - "wget"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_0"
 - "1.28.0--r42hdfd78af_0"
 - "1.24.0--r41hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r40hdfd78af_1"
 - "1.18.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-metabosignal"
config: {"url": "https://biocontainers.pro/tools/bioconductor-metabosignal", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-metabosignal", "latest": {"1.28.0--r42hdfd78af_0": "sha256:301fa25271b13aabbbe70aa8319b3963f45e608c5fbd1d2b07b95cb20a515c5f"}, "tags": {"1.8.0--r3.4.1_0": "sha256:910b79c21d580fa7eed3a032266d45b78b4123e142546fa2352814f95ccb4485", "1.28.0--r42hdfd78af_0": "sha256:301fa25271b13aabbbe70aa8319b3963f45e608c5fbd1d2b07b95cb20a515c5f", "1.24.0--r41hdfd78af_0": "sha256:46f8ca90b5b3a9bb8357960d1393c788f179fc6fb38d3e5da09c1d03b983f686", "1.22.0--r41hdfd78af_0": "sha256:2ca6580472d63d39f5022cf5b9a26b214bfbdacbc8f91cfc1f153a13f649b311", "1.20.0--r40hdfd78af_1": "sha256:877364ff0a0affb3f20b89e9a4e1c9b2b633fdb997251f7b6cf6ef5e48becafd", "1.18.0--r40_0": "sha256:c65fad9565c4431835aeb9c84119c364182dd38db1a0ff616f916b8d3e611ee6"}, "docker": "quay.io/biocontainers/bioconductor-metabosignal", "aliases": {"wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-metabosignal.
shpc-registry automated BioContainers addition for bioconductor-metabosignal
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-metabosignal
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-metabosignal:1.28.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-metabosignal/1.28.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-metabosignal/1.28.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-metabosignal-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metabosignal-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metabosignal-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-metabosignal-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-metabosignal-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-metabosignal-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncurses5-config

```bash
$ singularity exec <container> /usr/local/bin/ncurses5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncursesw5-config

```bash
$ singularity exec <container> /usr/local/bin/ncursesw5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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