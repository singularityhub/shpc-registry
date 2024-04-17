---
layout: container
name:  "quay.io/biocontainers/digestiflow-cli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/digestiflow-cli/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/digestiflow-cli/container.yaml"
updated_at: "2024-04-17 02:31:06.609017"
latest: "0.5.8--h5076881_5"
container_url: "https://biocontainers.pro/tools/digestiflow-cli"
aliases:
 - "digestiflow-cli"
versions:
 - "0.5.8--h1f4ba0c_3"
 - "0.5.8--h5076881_5"
description: "shpc-registry automated BioContainers addition for digestiflow-cli"
config: {"url": "https://biocontainers.pro/tools/digestiflow-cli", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for digestiflow-cli", "latest": {"0.5.8--h5076881_5": "sha256:f5fc07cfd49ee4d83259df6bc848c731fd0d384023c109cdc4537dfb1e7fc514"}, "tags": {"0.5.8--h1f4ba0c_3": "sha256:ef54a57a006785c13f8c45a5fa0851ef22dd4a01d051182fde086c2a4e51af59", "0.5.8--h5076881_5": "sha256:f5fc07cfd49ee4d83259df6bc848c731fd0d384023c109cdc4537dfb1e7fc514"}, "docker": "quay.io/biocontainers/digestiflow-cli", "aliases": {"digestiflow-cli": "/usr/local/bin/digestiflow-cli"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/digestiflow-cli.
shpc-registry automated BioContainers addition for digestiflow-cli
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/digestiflow-cli
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/digestiflow-cli:0.5.8--h5076881_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/digestiflow-cli/0.5.8--h5076881_5
$ module help quay.io/biocontainers/digestiflow-cli/0.5.8--h5076881_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### digestiflow-cli-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### digestiflow-cli-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### digestiflow-cli-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### digestiflow-cli-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### digestiflow-cli-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### digestiflow-cli-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### digestiflow-cli

```bash
$ singularity exec <container> /usr/local/bin/digestiflow-cli
$ podman run --it --rm --entrypoint /usr/local/bin/digestiflow-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/digestiflow-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
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