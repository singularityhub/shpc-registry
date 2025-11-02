---
layout: container
name:  "quay.io/biocontainers/bioconductor-nondetects"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-nondetects/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-nondetects/container.yaml"
updated_at: "2025-11-02 03:32:18.230006"
latest: "2.32.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-nondetects"
aliases:
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "2.8.0--r3.4.1_0"
 - "2.28.0--r42hdfd78af_0"
 - "2.24.0--r41hdfd78af_0"
 - "2.22.0--r41hdfd78af_0"
 - "2.20.0--r40hdfd78af_1"
 - "2.18.0--r40_0"
 - "2.30.0--r43hdfd78af_0"
 - "2.32.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-nondetects"
config: {"url": "https://biocontainers.pro/tools/bioconductor-nondetects", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-nondetects", "latest": {"2.32.0--r43hdfd78af_0": "sha256:a82d490bfdec92696da576d243e40b992a826b319f412981cd8ff4bbf0bc56c9"}, "tags": {"2.8.0--r3.4.1_0": "sha256:e7e33aed8a9e1aba948258cfab6f7cdfdab9a8c9604e6fa8e9ca7ef272cbd498", "2.28.0--r42hdfd78af_0": "sha256:cfabbcb8740a0cbb0a2efee732b64dcf7ea46fba1248e8ec0a06b5d191ba1322", "2.24.0--r41hdfd78af_0": "sha256:d5314f884682932c4ba9883bc7be0b187854328429b9f74a5ad6bcccc1424a0d", "2.22.0--r41hdfd78af_0": "sha256:30879d088c4f4bd1c07ec8d8eb5a11e65241fe66cb95fd102ddf204a003f1c8c", "2.20.0--r40hdfd78af_1": "sha256:c6187389aa439d962853bf96ed19a08f7c70cd52f8029929deceacef4f6af14e", "2.18.0--r40_0": "sha256:cdadd3d1a5d765392f32e6a70643b1f7f6d2c6516280a6a55a7d93765515913a", "2.30.0--r43hdfd78af_0": "sha256:409d7b9eaa52fff71325f10b83d8355994529314e1e9f18abd06b2bd50448e83", "2.32.0--r43hdfd78af_0": "sha256:a82d490bfdec92696da576d243e40b992a826b319f412981cd8ff4bbf0bc56c9"}, "docker": "quay.io/biocontainers/bioconductor-nondetects", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-nondetects.
shpc-registry automated BioContainers addition for bioconductor-nondetects
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-nondetects
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-nondetects:2.32.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-nondetects/2.32.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-nondetects/2.32.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-nondetects-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nondetects-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nondetects-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-nondetects-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-nondetects-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-nondetects-inspect-deffile:

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