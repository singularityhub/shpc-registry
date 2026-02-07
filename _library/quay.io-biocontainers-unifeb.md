---
layout: container
name:  "quay.io/biocontainers/unifeb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/unifeb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/unifeb/container.yaml"
updated_at: "2026-02-07 04:27:00.696814"
latest: "0.1.1--h3ab6199_0"
container_url: "https://biocontainers.pro/tools/unifeb"
aliases:
 - "unifeb"
versions:
 - "0.1.1--h3ab6199_0"
description: "singularity registry hpc automated addition for unifeb"
config: {"url": "https://biocontainers.pro/tools/unifeb", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for unifeb", "latest": {"0.1.1--h3ab6199_0": "sha256:625598953ecce1d52eebc5ffa5a24c00d4f9c5fa33f4672456ea410ec91d7c3a"}, "tags": {"0.1.1--h3ab6199_0": "sha256:625598953ecce1d52eebc5ffa5a24c00d4f9c5fa33f4672456ea410ec91d7c3a"}, "docker": "quay.io/biocontainers/unifeb", "aliases": {"unifeb": "/usr/local/bin/unifeb"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/unifeb.
singularity registry hpc automated addition for unifeb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/unifeb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/unifeb:0.1.1--h3ab6199_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/unifeb/0.1.1--h3ab6199_0
$ module help quay.io/biocontainers/unifeb/0.1.1--h3ab6199_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### unifeb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### unifeb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### unifeb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### unifeb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### unifeb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### unifeb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### unifeb

```bash
$ singularity exec <container> /usr/local/bin/unifeb
$ podman run --it --rm --entrypoint /usr/local/bin/unifeb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unifeb   -v ${PWD} -w ${PWD} <container> -c " $@"
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