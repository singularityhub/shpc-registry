---
layout: container
name:  "quay.io/biocontainers/mea"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mea/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mea/container.yaml"
updated_at: "2023-05-05 03:07:59.749554"
latest: "0.6.4--h9f5acd7_6"
container_url: "https://biocontainers.pro/tools/mea"
aliases:
 - "mea"
 - "mea_eval"
 - "mea_mix"
versions:
 - "0.6.4--h9f5acd7_6"
description: "shpc-registry automated BioContainers addition for mea"
config: {"url": "https://biocontainers.pro/tools/mea", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mea", "latest": {"0.6.4--h9f5acd7_6": "sha256:4ec460373e84be86764ff4a66b90fcaada455f94e2ca1f803cb20c47fa5396d1"}, "tags": {"0.6.4--h9f5acd7_6": "sha256:4ec460373e84be86764ff4a66b90fcaada455f94e2ca1f803cb20c47fa5396d1"}, "docker": "quay.io/biocontainers/mea", "aliases": {"mea": "/usr/local/bin/mea", "mea_eval": "/usr/local/bin/mea_eval", "mea_mix": "/usr/local/bin/mea_mix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mea.
shpc-registry automated BioContainers addition for mea
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mea
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mea:0.6.4--h9f5acd7_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mea/0.6.4--h9f5acd7_6
$ module help quay.io/biocontainers/mea/0.6.4--h9f5acd7_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mea-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mea-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mea-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mea-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mea-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mea-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mea

```bash
$ singularity exec <container> /usr/local/bin/mea
$ podman run --it --rm --entrypoint /usr/local/bin/mea   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mea   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mea_eval

```bash
$ singularity exec <container> /usr/local/bin/mea_eval
$ podman run --it --rm --entrypoint /usr/local/bin/mea_eval   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mea_eval   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mea_mix

```bash
$ singularity exec <container> /usr/local/bin/mea_mix
$ podman run --it --rm --entrypoint /usr/local/bin/mea_mix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mea_mix   -v ${PWD} -w ${PWD} <container> -c " $@"
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