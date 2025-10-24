---
layout: container
name:  "quay.io/biocontainers/bioconductor-transcriptr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-transcriptr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-transcriptr/container.yaml"
updated_at: "2025-10-24 03:26:32.895716"
latest: "1.34.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-transcriptr"
aliases:
 - "wget"
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
description: "shpc-registry automated BioContainers addition for bioconductor-transcriptr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-transcriptr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-transcriptr", "latest": {"1.34.0--r44hdfd78af_0": "sha256:c621cc7e978ad6ee6e9e2a8f4309e7c9be8d7bd02b9328e9bbb68ff7608de133"}, "tags": {"1.8.0--r341_0": "sha256:f323ea230e93fd5f13730f65d6208795386226b1945c43f31fd8772b4a6dedc6", "1.26.0--r42hdfd78af_0": "sha256:c6f05b5641226afbc7909c12a83f5a2d9e09ff6ab6a6329e32d483d98c2dec49", "1.22.0--r41hdfd78af_0": "sha256:4a8c94b64c5a5745246ecfb4fddccb1b83ad0ae0091a79024014faeccaa7c7b1", "1.20.0--r41hdfd78af_0": "sha256:9149a33c559fc32544d38e786c9e6882adccdd2202dc397a128a464c61026be8", "1.18.0--r40hdfd78af_1": "sha256:953747de45a10077a6b85202eb080337759fe429f4c1ec2a7bd9699c156f0d45", "1.16.0--r40_0": "sha256:2fde226d1a6a41c6a007f1fd7c71952e4b826d68dc53397c8ec9fdbe377cb809", "1.28.0--r43hdfd78af_0": "sha256:cd8b892ff151fadab6007c6352c4136eaf399993b61d1978b3405d13e19c2aac", "1.30.0--r43hdfd78af_0": "sha256:118a183ee51e1fcba809c280b0763e57e31f57e017fec8c3cdab6c6a2afe127d", "1.34.0--r44hdfd78af_0": "sha256:c621cc7e978ad6ee6e9e2a8f4309e7c9be8d7bd02b9328e9bbb68ff7608de133"}, "docker": "quay.io/biocontainers/bioconductor-transcriptr", "aliases": {"wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-transcriptr.
shpc-registry automated BioContainers addition for bioconductor-transcriptr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-transcriptr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-transcriptr:1.34.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-transcriptr/1.34.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-transcriptr/1.34.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-transcriptr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-transcriptr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-transcriptr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-transcriptr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-transcriptr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-transcriptr-inspect-deffile:

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