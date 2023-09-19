---
layout: container
name:  "quay.io/biocontainers/bioconductor-zinbwave"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-zinbwave/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-zinbwave/container.yaml"
updated_at: "2023-09-19 02:53:56.787168"
latest: "1.22.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-zinbwave"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.1--r41hdfd78af_0"
 - "1.12.0--r40hdfd78af_1"
 - "1.10.0--r40_0"
 - "1.20.0--r42hdfd78af_0"
 - "1.22.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-zinbwave"
config: {"url": "https://biocontainers.pro/tools/bioconductor-zinbwave", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-zinbwave", "latest": {"1.22.0--r43hdfd78af_0": "sha256:be4e7624abcb370c5226cc37457a124a3551d3bc3a418d76065fd5e37efde449"}, "tags": {"1.8.0--r36_0": "sha256:ebbc4508631522d30d100f76c18ef17990157dcfa4c68c592459478d2153d8d1", "1.16.0--r41hdfd78af_0": "sha256:e4c3e078827ad6d0898f59ace21b3f12c66076d583cacb8fab409d0b8711e0ad", "1.14.1--r41hdfd78af_0": "sha256:99c4f8fbd939e677bb759235475d5d2bd9b69aa07f82457d40711affdb8ee865", "1.12.0--r40hdfd78af_1": "sha256:4d40f949cb6729bae1e139d2c3e9d42d318ddc53d7b75b78b7ea39e9b5b242e1", "1.10.0--r40_0": "sha256:f4fa342bca6f8876e89d52a93651ce97591502bf4f3399cf319322082c920c1a", "1.20.0--r42hdfd78af_0": "sha256:5bc6cadeb7fc0a78239c1e7a84db01d1076e3d9a53a1619b628e773deecbe08b", "1.22.0--r43hdfd78af_0": "sha256:be4e7624abcb370c5226cc37457a124a3551d3bc3a418d76065fd5e37efde449"}, "docker": "quay.io/biocontainers/bioconductor-zinbwave", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-zinbwave.
shpc-registry automated BioContainers addition for bioconductor-zinbwave
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-zinbwave
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-zinbwave:1.22.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-zinbwave/1.22.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-zinbwave/1.22.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-zinbwave-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-zinbwave-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-zinbwave-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-zinbwave-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-zinbwave-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-zinbwave-inspect-deffile:

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