---
layout: container
name:  "quay.io/biocontainers/pbsim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pbsim/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pbsim/container.yaml"
updated_at: "2024-03-03 02:56:30.758349"
latest: "1.0.3--h4ac6f70_7"
container_url: "https://biocontainers.pro/tools/pbsim"

versions:
 - "1.0.3--h9f5acd7_5"
 - "1.0.3--h4ac6f70_7"
description: "shpc-registry automated BioContainers addition for pbsim"
config: {"url": "https://biocontainers.pro/tools/pbsim", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pbsim", "latest": {"1.0.3--h4ac6f70_7": "sha256:33f57511c6638f850c6a9c1e2ed5553ca0f061d6213b9ca62de275a1341a0b00"}, "tags": {"1.0.3--h9f5acd7_5": "sha256:442e922ff19db7a108815d76d513a0aa6529a4b4fda7587c74c11c1920e53541", "1.0.3--h4ac6f70_7": "sha256:33f57511c6638f850c6a9c1e2ed5553ca0f061d6213b9ca62de275a1341a0b00"}, "docker": "quay.io/biocontainers/pbsim"}
---

This module is a singularity container wrapper for quay.io/biocontainers/pbsim.
shpc-registry automated BioContainers addition for pbsim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pbsim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pbsim:1.0.3--h4ac6f70_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pbsim/1.0.3--h4ac6f70_7
$ module help quay.io/biocontainers/pbsim/1.0.3--h4ac6f70_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pbsim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pbsim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pbsim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pbsim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pbsim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pbsim-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### pbsim

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