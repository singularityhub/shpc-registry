---
layout: container
name:  "quay.io/biocontainers/ribotricer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ribotricer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ribotricer/container.yaml"
updated_at: "2024-09-02 05:04:18.888828"
latest: "1.4.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/ribotricer"

versions:
 - "1.3.2--py_0"
 - "1.3.3--pyhdfd78af_0"
 - "1.4.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for ribotricer"
config: {"url": "https://biocontainers.pro/tools/ribotricer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ribotricer", "latest": {"1.4.0--pyhdfd78af_0": "sha256:09b1efa9f235a38319126d712e332ed09742c72896a4438627c2bd4e5f93623f"}, "tags": {"1.3.2--py_0": "sha256:ee66d39c752f32f2b5de489d36063bc74e6739a2637fc78dd084ec116f3b4af3", "1.3.3--pyhdfd78af_0": "sha256:3e3ce814218b50555886b5d94697085d1c17de815a56dd20aa3b6408226d0e06", "1.4.0--pyhdfd78af_0": "sha256:09b1efa9f235a38319126d712e332ed09742c72896a4438627c2bd4e5f93623f"}, "docker": "quay.io/biocontainers/ribotricer"}
---

This module is a singularity container wrapper for quay.io/biocontainers/ribotricer.
shpc-registry automated BioContainers addition for ribotricer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ribotricer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ribotricer:1.4.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ribotricer/1.4.0--pyhdfd78af_0
$ module help quay.io/biocontainers/ribotricer/1.4.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ribotricer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ribotricer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ribotricer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ribotricer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ribotricer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ribotricer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### ribotricer

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