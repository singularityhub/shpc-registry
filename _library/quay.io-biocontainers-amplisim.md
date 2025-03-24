---
layout: container
name:  "quay.io/biocontainers/amplisim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/amplisim/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/amplisim/container.yaml"
updated_at: "2025-03-24 03:32:03.895290"
latest: "0.2.1--h69ac913_3"
container_url: "https://biocontainers.pro/tools/amplisim"
aliases:
 - "amplisim"
versions:
 - "0.2.1--h77de753_0"
 - "0.2.1--h3e2e0a8_1"
 - "0.2.1--h69ac913_3"
description: "singularity registry hpc automated addition for amplisim"
config: {"url": "https://biocontainers.pro/tools/amplisim", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for amplisim", "latest": {"0.2.1--h69ac913_3": "sha256:48bd07ee679e4a4b2e0ec01bef3c9d1af8978db9b4b2a8a4b97b1b6702a3b609"}, "tags": {"0.2.1--h77de753_0": "sha256:f598183be49b0f5787c8df70a06585acb551f7582a28d203822a502311b46ba7", "0.2.1--h3e2e0a8_1": "sha256:be7360f5c890f595dd88bad58e2d95a0123cd8bfb4595c24830bba626fcbadd6", "0.2.1--h69ac913_3": "sha256:48bd07ee679e4a4b2e0ec01bef3c9d1af8978db9b4b2a8a4b97b1b6702a3b609"}, "docker": "quay.io/biocontainers/amplisim", "aliases": {"amplisim": "/usr/local/bin/amplisim"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/amplisim.
singularity registry hpc automated addition for amplisim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/amplisim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/amplisim:0.2.1--h69ac913_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/amplisim/0.2.1--h69ac913_3
$ module help quay.io/biocontainers/amplisim/0.2.1--h69ac913_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### amplisim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### amplisim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### amplisim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### amplisim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### amplisim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### amplisim-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### amplisim

```bash
$ singularity exec <container> /usr/local/bin/amplisim
$ podman run --it --rm --entrypoint /usr/local/bin/amplisim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amplisim   -v ${PWD} -w ${PWD} <container> -c " $@"
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