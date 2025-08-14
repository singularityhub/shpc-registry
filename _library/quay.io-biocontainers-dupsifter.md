---
layout: container
name:  "quay.io/biocontainers/dupsifter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dupsifter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dupsifter/container.yaml"
updated_at: "2025-08-14 03:25:17.967016"
latest: "1.3.0.20241113--h566b1c6_1"
container_url: "https://biocontainers.pro/tools/dupsifter"
aliases:
 - "dupsifter"
versions:
 - "1.2.0.20230926--h81da01d_0"
 - "1.2.1.20240119--h81da01d_0"
 - "1.2.1.20240119--h5efdd21_1"
 - "1.3.0.20241113--h5efdd21_0"
 - "1.3.0.20241113--h566b1c6_1"
description: "singularity registry hpc automated addition for dupsifter"
config: {"url": "https://biocontainers.pro/tools/dupsifter", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for dupsifter", "latest": {"1.3.0.20241113--h566b1c6_1": "sha256:5c83c0e8501f2c2ae1bebaddaf4decbed7561f7546f7689b5da7c1bb4e42a6ca"}, "tags": {"1.2.0.20230926--h81da01d_0": "sha256:42004beb33f1b6bf83b5401f20f081f22cd6ee12a948531189fc46ae72d375dd", "1.2.1.20240119--h81da01d_0": "sha256:b0d1b51c00e6a4895d79c45d98d58ae11903d3f59ba8753162110e58cb3ce514", "1.2.1.20240119--h5efdd21_1": "sha256:79a07e54c9ba54d16cafac6a24c5543748b6a19ad197ddb6c048389987d6899c", "1.3.0.20241113--h5efdd21_0": "sha256:52005c70ea670a6bf0346a2dc7c7e3eaffc52fc3e75d3794f1141927d837d63e", "1.3.0.20241113--h566b1c6_1": "sha256:5c83c0e8501f2c2ae1bebaddaf4decbed7561f7546f7689b5da7c1bb4e42a6ca"}, "docker": "quay.io/biocontainers/dupsifter", "aliases": {"dupsifter": "/usr/local/bin/dupsifter"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dupsifter.
singularity registry hpc automated addition for dupsifter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dupsifter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dupsifter:1.3.0.20241113--h566b1c6_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dupsifter/1.3.0.20241113--h566b1c6_1
$ module help quay.io/biocontainers/dupsifter/1.3.0.20241113--h566b1c6_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dupsifter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dupsifter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dupsifter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dupsifter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dupsifter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dupsifter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dupsifter

```bash
$ singularity exec <container> /usr/local/bin/dupsifter
$ podman run --it --rm --entrypoint /usr/local/bin/dupsifter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dupsifter   -v ${PWD} -w ${PWD} <container> -c " $@"
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