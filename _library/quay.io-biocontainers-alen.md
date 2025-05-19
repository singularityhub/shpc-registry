---
layout: container
name:  "quay.io/biocontainers/alen"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/alen/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/alen/container.yaml"
updated_at: "2025-05-19 03:45:01.628130"
latest: "0.3.1--h4349ce8_0"
container_url: "https://biocontainers.pro/tools/alen"
aliases:
 - "alen"
versions:
 - "0.3.1--h4349ce8_0"
description: "singularity registry hpc automated addition for alen"
config: {"url": "https://biocontainers.pro/tools/alen", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for alen", "latest": {"0.3.1--h4349ce8_0": "sha256:cfbf29e4baa7b723f45ea2ef797cb6d9714fd6a89283a80d6e150e93e5eb2e79"}, "tags": {"0.3.1--h4349ce8_0": "sha256:cfbf29e4baa7b723f45ea2ef797cb6d9714fd6a89283a80d6e150e93e5eb2e79"}, "docker": "quay.io/biocontainers/alen", "aliases": {"alen": "/usr/local/bin/alen"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/alen.
singularity registry hpc automated addition for alen
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/alen
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/alen:0.3.1--h4349ce8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/alen/0.3.1--h4349ce8_0
$ module help quay.io/biocontainers/alen/0.3.1--h4349ce8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### alen-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### alen-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### alen-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### alen-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### alen-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### alen-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### alen

```bash
$ singularity exec <container> /usr/local/bin/alen
$ podman run --it --rm --entrypoint /usr/local/bin/alen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alen   -v ${PWD} -w ${PWD} <container> -c " $@"
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