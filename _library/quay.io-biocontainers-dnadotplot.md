---
layout: container
name:  "quay.io/biocontainers/dnadotplot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dnadotplot/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dnadotplot/container.yaml"
updated_at: "2025-09-20 03:02:00.597229"
latest: "0.1.4--hc1c3326_0"
container_url: "https://biocontainers.pro/tools/dnadotplot"
aliases:
 - "dnadotplot"
versions:
 - "0.1.4--hc1c3326_0"
description: "singularity registry hpc automated addition for dnadotplot"
config: {"url": "https://biocontainers.pro/tools/dnadotplot", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for dnadotplot", "latest": {"0.1.4--hc1c3326_0": "sha256:ca1fb41b447d19c0b79843e1489891f651bebc6c5602b52d4d977121f2ef50cf"}, "tags": {"0.1.4--hc1c3326_0": "sha256:ca1fb41b447d19c0b79843e1489891f651bebc6c5602b52d4d977121f2ef50cf"}, "docker": "quay.io/biocontainers/dnadotplot", "aliases": {"dnadotplot": "/usr/local/bin/dnadotplot"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dnadotplot.
singularity registry hpc automated addition for dnadotplot
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dnadotplot
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dnadotplot:0.1.4--hc1c3326_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dnadotplot/0.1.4--hc1c3326_0
$ module help quay.io/biocontainers/dnadotplot/0.1.4--hc1c3326_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dnadotplot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dnadotplot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dnadotplot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dnadotplot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dnadotplot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dnadotplot-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dnadotplot

```bash
$ singularity exec <container> /usr/local/bin/dnadotplot
$ podman run --it --rm --entrypoint /usr/local/bin/dnadotplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnadotplot   -v ${PWD} -w ${PWD} <container> -c " $@"
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