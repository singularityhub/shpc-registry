---
layout: container
name:  "quay.io/biocontainers/fmlrc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fmlrc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fmlrc/container.yaml"
updated_at: "2025-08-24 04:02:15.011371"
latest: "1.0.0--h9948957_6"
container_url: "https://biocontainers.pro/tools/fmlrc"

versions:
 - "1.0.0--h9f5acd7_3"
 - "1.0.0--h4ac6f70_5"
 - "1.0.0--h9948957_6"
description: "shpc-registry automated BioContainers addition for fmlrc"
config: {"url": "https://biocontainers.pro/tools/fmlrc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fmlrc", "latest": {"1.0.0--h9948957_6": "sha256:b00d22062c0c3fc5a4ea78df44c6443e6e6347cf73e556cdb66258174430b884"}, "tags": {"1.0.0--h9f5acd7_3": "sha256:d25fa01b746efa08c7041461c8866aba3f242c4c522186886ad5dc680daed85a", "1.0.0--h4ac6f70_5": "sha256:324f4087751288dfb6ceae4e1353610a4feb0c87ebb96d214ca58a13cf7ace04", "1.0.0--h9948957_6": "sha256:b00d22062c0c3fc5a4ea78df44c6443e6e6347cf73e556cdb66258174430b884"}, "docker": "quay.io/biocontainers/fmlrc"}
---

This module is a singularity container wrapper for quay.io/biocontainers/fmlrc.
shpc-registry automated BioContainers addition for fmlrc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fmlrc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fmlrc:1.0.0--h9948957_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fmlrc/1.0.0--h9948957_6
$ module help quay.io/biocontainers/fmlrc/1.0.0--h9948957_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fmlrc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fmlrc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fmlrc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fmlrc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fmlrc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fmlrc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### fmlrc

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