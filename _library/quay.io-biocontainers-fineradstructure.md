---
layout: container
name:  "quay.io/biocontainers/fineradstructure"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fineradstructure/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fineradstructure/container.yaml"
updated_at: "2024-04-24 03:00:41.483389"
latest: "0.3.2r109--hc66845c_6"
container_url: "https://biocontainers.pro/tools/fineradstructure"
aliases:
 - "RADpainter"
 - "finestructure"
versions:
 - "0.3.2r109--h5269a4d_4"
 - "0.3.2r109--hc66845c_6"
description: "shpc-registry automated BioContainers addition for fineradstructure"
config: {"url": "https://biocontainers.pro/tools/fineradstructure", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fineradstructure", "latest": {"0.3.2r109--hc66845c_6": "sha256:e47b3f841063da965f23eb2566d720882fb7332607ae680e7723e6be0de10f08"}, "tags": {"0.3.2r109--h5269a4d_4": "sha256:a1b784484d29614f2da7c53ca3295007e4a6b34bf65969acee22477485856114", "0.3.2r109--hc66845c_6": "sha256:e47b3f841063da965f23eb2566d720882fb7332607ae680e7723e6be0de10f08"}, "docker": "quay.io/biocontainers/fineradstructure", "aliases": {"RADpainter": "/usr/local/bin/RADpainter", "finestructure": "/usr/local/bin/finestructure"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fineradstructure.
shpc-registry automated BioContainers addition for fineradstructure
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fineradstructure
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fineradstructure:0.3.2r109--hc66845c_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fineradstructure/0.3.2r109--hc66845c_6
$ module help quay.io/biocontainers/fineradstructure/0.3.2r109--hc66845c_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fineradstructure-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fineradstructure-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fineradstructure-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fineradstructure-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fineradstructure-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fineradstructure-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### RADpainter

```bash
$ singularity exec <container> /usr/local/bin/RADpainter
$ podman run --it --rm --entrypoint /usr/local/bin/RADpainter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RADpainter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### finestructure

```bash
$ singularity exec <container> /usr/local/bin/finestructure
$ podman run --it --rm --entrypoint /usr/local/bin/finestructure   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/finestructure   -v ${PWD} -w ${PWD} <container> -c " $@"
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