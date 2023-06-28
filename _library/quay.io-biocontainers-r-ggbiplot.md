---
layout: container
name:  "quay.io/biocontainers/r-ggbiplot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-ggbiplot/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-ggbiplot/container.yaml"
updated_at: "2023-06-28 03:21:46.144569"
latest: "0.55--r42h031d066_9"
container_url: "https://biocontainers.pro/tools/r-ggbiplot"

versions:
 - "0.55--r41hec16e2b_6"
 - "0.55--r42hec16e2b_7"
 - "0.55--r42h031d066_9"
description: "shpc-registry automated BioContainers addition for r-ggbiplot"
config: {"url": "https://biocontainers.pro/tools/r-ggbiplot", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-ggbiplot", "latest": {"0.55--r42h031d066_9": "sha256:ca309c0cd7943f0c5e2d051dea3f66f7adad0ce51adb40ca72f0da3329c18758"}, "tags": {"0.55--r41hec16e2b_6": "sha256:472700031cca35b92a885cfbbce9c5467f24f83a890988c34c6781181af9636e", "0.55--r42hec16e2b_7": "sha256:0354c939a170cba20cfd76e5038edc376804f9fc53ba5360698f28535326b088", "0.55--r42h031d066_9": "sha256:ca309c0cd7943f0c5e2d051dea3f66f7adad0ce51adb40ca72f0da3329c18758"}, "docker": "quay.io/biocontainers/r-ggbiplot"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-ggbiplot.
shpc-registry automated BioContainers addition for r-ggbiplot
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-ggbiplot
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-ggbiplot:0.55--r42h031d066_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-ggbiplot/0.55--r42h031d066_9
$ module help quay.io/biocontainers/r-ggbiplot/0.55--r42h031d066_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-ggbiplot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-ggbiplot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-ggbiplot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-ggbiplot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-ggbiplot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-ggbiplot-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-ggbiplot

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