---
layout: container
name:  "quay.io/biocontainers/ribowaltz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ribowaltz/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ribowaltz/container.yaml"
updated_at: "2024-02-26 02:37:40.669431"
latest: "2.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/ribowaltz"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.2.0--r42hdfd78af_1"
 - "2.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for ribowaltz"
config: {"url": "https://biocontainers.pro/tools/ribowaltz", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ribowaltz", "latest": {"2.0--r43hdfd78af_0": "sha256:650571dd78442f2dafe041e962976b1fb1451262608eec5057842ef0e66efa7f"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:880cedb414633d44e467c39feed9f85212fc5270c3149a2d966b4fd2cf980426", "1.2.0--r42hdfd78af_1": "sha256:ba7e0e4413de7acd6c263f89b6c861265c26598bdb7113b9239d42e5a08694c0", "2.0--r43hdfd78af_0": "sha256:650571dd78442f2dafe041e962976b1fb1451262608eec5057842ef0e66efa7f"}, "docker": "quay.io/biocontainers/ribowaltz"}
---

This module is a singularity container wrapper for quay.io/biocontainers/ribowaltz.
shpc-registry automated BioContainers addition for ribowaltz
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ribowaltz
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ribowaltz:2.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ribowaltz/2.0--r43hdfd78af_0
$ module help quay.io/biocontainers/ribowaltz/2.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ribowaltz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ribowaltz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ribowaltz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ribowaltz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ribowaltz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ribowaltz-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### ribowaltz

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