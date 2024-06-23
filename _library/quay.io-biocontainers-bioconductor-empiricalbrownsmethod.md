---
layout: container
name:  "quay.io/biocontainers/bioconductor-empiricalbrownsmethod"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-empiricalbrownsmethod/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-empiricalbrownsmethod/container.yaml"
updated_at: "2024-06-23 02:43:44.100123"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-empiricalbrownsmethod"
aliases:
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r341_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_1"
 - "1.16.0--r40_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-empiricalbrownsmethod"
config: {"url": "https://biocontainers.pro/tools/bioconductor-empiricalbrownsmethod", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-empiricalbrownsmethod", "latest": {"1.30.0--r43hdfd78af_0": "sha256:fa82c500099876fdf1569674d6dc4cdb6be23b684c88583dc72b9c69c85e60b5"}, "tags": {"1.8.0--r341_0": "sha256:0fa56e514741d38ae3ea67d97a6782258353267a287703bdb777d9a513cb660c", "1.26.0--r42hdfd78af_0": "sha256:ce5dd6a5b685d1dfa5bef218b871f3cf7ac17bf85ad8f2fb20b56b8d7ed18504", "1.22.0--r41hdfd78af_0": "sha256:6a2df0b121b1b600c32610b8b585ff392726e116180ad2e74cda901fbe1f0dd9", "1.20.0--r41hdfd78af_0": "sha256:d2f0c76e24ef7b270137da1906a4a54f3d937a8fc38696dd1212718b669e7f4c", "1.18.0--r40hdfd78af_1": "sha256:803a9f8f4f8b3f543f13aae17e8f09f99f56b9a839b2aada33ad15273320cdf2", "1.16.0--r40_0": "sha256:31e691408c4c4abd83c8ffdf563d1c03c6247c5644df2945fc9a0325146906c4", "1.28.0--r43hdfd78af_0": "sha256:82d76dba71f34563b49ae298d488aaa25bc531be90eff27e7ec661756d163254", "1.30.0--r43hdfd78af_0": "sha256:fa82c500099876fdf1569674d6dc4cdb6be23b684c88583dc72b9c69c85e60b5"}, "docker": "quay.io/biocontainers/bioconductor-empiricalbrownsmethod", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-empiricalbrownsmethod.
shpc-registry automated BioContainers addition for bioconductor-empiricalbrownsmethod
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-empiricalbrownsmethod
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-empiricalbrownsmethod:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-empiricalbrownsmethod/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-empiricalbrownsmethod/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-empiricalbrownsmethod-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-empiricalbrownsmethod-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-empiricalbrownsmethod-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-empiricalbrownsmethod-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-empiricalbrownsmethod-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-empiricalbrownsmethod-inspect-deffile:

```bash
$ singularity inspect -d <container>
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