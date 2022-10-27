---
layout: container
name:  "quay.io/biocontainers/bird_tool_utils_python"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bird_tool_utils_python/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bird_tool_utils_python/container.yaml"
updated_at: "2022-10-27 01:05:55.441511"
latest: "0.4.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/bird_tool_utils_python"

versions:
 - "0.4.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for bird_tool_utils_python"
config: {"url": "https://biocontainers.pro/tools/bird_tool_utils_python", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bird_tool_utils_python", "latest": {"0.4.1--pyhdfd78af_0": "sha256:03d3475f0f21960e5f4364d159433489a1775212508c79a7973030bb6756fc5b"}, "tags": {"0.4.1--pyhdfd78af_0": "sha256:03d3475f0f21960e5f4364d159433489a1775212508c79a7973030bb6756fc5b"}, "docker": "quay.io/biocontainers/bird_tool_utils_python"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bird_tool_utils_python.
shpc-registry automated BioContainers addition for bird_tool_utils_python
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bird_tool_utils_python
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bird_tool_utils_python:0.4.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bird_tool_utils_python/0.4.1--pyhdfd78af_0
$ module help quay.io/biocontainers/bird_tool_utils_python/0.4.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bird_tool_utils_python-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bird_tool_utils_python-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bird_tool_utils_python-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bird_tool_utils_python-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bird_tool_utils_python-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bird_tool_utils_python-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bird_tool_utils_python

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