---
layout: container
name:  "quay.io/biocontainers/r-perfmeas"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-perfmeas/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-perfmeas/container.yaml"
updated_at: "2023-02-03 03:29:16.187234"
latest: "1.2.5--r42h73dbb54_1"
container_url: "https://biocontainers.pro/tools/r-perfmeas"

versions:
 - "1.2.5--r41h73dbb54_0"
 - "1.2.5--r42h73dbb54_1"
description: "shpc-registry automated BioContainers addition for r-perfmeas"
config: {"url": "https://biocontainers.pro/tools/r-perfmeas", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-perfmeas", "latest": {"1.2.5--r42h73dbb54_1": "sha256:459b4cd99f1173443ff77bb0548508617bf96bf3547d1c6f052b10176ad6aca7"}, "tags": {"1.2.5--r41h73dbb54_0": "sha256:9601f5a971ebdf413b8bcb2b3d8c8d06b083fe847e7e2702287ea3d31af7d922", "1.2.5--r42h73dbb54_1": "sha256:459b4cd99f1173443ff77bb0548508617bf96bf3547d1c6f052b10176ad6aca7"}, "docker": "quay.io/biocontainers/r-perfmeas"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-perfmeas.
shpc-registry automated BioContainers addition for r-perfmeas
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-perfmeas
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-perfmeas:1.2.5--r42h73dbb54_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-perfmeas/1.2.5--r42h73dbb54_1
$ module help quay.io/biocontainers/r-perfmeas/1.2.5--r42h73dbb54_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-perfmeas-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-perfmeas-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-perfmeas-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-perfmeas-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-perfmeas-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-perfmeas-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-perfmeas

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