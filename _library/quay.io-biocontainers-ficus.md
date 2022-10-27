---
layout: container
name:  "quay.io/biocontainers/ficus"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ficus/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ficus/container.yaml"
updated_at: "2022-10-27 01:03:00.870378"
latest: "0.5--pyh864c0ab_4"
container_url: "https://biocontainers.pro/tools/ficus"

versions:
 - "0.5--pyh864c0ab_4"
description: "shpc-registry automated BioContainers addition for ficus"
config: {"url": "https://biocontainers.pro/tools/ficus", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ficus", "latest": {"0.5--pyh864c0ab_4": "sha256:27f7965e9db335fcc583b7e1cb7b3b51cd3eb011dece075fc2486efb5fe334c6"}, "tags": {"0.5--pyh864c0ab_4": "sha256:27f7965e9db335fcc583b7e1cb7b3b51cd3eb011dece075fc2486efb5fe334c6"}, "docker": "quay.io/biocontainers/ficus"}
---

This module is a singularity container wrapper for quay.io/biocontainers/ficus.
shpc-registry automated BioContainers addition for ficus
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ficus
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ficus:0.5--pyh864c0ab_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ficus/0.5--pyh864c0ab_4
$ module help quay.io/biocontainers/ficus/0.5--pyh864c0ab_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ficus-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ficus-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ficus-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ficus-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ficus-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ficus-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### ficus

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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