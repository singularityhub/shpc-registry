---
layout: container
name:  "quay.io/biocontainers/bioconductor-scmap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scmap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scmap/container.yaml"
updated_at: "2024-02-19 02:36:38.526538"
latest: "1.24.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scmap"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36he1b5a44_0"
 - "1.20.0--r42hc247a5b_0"
 - "1.16.0--r41hc247a5b_2"
 - "1.14.0--r41h399db7b_0"
 - "1.12.0--r40h399db7b_1"
 - "1.10.0--r40h5f743cb_0"
 - "1.20.0--r42hf17093f_1"
 - "1.22.3--r43hf17093f_0"
 - "1.24.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scmap"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scmap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scmap", "latest": {"1.24.0--r43hf17093f_0": "sha256:71fc500cff1d9d465ed80fe3800cdb47dfec7a309c870b4c9498a5a8dd82a6d9"}, "tags": {"1.8.0--r36he1b5a44_0": "sha256:21fd2e557b6371209a3d84d576e3691bbbdb357873d36848a633c13830ebe882", "1.20.0--r42hc247a5b_0": "sha256:97a99d284fe8668a0a1a269e61840d3252f9a70beea80d7ef4c5ed5c3be98d2d", "1.16.0--r41hc247a5b_2": "sha256:31ea996d03f43a7d47d9fcbd6360e8b83a6af9a71f164890ec079098f927e59b", "1.14.0--r41h399db7b_0": "sha256:1563e8adcdaddae3fbea958f2b1d1fad4e1606e72e4fa69e8cf2e85aa31bd6a1", "1.12.0--r40h399db7b_1": "sha256:d32d00dac35f35c288683d556044d184ea34534747a37f2f5de96d7253f08a3c", "1.10.0--r40h5f743cb_0": "sha256:bce7cef01e7bf0e6e814f5fecc9e82a22e72bc8f5c9591fecceb4c9ea03bf252", "1.20.0--r42hf17093f_1": "sha256:5555e35328f7f95643bd646b580bc5117144decf921ab8c1e904cf6020ee4ebe", "1.22.3--r43hf17093f_0": "sha256:91e52110ec7cafb31422b874c175afe4cc3cf284a8b58bf2ca075560d3d67a5e", "1.24.0--r43hf17093f_0": "sha256:71fc500cff1d9d465ed80fe3800cdb47dfec7a309c870b4c9498a5a8dd82a6d9"}, "docker": "quay.io/biocontainers/bioconductor-scmap", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scmap.
shpc-registry automated BioContainers addition for bioconductor-scmap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scmap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scmap:1.24.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scmap/1.24.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-scmap/1.24.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scmap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scmap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scmap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scmap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scmap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scmap-inspect-deffile:

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