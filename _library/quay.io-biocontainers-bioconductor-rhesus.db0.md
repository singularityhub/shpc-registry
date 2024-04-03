---
layout: container
name:  "quay.io/biocontainers/bioconductor-rhesus.db0"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rhesus.db0/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rhesus.db0/container.yaml"
updated_at: "2024-04-03 02:33:43.075728"
latest: "3.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rhesus.db0"
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
 - "3.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rhesus.db0"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rhesus.db0", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rhesus.db0", "latest": {"3.18.0--r43hdfd78af_0": "sha256:c1a74e911863a62b744f12c3d76b4fb082cbe8de365b8f2d4ebb94cbcafd4f6f"}, "tags": {"3.8.2--r36_1": "sha256:9c1567a6385beca1554f027af9cf644a2a431cc8c26f367528b4269212156703", "3.16.0--r42hdfd78af_0": "sha256:e19095a292747298f7f14400cb7e70428e636e1982b9868006cd860da65d9860", "3.14.0--r41hdfd78af_1": "sha256:1705ed071177b28128739de86e00b1a2983cada8eae96aa16b6196bddff219cc", "3.13.0--r41hdfd78af_0": "sha256:726128ab21130d056cb9a87fe6cc20edf10ab9f8c93ac66b6711f1f638f94366", "3.12.0--r40hdfd78af_1": "sha256:0b7ee91995fcaca4a5a822075b985194d0222afff9f8b288b40c722df4a7a610", "3.11.2--r40_0": "sha256:52a095d857a2a80088881f7649cacc70655e187d0fd7e3e23ce3c703965dfde5", "3.17.0--r43hdfd78af_0": "sha256:949fc6a6d4aae2818118d2230e228090bc2b4cd051d78bb37cef4ccc3d99ad46", "3.18.0--r43hdfd78af_0": "sha256:c1a74e911863a62b744f12c3d76b4fb082cbe8de365b8f2d4ebb94cbcafd4f6f"}, "docker": "quay.io/biocontainers/bioconductor-rhesus.db0", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rhesus.db0.
shpc-registry automated BioContainers addition for bioconductor-rhesus.db0
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rhesus.db0
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rhesus.db0:3.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rhesus.db0/3.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rhesus.db0/3.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rhesus.db0-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rhesus.db0-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rhesus.db0-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rhesus.db0-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rhesus.db0-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rhesus.db0-inspect-deffile:

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