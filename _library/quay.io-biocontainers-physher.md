---
layout: container
name:  "quay.io/biocontainers/physher"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/physher/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/physher/container.yaml"
updated_at: "2025-11-12 03:19:32.022213"
latest: "2.0.1--h4656aac_3"
container_url: "https://biocontainers.pro/tools/physher"
aliases:
 - "physher"
versions:
 - "2.0.0--h8cec121_0"
 - "2.0.1--h8cec121_1"
 - "2.0.1--h4656aac_3"
description: "singularity registry hpc automated addition for physher"
config: {"url": "https://biocontainers.pro/tools/physher", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for physher", "latest": {"2.0.1--h4656aac_3": "sha256:a27c6b94573f9e68be607d4aea9666224d5d6d15486467c97c3cd45297e47fc3"}, "tags": {"2.0.0--h8cec121_0": "sha256:10bcf7640dfed877c2172e0c2657e52bc3b4291243555b58afc1de7fa6311c26", "2.0.1--h8cec121_1": "sha256:afae2d66cf4b0e3ec47a1859896176b6216bc5bddffed1902f1d2f45166b1013", "2.0.1--h4656aac_3": "sha256:a27c6b94573f9e68be607d4aea9666224d5d6d15486467c97c3cd45297e47fc3"}, "docker": "quay.io/biocontainers/physher", "aliases": {"physher": "/usr/local/bin/physher"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/physher.
singularity registry hpc automated addition for physher
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/physher
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/physher:2.0.1--h4656aac_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/physher/2.0.1--h4656aac_3
$ module help quay.io/biocontainers/physher/2.0.1--h4656aac_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### physher-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### physher-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### physher-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### physher-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### physher-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### physher-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### physher

```bash
$ singularity exec <container> /usr/local/bin/physher
$ podman run --it --rm --entrypoint /usr/local/bin/physher   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/physher   -v ${PWD} -w ${PWD} <container> -c " $@"
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