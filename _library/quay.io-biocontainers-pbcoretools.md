---
layout: container
name:  "quay.io/biocontainers/pbcoretools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pbcoretools/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/pbcoretools/container.yaml"
updated_at: "2022-10-27 00:27:41.193601"
latest: "0.8.1--py_1"
container_url: "https://biocontainers.pro/tools/pbcoretools"
aliases:
 - ".open"
 - ".pbcommand-post-link.sh"
 - ".pbcore-post-link.sh"
 - ".pbcoretools-post-link.sh"
 - "bamsieve"
 - "dataset"
 - "pbtools-gather"
 - "pbvalidate"
versions:
 - "0.8.1--py_1"
description: "shpc-registry automated BioContainers addition for pbcoretools"
config: {"url": "https://biocontainers.pro/tools/pbcoretools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pbcoretools", "latest": {"0.8.1--py_1": "sha256:f7e6370222d5f5035ee2f32dd75d5c8b50d3d6106d18b7d6bf45fbfbb2e6dd15"}, "tags": {"0.8.1--py_1": "sha256:f7e6370222d5f5035ee2f32dd75d5c8b50d3d6106d18b7d6bf45fbfbb2e6dd15"}, "docker": "quay.io/biocontainers/pbcoretools", "aliases": {".open": "/usr/local/bin/.open", ".pbcommand-post-link.sh": "/usr/local/bin/.pbcommand-post-link.sh", ".pbcore-post-link.sh": "/usr/local/bin/.pbcore-post-link.sh", ".pbcoretools-post-link.sh": "/usr/local/bin/.pbcoretools-post-link.sh", "bamsieve": "/usr/local/bin/bamsieve", "dataset": "/usr/local/bin/dataset", "pbtools-gather": "/usr/local/bin/pbtools-gather", "pbvalidate": "/usr/local/bin/pbvalidate"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pbcoretools.
shpc-registry automated BioContainers addition for pbcoretools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pbcoretools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pbcoretools:0.8.1--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pbcoretools/0.8.1--py_1
$ module help quay.io/biocontainers/pbcoretools/0.8.1--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pbcoretools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pbcoretools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pbcoretools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pbcoretools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pbcoretools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pbcoretools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .open

```bash
$ singularity exec <container> /usr/local/bin/.open
$ podman run --it --rm --entrypoint /usr/local/bin/.open   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.open   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .pbcommand-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.pbcommand-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.pbcommand-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.pbcommand-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .pbcore-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.pbcore-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.pbcore-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.pbcore-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .pbcoretools-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.pbcoretools-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.pbcoretools-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.pbcoretools-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamsieve

```bash
$ singularity exec <container> /usr/local/bin/bamsieve
$ podman run --it --rm --entrypoint /usr/local/bin/bamsieve   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamsieve   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dataset

```bash
$ singularity exec <container> /usr/local/bin/dataset
$ podman run --it --rm --entrypoint /usr/local/bin/dataset   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dataset   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbtools-gather

```bash
$ singularity exec <container> /usr/local/bin/pbtools-gather
$ podman run --it --rm --entrypoint /usr/local/bin/pbtools-gather   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbtools-gather   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbvalidate

```bash
$ singularity exec <container> /usr/local/bin/pbvalidate
$ podman run --it --rm --entrypoint /usr/local/bin/pbvalidate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbvalidate   -v ${PWD} -w ${PWD} <container> -c " $@"
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