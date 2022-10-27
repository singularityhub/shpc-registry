---
layout: container
name:  "quay.io/biocontainers/transit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/transit/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/transit/container.yaml"
updated_at: "2022-10-27 00:28:43.788235"
latest: "3.2.3--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/transit"
aliases:
 - "tpp"
 - "transit"
versions:
 - "3.2.3--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for transit"
config: {"url": "https://biocontainers.pro/tools/transit", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for transit", "latest": {"3.2.3--pyhdfd78af_0": "sha256:423dd80c1ec97b4aa09a4f9c50bf7e038f6ad069e5a64fd51971f55168f6ee0a"}, "tags": {"3.2.3--pyhdfd78af_0": "sha256:423dd80c1ec97b4aa09a4f9c50bf7e038f6ad069e5a64fd51971f55168f6ee0a"}, "docker": "quay.io/biocontainers/transit", "aliases": {"tpp": "/usr/local/bin/tpp", "transit": "/usr/local/bin/transit"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/transit.
shpc-registry automated BioContainers addition for transit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/transit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/transit:3.2.3--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/transit/3.2.3--pyhdfd78af_0
$ module help quay.io/biocontainers/transit/3.2.3--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### transit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### transit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### transit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### transit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### transit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### transit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tpp

```bash
$ singularity exec <container> /usr/local/bin/tpp
$ podman run --it --rm --entrypoint /usr/local/bin/tpp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tpp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transit

```bash
$ singularity exec <container> /usr/local/bin/transit
$ podman run --it --rm --entrypoint /usr/local/bin/transit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transit   -v ${PWD} -w ${PWD} <container> -c " $@"
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