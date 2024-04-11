---
layout: container
name:  "quay.io/biocontainers/bioconductor-swathxtend"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-swathxtend/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-swathxtend/container.yaml"
updated_at: "2024-04-11 03:14:43.074010"
latest: "2.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-swathxtend"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "2.8.0--r36_0"
 - "2.20.0--r42hdfd78af_0"
 - "2.16.0--r41hdfd78af_0"
 - "2.14.0--r41hdfd78af_0"
 - "2.12.0--r40hdfd78af_1"
 - "2.10.0--r40_0"
 - "2.22.0--r43hdfd78af_0"
 - "2.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-swathxtend"
config: {"url": "https://biocontainers.pro/tools/bioconductor-swathxtend", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-swathxtend", "latest": {"2.24.0--r43hdfd78af_0": "sha256:3bda8600a82983b149d4e7f986edf8ae68930e7c73c9a0c8b44a22bf2a5fa1b9"}, "tags": {"2.8.0--r36_0": "sha256:0264896db1620649ebf1054612b21c64eed956d6cf3edc0e36688eddd2918c28", "2.20.0--r42hdfd78af_0": "sha256:49857f94ea16e971754b2f37513d2e841d9ded064082c6ed560811dba3273ddf", "2.16.0--r41hdfd78af_0": "sha256:b619f53629b6864dc428b0eebd00a7ba75c93c46ff9fa141e239b778fdb21cd6", "2.14.0--r41hdfd78af_0": "sha256:96df12c0fbc1c6552e6b6ded0c1275076b27dd4c881956bc0796fcb8c63947cb", "2.12.0--r40hdfd78af_1": "sha256:2259e3cac55ac87cea6dc71da9fdbb0f780394f4a0306dc3422316baae42a08f", "2.10.0--r40_0": "sha256:a97337392e59a858d21c8f37f889a876f90e162e7221b7159bff065b5f05d0bc", "2.22.0--r43hdfd78af_0": "sha256:3d01bdf4169296dcdfd819038dd0f8b2e7df5f3f74539df355fea7ad5e537407", "2.24.0--r43hdfd78af_0": "sha256:3bda8600a82983b149d4e7f986edf8ae68930e7c73c9a0c8b44a22bf2a5fa1b9"}, "docker": "quay.io/biocontainers/bioconductor-swathxtend", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-swathxtend.
shpc-registry automated BioContainers addition for bioconductor-swathxtend
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-swathxtend
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-swathxtend:2.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-swathxtend/2.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-swathxtend/2.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-swathxtend-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-swathxtend-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-swathxtend-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-swathxtend-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-swathxtend-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-swathxtend-inspect-deffile:

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