---
layout: container
name:  "quay.io/biocontainers/delve-bio"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/delve-bio/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/delve-bio/container.yaml"
updated_at: "2025-10-17 03:33:07.131328"
latest: "0.2.0--h4349ce8_0"
container_url: "https://biocontainers.pro/tools/delve-bio"
aliases:
 - "delve"
versions:
 - "0.1.0--h4349ce8_0"
 - "0.2.0--h4349ce8_0"
description: "singularity registry hpc automated addition for delve-bio"
config: {"url": "https://biocontainers.pro/tools/delve-bio", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for delve-bio", "latest": {"0.2.0--h4349ce8_0": "sha256:dd9a89d2eba3c04b9f765641368a87377638a70c6d37f7ca4eef1dea39289442"}, "tags": {"0.1.0--h4349ce8_0": "sha256:1ac2a421f83ee9487c2888e75ea09bab42170c7e358a50c4506df03f53e01fbc", "0.2.0--h4349ce8_0": "sha256:dd9a89d2eba3c04b9f765641368a87377638a70c6d37f7ca4eef1dea39289442"}, "docker": "quay.io/biocontainers/delve-bio", "aliases": {"delve": "/usr/local/bin/delve"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/delve-bio.
singularity registry hpc automated addition for delve-bio
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/delve-bio
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/delve-bio:0.2.0--h4349ce8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/delve-bio/0.2.0--h4349ce8_0
$ module help quay.io/biocontainers/delve-bio/0.2.0--h4349ce8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### delve-bio-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### delve-bio-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### delve-bio-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### delve-bio-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### delve-bio-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### delve-bio-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### delve

```bash
$ singularity exec <container> /usr/local/bin/delve
$ podman run --it --rm --entrypoint /usr/local/bin/delve   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delve   -v ${PWD} -w ${PWD} <container> -c " $@"
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