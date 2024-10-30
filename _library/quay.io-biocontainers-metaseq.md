---
layout: container
name:  "quay.io/biocontainers/metaseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metaseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metaseq/container.yaml"
updated_at: "2024-10-30 03:24:59.187796"
latest: "0.5.6--py27h9801fc8_5"
container_url: "https://biocontainers.pro/tools/metaseq"

versions:
 - "0.5.6--py27h9801fc8_5"
description: "shpc-registry automated BioContainers addition for metaseq"
config: {"url": "https://biocontainers.pro/tools/metaseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metaseq", "latest": {"0.5.6--py27h9801fc8_5": "sha256:c77898d8a6c7257d819b6d57b42e9e528523bf86169fc33660f710b9e80935e4"}, "tags": {"0.5.6--py27h9801fc8_5": "sha256:c77898d8a6c7257d819b6d57b42e9e528523bf86169fc33660f710b9e80935e4"}, "docker": "quay.io/biocontainers/metaseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/metaseq.
shpc-registry automated BioContainers addition for metaseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metaseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metaseq:0.5.6--py27h9801fc8_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metaseq/0.5.6--py27h9801fc8_5
$ module help quay.io/biocontainers/metaseq/0.5.6--py27h9801fc8_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metaseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metaseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metaseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metaseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metaseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metaseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### metaseq

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