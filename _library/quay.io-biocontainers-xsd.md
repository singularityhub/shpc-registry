---
layout: container
name:  "quay.io/biocontainers/xsd"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/xsd/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/xsd/container.yaml"
updated_at: "2022-10-27 01:13:24.018970"
latest: "4.0.0_dep--h0a036d8_4"
container_url: "https://biocontainers.pro/tools/xsd"

versions:
 - "4.0.0_dep--h0a036d8_4"
description: "shpc-registry automated BioContainers addition for xsd"
config: {"url": "https://biocontainers.pro/tools/xsd", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for xsd", "latest": {"4.0.0_dep--h0a036d8_4": "sha256:d7818b81d3d534e99241b87cca802d8199ccec9406fc0ae629c5db3cbf0b776f"}, "tags": {"4.0.0_dep--h0a036d8_4": "sha256:d7818b81d3d534e99241b87cca802d8199ccec9406fc0ae629c5db3cbf0b776f"}, "docker": "quay.io/biocontainers/xsd"}
---

This module is a singularity container wrapper for quay.io/biocontainers/xsd.
shpc-registry automated BioContainers addition for xsd
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/xsd
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/xsd:4.0.0_dep--h0a036d8_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/xsd/4.0.0_dep--h0a036d8_4
$ module help quay.io/biocontainers/xsd/4.0.0_dep--h0a036d8_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### xsd-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### xsd-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### xsd-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### xsd-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### xsd-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### xsd-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### xsd

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