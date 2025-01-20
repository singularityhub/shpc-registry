---
layout: container
name:  "quay.io/biocontainers/var-agg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/var-agg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/var-agg/container.yaml"
updated_at: "2025-01-20 04:06:45.531808"
latest: "0.1.1--hbcae180_1"
container_url: "https://biocontainers.pro/tools/var-agg"
aliases:
 - "var-agg"
versions:
 - "0.1.1--hbcae180_1"
description: "shpc-registry automated BioContainers addition for var-agg"
config: {"url": "https://biocontainers.pro/tools/var-agg", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for var-agg", "latest": {"0.1.1--hbcae180_1": "sha256:c825883dcd89ec0c7a2715157b7d6e312acff23496985c079a596ba879392973"}, "tags": {"0.1.1--hbcae180_1": "sha256:c825883dcd89ec0c7a2715157b7d6e312acff23496985c079a596ba879392973"}, "docker": "quay.io/biocontainers/var-agg", "aliases": {"var-agg": "/usr/local/bin/var-agg"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/var-agg.
shpc-registry automated BioContainers addition for var-agg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/var-agg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/var-agg:0.1.1--hbcae180_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/var-agg/0.1.1--hbcae180_1
$ module help quay.io/biocontainers/var-agg/0.1.1--hbcae180_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### var-agg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### var-agg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### var-agg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### var-agg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### var-agg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### var-agg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### var-agg

```bash
$ singularity exec <container> /usr/local/bin/var-agg
$ podman run --it --rm --entrypoint /usr/local/bin/var-agg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/var-agg   -v ${PWD} -w ${PWD} <container> -c " $@"
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