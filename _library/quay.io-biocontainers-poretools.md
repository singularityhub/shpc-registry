---
layout: container
name:  "quay.io/biocontainers/poretools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/poretools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/poretools/container.yaml"
updated_at: "2023-01-27 02:53:02.330751"
latest: "0.6.1a1--py_8"
container_url: "https://biocontainers.pro/tools/poretools"

versions:
 - "0.6.1a1--py_8"
description: "shpc-registry automated BioContainers addition for poretools"
config: {"url": "https://biocontainers.pro/tools/poretools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for poretools", "latest": {"0.6.1a1--py_8": "sha256:3c89ebbb05e8885ad5886437bf4771e0a1c4204a260528742f497e3c9fcb8bc3"}, "tags": {"0.6.1a1--py_8": "sha256:3c89ebbb05e8885ad5886437bf4771e0a1c4204a260528742f497e3c9fcb8bc3"}, "docker": "quay.io/biocontainers/poretools"}
---

This module is a singularity container wrapper for quay.io/biocontainers/poretools.
shpc-registry automated BioContainers addition for poretools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/poretools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/poretools:0.6.1a1--py_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/poretools/0.6.1a1--py_8
$ module help quay.io/biocontainers/poretools/0.6.1a1--py_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### poretools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### poretools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### poretools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### poretools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### poretools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### poretools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### poretools

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