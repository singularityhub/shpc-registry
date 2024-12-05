---
layout: container
name:  "quay.io/biocontainers/amplici"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/amplici/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/amplici/container.yaml"
updated_at: "2024-12-05 03:28:53.364187"
latest: "2.2--hd50232a_0"
container_url: "https://biocontainers.pro/tools/amplici"
aliases:
 - "run_AmpliCI"
versions:
 - "2.2--hd50232a_0"
description: "singularity registry hpc automated addition for amplici"
config: {"url": "https://biocontainers.pro/tools/amplici", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for amplici", "latest": {"2.2--hd50232a_0": "sha256:e48a24dabce073d0a224eab3c28a208ada53900e1944cec2c1d8c931e97377b0"}, "tags": {"2.2--hd50232a_0": "sha256:e48a24dabce073d0a224eab3c28a208ada53900e1944cec2c1d8c931e97377b0"}, "docker": "quay.io/biocontainers/amplici", "aliases": {"run_AmpliCI": "/usr/local/bin/run_AmpliCI"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/amplici.
singularity registry hpc automated addition for amplici
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/amplici
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/amplici:2.2--hd50232a_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/amplici/2.2--hd50232a_0
$ module help quay.io/biocontainers/amplici/2.2--hd50232a_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### amplici-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### amplici-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### amplici-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### amplici-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### amplici-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### amplici-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### run_AmpliCI

```bash
$ singularity exec <container> /usr/local/bin/run_AmpliCI
$ podman run --it --rm --entrypoint /usr/local/bin/run_AmpliCI   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_AmpliCI   -v ${PWD} -w ${PWD} <container> -c " $@"
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