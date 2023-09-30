---
layout: container
name:  "quay.io/biocontainers/bioconductor-ecolisakai.db0"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ecolisakai.db0/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ecolisakai.db0/container.yaml"
updated_at: "2023-09-30 02:50:07.457330"
latest: "3.17.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ecolisakai.db0"
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
description: "shpc-registry automated BioContainers addition for bioconductor-ecolisakai.db0"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ecolisakai.db0", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ecolisakai.db0", "latest": {"3.17.0--r43hdfd78af_0": "sha256:67182944abd8331df6a7eebd0ae5c30decf4d2a6b630ce951a99385bd0f44dc3"}, "tags": {"3.8.2--r36_1": "sha256:7218fc34ce39b6f92e51f4692252c763c2b8e7a9a47e1e1dcd996d67f174751f", "3.16.0--r42hdfd78af_0": "sha256:118d41229c49fff12610a979f708eead94005d72d023409302f6820857a1df5d", "3.14.0--r41hdfd78af_1": "sha256:79d4126e107ac80e35d00d14330141704f72b8311a9e17fbc58e953eb118a908", "3.13.0--r41hdfd78af_0": "sha256:cb071b966ab78df67ea647e21fa60c1d6d8d19dbc19104938c10d9b9fc094dbd", "3.12.0--r40hdfd78af_1": "sha256:1610cca8682f3c8ce99c16e30bd5ea34dd90be5fd59e9ecb0aa092d90898a24c", "3.11.2--r40_0": "sha256:d1f7e0e00bf7728df247584b022d34689b3b6b9efa60410e4c655f4dc3832c6a", "3.17.0--r43hdfd78af_0": "sha256:67182944abd8331df6a7eebd0ae5c30decf4d2a6b630ce951a99385bd0f44dc3"}, "docker": "quay.io/biocontainers/bioconductor-ecolisakai.db0", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ecolisakai.db0.
shpc-registry automated BioContainers addition for bioconductor-ecolisakai.db0
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ecolisakai.db0
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ecolisakai.db0:3.17.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ecolisakai.db0/3.17.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ecolisakai.db0/3.17.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ecolisakai.db0-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ecolisakai.db0-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ecolisakai.db0-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ecolisakai.db0-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ecolisakai.db0-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ecolisakai.db0-inspect-deffile:

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