---
layout: container
name:  "quay.io/biocontainers/r-taxa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-taxa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-taxa/container.yaml"
updated_at: "2024-02-10 02:27:22.268634"
latest: "0.3.2--r351h6115d3f_0"
container_url: "https://biocontainers.pro/tools/r-taxa"

versions:
 - "0.3.2--r351h6115d3f_0"
description: "shpc-registry automated BioContainers addition for r-taxa"
config: {"url": "https://biocontainers.pro/tools/r-taxa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-taxa", "latest": {"0.3.2--r351h6115d3f_0": "sha256:360337b67f9c19ae34a6a37e882bb53936d287c4cb02174d51017a9299395b87"}, "tags": {"0.3.2--r351h6115d3f_0": "sha256:360337b67f9c19ae34a6a37e882bb53936d287c4cb02174d51017a9299395b87"}, "docker": "quay.io/biocontainers/r-taxa"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-taxa.
shpc-registry automated BioContainers addition for r-taxa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-taxa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-taxa:0.3.2--r351h6115d3f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-taxa/0.3.2--r351h6115d3f_0
$ module help quay.io/biocontainers/r-taxa/0.3.2--r351h6115d3f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-taxa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-taxa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-taxa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-taxa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-taxa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-taxa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-taxa

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