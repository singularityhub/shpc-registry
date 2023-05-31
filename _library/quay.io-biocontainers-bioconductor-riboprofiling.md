---
layout: container
name:  "quay.io/biocontainers/bioconductor-riboprofiling"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-riboprofiling/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-riboprofiling/container.yaml"
updated_at: "2023-05-31 03:35:55.935820"
latest: "1.28.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-riboprofiling"
aliases:
 - "my_print_defaults"
 - "mysql_config"
 - "perror"
 - "wget"
 - "tclsh8.5"
 - "wish8.5"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.7.1--r3.4.1_0"
 - "1.24.0--r41hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r40hdfd78af_1"
 - "1.18.0--r40_0"
 - "1.16.0--r36_0"
 - "1.28.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-riboprofiling"
config: {"url": "https://biocontainers.pro/tools/bioconductor-riboprofiling", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-riboprofiling", "latest": {"1.28.0--r42hdfd78af_0": "sha256:94d950361b7772a8488817c7351b0e63a5ae1937491ec0e79debc33591bfbacd"}, "tags": {"1.7.1--r3.4.1_0": "sha256:ba75bc0b5cc0cb6a52e64be209cda149bfe74b5e5bdd27f219990a6fbe4e2364", "1.24.0--r41hdfd78af_0": "sha256:6775a1f7d377fe1a098904a675c30f894169b94e97f8ce8145aa618f25030945", "1.22.0--r41hdfd78af_0": "sha256:f697ffcd8e27bc46a2d13771a87e67514b3a762bbf0d29bc5e42ee3d30f15c94", "1.20.0--r40hdfd78af_1": "sha256:1f15cda22a5512dd3b711ec060372d550c79681e27d8ae3182698f9569c7a85d", "1.18.0--r40_0": "sha256:fe3f5a1e0b4b02b0c5d8cdc073930537c18e5d078b4ba6bf136f8f5479ee0866", "1.16.0--r36_0": "sha256:471d4c292875dcb7384d87edffe0534bd40d2a4ffc01d6fb3fbb0f585f0d6316", "1.28.0--r42hdfd78af_0": "sha256:94d950361b7772a8488817c7351b0e63a5ae1937491ec0e79debc33591bfbacd"}, "docker": "quay.io/biocontainers/bioconductor-riboprofiling", "aliases": {"my_print_defaults": "/usr/local/bin/my_print_defaults", "mysql_config": "/usr/local/bin/mysql_config", "perror": "/usr/local/bin/perror", "wget": "/usr/local/bin/wget", "tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-riboprofiling.
shpc-registry automated BioContainers addition for bioconductor-riboprofiling
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-riboprofiling
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-riboprofiling:1.28.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-riboprofiling/1.28.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-riboprofiling/1.28.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-riboprofiling-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-riboprofiling-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-riboprofiling-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-riboprofiling-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-riboprofiling-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-riboprofiling-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### my_print_defaults

```bash
$ singularity exec <container> /usr/local/bin/my_print_defaults
$ podman run --it --rm --entrypoint /usr/local/bin/my_print_defaults   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/my_print_defaults   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mysql_config

```bash
$ singularity exec <container> /usr/local/bin/mysql_config
$ podman run --it --rm --entrypoint /usr/local/bin/mysql_config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mysql_config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perror

```bash
$ singularity exec <container> /usr/local/bin/perror
$ podman run --it --rm --entrypoint /usr/local/bin/perror   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perror   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tclsh8.5

```bash
$ singularity exec <container> /usr/local/bin/tclsh8.5
$ podman run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wish8.5

```bash
$ singularity exec <container> /usr/local/bin/wish8.5
$ podman run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
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