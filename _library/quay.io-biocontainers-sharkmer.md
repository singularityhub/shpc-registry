---
layout: container
name:  "quay.io/biocontainers/sharkmer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sharkmer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sharkmer/container.yaml"
updated_at: "2026-03-26 04:40:46.806016"
latest: "1.0.1--h4349ce8_1"
container_url: "https://biocontainers.pro/tools/sharkmer"
aliases:
 - "sharkmer"
versions:
 - "1.0.1--h4349ce8_0"
 - "1.0.1--h4349ce8_1"
description: "singularity registry hpc automated addition for sharkmer"
config: {"url": "https://biocontainers.pro/tools/sharkmer", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for sharkmer", "latest": {"1.0.1--h4349ce8_1": "sha256:744b4570fe61fc18393e8f82cd7383cec63149a80477647f2087f464baf752b2"}, "tags": {"1.0.1--h4349ce8_0": "sha256:1e969bb0e62b66dcf71b97db150e8b4f03511d25f9c63ae854ae219eafb67b40", "1.0.1--h4349ce8_1": "sha256:744b4570fe61fc18393e8f82cd7383cec63149a80477647f2087f464baf752b2"}, "docker": "quay.io/biocontainers/sharkmer", "aliases": {"sharkmer": "/usr/local/bin/sharkmer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sharkmer.
singularity registry hpc automated addition for sharkmer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sharkmer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sharkmer:1.0.1--h4349ce8_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sharkmer/1.0.1--h4349ce8_1
$ module help quay.io/biocontainers/sharkmer/1.0.1--h4349ce8_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sharkmer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sharkmer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sharkmer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sharkmer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sharkmer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sharkmer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sharkmer

```bash
$ singularity exec <container> /usr/local/bin/sharkmer
$ podman run --it --rm --entrypoint /usr/local/bin/sharkmer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sharkmer   -v ${PWD} -w ${PWD} <container> -c " $@"
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