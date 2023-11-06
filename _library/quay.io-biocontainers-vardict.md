---
layout: container
name:  "quay.io/biocontainers/vardict"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vardict/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vardict/container.yaml"
updated_at: "2023-11-06 02:54:39.718351"
latest: "2019.06.04--pl526_0"
container_url: "https://biocontainers.pro/tools/vardict"

versions:
 - "2019.06.04--pl526_0"
description: "shpc-registry automated BioContainers addition for vardict"
config: {"url": "https://biocontainers.pro/tools/vardict", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for vardict", "latest": {"2019.06.04--pl526_0": "sha256:7ce6a6f58f45f3e62f7308675813e95eb215fc30852041f6e90c9dbf7d5f4bac"}, "tags": {"2019.06.04--pl526_0": "sha256:7ce6a6f58f45f3e62f7308675813e95eb215fc30852041f6e90c9dbf7d5f4bac"}, "docker": "quay.io/biocontainers/vardict"}
---

This module is a singularity container wrapper for quay.io/biocontainers/vardict.
shpc-registry automated BioContainers addition for vardict
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vardict
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vardict:2019.06.04--pl526_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vardict/2019.06.04--pl526_0
$ module help quay.io/biocontainers/vardict/2019.06.04--pl526_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vardict-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vardict-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vardict-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vardict-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vardict-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vardict-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### vardict

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