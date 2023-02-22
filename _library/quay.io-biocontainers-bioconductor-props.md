---
layout: container
name:  "quay.io/biocontainers/bioconductor-props"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-props/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-props/container.yaml"
updated_at: "2023-02-22 03:34:38.802457"
latest: "1.20.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-props"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.0--r40hdfd78af_1"
 - "1.10.0--r40_0"
 - "1.20.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-props"
config: {"url": "https://biocontainers.pro/tools/bioconductor-props", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-props", "latest": {"1.20.0--r42hdfd78af_0": "sha256:687aa389726fe4dcc80c17766f6c1ced93539b5d1fa25dfd035a2eaf46597dea"}, "tags": {"1.8.0--r36_0": "sha256:35a494ac17c5b57fe1d4cbf6962d062a1e84445f57ac6bd25cf26f385f8853e0", "1.16.0--r41hdfd78af_0": "sha256:3cd47d0b1e9edf6a520b081d25137b1a7e18158bc9ca8f6f754525cda270c399", "1.14.0--r41hdfd78af_0": "sha256:86a6bec6c354de75ad09566b831d3328d472947ddcaad5c9b60a734ca436c8fe", "1.12.0--r40hdfd78af_1": "sha256:da605837e45c7a593737f366f9c5523dcc33a422e6cce5fb4609d4367d54cc1a", "1.10.0--r40_0": "sha256:acb6c118b09a27d0f77217e1902a6bab4c34d64c3ce3c49c9825887e69948df7", "1.20.0--r42hdfd78af_0": "sha256:687aa389726fe4dcc80c17766f6c1ced93539b5d1fa25dfd035a2eaf46597dea"}, "docker": "quay.io/biocontainers/bioconductor-props", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-props.
shpc-registry automated BioContainers addition for bioconductor-props
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-props
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-props:1.20.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-props/1.20.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-props/1.20.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-props-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-props-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-props-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-props-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-props-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-props-inspect-deffile:

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