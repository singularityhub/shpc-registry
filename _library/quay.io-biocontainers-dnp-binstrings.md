---
layout: container
name:  "quay.io/biocontainers/dnp-binstrings"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dnp-binstrings/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dnp-binstrings/container.yaml"
updated_at: "2022-11-21 13:08:02.420978"
latest: "1.0--hf1761c0_3"
container_url: "https://biocontainers.pro/tools/dnp-binstrings"
aliases:
 - "dnp-binstrings"
versions:
 - "1.0--hf1761c0_3"
description: "shpc-registry automated BioContainers addition for dnp-binstrings"
config: {"url": "https://biocontainers.pro/tools/dnp-binstrings", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dnp-binstrings", "latest": {"1.0--hf1761c0_3": "sha256:6639e192eb293a40e7b38d18900a3e41d5900003231e5b02ef34db5b384fbfaa"}, "tags": {"1.0--hf1761c0_3": "sha256:6639e192eb293a40e7b38d18900a3e41d5900003231e5b02ef34db5b384fbfaa"}, "docker": "quay.io/biocontainers/dnp-binstrings", "aliases": {"dnp-binstrings": "/usr/local/bin/dnp-binstrings"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dnp-binstrings.
shpc-registry automated BioContainers addition for dnp-binstrings
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dnp-binstrings
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dnp-binstrings:1.0--hf1761c0_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dnp-binstrings/1.0--hf1761c0_3
$ module help quay.io/biocontainers/dnp-binstrings/1.0--hf1761c0_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dnp-binstrings-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dnp-binstrings-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dnp-binstrings-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dnp-binstrings-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dnp-binstrings-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dnp-binstrings-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dnp-binstrings

```bash
$ singularity exec <container> /usr/local/bin/dnp-binstrings
$ podman run --it --rm --entrypoint /usr/local/bin/dnp-binstrings   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnp-binstrings   -v ${PWD} -w ${PWD} <container> -c " $@"
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