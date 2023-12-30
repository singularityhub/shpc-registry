---
layout: container
name:  "quay.io/biocontainers/seq-gen"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/seq-gen/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/seq-gen/container.yaml"
updated_at: "2023-12-30 02:46:46.480018"
latest: "1.3.4--h031d066_7"
container_url: "https://biocontainers.pro/tools/seq-gen"
aliases:
 - "seq-gen"
versions:
 - "1.3.4--hec16e2b_5"
 - "1.3.4--hec16e2b_6"
 - "1.3.4--h031d066_7"
description: "shpc-registry automated BioContainers addition for seq-gen"
config: {"url": "https://biocontainers.pro/tools/seq-gen", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for seq-gen", "latest": {"1.3.4--h031d066_7": "sha256:04e12317a609a3b2a1c2322901d9fd18f273b9d9e358f896dab2fbf7ca220d3f"}, "tags": {"1.3.4--hec16e2b_5": "sha256:0eb70dcc3eec532514832056071ba3d9ec250807ef9268e2ceebc91d71d85e39", "1.3.4--hec16e2b_6": "sha256:14a0659111fa4b722cd21db1eebea72ee3ec2ab2e5833215935690565f925961", "1.3.4--h031d066_7": "sha256:04e12317a609a3b2a1c2322901d9fd18f273b9d9e358f896dab2fbf7ca220d3f"}, "docker": "quay.io/biocontainers/seq-gen", "aliases": {"seq-gen": "/usr/local/bin/seq-gen"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/seq-gen.
shpc-registry automated BioContainers addition for seq-gen
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/seq-gen
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/seq-gen:1.3.4--h031d066_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/seq-gen/1.3.4--h031d066_7
$ module help quay.io/biocontainers/seq-gen/1.3.4--h031d066_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### seq-gen-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### seq-gen-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### seq-gen-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### seq-gen-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### seq-gen-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### seq-gen-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### seq-gen

```bash
$ singularity exec <container> /usr/local/bin/seq-gen
$ podman run --it --rm --entrypoint /usr/local/bin/seq-gen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seq-gen   -v ${PWD} -w ${PWD} <container> -c " $@"
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