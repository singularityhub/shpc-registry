---
layout: container
name:  "quay.io/biocontainers/bcdoc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bcdoc/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bcdoc/container.yaml"
updated_at: "2022-10-27 01:09:34.013920"
latest: "0.16.0--py35_0"
container_url: "https://biocontainers.pro/tools/bcdoc"

versions:
 - "0.16.0--py35_0"
description: "shpc-registry automated BioContainers addition for bcdoc"
config: {"url": "https://biocontainers.pro/tools/bcdoc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bcdoc", "latest": {"0.16.0--py35_0": "sha256:84b262c5b3e79b98d26086fa721be9d54f8403f7c676107bc745643549ccabdf"}, "tags": {"0.16.0--py35_0": "sha256:84b262c5b3e79b98d26086fa721be9d54f8403f7c676107bc745643549ccabdf"}, "docker": "quay.io/biocontainers/bcdoc"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bcdoc.
shpc-registry automated BioContainers addition for bcdoc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bcdoc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bcdoc:0.16.0--py35_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bcdoc/0.16.0--py35_0
$ module help quay.io/biocontainers/bcdoc/0.16.0--py35_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bcdoc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bcdoc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bcdoc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bcdoc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bcdoc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bcdoc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bcdoc

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