---
layout: container
name:  "quay.io/biocontainers/fmlrc2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fmlrc2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fmlrc2/container.yaml"
updated_at: "2024-07-26 03:07:20.613257"
latest: "0.1.7--hb7a5142_0"
container_url: "https://biocontainers.pro/tools/fmlrc2"
aliases:
 - "fmlrc2"
 - "fmlrc2-convert"
 - "starcode"
versions:
 - "0.1.7--hb7a5142_0"
description: "shpc-registry automated BioContainers addition for fmlrc2"
config: {"url": "https://biocontainers.pro/tools/fmlrc2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fmlrc2", "latest": {"0.1.7--hb7a5142_0": "sha256:9020d1fa0e5147e0d7205c298b20a64d115561aaaaba800793578c74e16eaf28"}, "tags": {"0.1.7--hb7a5142_0": "sha256:9020d1fa0e5147e0d7205c298b20a64d115561aaaaba800793578c74e16eaf28"}, "docker": "quay.io/biocontainers/fmlrc2", "aliases": {"fmlrc2": "/usr/local/bin/fmlrc2", "fmlrc2-convert": "/usr/local/bin/fmlrc2-convert", "starcode": "/usr/local/bin/starcode"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fmlrc2.
shpc-registry automated BioContainers addition for fmlrc2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fmlrc2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fmlrc2:0.1.7--hb7a5142_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fmlrc2/0.1.7--hb7a5142_0
$ module help quay.io/biocontainers/fmlrc2/0.1.7--hb7a5142_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fmlrc2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fmlrc2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fmlrc2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fmlrc2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fmlrc2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fmlrc2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fmlrc2

```bash
$ singularity exec <container> /usr/local/bin/fmlrc2
$ podman run --it --rm --entrypoint /usr/local/bin/fmlrc2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fmlrc2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fmlrc2-convert

```bash
$ singularity exec <container> /usr/local/bin/fmlrc2-convert
$ podman run --it --rm --entrypoint /usr/local/bin/fmlrc2-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fmlrc2-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### starcode

```bash
$ singularity exec <container> /usr/local/bin/starcode
$ podman run --it --rm --entrypoint /usr/local/bin/starcode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/starcode   -v ${PWD} -w ${PWD} <container> -c " $@"
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