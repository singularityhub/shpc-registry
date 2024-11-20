---
layout: container
name:  "quay.io/biocontainers/bioconductor-stan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-stan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-stan/container.yaml"
updated_at: "2024-11-20 03:36:52.341819"
latest: "2.26.0--r42hf17093f_1"
container_url: "https://biocontainers.pro/tools/bioconductor-stan"
aliases:
 - "wget"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "2.8.0--r341hfc679d8_0"
 - "2.26.0--r42hc247a5b_0"
 - "2.22.0--r41hc247a5b_2"
 - "2.20.0--r41h399db7b_0"
 - "2.18.0--r40h399db7b_1"
 - "2.16.0--r40h5f743cb_0"
 - "2.26.0--r42hf17093f_1"
description: "shpc-registry automated BioContainers addition for bioconductor-stan"
config: {"url": "https://biocontainers.pro/tools/bioconductor-stan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-stan", "latest": {"2.26.0--r42hf17093f_1": "sha256:0fb2979aafb82bb83fe994312d465572e6f0b877d83494eec219c31f33a3866f"}, "tags": {"2.8.0--r341hfc679d8_0": "sha256:f70b12aa7f0bb600e142e53cd2ea4e423fea2cae8b14e0cefae4580393339b8d", "2.26.0--r42hc247a5b_0": "sha256:8ac238eb216b98555a2da83fef1291f736a84a5f3390572fed17878b164d3ae8", "2.22.0--r41hc247a5b_2": "sha256:6775859cb640afce49eb818408fce31b4b6fac920ea661fcb0ad10ab8ecef4ab", "2.20.0--r41h399db7b_0": "sha256:4f6603738e96b80a5cd9d97fe08ce5d3d730e3f3f043f53270ae87d21dd469dc", "2.18.0--r40h399db7b_1": "sha256:0dc05578d2d83e5157b325997249767ee544bae064f5ebf5a1d99daff14054eb", "2.16.0--r40h5f743cb_0": "sha256:e43e37b50b87b29e2ed588c26218964a8d1666a35877987872bd487fba6afcab", "2.26.0--r42hf17093f_1": "sha256:0fb2979aafb82bb83fe994312d465572e6f0b877d83494eec219c31f33a3866f"}, "docker": "quay.io/biocontainers/bioconductor-stan", "aliases": {"wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-stan.
shpc-registry automated BioContainers addition for bioconductor-stan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-stan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-stan:2.26.0--r42hf17093f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-stan/2.26.0--r42hf17093f_1
$ module help quay.io/biocontainers/bioconductor-stan/2.26.0--r42hf17093f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-stan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-stan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-stan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-stan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-stan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-stan-inspect-deffile:

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