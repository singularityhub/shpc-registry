---
layout: container
name:  "quay.io/biocontainers/bcbreport"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bcbreport/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bcbreport/container.yaml"
updated_at: "2022-10-27 00:34:26.823567"
latest: "0.99.29--py_2"
container_url: "https://biocontainers.pro/tools/bcbreport"

versions:
 - "0.99.29--py_2"
description: "shpc-registry automated BioContainers addition for bcbreport"
config: {"url": "https://biocontainers.pro/tools/bcbreport", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bcbreport", "latest": {"0.99.29--py_2": "sha256:99d982a15fd5305b058cabf1c1c4b55fdec666269222ef2fa26758ae53701515"}, "tags": {"0.99.29--py_2": "sha256:99d982a15fd5305b058cabf1c1c4b55fdec666269222ef2fa26758ae53701515"}, "docker": "quay.io/biocontainers/bcbreport"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bcbreport.
shpc-registry automated BioContainers addition for bcbreport
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bcbreport
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bcbreport:0.99.29--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bcbreport/0.99.29--py_2
$ module help quay.io/biocontainers/bcbreport/0.99.29--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bcbreport-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bcbreport-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bcbreport-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bcbreport-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bcbreport-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bcbreport-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bcbreport

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