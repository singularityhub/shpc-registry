---
layout: container
name:  "quay.io/biocontainers/bioconductor-tfhaz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tfhaz/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tfhaz/container.yaml"
updated_at: "2023-04-30 02:44:45.432822"
latest: "1.20.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tfhaz"
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
description: "shpc-registry automated BioContainers addition for bioconductor-tfhaz"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tfhaz", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tfhaz", "latest": {"1.20.0--r42hdfd78af_0": "sha256:0edbe17c67a095cd2ec618a1fe6483bbd37dde3314e88a1538fa86bf7e11113b"}, "tags": {"1.8.0--r36_0": "sha256:a22c792efcbe59aadd21eb5652dfc541029f9ccaeef57b234e2052b9e26c1f9c", "1.20.0--r42hdfd78af_0": "sha256:0edbe17c67a095cd2ec618a1fe6483bbd37dde3314e88a1538fa86bf7e11113b", "1.16.0--r41hdfd78af_0": "sha256:2d835d053370116af4d4d5fd0a371680d4a153eb911456a7a3130b76004aca8c", "1.14.0--r41hdfd78af_0": "sha256:18e8d3245ef03e3396fb2416b2cd14df50d2fc83e77a8d71e5f42d63d5176bf9", "1.12.0--r40hdfd78af_1": "sha256:1bdaf4ae13da938a325d056c075aee135767d16b6fec74e8881ae4164f0600ff", "1.10.0--r40_0": "sha256:59e71ca10c7b10a86dc964072b15f6d35521311e242a6839f64df3f08f0a2663"}, "docker": "quay.io/biocontainers/bioconductor-tfhaz", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tfhaz.
shpc-registry automated BioContainers addition for bioconductor-tfhaz
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tfhaz
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tfhaz:1.20.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tfhaz/1.20.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tfhaz/1.20.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tfhaz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tfhaz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tfhaz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tfhaz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tfhaz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tfhaz-inspect-deffile:

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