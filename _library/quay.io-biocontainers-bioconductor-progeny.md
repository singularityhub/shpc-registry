---
layout: container
name:  "quay.io/biocontainers/bioconductor-progeny"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-progeny/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-progeny/container.yaml"
updated_at: "2024-04-25 03:00:13.064406"
latest: "1.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-progeny"
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
 - "1.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-progeny"
config: {"url": "https://biocontainers.pro/tools/bioconductor-progeny", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-progeny", "latest": {"1.24.0--r43hdfd78af_0": "sha256:aba7381016e5ad6c648980472fdf97026501ec37764105e1a0b92f2294814a43"}, "tags": {"1.8.0--r36_0": "sha256:e9090364da05edb2e71262f548d6f24d8435ef37f57d7e0edc7c92af0ecb0cc3", "1.20.0--r42hdfd78af_0": "sha256:46edabdfd4171f3ad9b80c780df534eb63f392aa03add9299cf0c8b45386bde3", "1.16.0--r41hdfd78af_0": "sha256:39b8891adcda56c56aada73837a4df6ae7852db489f94118ef77183cbd2943e5", "1.14.0--r41hdfd78af_0": "sha256:31494f9ee2d6fbf00ec6e72862a1db1a504aa177c3420877dae4b015317ef57e", "1.12.0--r40hdfd78af_1": "sha256:beaeffcc8aac3cdd55e38ef176dbbed42f37f41f58ba77a34be587a4a88a1894", "1.10.0--r40_0": "sha256:12b2422183a10783618bb7faaeaddaf3cd8e912febb8cb81d01e095db05b1264", "1.22.0--r43hdfd78af_0": "sha256:723373f7121d3d5f7e3c1bb97576e01e2a03971358ff62250d5c7e41ce7e79ed", "1.24.0--r43hdfd78af_0": "sha256:aba7381016e5ad6c648980472fdf97026501ec37764105e1a0b92f2294814a43"}, "docker": "quay.io/biocontainers/bioconductor-progeny", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-progeny.
shpc-registry automated BioContainers addition for bioconductor-progeny
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-progeny
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-progeny:1.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-progeny/1.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-progeny/1.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-progeny-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-progeny-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-progeny-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-progeny-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-progeny-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-progeny-inspect-deffile:

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