---
layout: container
name:  "quay.io/biocontainers/r-annotables"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-annotables/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-annotables/container.yaml"
updated_at: "2024-10-05 02:55:20.249432"
latest: "0.2.0--r43hdfd78af_1"
container_url: "https://biocontainers.pro/tools/r-annotables"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "v0.1.90--r36_3"
 - "0.1.90--r42hdfd78af_4"
 - "0.2.0--r42hdfd78af_0"
 - "0.2.0--r43hdfd78af_1"
description: "shpc-registry automated BioContainers addition for r-annotables"
config: {"url": "https://biocontainers.pro/tools/r-annotables", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-annotables", "latest": {"0.2.0--r43hdfd78af_1": "sha256:ab7126f9c56b36ba8df9193f776ababd379adfea5c641bc2f3fb0664334121e0"}, "tags": {"v0.1.90--r36_3": "sha256:13f52ad4a7576075e3397d4ce9e748239409e4aa000b62fd7bf7739ff9dd8058", "0.1.90--r42hdfd78af_4": "sha256:c5df97398d54e822d3ac6a499d55d14752ae0d3f9e2fe543285d301dd8615c0a", "0.2.0--r42hdfd78af_0": "sha256:930d1c154053673af0dae3d71a18ece7d63687b9f3ff6d54bfa27bdb1587582b", "0.2.0--r43hdfd78af_1": "sha256:ab7126f9c56b36ba8df9193f776ababd379adfea5c641bc2f3fb0664334121e0"}, "docker": "quay.io/biocontainers/r-annotables", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-annotables.
shpc-registry automated BioContainers addition for r-annotables
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-annotables
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-annotables:0.2.0--r43hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-annotables/0.2.0--r43hdfd78af_1
$ module help quay.io/biocontainers/r-annotables/0.2.0--r43hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-annotables-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-annotables-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-annotables-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-annotables-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-annotables-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-annotables-inspect-deffile:

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