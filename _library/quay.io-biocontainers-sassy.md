---
layout: container
name:  "quay.io/biocontainers/sassy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sassy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sassy/container.yaml"
updated_at: "2026-01-19 04:37:14.305592"
latest: "0.1.8--h4349ce8_0"
container_url: "https://biocontainers.pro/tools/sassy"
aliases:
 - "sassy"
versions:
 - "0.1.8--h4349ce8_0"
description: "singularity registry hpc automated addition for sassy"
config: {"url": "https://biocontainers.pro/tools/sassy", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for sassy", "latest": {"0.1.8--h4349ce8_0": "sha256:fc0d405bac26d99f5256ca822af4e085285fa68d8b2e873fd6562058d865aeab"}, "tags": {"0.1.8--h4349ce8_0": "sha256:fc0d405bac26d99f5256ca822af4e085285fa68d8b2e873fd6562058d865aeab"}, "docker": "quay.io/biocontainers/sassy", "aliases": {"sassy": "/usr/local/bin/sassy"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sassy.
singularity registry hpc automated addition for sassy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sassy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sassy:0.1.8--h4349ce8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sassy/0.1.8--h4349ce8_0
$ module help quay.io/biocontainers/sassy/0.1.8--h4349ce8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sassy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sassy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sassy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sassy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sassy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sassy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sassy

```bash
$ singularity exec <container> /usr/local/bin/sassy
$ podman run --it --rm --entrypoint /usr/local/bin/sassy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sassy   -v ${PWD} -w ${PWD} <container> -c " $@"
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