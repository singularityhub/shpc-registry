---
layout: container
name:  "quay.io/biocontainers/ngs-tools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ngs-tools/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ngs-tools/container.yaml"
updated_at: "2022-10-27 00:41:46.656284"
latest: "1.8.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/ngs-tools"
aliases:
 - "shortuuid"
versions:
 - "1.8.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for ngs-tools"
config: {"url": "https://biocontainers.pro/tools/ngs-tools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ngs-tools", "latest": {"1.8.1--pyhdfd78af_0": "sha256:8b2ec1c38f3a01a4792702492ea405b4c85310a4b146ee4fb1bae2eabbdfd750"}, "tags": {"1.8.1--pyhdfd78af_0": "sha256:8b2ec1c38f3a01a4792702492ea405b4c85310a4b146ee4fb1bae2eabbdfd750"}, "docker": "quay.io/biocontainers/ngs-tools", "aliases": {"shortuuid": "/usr/local/bin/shortuuid"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ngs-tools.
shpc-registry automated BioContainers addition for ngs-tools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ngs-tools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ngs-tools:1.8.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ngs-tools/1.8.1--pyhdfd78af_0
$ module help quay.io/biocontainers/ngs-tools/1.8.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ngs-tools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ngs-tools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ngs-tools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ngs-tools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ngs-tools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ngs-tools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### shortuuid

```bash
$ singularity exec <container> /usr/local/bin/shortuuid
$ podman run --it --rm --entrypoint /usr/local/bin/shortuuid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shortuuid   -v ${PWD} -w ${PWD} <container> -c " $@"
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