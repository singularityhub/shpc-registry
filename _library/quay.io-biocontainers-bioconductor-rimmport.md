---
layout: container
name:  "quay.io/biocontainers/bioconductor-rimmport"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rimmport/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rimmport/container.yaml"
updated_at: "2025-08-05 04:28:00.363389"
latest: "1.34.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rimmport"
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
 - "1.34.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rimmport"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rimmport", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rimmport", "latest": {"1.34.0--r44hdfd78af_0": "sha256:28c8b92eb4cd3d9bff27f7bf06aa8d2491be60be530a9b964096d8622dcf35be"}, "tags": {"1.8.0--r341_0": "sha256:175915a6039c3dd55039dc458d526683a130b8392b875b713e6cbcebf93af4e7", "1.26.0--r42hdfd78af_0": "sha256:f75d30f1978b278fac325521d85897825eeec64770440650f55553bdc370d945", "1.22.0--r41hdfd78af_0": "sha256:ad228178ab8fb8fc4337f027f5fb53e30cec437e631efcc9849e7f178fe1b8e3", "1.20.0--r41hdfd78af_0": "sha256:8ab03d82e93e8ffd77f376f4979f4f17b38c00dcaf1e07e88d3408212a7ec093", "1.18.0--r40hdfd78af_1": "sha256:21934d06fefbf34031d26a62b332e2df3740d3f8de09c77e4735db9f22e31e8f", "1.16.0--r40_0": "sha256:c4b004ffcc6265c65a9a14c822b7a3d49650a862bed7b72fd02f455921e19161", "1.28.0--r43hdfd78af_0": "sha256:8ad8d3cf1a0305decd4acfb6c26a401639dde9352e0eed1b667f17f301bbbcc5", "1.30.0--r43hdfd78af_0": "sha256:342ea4f57e95074d19f6ec1b342b891412603f58f525e0841a73dece6d236cf8", "1.34.0--r44hdfd78af_0": "sha256:28c8b92eb4cd3d9bff27f7bf06aa8d2491be60be530a9b964096d8622dcf35be"}, "docker": "quay.io/biocontainers/bioconductor-rimmport", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rimmport.
shpc-registry automated BioContainers addition for bioconductor-rimmport
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rimmport
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rimmport:1.34.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rimmport/1.34.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rimmport/1.34.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rimmport-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rimmport-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rimmport-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rimmport-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rimmport-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rimmport-inspect-deffile:

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