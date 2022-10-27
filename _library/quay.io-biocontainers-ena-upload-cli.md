---
layout: container
name:  "quay.io/biocontainers/ena-upload-cli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ena-upload-cli/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ena-upload-cli/container.yaml"
updated_at: "2022-10-27 00:37:35.113525"
latest: "0.6.1--pyh5e36f6f_0"
container_url: "https://biocontainers.pro/tools/ena-upload-cli"
aliases:
 - "ena-upload-cli"
versions:
 - "0.6.1--pyh5e36f6f_0"
description: "shpc-registry automated BioContainers addition for ena-upload-cli"
config: {"url": "https://biocontainers.pro/tools/ena-upload-cli", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ena-upload-cli", "latest": {"0.6.1--pyh5e36f6f_0": "sha256:b3244a8caf8c18efd7fc7970ed5f79c18b4eeed933be1c488ec90f0741061ca6"}, "tags": {"0.6.1--pyh5e36f6f_0": "sha256:b3244a8caf8c18efd7fc7970ed5f79c18b4eeed933be1c488ec90f0741061ca6"}, "docker": "quay.io/biocontainers/ena-upload-cli", "aliases": {"ena-upload-cli": "/usr/local/bin/ena-upload-cli"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ena-upload-cli.
shpc-registry automated BioContainers addition for ena-upload-cli
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ena-upload-cli
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ena-upload-cli:0.6.1--pyh5e36f6f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ena-upload-cli/0.6.1--pyh5e36f6f_0
$ module help quay.io/biocontainers/ena-upload-cli/0.6.1--pyh5e36f6f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ena-upload-cli-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ena-upload-cli-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ena-upload-cli-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ena-upload-cli-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ena-upload-cli-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ena-upload-cli-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ena-upload-cli

```bash
$ singularity exec <container> /usr/local/bin/ena-upload-cli
$ podman run --it --rm --entrypoint /usr/local/bin/ena-upload-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ena-upload-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
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