---
layout: container
name:  "quay.io/biocontainers/kart"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kart/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kart/container.yaml"
updated_at: "2023-11-20 03:17:35.579757"
latest: "2.5.6--hcd5855d_4"
container_url: "https://biocontainers.pro/tools/kart"
aliases:
 - "bwt_index"
 - "kart"
versions:
 - "2.5.6--h2ccddb4_2"
 - "2.5.6--hcd5855d_4"
description: "shpc-registry automated BioContainers addition for kart"
config: {"url": "https://biocontainers.pro/tools/kart", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kart", "latest": {"2.5.6--hcd5855d_4": "sha256:38f49d8c8ab1b68341f1cb3e788c1d5eba7f2197fe267b4a1a8e0b370a829dd2"}, "tags": {"2.5.6--h2ccddb4_2": "sha256:56652c970bb60463bdecca7402a51fc689e6f4addac1d48263b6461edd9d0f6c", "2.5.6--hcd5855d_4": "sha256:38f49d8c8ab1b68341f1cb3e788c1d5eba7f2197fe267b4a1a8e0b370a829dd2"}, "docker": "quay.io/biocontainers/kart", "aliases": {"bwt_index": "/usr/local/bin/bwt_index", "kart": "/usr/local/bin/kart"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kart.
shpc-registry automated BioContainers addition for kart
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kart
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kart:2.5.6--hcd5855d_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kart/2.5.6--hcd5855d_4
$ module help quay.io/biocontainers/kart/2.5.6--hcd5855d_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kart-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kart-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kart-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kart-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kart-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kart-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bwt_index

```bash
$ singularity exec <container> /usr/local/bin/bwt_index
$ podman run --it --rm --entrypoint /usr/local/bin/bwt_index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwt_index   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kart

```bash
$ singularity exec <container> /usr/local/bin/kart
$ podman run --it --rm --entrypoint /usr/local/bin/kart   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kart   -v ${PWD} -w ${PWD} <container> -c " $@"
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