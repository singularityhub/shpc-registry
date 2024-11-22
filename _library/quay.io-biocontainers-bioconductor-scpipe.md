---
layout: container
name:  "quay.io/biocontainers/bioconductor-scpipe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scpipe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scpipe/container.yaml"
updated_at: "2024-11-22 04:38:58.014272"
latest: "2.2.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scpipe"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36he1b5a44_0"
 - "1.19.0--r42hc247a5b_0"
 - "1.16.1--r41hc247a5b_0"
 - "1.14.0--r41h399db7b_0"
 - "1.12.0--r40h399db7b_1"
 - "1.10.0--r40h5f743cb_0"
 - "1.19.0--r42hf17093f_1"
 - "2.0.0--r43hf17093f_0"
 - "2.2.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scpipe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scpipe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scpipe", "latest": {"2.2.0--r43hf17093f_0": "sha256:fcfbdea309c09795e60a4e0264b8831c2c8a06367f501eb559dd3d1b724be834"}, "tags": {"1.8.0--r36he1b5a44_0": "sha256:5532223f9f880712263b5efc3ef8510c0dd7f79ec040271b42421be60e9bef34", "1.19.0--r42hc247a5b_0": "sha256:604e739251bbcc8f7e5f68a939efcebe09ca195e6a735a23bd5abaf0345e8308", "1.16.1--r41hc247a5b_0": "sha256:e6cfb0a02988f91785e165128b37a84998972e823ced4eb20f5911c60dc3ed39", "1.14.0--r41h399db7b_0": "sha256:4deca97d07c9cb9c6f74199b01a7a776aaa2aff637debb2a44b481af77d6116a", "1.12.0--r40h399db7b_1": "sha256:f0e3a72a4c05fb9b8eb92f21ae21c430464fcfe1ee0cc9cf5c8126b634f07ffb", "1.10.0--r40h5f743cb_0": "sha256:348cb2cc0638dbcaeefcead89b5d0dfe0ccbc28e3e5bf8659835e84edfe63da6", "1.19.0--r42hf17093f_1": "sha256:865c3aa5756e523c91a7299a3c7a7daab9d6e5624d6e3de811bb7eecd124c71f", "2.0.0--r43hf17093f_0": "sha256:9dfa3f0b5683af9ed7fde9defa3e8b475f7586f6d4cd2c75db16bffabfa57743", "2.2.0--r43hf17093f_0": "sha256:fcfbdea309c09795e60a4e0264b8831c2c8a06367f501eb559dd3d1b724be834"}, "docker": "quay.io/biocontainers/bioconductor-scpipe", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scpipe.
shpc-registry automated BioContainers addition for bioconductor-scpipe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scpipe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scpipe:2.2.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scpipe/2.2.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-scpipe/2.2.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scpipe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scpipe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scpipe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scpipe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scpipe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scpipe-inspect-deffile:

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