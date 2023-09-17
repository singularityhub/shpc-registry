---
layout: container
name:  "quay.io/biocontainers/pandoc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pandoc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pandoc/container.yaml"
updated_at: "2023-09-16 23:56:10.879554"
latest: "2.1.3--0"
container_url: "https://biocontainers.pro/tools/pandoc"
aliases:
 - "pandoc"
 - "pandoc-citeproc"
versions:
 - "2.1.3--0"
description: "shpc-registry automated BioContainers addition for pandoc"
config: {"url": "https://biocontainers.pro/tools/pandoc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pandoc", "latest": {"2.1.3--0": "sha256:e3782e6f3099ff22f49f18504727bbeea8dcc4b82bc94598184377e096c5af68"}, "tags": {"2.1.3--0": "sha256:e3782e6f3099ff22f49f18504727bbeea8dcc4b82bc94598184377e096c5af68"}, "docker": "quay.io/biocontainers/pandoc", "aliases": {"pandoc": "/usr/local/bin/pandoc", "pandoc-citeproc": "/usr/local/bin/pandoc-citeproc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pandoc.
shpc-registry automated BioContainers addition for pandoc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pandoc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pandoc:2.1.3--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pandoc/2.1.3--0
$ module help quay.io/biocontainers/pandoc/2.1.3--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pandoc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pandoc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pandoc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pandoc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pandoc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pandoc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc-citeproc

```bash
$ singularity exec <container> /usr/local/bin/pandoc-citeproc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-citeproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-citeproc   -v ${PWD} -w ${PWD} <container> -c " $@"
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