---
layout: container
name:  "quay.io/biocontainers/bioconductor-scnorm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scnorm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scnorm/container.yaml"
updated_at: "2023-09-08 02:43:54.352975"
latest: "1.22.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scnorm"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.20.0--r42hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.0--r40hdfd78af_1"
 - "1.10.0--r40_0"
 - "1.22.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scnorm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scnorm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scnorm", "latest": {"1.22.0--r43hdfd78af_0": "sha256:ec67777b78d7300bd9f920650a0522805d834f5fd8971d33d775fa9796fec621"}, "tags": {"1.8.0--r36_0": "sha256:8d345ad1d9d887350efc09c60eab03bc37ed331316e3ef041b78e1c8af9e925f", "1.20.0--r42hdfd78af_0": "sha256:6de0d9021db31522ae61b783924c744a4f8388aea1210661e959c5cc8c0b15de", "1.16.0--r41hdfd78af_0": "sha256:9c0c916b8d0d8dc744e06bff74214472af5043acbd8ec96d2a2011a14bdbcb19", "1.14.0--r41hdfd78af_0": "sha256:6104cb06e3105337e2cc85bdc7b054bc03ce3c0214c7970506632bb364046950", "1.12.0--r40hdfd78af_1": "sha256:99fd4f79421cc72c4bd965b564e850b95887c4a1d41b319fa31d3e232959f6c7", "1.10.0--r40_0": "sha256:eedfd1c16ac2e25e1774fd99d48bfa001294431c5ab69ca93bbbb44cfc5fa4a5", "1.22.0--r43hdfd78af_0": "sha256:ec67777b78d7300bd9f920650a0522805d834f5fd8971d33d775fa9796fec621"}, "docker": "quay.io/biocontainers/bioconductor-scnorm", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scnorm.
shpc-registry automated BioContainers addition for bioconductor-scnorm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scnorm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scnorm:1.22.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scnorm/1.22.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-scnorm/1.22.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scnorm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scnorm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scnorm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scnorm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scnorm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scnorm-inspect-deffile:

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