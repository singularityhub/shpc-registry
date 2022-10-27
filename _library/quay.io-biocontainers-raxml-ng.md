---
layout: container
name:  "quay.io/biocontainers/raxml-ng"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/raxml-ng/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/raxml-ng/container.yaml"
updated_at: "2022-10-27 01:14:16.910293"
latest: "1.1.0--h22e3c99_1"
container_url: "https://biocontainers.pro/tools/raxml-ng"

versions:
 - "1.1.0--h22e3c99_1"
description: "shpc-registry automated BioContainers addition for raxml-ng"
config: {"url": "https://biocontainers.pro/tools/raxml-ng", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for raxml-ng", "latest": {"1.1.0--h22e3c99_1": "sha256:1f7d3b92b50ef5e2f7ec6330cdadf41e252e878b80657b15290e57cb54e86a82"}, "tags": {"1.1.0--h22e3c99_1": "sha256:1f7d3b92b50ef5e2f7ec6330cdadf41e252e878b80657b15290e57cb54e86a82"}, "docker": "quay.io/biocontainers/raxml-ng"}
---

This module is a singularity container wrapper for quay.io/biocontainers/raxml-ng.
shpc-registry automated BioContainers addition for raxml-ng
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/raxml-ng
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/raxml-ng:1.1.0--h22e3c99_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/raxml-ng/1.1.0--h22e3c99_1
$ module help quay.io/biocontainers/raxml-ng/1.1.0--h22e3c99_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### raxml-ng-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### raxml-ng-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### raxml-ng-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### raxml-ng-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### raxml-ng-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### raxml-ng-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### raxml-ng

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