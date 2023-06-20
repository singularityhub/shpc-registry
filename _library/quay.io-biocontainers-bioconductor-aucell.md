---
layout: container
name:  "quay.io/biocontainers/bioconductor-aucell"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-aucell/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-aucell/container.yaml"
updated_at: "2023-06-20 03:07:02.884387"
latest: "1.20.1--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-aucell"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.20.1--r42hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.0--r40hdfd78af_1"
 - "1.10.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-aucell"
config: {"url": "https://biocontainers.pro/tools/bioconductor-aucell", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-aucell", "latest": {"1.20.1--r42hdfd78af_0": "sha256:c17fda89801092955ea75432b5855862f56137f80a1600861b5b64da122947e7"}, "tags": {"1.8.0--r36_0": "sha256:9a32f14b0efb499dd6dfe9450282d9a756922c7079a087a1dcafb110b7dd5273", "1.20.1--r42hdfd78af_0": "sha256:c17fda89801092955ea75432b5855862f56137f80a1600861b5b64da122947e7", "1.16.0--r41hdfd78af_0": "sha256:7877257a4c0c464675c65982b6ee215ef20cd6557b7924e927251f861b60d2d1", "1.14.0--r41hdfd78af_0": "sha256:8360f73001a192012b7b68dbcee3e2491fb6b90fd0e85d07931e4ad82e0cec89", "1.12.0--r40hdfd78af_1": "sha256:8b9dfde9ed4785d44097ae59e4a6a1fb492076d0e189e732a94c7c2f5d449109", "1.10.0--r40_0": "sha256:fb0e10c7e339656f0d22e18c29c69c5cc483ef2ca14b7e81772e25695257a381"}, "docker": "quay.io/biocontainers/bioconductor-aucell", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-aucell.
shpc-registry automated BioContainers addition for bioconductor-aucell
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-aucell
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-aucell:1.20.1--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-aucell/1.20.1--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-aucell/1.20.1--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-aucell-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-aucell-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-aucell-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-aucell-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-aucell-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-aucell-inspect-deffile:

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