---
layout: container
name:  "quay.io/biocontainers/ymp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ymp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ymp/container.yaml"
updated_at: "2024-08-27 03:00:47.080600"
latest: "0.3.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/ymp"

versions:
 - "0.2.1--py_0"
 - "0.3.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for ymp"
config: {"url": "https://biocontainers.pro/tools/ymp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ymp", "latest": {"0.3.1--pyhdfd78af_0": "sha256:efc80c66cf918e6cd3a609997ba77255f78149c9e6ab603473795c51fa306b27"}, "tags": {"0.2.1--py_0": "sha256:4b335f3bf74c50987bd27f4f4f7e52c34960bde5681606335d1b15b8484d5245", "0.3.1--pyhdfd78af_0": "sha256:efc80c66cf918e6cd3a609997ba77255f78149c9e6ab603473795c51fa306b27"}, "docker": "quay.io/biocontainers/ymp"}
---

This module is a singularity container wrapper for quay.io/biocontainers/ymp.
shpc-registry automated BioContainers addition for ymp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ymp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ymp:0.3.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ymp/0.3.1--pyhdfd78af_0
$ module help quay.io/biocontainers/ymp/0.3.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ymp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ymp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ymp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ymp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ymp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ymp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### ymp

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