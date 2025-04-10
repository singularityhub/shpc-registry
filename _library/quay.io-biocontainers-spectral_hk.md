---
layout: container
name:  "quay.io/biocontainers/spectral_hk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/spectral_hk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/spectral_hk/container.yaml"
updated_at: "2025-04-10 03:13:17.943766"
latest: "0.1--0"
container_url: "https://biocontainers.pro/tools/spectral_hk"
aliases:
 - "spectral_hk"
versions:
 - "0.1--0"
description: "shpc-registry automated BioContainers addition for spectral_hk"
config: {"url": "https://biocontainers.pro/tools/spectral_hk", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for spectral_hk", "latest": {"0.1--0": "sha256:ab29b787b0636b92892fa93b3481b0f2b6f23d70889a5f17da381345b0b8adb3"}, "tags": {"0.1--0": "sha256:ab29b787b0636b92892fa93b3481b0f2b6f23d70889a5f17da381345b0b8adb3"}, "docker": "quay.io/biocontainers/spectral_hk", "aliases": {"spectral_hk": "/usr/local/bin/spectral_hk"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/spectral_hk.
shpc-registry automated BioContainers addition for spectral_hk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/spectral_hk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/spectral_hk:0.1--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/spectral_hk/0.1--0
$ module help quay.io/biocontainers/spectral_hk/0.1--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### spectral_hk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### spectral_hk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### spectral_hk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### spectral_hk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### spectral_hk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### spectral_hk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### spectral_hk

```bash
$ singularity exec <container> /usr/local/bin/spectral_hk
$ podman run --it --rm --entrypoint /usr/local/bin/spectral_hk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spectral_hk   -v ${PWD} -w ${PWD} <container> -c " $@"
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