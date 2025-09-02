---
layout: container
name:  "quay.io/biocontainers/bioconductor-mirintegrator"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mirintegrator/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mirintegrator/container.yaml"
updated_at: "2025-09-02 03:33:06.877586"
latest: "1.36.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mirintegrator"
aliases:
 - "wget"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_0"
 - "1.24.0--r41hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r40hdfd78af_1"
 - "1.18.0--r40_0"
 - "1.16.0--r36_0"
 - "1.28.0--r42hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
 - "1.36.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mirintegrator"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mirintegrator", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mirintegrator", "latest": {"1.36.0--r44hdfd78af_0": "sha256:604397931ab6b40072eb824a3a48e239c98cce088ed6fbcdeb48f579004b2e4b"}, "tags": {"1.8.0--r3.4.1_0": "sha256:db03f6778b30c02eb967264eff38cc367cf4078222bc1c3516960de4cf189c6f", "1.24.0--r41hdfd78af_0": "sha256:03e60d5c1babfa48e78fe55a097fc010b243e7fafdc45b1ad8422d21aefe97bb", "1.22.0--r41hdfd78af_0": "sha256:d2475fe0652b5ff19804bb521f7aabe87ae413f8b310e73ebe05d80a710e1c04", "1.20.0--r40hdfd78af_1": "sha256:f4d0112d3bfa84c1333575e63614e78b9ef0715ff0a183d5650a0eb999963d5c", "1.18.0--r40_0": "sha256:46b1dc45b4783bed4b9bb6b936664963df9ba9c90bf61ecc26627fe62b79b851", "1.16.0--r36_0": "sha256:8b2166b6fafd0537acaff97bc26b51ae64bf9a216ffff5deeba07890112da261", "1.28.0--r42hdfd78af_0": "sha256:33ad79e7030b4d67207ef36ab1965bb13055222b5cdead07ada3ed571f58e0cd", "1.30.0--r43hdfd78af_0": "sha256:9df0d04ede54e042efdd888a6dcf45722ab6810349b06ff52aa0ae4ec31a847a", "1.32.0--r43hdfd78af_0": "sha256:b95e3de04fcd83712cd6d6a48d1d4e32294545782b2b861169c47bf1f5d55327", "1.36.0--r44hdfd78af_0": "sha256:604397931ab6b40072eb824a3a48e239c98cce088ed6fbcdeb48f579004b2e4b"}, "docker": "quay.io/biocontainers/bioconductor-mirintegrator", "aliases": {"wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mirintegrator.
shpc-registry automated BioContainers addition for bioconductor-mirintegrator
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mirintegrator
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mirintegrator:1.36.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mirintegrator/1.36.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mirintegrator/1.36.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mirintegrator-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mirintegrator-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mirintegrator-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mirintegrator-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mirintegrator-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mirintegrator-inspect-deffile:

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