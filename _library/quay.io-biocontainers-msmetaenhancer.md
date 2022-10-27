---
layout: container
name:  "quay.io/biocontainers/msmetaenhancer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/msmetaenhancer/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/msmetaenhancer/container.yaml"
updated_at: "2022-10-27 00:51:52.741941"
latest: "0.2.5--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/msmetaenhancer"

versions:
 - "0.2.5--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for msmetaenhancer"
config: {"url": "https://biocontainers.pro/tools/msmetaenhancer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for msmetaenhancer", "latest": {"0.2.5--pyhdfd78af_0": "sha256:ff09e6c18c69be623dae7a7063d3bf031ba0e7eea721be8eae918e282e74d48d"}, "tags": {"0.2.5--pyhdfd78af_0": "sha256:ff09e6c18c69be623dae7a7063d3bf031ba0e7eea721be8eae918e282e74d48d"}, "docker": "quay.io/biocontainers/msmetaenhancer"}
---

This module is a singularity container wrapper for quay.io/biocontainers/msmetaenhancer.
shpc-registry automated BioContainers addition for msmetaenhancer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/msmetaenhancer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/msmetaenhancer:0.2.5--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/msmetaenhancer/0.2.5--pyhdfd78af_0
$ module help quay.io/biocontainers/msmetaenhancer/0.2.5--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### msmetaenhancer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### msmetaenhancer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### msmetaenhancer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### msmetaenhancer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### msmetaenhancer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### msmetaenhancer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### msmetaenhancer

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