---
layout: container
name:  "quay.io/biocontainers/nanoplotter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nanoplotter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nanoplotter/container.yaml"
updated_at: "2025-02-05 02:53:09.748210"
latest: "1.10.0--py_1"
container_url: "https://biocontainers.pro/tools/nanoplotter"

versions:
 - "1.9.1--py_0"
 - "1.10.0--py_1"
description: "shpc-registry automated BioContainers addition for nanoplotter"
config: {"url": "https://biocontainers.pro/tools/nanoplotter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nanoplotter", "latest": {"1.10.0--py_1": "sha256:a174dc07f3bbca8b8e61a8288ed1164eedea7a87140aeee74c34b4bb45e605fc"}, "tags": {"1.9.1--py_0": "sha256:ecce803c9244e7d14324a2df55d2ef574856096c2907062f6a707854c3e5b9d1", "1.10.0--py_1": "sha256:a174dc07f3bbca8b8e61a8288ed1164eedea7a87140aeee74c34b4bb45e605fc"}, "docker": "quay.io/biocontainers/nanoplotter"}
---

This module is a singularity container wrapper for quay.io/biocontainers/nanoplotter.
shpc-registry automated BioContainers addition for nanoplotter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nanoplotter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nanoplotter:1.10.0--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nanoplotter/1.10.0--py_1
$ module help quay.io/biocontainers/nanoplotter/1.10.0--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nanoplotter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nanoplotter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nanoplotter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nanoplotter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nanoplotter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nanoplotter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### nanoplotter

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