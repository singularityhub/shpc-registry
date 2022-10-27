---
layout: container
name:  "quay.io/biocontainers/sphinx-argparse"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sphinx-argparse/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/sphinx-argparse/container.yaml"
updated_at: "2022-10-27 00:54:19.004415"
latest: "0.1.15--py36_0"
container_url: "https://biocontainers.pro/tools/sphinx-argparse"

versions:
 - "0.1.15--py36_0"
description: "shpc-registry automated BioContainers addition for sphinx-argparse"
config: {"url": "https://biocontainers.pro/tools/sphinx-argparse", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sphinx-argparse", "latest": {"0.1.15--py36_0": "sha256:d67e0097073d911513c0d3e966a07c206c581fac94e9a43687bb1462c6903dc5"}, "tags": {"0.1.15--py36_0": "sha256:d67e0097073d911513c0d3e966a07c206c581fac94e9a43687bb1462c6903dc5"}, "docker": "quay.io/biocontainers/sphinx-argparse"}
---

This module is a singularity container wrapper for quay.io/biocontainers/sphinx-argparse.
shpc-registry automated BioContainers addition for sphinx-argparse
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sphinx-argparse
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sphinx-argparse:0.1.15--py36_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sphinx-argparse/0.1.15--py36_0
$ module help quay.io/biocontainers/sphinx-argparse/0.1.15--py36_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sphinx-argparse-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sphinx-argparse-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sphinx-argparse-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sphinx-argparse-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sphinx-argparse-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sphinx-argparse-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### sphinx-argparse

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