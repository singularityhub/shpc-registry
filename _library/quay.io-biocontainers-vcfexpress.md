---
layout: container
name:  "quay.io/biocontainers/vcfexpress"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vcfexpress/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vcfexpress/container.yaml"
updated_at: "2025-08-08 04:34:21.988869"
latest: "0.3.4--h3ab6199_0"
container_url: "https://biocontainers.pro/tools/vcfexpress"
aliases:
 - "vcfexpress"
versions:
 - "0.3.4--h3ab6199_0"
description: "singularity registry hpc automated addition for vcfexpress"
config: {"url": "https://biocontainers.pro/tools/vcfexpress", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for vcfexpress", "latest": {"0.3.4--h3ab6199_0": "sha256:90f99a8fce4d3b5e8ab6c106edc11b19080ea2443ef26e14383b8b07d7c1bff2"}, "tags": {"0.3.4--h3ab6199_0": "sha256:90f99a8fce4d3b5e8ab6c106edc11b19080ea2443ef26e14383b8b07d7c1bff2"}, "docker": "quay.io/biocontainers/vcfexpress", "aliases": {"vcfexpress": "/usr/local/bin/vcfexpress"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vcfexpress.
singularity registry hpc automated addition for vcfexpress
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vcfexpress
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vcfexpress:0.3.4--h3ab6199_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vcfexpress/0.3.4--h3ab6199_0
$ module help quay.io/biocontainers/vcfexpress/0.3.4--h3ab6199_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vcfexpress-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vcfexpress-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vcfexpress-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vcfexpress-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vcfexpress-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vcfexpress-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### vcfexpress

```bash
$ singularity exec <container> /usr/local/bin/vcfexpress
$ podman run --it --rm --entrypoint /usr/local/bin/vcfexpress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfexpress   -v ${PWD} -w ${PWD} <container> -c " $@"
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