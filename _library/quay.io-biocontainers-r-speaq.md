---
layout: container
name:  "quay.io/biocontainers/r-speaq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-speaq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-speaq/container.yaml"
updated_at: "2024-03-21 04:31:34.305440"
latest: "2.7.0--r43h3121a25_2"
container_url: "https://biocontainers.pro/tools/r-speaq"

versions:
 - "2.7.0--r41h3121a25_0"
 - "2.7.0--r42h3121a25_1"
 - "2.7.0--r43h3121a25_2"
description: "shpc-registry automated BioContainers addition for r-speaq"
config: {"url": "https://biocontainers.pro/tools/r-speaq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-speaq", "latest": {"2.7.0--r43h3121a25_2": "sha256:1477f43eae8d6cbbf8380d3b9cfc481b0f17ad5ad71e857c0489c73f67833f4a"}, "tags": {"2.7.0--r41h3121a25_0": "sha256:5b734b07ac61320950016eb358d17a71c726859819c729aa315607a78a2c4ea8", "2.7.0--r42h3121a25_1": "sha256:cbd40762858c037b57e565f32e8f6a25b24b43bda794609b1bd99b3fe2d156e4", "2.7.0--r43h3121a25_2": "sha256:1477f43eae8d6cbbf8380d3b9cfc481b0f17ad5ad71e857c0489c73f67833f4a"}, "docker": "quay.io/biocontainers/r-speaq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-speaq.
shpc-registry automated BioContainers addition for r-speaq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-speaq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-speaq:2.7.0--r43h3121a25_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-speaq/2.7.0--r43h3121a25_2
$ module help quay.io/biocontainers/r-speaq/2.7.0--r43h3121a25_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-speaq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-speaq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-speaq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-speaq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-speaq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-speaq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-speaq

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