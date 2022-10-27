---
layout: container
name:  "quay.io/biocontainers/glimmerhmm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/glimmerhmm/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/glimmerhmm/container.yaml"
updated_at: "2022-10-27 00:22:11.389219"
latest: "3.0.4--pl5321h87f3376_5"
container_url: "https://biocontainers.pro/tools/glimmerhmm"

versions:
 - "3.0.4--pl5321h87f3376_5"
description: "shpc-registry automated BioContainers addition for glimmerhmm"
config: {"url": "https://biocontainers.pro/tools/glimmerhmm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for glimmerhmm", "latest": {"3.0.4--pl5321h87f3376_5": "sha256:efcb52d8586dffdd54c001570ef0e660fba5168d74c4d2cf90930f8a85733281"}, "tags": {"3.0.4--pl5321h87f3376_5": "sha256:efcb52d8586dffdd54c001570ef0e660fba5168d74c4d2cf90930f8a85733281"}, "docker": "quay.io/biocontainers/glimmerhmm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/glimmerhmm.
shpc-registry automated BioContainers addition for glimmerhmm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/glimmerhmm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/glimmerhmm:3.0.4--pl5321h87f3376_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/glimmerhmm/3.0.4--pl5321h87f3376_5
$ module help quay.io/biocontainers/glimmerhmm/3.0.4--pl5321h87f3376_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### glimmerhmm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### glimmerhmm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### glimmerhmm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### glimmerhmm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### glimmerhmm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### glimmerhmm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### glimmerhmm

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