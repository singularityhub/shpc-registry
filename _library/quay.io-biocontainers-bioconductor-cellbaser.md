---
layout: container
name:  "quay.io/biocontainers/bioconductor-cellbaser"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cellbaser/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cellbaser/container.yaml"
updated_at: "2024-10-31 03:08:07.187761"
latest: "1.26.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cellbaser"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.22.0--r42hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.12.0--r40_0"
 - "1.24.0--r43hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cellbaser"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cellbaser", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cellbaser", "latest": {"1.26.0--r43hdfd78af_0": "sha256:cfea70af3896c9ae745214d0e66686adbdd6ad562671f46ec186179c922f4788"}, "tags": {"1.8.0--r36_1": "sha256:82c390d863115c7c013ab5af17ed662328796f08481f8e80f2d271af69c39120", "1.22.0--r42hdfd78af_0": "sha256:cf3ac1f16f25768a5567318da7d46ce2c3a9ddfa81ca6c5cd1a60d367ec88213", "1.18.0--r41hdfd78af_0": "sha256:70b1e2dac000062d1db20ca72b393c260a24b1ba724c5b8c9ce6cfc7ea4ce6a9", "1.16.0--r41hdfd78af_0": "sha256:cb77f7c4df8d297af1689eec62b3d22b1b1f3cd16b499662b3913d929600520f", "1.14.0--r40hdfd78af_1": "sha256:ad89b54aa136b277639782c9b8e8e5cdd0031ae106286a4c4455dbc5be1d41ab", "1.12.0--r40_0": "sha256:851084d4978ef10b6212c505cf7e703cf48854a0698fd2f983be7faf975c01d8", "1.24.0--r43hdfd78af_0": "sha256:444c24fcd55597bfb79af55fa818bab79915549d8d66820cb250441804822cc5", "1.26.0--r43hdfd78af_0": "sha256:cfea70af3896c9ae745214d0e66686adbdd6ad562671f46ec186179c922f4788"}, "docker": "quay.io/biocontainers/bioconductor-cellbaser", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cellbaser.
shpc-registry automated BioContainers addition for bioconductor-cellbaser
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cellbaser
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cellbaser:1.26.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cellbaser/1.26.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cellbaser/1.26.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cellbaser-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cellbaser-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cellbaser-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cellbaser-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cellbaser-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cellbaser-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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