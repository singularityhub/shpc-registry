---
layout: container
name:  "ghcr.io/autamus/flit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/flit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/flit/container.yaml"
updated_at: "2025-01-20 02:48:32.805732"
latest: "2.1.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/flit"
aliases:
 - "flit"
versions:
 - "2.1.0"
 - "latest"
description: "Floating-point Litmus Tests (FLiT) is a C++ test infrastructure for detecting variability in floating-point code caused by variations in compiler code generation, hardware and execution environments."
config: {"docker": "ghcr.io/autamus/flit", "url": "https://github.com/orgs/autamus/packages/container/package/flit", "maintainer": "@vsoch", "description": "Floating-point Litmus Tests (FLiT) is a C++ test infrastructure for detecting variability in floating-point code caused by variations in compiler code generation, hardware and execution environments.", "latest": {"2.1.0": "sha256:c846aae5413546b722576b469b52ce1a52948040b778111cb4de4c8501161354"}, "tags": {"2.1.0": "sha256:c846aae5413546b722576b469b52ce1a52948040b778111cb4de4c8501161354", "latest": "sha256:c846aae5413546b722576b469b52ce1a52948040b778111cb4de4c8501161354"}, "aliases": {"flit": "/opt/view/bin/flit"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/flit.
Floating-point Litmus Tests (FLiT) is a C++ test infrastructure for detecting variability in floating-point code caused by variations in compiler code generation, hardware and execution environments.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/flit
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/flit:2.1.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/flit/2.1.0
$ module help ghcr.io/autamus/flit/2.1.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### flit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### flit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### flit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### flit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### flit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### flit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### flit

```bash
$ singularity exec <container> /opt/view/bin/flit
$ podman run --it --rm --entrypoint /opt/view/bin/flit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/flit   -v ${PWD} -w ${PWD} <container> -c " $@"
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