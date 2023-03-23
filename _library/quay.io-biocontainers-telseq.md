---
layout: container
name:  "quay.io/biocontainers/telseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/telseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/telseq/container.yaml"
updated_at: "2023-03-23 03:02:44.358480"
latest: "0.0.2--ha7703dc_5"
container_url: "https://biocontainers.pro/tools/telseq"
aliases:
 - "telseq"
 - "bamtools"
versions:
 - "0.0.2--ha7703dc_5"
description: "shpc-registry automated BioContainers addition for telseq"
config: {"url": "https://biocontainers.pro/tools/telseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for telseq", "latest": {"0.0.2--ha7703dc_5": "sha256:9a8b8628f4e1d8d80ab890b49764269d70a32de89eead7e8cd517055133d07f0"}, "tags": {"0.0.2--ha7703dc_5": "sha256:9a8b8628f4e1d8d80ab890b49764269d70a32de89eead7e8cd517055133d07f0"}, "docker": "quay.io/biocontainers/telseq", "aliases": {"telseq": "/usr/local/bin/telseq", "bamtools": "/usr/local/bin/bamtools"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/telseq.
shpc-registry automated BioContainers addition for telseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/telseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/telseq:0.0.2--ha7703dc_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/telseq/0.0.2--ha7703dc_5
$ module help quay.io/biocontainers/telseq/0.0.2--ha7703dc_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### telseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### telseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### telseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### telseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### telseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### telseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### telseq

```bash
$ singularity exec <container> /usr/local/bin/telseq
$ podman run --it --rm --entrypoint /usr/local/bin/telseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/telseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamtools

```bash
$ singularity exec <container> /usr/local/bin/bamtools
$ podman run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
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