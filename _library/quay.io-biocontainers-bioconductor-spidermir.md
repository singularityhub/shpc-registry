---
layout: container
name:  "quay.io/biocontainers/bioconductor-spidermir"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-spidermir/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-spidermir/container.yaml"
updated_at: "2023-05-12 02:53:02.680315"
latest: "1.28.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-spidermir"
aliases:
 - "wget"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.2--r3.4.1_0"
 - "1.24.0--r41hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r40hdfd78af_1"
 - "1.18.0--r40_0"
 - "1.16.0--r36_0"
 - "1.28.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-spidermir"
config: {"url": "https://biocontainers.pro/tools/bioconductor-spidermir", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-spidermir", "latest": {"1.28.0--r42hdfd78af_0": "sha256:6c3efb5e537c6b735b5b4342627b08a3561ab5496a098d1075692d900da07ee0"}, "tags": {"1.8.2--r3.4.1_0": "sha256:7c1cbd8b6a2ce06b93b4a0bd3e5495f4fd7b4bd9cfe6f48d4317bce4a5c6c4be", "1.24.0--r41hdfd78af_0": "sha256:cd96ad5b6eec227adb68ad933346004836f77add9e80b71cffcf4daf7a2bb8dc", "1.22.0--r41hdfd78af_0": "sha256:da62464fc5a9369d55836cd5d2da989afe898e307ecb15b45b171f7b18eff159", "1.20.0--r40hdfd78af_1": "sha256:e278a2a37f645e77d21cd98cffad9cd4806a4a3bfbcda4efaf1e18af2e8fcfe8", "1.18.0--r40_0": "sha256:42220c8ebdbae253c1b8b583afe5a562ba4863d28f820303e4dbd26565921ca0", "1.16.0--r36_0": "sha256:eecf20c2c5e216bff6f8d82220bd7e755194ba0eee4bb71d80522d062b8dc392", "1.28.0--r42hdfd78af_0": "sha256:6c3efb5e537c6b735b5b4342627b08a3561ab5496a098d1075692d900da07ee0"}, "docker": "quay.io/biocontainers/bioconductor-spidermir", "aliases": {"wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-spidermir.
shpc-registry automated BioContainers addition for bioconductor-spidermir
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-spidermir
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-spidermir:1.28.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-spidermir/1.28.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-spidermir/1.28.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-spidermir-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spidermir-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spidermir-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-spidermir-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-spidermir-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-spidermir-inspect-deffile:

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