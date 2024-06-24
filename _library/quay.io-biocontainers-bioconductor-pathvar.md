---
layout: container
name:  "quay.io/biocontainers/bioconductor-pathvar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pathvar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pathvar/container.yaml"
updated_at: "2024-06-24 02:36:34.283658"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pathvar"
aliases:
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_0"
 - "1.28.0--r42hdfd78af_0"
 - "1.24.0--r41hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r40hdfd78af_1"
 - "1.18.0--r40_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pathvar"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pathvar", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pathvar", "latest": {"1.30.0--r43hdfd78af_0": "sha256:462a87386c0f039d21931f69297ce23514c97fae73c47cfa6003757a04cfc75a"}, "tags": {"1.8.0--r3.4.1_0": "sha256:b653598cda227bfadefb08033b7906928132409ac3c725b776d5aeed7027672c", "1.28.0--r42hdfd78af_0": "sha256:e65c1abcbdeb9c5f297c09f36dc3ab281b6c2625a0854bd677040610db80baf2", "1.24.0--r41hdfd78af_0": "sha256:c6ddd02316920a3aa26be115213d76e22cceaa250695a4ac1f366066b8c28693", "1.22.0--r41hdfd78af_0": "sha256:b7e90cbca2452e6db09c40cae74b04eda6b10f8faa641ff0caed485f0ffa262f", "1.20.0--r40hdfd78af_1": "sha256:e7922bcbf4c872b10b05a94a278680e1f46df3956e24c31c4e7d84d799787aac", "1.18.0--r40_0": "sha256:a257e82dbb9f1116ec1fc19edd6b624f9bcef598d7a2abb01711e9a397f0b5be", "1.30.0--r43hdfd78af_0": "sha256:462a87386c0f039d21931f69297ce23514c97fae73c47cfa6003757a04cfc75a"}, "docker": "quay.io/biocontainers/bioconductor-pathvar", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pathvar.
shpc-registry automated BioContainers addition for bioconductor-pathvar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pathvar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pathvar:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pathvar/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pathvar/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pathvar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pathvar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pathvar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pathvar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pathvar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pathvar-inspect-deffile:

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