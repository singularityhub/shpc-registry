---
layout: container
name:  "quay.io/biocontainers/winnowmap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/winnowmap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/winnowmap/container.yaml"
updated_at: "2024-07-15 03:00:22.397479"
latest: "2.03--h43eeafb_2"
container_url: "https://biocontainers.pro/tools/winnowmap"
aliases:
 - "meryl-analyze"
 - "meryl-import"
 - "meryl-lookup"
 - "meryl-simple"
 - "winnowmap"
 - "meryl"
versions:
 - "2.03--h5b5514e_1"
 - "2.03--h43eeafb_2"
description: "shpc-registry automated BioContainers addition for winnowmap"
config: {"url": "https://biocontainers.pro/tools/winnowmap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for winnowmap", "latest": {"2.03--h43eeafb_2": "sha256:7777b40ec169259b9a4f2f144d1f48111601a18a41a00aef3bc6a93a3ac08243"}, "tags": {"2.03--h5b5514e_1": "sha256:e38b81b7d387ce4f38b290c83ad06a84f26331c4e9decfd503b8ddbf4a931aa9", "2.03--h43eeafb_2": "sha256:7777b40ec169259b9a4f2f144d1f48111601a18a41a00aef3bc6a93a3ac08243"}, "docker": "quay.io/biocontainers/winnowmap", "aliases": {"meryl-analyze": "/usr/local/bin/meryl-analyze", "meryl-import": "/usr/local/bin/meryl-import", "meryl-lookup": "/usr/local/bin/meryl-lookup", "meryl-simple": "/usr/local/bin/meryl-simple", "winnowmap": "/usr/local/bin/winnowmap", "meryl": "/usr/local/bin/meryl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/winnowmap.
shpc-registry automated BioContainers addition for winnowmap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/winnowmap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/winnowmap:2.03--h43eeafb_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/winnowmap/2.03--h43eeafb_2
$ module help quay.io/biocontainers/winnowmap/2.03--h43eeafb_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### winnowmap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### winnowmap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### winnowmap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### winnowmap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### winnowmap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### winnowmap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### meryl-analyze

```bash
$ singularity exec <container> /usr/local/bin/meryl-analyze
$ podman run --it --rm --entrypoint /usr/local/bin/meryl-analyze   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/meryl-analyze   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### meryl-import

```bash
$ singularity exec <container> /usr/local/bin/meryl-import
$ podman run --it --rm --entrypoint /usr/local/bin/meryl-import   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/meryl-import   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### meryl-lookup

```bash
$ singularity exec <container> /usr/local/bin/meryl-lookup
$ podman run --it --rm --entrypoint /usr/local/bin/meryl-lookup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/meryl-lookup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### meryl-simple

```bash
$ singularity exec <container> /usr/local/bin/meryl-simple
$ podman run --it --rm --entrypoint /usr/local/bin/meryl-simple   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/meryl-simple   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### winnowmap

```bash
$ singularity exec <container> /usr/local/bin/winnowmap
$ podman run --it --rm --entrypoint /usr/local/bin/winnowmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/winnowmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### meryl

```bash
$ singularity exec <container> /usr/local/bin/meryl
$ podman run --it --rm --entrypoint /usr/local/bin/meryl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/meryl   -v ${PWD} -w ${PWD} <container> -c " $@"
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