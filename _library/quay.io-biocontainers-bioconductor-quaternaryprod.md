---
layout: container
name:  "quay.io/biocontainers/bioconductor-quaternaryprod"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-quaternaryprod/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-quaternaryprod/container.yaml"
updated_at: "2023-08-17 03:06:12.309575"
latest: "1.34.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-quaternaryprod"
aliases:
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.6.0--r3.4.1_0"
 - "1.28.0--r41hc247a5b_2"
 - "1.26.0--r41h399db7b_0"
 - "1.24.0--r40h399db7b_1"
 - "1.22.0--r40h5f743cb_0"
 - "1.20.0--r36he1b5a44_0"
 - "1.32.0--r42hc247a5b_0"
 - "1.32.0--r42hf17093f_2"
 - "1.34.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-quaternaryprod"
config: {"url": "https://biocontainers.pro/tools/bioconductor-quaternaryprod", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-quaternaryprod", "latest": {"1.34.0--r43hf17093f_0": "sha256:de0db09875fd54ba4a13a75f762dddc173efdf224da40a3be5b816e261c861c0"}, "tags": {"1.6.0--r3.4.1_0": "sha256:2d6c93ceecf1c2c11881775b35763b0175da2b2d9e6315103e74abb4d14c7fac", "1.28.0--r41hc247a5b_2": "sha256:2f927445e57b0f6c5f6174a901bb12dd9af3b0d5b7142a73637839036be4078c", "1.26.0--r41h399db7b_0": "sha256:e6c770498577785b5adcd4762048f70660134b2769f1d9c6a6ce89308d8de1a4", "1.24.0--r40h399db7b_1": "sha256:26537ef36df088a1bbdc876b0e2c984e9d47c6a1b668c680d73db1dd262ce8eb", "1.22.0--r40h5f743cb_0": "sha256:5751801da87e3d3f350062d9263d9af9ff68880377fd05178bca30b010494d3c", "1.20.0--r36he1b5a44_0": "sha256:6d7b0238d4412a323c7832e0f30eb3cf7a7e0984128145e360f2bc1486e37c38", "1.32.0--r42hc247a5b_0": "sha256:83f4c0302d13fcdb79d04da2897cba3874220cc43a4325bfb20a515b1925e442", "1.32.0--r42hf17093f_2": "sha256:5add3bcfce89574be49d9d14a9462da6bf60f48f0d61616182a536bf4ef07765", "1.34.0--r43hf17093f_0": "sha256:de0db09875fd54ba4a13a75f762dddc173efdf224da40a3be5b816e261c861c0"}, "docker": "quay.io/biocontainers/bioconductor-quaternaryprod", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-quaternaryprod.
shpc-registry automated BioContainers addition for bioconductor-quaternaryprod
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-quaternaryprod
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-quaternaryprod:1.34.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-quaternaryprod/1.34.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-quaternaryprod/1.34.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-quaternaryprod-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-quaternaryprod-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-quaternaryprod-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-quaternaryprod-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-quaternaryprod-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-quaternaryprod-inspect-deffile:

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