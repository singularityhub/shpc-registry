---
layout: container
name:  "quay.io/biocontainers/bioconductor-fly.db0"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-fly.db0/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-fly.db0/container.yaml"
updated_at: "2023-08-10 03:02:06.746366"
latest: "3.17.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-fly.db0"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.8.2--r36_1"
 - "3.16.0--r42hdfd78af_0"
 - "3.14.0--r41hdfd78af_1"
 - "3.13.0--r41hdfd78af_0"
 - "3.12.0--r40hdfd78af_1"
 - "3.11.2--r40_0"
 - "3.17.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-fly.db0"
config: {"url": "https://biocontainers.pro/tools/bioconductor-fly.db0", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-fly.db0", "latest": {"3.17.0--r43hdfd78af_0": "sha256:5b03186210d14e6b861c74b596f7b0d915c0d4b3095920420b1a1eb8d4832e0a"}, "tags": {"3.8.2--r36_1": "sha256:392ad468196793bb43d42f392c40715b3e8aacfa4360824a8527046ece60ca16", "3.16.0--r42hdfd78af_0": "sha256:6832167b822035d38226b18dc08c681c8f4dab744bd95484b9464bf7987c3138", "3.14.0--r41hdfd78af_1": "sha256:4eb403bddba0eeed79bb5b5317ddd1e8396e9fb7397f04dfc3e6c50b282fd768", "3.13.0--r41hdfd78af_0": "sha256:7523e1b56a8eefccbc61cca66242a045973426eb52cb42e6854061d7e262a468", "3.12.0--r40hdfd78af_1": "sha256:60bba6aa8032afba07fc753da5f8bcd58565549083554a10212ce0047c782e6e", "3.11.2--r40_0": "sha256:3fe8d40ade63042e1d86843da08af47f2d5e33d2f2f8be85e066f4d5bea66009", "3.17.0--r43hdfd78af_0": "sha256:5b03186210d14e6b861c74b596f7b0d915c0d4b3095920420b1a1eb8d4832e0a"}, "docker": "quay.io/biocontainers/bioconductor-fly.db0", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-fly.db0.
shpc-registry automated BioContainers addition for bioconductor-fly.db0
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-fly.db0
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-fly.db0:3.17.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-fly.db0/3.17.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-fly.db0/3.17.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-fly.db0-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fly.db0-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fly.db0-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-fly.db0-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-fly.db0-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-fly.db0-inspect-deffile:

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