---
layout: container
name:  "quay.io/biocontainers/r-lymphclon"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-lymphclon/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-lymphclon/container.yaml"
updated_at: "2024-10-30 15:59:17.305903"
latest: "1.3.0--r43h3121a25_3"
container_url: "https://biocontainers.pro/tools/r-lymphclon"

versions:
 - "1.3.0--r42h3121a25_2"
 - "1.3.0--r43h3121a25_3"
description: "singularity registry hpc automated addition for r-lymphclon"
config: {"url": "https://biocontainers.pro/tools/r-lymphclon", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for r-lymphclon", "latest": {"1.3.0--r43h3121a25_3": "sha256:f7801680148ffcd6419ec7b3b96c7ac508f561770fccc462bdca06adfd2277f5"}, "tags": {"1.3.0--r42h3121a25_2": "sha256:6b34135ab92378c84b52da8b655e52801941650c21b8cd4b451ca6d83950b76c", "1.3.0--r43h3121a25_3": "sha256:f7801680148ffcd6419ec7b3b96c7ac508f561770fccc462bdca06adfd2277f5"}, "docker": "quay.io/biocontainers/r-lymphclon"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-lymphclon.
singularity registry hpc automated addition for r-lymphclon
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-lymphclon
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-lymphclon:1.3.0--r43h3121a25_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-lymphclon/1.3.0--r43h3121a25_3
$ module help quay.io/biocontainers/r-lymphclon/1.3.0--r43h3121a25_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-lymphclon-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-lymphclon-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-lymphclon-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-lymphclon-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-lymphclon-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-lymphclon-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-lymphclon

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