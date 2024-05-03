---
layout: container
name:  "quay.io/biocontainers/bioconductor-samexplorer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-samexplorer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-samexplorer/container.yaml"
updated_at: "2024-05-03 03:01:58.331149"
latest: "1.13.0--r40hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-samexplorer"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.13.0--r40hdfd78af_1"
 - "1.12.0--r40_0"
 - "1.10.0--r36_1"
description: "shpc-registry automated BioContainers addition for bioconductor-samexplorer"
config: {"url": "https://biocontainers.pro/tools/bioconductor-samexplorer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-samexplorer", "latest": {"1.13.0--r40hdfd78af_1": "sha256:a0e9892ff281a5370055e355fd61f0ccd530ffd5c69a709f1f484d6f9be40309"}, "tags": {"1.8.0--r36_1": "sha256:a59dd311147a30b9c34bbd98ce142fdd909b703954c5078b0fc3d2f25699e9b3", "1.13.0--r40hdfd78af_1": "sha256:a0e9892ff281a5370055e355fd61f0ccd530ffd5c69a709f1f484d6f9be40309", "1.12.0--r40_0": "sha256:dff440c6caec8b3f690d5190208c6de0ebdce36a9233465e1cd24a2700ea3a6e", "1.10.0--r36_1": "sha256:55946c467617b035d41157bb9380cd079780bf870c535831c51604c4df963415"}, "docker": "quay.io/biocontainers/bioconductor-samexplorer", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-samexplorer.
shpc-registry automated BioContainers addition for bioconductor-samexplorer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-samexplorer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-samexplorer:1.13.0--r40hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-samexplorer/1.13.0--r40hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-samexplorer/1.13.0--r40hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-samexplorer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-samexplorer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-samexplorer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-samexplorer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-samexplorer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-samexplorer-inspect-deffile:

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