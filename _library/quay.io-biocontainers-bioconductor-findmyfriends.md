---
layout: container
name:  "quay.io/biocontainers/bioconductor-findmyfriends"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-findmyfriends/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-findmyfriends/container.yaml"
updated_at: "2026-01-05 06:15:13.991463"
latest: "1.23.0--r41h619a076_1"
container_url: "https://biocontainers.pro/tools/bioconductor-findmyfriends"
aliases:
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_0"
 - "1.23.0--r41h619a076_1"
 - "1.22.0--r41h399db7b_0"
 - "1.20.0--r40h399db7b_1"
 - "1.18.0--r40h5f743cb_0"
 - "1.16.0--r36he1b5a44_0"
description: "shpc-registry automated BioContainers addition for bioconductor-findmyfriends"
config: {"url": "https://biocontainers.pro/tools/bioconductor-findmyfriends", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-findmyfriends", "latest": {"1.23.0--r41h619a076_1": "sha256:a0f32fcd88acee95e4192a4bd439ce5b0998ff96ec25694989f405258268d06a"}, "tags": {"1.8.0--r3.4.1_0": "sha256:baaddc69030c4e81f64f7fbd85832b83807a7d6275f1891917ddd86eff89e453", "1.23.0--r41h619a076_1": "sha256:a0f32fcd88acee95e4192a4bd439ce5b0998ff96ec25694989f405258268d06a", "1.22.0--r41h399db7b_0": "sha256:da7aaf7165e192111746e7265a9d5500fb57b4cbc8e32342abc11345853152ab", "1.20.0--r40h399db7b_1": "sha256:ea79f63a1b828488cd3142026813f082b3ad8850c1a77975236f2c15839cdf9c", "1.18.0--r40h5f743cb_0": "sha256:d8887d82a696ac551811ccf848d04e13634303e8370c6ad051b7928429f3923c", "1.16.0--r36he1b5a44_0": "sha256:bc856d76e84862ac7ebca0329509f48492a2fb2795762df57ccc98614ab7b926"}, "docker": "quay.io/biocontainers/bioconductor-findmyfriends", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-findmyfriends.
shpc-registry automated BioContainers addition for bioconductor-findmyfriends
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-findmyfriends
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-findmyfriends:1.23.0--r41h619a076_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-findmyfriends/1.23.0--r41h619a076_1
$ module help quay.io/biocontainers/bioconductor-findmyfriends/1.23.0--r41h619a076_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-findmyfriends-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-findmyfriends-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-findmyfriends-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-findmyfriends-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-findmyfriends-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-findmyfriends-inspect-deffile:

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