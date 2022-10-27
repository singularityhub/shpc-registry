---
layout: container
name:  "quay.io/biocontainers/hmftools-linx"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hmftools-linx/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/hmftools-linx/container.yaml"
updated_at: "2022-10-27 01:01:06.459910"
latest: "1.7--0"
container_url: "https://biocontainers.pro/tools/hmftools-linx"
aliases:
 - "linx"
 - "x86_64-conda_cos6-linux-gnu-pkg-config"
versions:
 - "1.7--0"
description: "shpc-registry automated BioContainers addition for hmftools-linx"
config: {"url": "https://biocontainers.pro/tools/hmftools-linx", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hmftools-linx", "latest": {"1.7--0": "sha256:96ad73788663f0f2576719e7f8f0c415bad6211cbec5685168f00a966b87b4b9"}, "tags": {"1.7--0": "sha256:96ad73788663f0f2576719e7f8f0c415bad6211cbec5685168f00a966b87b4b9"}, "docker": "quay.io/biocontainers/hmftools-linx", "aliases": {"linx": "/usr/local/bin/linx", "x86_64-conda_cos6-linux-gnu-pkg-config": "/usr/local/bin/x86_64-conda_cos6-linux-gnu-pkg-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hmftools-linx.
shpc-registry automated BioContainers addition for hmftools-linx
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hmftools-linx
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hmftools-linx:1.7--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hmftools-linx/1.7--0
$ module help quay.io/biocontainers/hmftools-linx/1.7--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hmftools-linx-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hmftools-linx-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hmftools-linx-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hmftools-linx-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hmftools-linx-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hmftools-linx-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### linx

```bash
$ singularity exec <container> /usr/local/bin/linx
$ podman run --it --rm --entrypoint /usr/local/bin/linx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/linx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x86_64-conda_cos6-linux-gnu-pkg-config

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda_cos6-linux-gnu-pkg-config
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda_cos6-linux-gnu-pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda_cos6-linux-gnu-pkg-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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