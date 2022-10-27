---
layout: container
name:  "quay.io/biocontainers/visitor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/visitor/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/visitor/container.yaml"
updated_at: "2022-10-27 01:14:27.827212"
latest: "0.1.2--py36_0"
container_url: "https://biocontainers.pro/tools/visitor"

versions:
 - "0.1.2--py36_0"
description: "shpc-registry automated BioContainers addition for visitor"
config: {"url": "https://biocontainers.pro/tools/visitor", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for visitor", "latest": {"0.1.2--py36_0": "sha256:0f5c6f258e284d9f765b88e051e3ea25a54b6e9041b08b97f519efbac3465235"}, "tags": {"0.1.2--py36_0": "sha256:0f5c6f258e284d9f765b88e051e3ea25a54b6e9041b08b97f519efbac3465235"}, "docker": "quay.io/biocontainers/visitor"}
---

This module is a singularity container wrapper for quay.io/biocontainers/visitor.
shpc-registry automated BioContainers addition for visitor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/visitor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/visitor:0.1.2--py36_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/visitor/0.1.2--py36_0
$ module help quay.io/biocontainers/visitor/0.1.2--py36_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### visitor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### visitor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### visitor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### visitor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### visitor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### visitor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### visitor

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