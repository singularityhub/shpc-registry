---
layout: container
name:  "quay.io/biocontainers/r-vision"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-vision/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-vision/container.yaml"
updated_at: "2023-10-14 03:02:00.726189"
latest: "2.0.0--r43h4ac6f70_7"
container_url: "https://biocontainers.pro/tools/r-vision"

versions:
 - "2.0.0--r41h9f5acd7_4"
 - "2.0.0--r42h9f5acd7_5"
 - "2.0.0--r42h4ac6f70_6"
 - "2.0.0--r43h4ac6f70_7"
description: "shpc-registry automated BioContainers addition for r-vision"
config: {"url": "https://biocontainers.pro/tools/r-vision", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-vision", "latest": {"2.0.0--r43h4ac6f70_7": "sha256:47f7ec16f899b811f29615d53363791665a65d01c77df60190c85b9c45f02c19"}, "tags": {"2.0.0--r41h9f5acd7_4": "sha256:830d705ad5f71a5a57839ab0800055f3021ea7b4966c87c56644b359df54779c", "2.0.0--r42h9f5acd7_5": "sha256:a3d26c798640261bf78ca83e075ce8c39073a11983bf0740b8c0d909616f20c8", "2.0.0--r42h4ac6f70_6": "sha256:cb0635d018c1f42af0b06373bcbce3b5eafb078ee0e85316ea9270001f3622b8", "2.0.0--r43h4ac6f70_7": "sha256:47f7ec16f899b811f29615d53363791665a65d01c77df60190c85b9c45f02c19"}, "docker": "quay.io/biocontainers/r-vision"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-vision.
shpc-registry automated BioContainers addition for r-vision
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-vision
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-vision:2.0.0--r43h4ac6f70_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-vision/2.0.0--r43h4ac6f70_7
$ module help quay.io/biocontainers/r-vision/2.0.0--r43h4ac6f70_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-vision-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-vision-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-vision-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-vision-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-vision-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-vision-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-vision

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