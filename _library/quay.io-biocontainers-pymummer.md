---
layout: container
name:  "quay.io/biocontainers/pymummer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pymummer/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/pymummer/container.yaml"
updated_at: "2022-10-27 00:57:41.868954"
latest: "0.9.0--py35_0"
container_url: "https://biocontainers.pro/tools/pymummer"

versions:
 - "0.9.0--py35_0"
description: "shpc-registry automated BioContainers addition for pymummer"
config: {"url": "https://biocontainers.pro/tools/pymummer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pymummer", "latest": {"0.9.0--py35_0": "sha256:b608927d77cd74781f3f77267b2dc96cabef0cc70554d47c23a835f5de41127e"}, "tags": {"0.9.0--py35_0": "sha256:b608927d77cd74781f3f77267b2dc96cabef0cc70554d47c23a835f5de41127e"}, "docker": "quay.io/biocontainers/pymummer"}
---

This module is a singularity container wrapper for quay.io/biocontainers/pymummer.
shpc-registry automated BioContainers addition for pymummer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pymummer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pymummer:0.9.0--py35_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pymummer/0.9.0--py35_0
$ module help quay.io/biocontainers/pymummer/0.9.0--py35_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pymummer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pymummer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pymummer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pymummer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pymummer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pymummer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### pymummer

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