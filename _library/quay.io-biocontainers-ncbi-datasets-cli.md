---
layout: container
name:  "quay.io/biocontainers/ncbi-datasets-cli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ncbi-datasets-cli/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ncbi-datasets-cli/container.yaml"
updated_at: "2023-03-17 02:44:22.042045"
latest: "13.14.0"
container_url: "https://biocontainers.pro/tools/ncbi-datasets-cli"
aliases:
 - "dataformat"
 - "datasets"
versions:
 - "13.14.0"
description: "shpc-registry automated BioContainers addition for ncbi-datasets-cli"
config: {"url": "https://biocontainers.pro/tools/ncbi-datasets-cli", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ncbi-datasets-cli", "latest": {"13.14.0": "sha256:03bff7f6d75ef7fb00839fb9ab9a5afbe13465905274a1fd4bc2e365ed00338f"}, "tags": {"13.14.0": "sha256:03bff7f6d75ef7fb00839fb9ab9a5afbe13465905274a1fd4bc2e365ed00338f"}, "docker": "quay.io/biocontainers/ncbi-datasets-cli", "aliases": {"dataformat": "/usr/local/bin/dataformat", "datasets": "/usr/local/bin/datasets"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ncbi-datasets-cli.
shpc-registry automated BioContainers addition for ncbi-datasets-cli
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ncbi-datasets-cli
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ncbi-datasets-cli:13.14.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ncbi-datasets-cli/13.14.0
$ module help quay.io/biocontainers/ncbi-datasets-cli/13.14.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ncbi-datasets-cli-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ncbi-datasets-cli-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ncbi-datasets-cli-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ncbi-datasets-cli-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ncbi-datasets-cli-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ncbi-datasets-cli-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dataformat

```bash
$ singularity exec <container> /usr/local/bin/dataformat
$ podman run --it --rm --entrypoint /usr/local/bin/dataformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dataformat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### datasets

```bash
$ singularity exec <container> /usr/local/bin/datasets
$ podman run --it --rm --entrypoint /usr/local/bin/datasets   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/datasets   -v ${PWD} -w ${PWD} <container> -c " $@"
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