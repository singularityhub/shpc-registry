---
layout: container
name:  "ghcr.io/autamus/loki"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/loki/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/loki/container.yaml"
updated_at: "2025-09-04 02:58:22.566337"
latest: "0.1.7"
container_url: "https://github.com/orgs/autamus/packages/container/package/loki"

versions:
 - "0.1.7"
 - "latest"
description: "Loki is a C++ library of designs, containing flexible implementations of common design patterns and idioms."
config: {"docker": "ghcr.io/autamus/loki", "url": "https://github.com/orgs/autamus/packages/container/package/loki", "maintainer": "@vsoch", "description": "Loki is a C++ library of designs, containing flexible implementations of common design patterns and idioms.", "latest": {"0.1.7": "sha256:049e798b85a54719a00abc58a8e1edd002cd3691014412fd352fcc7cfe871cdd"}, "tags": {"0.1.7": "sha256:049e798b85a54719a00abc58a8e1edd002cd3691014412fd352fcc7cfe871cdd", "latest": "sha256:049e798b85a54719a00abc58a8e1edd002cd3691014412fd352fcc7cfe871cdd"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/loki.
Loki is a C++ library of designs, containing flexible implementations of common design patterns and idioms.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/loki
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/loki:0.1.7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/loki/0.1.7
$ module help ghcr.io/autamus/loki/0.1.7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### loki-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### loki-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### loki-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### loki-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### loki-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### loki-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### loki

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