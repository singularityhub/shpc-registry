---
layout: container
name:  "quay.io/biocontainers/piscem-infer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/piscem-infer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/piscem-infer/container.yaml"
updated_at: "2024-04-01 02:56:50.184041"
latest: "0.6.0--h4349ce8_0"
container_url: "https://biocontainers.pro/tools/piscem-infer"
aliases:
 - "piscem-infer"
versions:
 - "0.6.0--h4349ce8_0"
description: "singularity registry hpc automated addition for piscem-infer"
config: {"url": "https://biocontainers.pro/tools/piscem-infer", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for piscem-infer", "latest": {"0.6.0--h4349ce8_0": "sha256:e73bbcfed24977527fce0669a6b4c76a30fefbff6021223c3cec296363ec6893"}, "tags": {"0.6.0--h4349ce8_0": "sha256:e73bbcfed24977527fce0669a6b4c76a30fefbff6021223c3cec296363ec6893"}, "docker": "quay.io/biocontainers/piscem-infer", "aliases": {"piscem-infer": "/usr/local/bin/piscem-infer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/piscem-infer.
singularity registry hpc automated addition for piscem-infer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/piscem-infer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/piscem-infer:0.6.0--h4349ce8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/piscem-infer/0.6.0--h4349ce8_0
$ module help quay.io/biocontainers/piscem-infer/0.6.0--h4349ce8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### piscem-infer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### piscem-infer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### piscem-infer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### piscem-infer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### piscem-infer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### piscem-infer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### piscem-infer

```bash
$ singularity exec <container> /usr/local/bin/piscem-infer
$ podman run --it --rm --entrypoint /usr/local/bin/piscem-infer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/piscem-infer   -v ${PWD} -w ${PWD} <container> -c " $@"
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