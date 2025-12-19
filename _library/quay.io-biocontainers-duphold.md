---
layout: container
name:  "quay.io/biocontainers/duphold"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/duphold/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/duphold/container.yaml"
updated_at: "2025-12-19 03:52:29.888760"
latest: "0.2.1--h031d066_4"
container_url: "https://biocontainers.pro/tools/duphold"
aliases:
 - "duphold"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.2.1--hec16e2b_3"
 - "0.2.1--h031d066_4"
description: "shpc-registry automated BioContainers addition for duphold"
config: {"url": "https://biocontainers.pro/tools/duphold", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for duphold", "latest": {"0.2.1--h031d066_4": "sha256:c87ba36d6c06c0b88283425e1914dba45fef68a8a06ea4792d99819706d2e5f0"}, "tags": {"0.2.1--hec16e2b_3": "sha256:b7b1e1ae83345ba8528d54fba19127aab0e9fda166e3d7a7c19da6d951d99237", "0.2.1--h031d066_4": "sha256:c87ba36d6c06c0b88283425e1914dba45fef68a8a06ea4792d99819706d2e5f0"}, "docker": "quay.io/biocontainers/duphold", "aliases": {"duphold": "/usr/local/bin/duphold", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/duphold.
shpc-registry automated BioContainers addition for duphold
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/duphold
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/duphold:0.2.1--h031d066_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/duphold/0.2.1--h031d066_4
$ module help quay.io/biocontainers/duphold/0.2.1--h031d066_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### duphold-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### duphold-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### duphold-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### duphold-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### duphold-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### duphold-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### duphold

```bash
$ singularity exec <container> /usr/local/bin/duphold
$ podman run --it --rm --entrypoint /usr/local/bin/duphold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/duphold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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