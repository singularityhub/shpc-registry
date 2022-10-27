---
layout: container
name:  "quay.io/biocontainers/bioframe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioframe/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioframe/container.yaml"
updated_at: "2022-10-27 01:14:10.824221"
latest: "0.3.3--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioframe"

versions:
 - "0.3.3--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioframe"
config: {"url": "https://biocontainers.pro/tools/bioframe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioframe", "latest": {"0.3.3--pyhdfd78af_0": "sha256:d0d4f6e99abcbc4b5b94225ead9eb539b58749e58da0bf1387dbac36281355ab"}, "tags": {"0.3.3--pyhdfd78af_0": "sha256:d0d4f6e99abcbc4b5b94225ead9eb539b58749e58da0bf1387dbac36281355ab"}, "docker": "quay.io/biocontainers/bioframe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioframe.
shpc-registry automated BioContainers addition for bioframe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioframe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioframe:0.3.3--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioframe/0.3.3--pyhdfd78af_0
$ module help quay.io/biocontainers/bioframe/0.3.3--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioframe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioframe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioframe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioframe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioframe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioframe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioframe

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