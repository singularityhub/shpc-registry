---
layout: container
name:  "quay.io/biocontainers/r-anndata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-anndata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-anndata/container.yaml"
updated_at: "2024-11-16 03:42:49.067821"
latest: "0.7.5.6--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/r-anndata"

versions:
 - "0.7.5.4--r41hdfd78af_0"
 - "0.7.5.4--r42hdfd78af_1"
 - "0.7.5.4--r43hdfd78af_2"
 - "0.7.5.6--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for r-anndata"
config: {"url": "https://biocontainers.pro/tools/r-anndata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-anndata", "latest": {"0.7.5.6--r43hdfd78af_0": "sha256:9ef685b892761923245a8ebb90bd2c3606ef23d61a020bc0b694454f7cdc2d07"}, "tags": {"0.7.5.4--r41hdfd78af_0": "sha256:221ffed999bdfadda221aa48191e7dacf16d1ffad3271bbe9c93c2e0d4cb3c96", "0.7.5.4--r42hdfd78af_1": "sha256:bc2ed019f8cc88733c4bc4822c32b4ae8a9d88fd16fcdbb808cf06a0ef74e6aa", "0.7.5.4--r43hdfd78af_2": "sha256:af719aa806bed7b410dddc3ae50c5d54dc83772cd5bf1887d4319430eb705e5f", "0.7.5.6--r43hdfd78af_0": "sha256:9ef685b892761923245a8ebb90bd2c3606ef23d61a020bc0b694454f7cdc2d07"}, "docker": "quay.io/biocontainers/r-anndata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-anndata.
shpc-registry automated BioContainers addition for r-anndata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-anndata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-anndata:0.7.5.6--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-anndata/0.7.5.6--r43hdfd78af_0
$ module help quay.io/biocontainers/r-anndata/0.7.5.6--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-anndata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-anndata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-anndata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-anndata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-anndata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-anndata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-anndata

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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