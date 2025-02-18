---
layout: container
name:  "quay.io/biocontainers/nemo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nemo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nemo/container.yaml"
updated_at: "2025-02-18 03:34:22.846812"
latest: "2.3.51--h1c77041_2"
container_url: "https://biocontainers.pro/tools/nemo"

versions:
 - "2.3.51--h1c77041_2"
description: "shpc-registry automated BioContainers addition for nemo"
config: {"url": "https://biocontainers.pro/tools/nemo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nemo", "latest": {"2.3.51--h1c77041_2": "sha256:f31653d21d25f5a27443e4ab5ae4870f64ba47422e1f50f369850ad96d12ca99"}, "tags": {"2.3.51--h1c77041_2": "sha256:f31653d21d25f5a27443e4ab5ae4870f64ba47422e1f50f369850ad96d12ca99"}, "docker": "quay.io/biocontainers/nemo"}
---

This module is a singularity container wrapper for quay.io/biocontainers/nemo.
shpc-registry automated BioContainers addition for nemo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nemo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nemo:2.3.51--h1c77041_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nemo/2.3.51--h1c77041_2
$ module help quay.io/biocontainers/nemo/2.3.51--h1c77041_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nemo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nemo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nemo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nemo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nemo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nemo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### nemo

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