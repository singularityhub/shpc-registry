---
layout: container
name:  "quay.io/biocontainers/go"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/go/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/go/container.yaml"
updated_at: "2023-09-17 00:17:38.629221"
latest: "1.11.3"
container_url: "https://biocontainers.pro/tools/go"
aliases:
 - "go"
 - "gofmt"
versions:
 - "1.11.3"
description: "shpc-registry automated BioContainers addition for go"
config: {"url": "https://biocontainers.pro/tools/go", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for go", "latest": {"1.11.3": "sha256:96cb667782057597042728273507e8bc1cb218516080896c95c704a8e94a0c24"}, "tags": {"1.11.3": "sha256:96cb667782057597042728273507e8bc1cb218516080896c95c704a8e94a0c24"}, "docker": "quay.io/biocontainers/go", "aliases": {"go": "/usr/local/bin/go", "gofmt": "/usr/local/bin/gofmt"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/go.
shpc-registry automated BioContainers addition for go
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/go
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/go:1.11.3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/go/1.11.3
$ module help quay.io/biocontainers/go/1.11.3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### go-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### go-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### go-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### go-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### go-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### go-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### go

```bash
$ singularity exec <container> /usr/local/bin/go
$ podman run --it --rm --entrypoint /usr/local/bin/go   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gofmt

```bash
$ singularity exec <container> /usr/local/bin/gofmt
$ podman run --it --rm --entrypoint /usr/local/bin/gofmt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gofmt   -v ${PWD} -w ${PWD} <container> -c " $@"
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