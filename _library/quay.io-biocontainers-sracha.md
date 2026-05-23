---
layout: container
name:  "quay.io/biocontainers/sracha"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sracha/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sracha/container.yaml"
updated_at: "2026-05-23 06:14:42.400920"
latest: "0.3.0--h54198d6_0"
container_url: "https://biocontainers.pro/tools/sracha"
aliases:
 - "sracha"
versions:
 - "0.3.0--h54198d6_0"
description: "singularity registry hpc automated addition for sracha"
config: {"url": "https://biocontainers.pro/tools/sracha", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for sracha", "latest": {"0.3.0--h54198d6_0": "sha256:a1111c1a943a9f87b0e8dc4d42efa5f645fa8660e17ba5a5751b4c0e5a9f5667"}, "tags": {"0.3.0--h54198d6_0": "sha256:a1111c1a943a9f87b0e8dc4d42efa5f645fa8660e17ba5a5751b4c0e5a9f5667"}, "docker": "quay.io/biocontainers/sracha", "aliases": {"sracha": "/usr/local/bin/sracha"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sracha.
singularity registry hpc automated addition for sracha
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sracha
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sracha:0.3.0--h54198d6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sracha/0.3.0--h54198d6_0
$ module help quay.io/biocontainers/sracha/0.3.0--h54198d6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sracha-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sracha-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sracha-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sracha-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sracha-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sracha-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sracha

```bash
$ singularity exec <container> /usr/local/bin/sracha
$ podman run --it --rm --entrypoint /usr/local/bin/sracha   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sracha   -v ${PWD} -w ${PWD} <container> -c " $@"
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