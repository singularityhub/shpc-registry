---
layout: container
name:  "quay.io/biocontainers/gassst"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gassst/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gassst/container.yaml"
updated_at: "2026-01-28 04:42:21.317413"
latest: "1.28--h503566f_3"
container_url: "https://biocontainers.pro/tools/gassst"
aliases:
 - "Gassst"
versions:
 - "1.28--h87f3376_0"
 - "1.28--hdbdd923_2"
 - "1.28--h503566f_3"
description: "singularity registry hpc automated addition for gassst"
config: {"url": "https://biocontainers.pro/tools/gassst", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for gassst", "latest": {"1.28--h503566f_3": "sha256:e6b335b4289c5bdef26df333b37340a109e3f62a535c510cde23742d464a0732"}, "tags": {"1.28--h87f3376_0": "sha256:542b88b547b43885076a66778eda80cd4af6e3643706db82bff071bb4e605b38", "1.28--hdbdd923_2": "sha256:72eecf1e1c281b6806e410c7d50e458b63ef76dd102b3de3be53bff60fd64286", "1.28--h503566f_3": "sha256:e6b335b4289c5bdef26df333b37340a109e3f62a535c510cde23742d464a0732"}, "docker": "quay.io/biocontainers/gassst", "aliases": {"Gassst": "/usr/local/bin/Gassst"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gassst.
singularity registry hpc automated addition for gassst
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gassst
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gassst:1.28--h503566f_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gassst/1.28--h503566f_3
$ module help quay.io/biocontainers/gassst/1.28--h503566f_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gassst-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gassst-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gassst-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gassst-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gassst-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gassst-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Gassst

```bash
$ singularity exec <container> /usr/local/bin/Gassst
$ podman run --it --rm --entrypoint /usr/local/bin/Gassst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Gassst   -v ${PWD} -w ${PWD} <container> -c " $@"
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