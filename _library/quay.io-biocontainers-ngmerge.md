---
layout: container
name:  "quay.io/biocontainers/ngmerge"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ngmerge/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ngmerge/container.yaml"
updated_at: "2024-12-19 03:31:49.433870"
latest: "0.3--ha92aebf_1"
container_url: "https://biocontainers.pro/tools/ngmerge"
aliases:
 - "NGmerge"
versions:
 - "0.3--ha92aebf_1"
description: "shpc-registry automated BioContainers addition for ngmerge"
config: {"url": "https://biocontainers.pro/tools/ngmerge", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ngmerge", "latest": {"0.3--ha92aebf_1": "sha256:d4adad96fbfba3bedf655f684a0070a2bff5b9ba860c782ac7073bcc029a6414"}, "tags": {"0.3--ha92aebf_1": "sha256:d4adad96fbfba3bedf655f684a0070a2bff5b9ba860c782ac7073bcc029a6414"}, "docker": "quay.io/biocontainers/ngmerge", "aliases": {"NGmerge": "/usr/local/bin/NGmerge"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ngmerge.
shpc-registry automated BioContainers addition for ngmerge
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ngmerge
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ngmerge:0.3--ha92aebf_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ngmerge/0.3--ha92aebf_1
$ module help quay.io/biocontainers/ngmerge/0.3--ha92aebf_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ngmerge-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ngmerge-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ngmerge-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ngmerge-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ngmerge-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ngmerge-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### NGmerge

```bash
$ singularity exec <container> /usr/local/bin/NGmerge
$ podman run --it --rm --entrypoint /usr/local/bin/NGmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/NGmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
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