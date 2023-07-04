---
layout: container
name:  "quay.io/biocontainers/bioconductor-chipexoqualexample"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chipexoqualexample/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chipexoqualexample/container.yaml"
updated_at: "2023-07-04 03:26:19.619250"
latest: "1.21.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-chipexoqualexample"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.21.0--r42hdfd78af_0"
 - "1.18.0--r41hdfd78af_1"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.13.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-chipexoqualexample"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chipexoqualexample", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chipexoqualexample", "latest": {"1.21.0--r42hdfd78af_0": "sha256:6a95a8e740a4f8950c4c06c6ffafe88bb4e2a7be4ae2ed15e3dffc13029a0d4c"}, "tags": {"1.8.0--r36_1": "sha256:ed284a73f9f99f4dd6a8d6a73dc5d4a05d1e17a416bf61609568254205563ed2", "1.21.0--r42hdfd78af_0": "sha256:6a95a8e740a4f8950c4c06c6ffafe88bb4e2a7be4ae2ed15e3dffc13029a0d4c", "1.18.0--r41hdfd78af_1": "sha256:cfdc2414c35081d3e51591f9dbb6323aeca00bc48e807323b4f17351f5df1af4", "1.16.0--r41hdfd78af_0": "sha256:74d1b74689d1cc748b65793438688d8b3625f426096e82d4b39996545a0c31f7", "1.14.0--r40hdfd78af_1": "sha256:62b94b2a79f643933e036a300bea98c50fc1a818b376f4d826577a73adbca169", "1.13.0--r40_0": "sha256:938d9488eb7d5b8a87b35d3b04abd12fa9c0c641984f7a920ba312e547e45caa"}, "docker": "quay.io/biocontainers/bioconductor-chipexoqualexample", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chipexoqualexample.
shpc-registry automated BioContainers addition for bioconductor-chipexoqualexample
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chipexoqualexample
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chipexoqualexample:1.21.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chipexoqualexample/1.21.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-chipexoqualexample/1.21.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chipexoqualexample-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chipexoqualexample-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chipexoqualexample-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chipexoqualexample-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chipexoqualexample-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chipexoqualexample-inspect-deffile:

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