---
layout: container
name:  "quay.io/biocontainers/kalign3"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kalign3/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kalign3/container.yaml"
updated_at: "2024-05-06 18:54:13.698131"
latest: "3.4.0--hdbdd923_0"
container_url: "https://biocontainers.pro/tools/kalign3"
aliases:
 - "kalign"
 - "kchaos"
versions:
 - "3.3.2--hec16e2b_0"
 - "3.3.2--h031d066_2"
 - "3.3.5--hdbdd923_0"
 - "3.4.0--hdbdd923_0"
description: "shpc-registry automated BioContainers addition for kalign3"
config: {"url": "https://biocontainers.pro/tools/kalign3", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kalign3", "latest": {"3.4.0--hdbdd923_0": "sha256:7ec9af4743a4c59b8a61b2c3e006c51ea94d3ed6cdf4183ad3816bb7f9a771ed"}, "tags": {"3.3.2--hec16e2b_0": "sha256:23b624001b98d1c7374b7c77303b3dadef92a46e5a986a3c5f94ec525992fb25", "3.3.2--h031d066_2": "sha256:51693074f7dca989620607ae3578854830880e2971fa34feba8537b71d471b08", "3.3.5--hdbdd923_0": "sha256:735e4bb1f5310f2a314979951ad9f8ffec7f5bb764f8b5b50160940310f6a325", "3.4.0--hdbdd923_0": "sha256:7ec9af4743a4c59b8a61b2c3e006c51ea94d3ed6cdf4183ad3816bb7f9a771ed"}, "docker": "quay.io/biocontainers/kalign3", "aliases": {"kalign": "/usr/local/bin/kalign", "kchaos": "/usr/local/bin/kchaos"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kalign3.
shpc-registry automated BioContainers addition for kalign3
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kalign3
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kalign3:3.4.0--hdbdd923_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kalign3/3.4.0--hdbdd923_0
$ module help quay.io/biocontainers/kalign3/3.4.0--hdbdd923_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kalign3-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kalign3-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kalign3-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kalign3-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kalign3-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kalign3-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### kalign

```bash
$ singularity exec <container> /usr/local/bin/kalign
$ podman run --it --rm --entrypoint /usr/local/bin/kalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kchaos

```bash
$ singularity exec <container> /usr/local/bin/kchaos
$ podman run --it --rm --entrypoint /usr/local/bin/kchaos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kchaos   -v ${PWD} -w ${PWD} <container> -c " $@"
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