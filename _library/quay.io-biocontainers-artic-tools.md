---
layout: container
name:  "quay.io/biocontainers/artic-tools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/artic-tools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/artic-tools/container.yaml"
updated_at: "2023-03-15 03:17:48.856255"
latest: "0.3.1--hb777114_3"
container_url: "https://biocontainers.pro/tools/artic-tools"
aliases:
 - "artic-tools"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.3.1--hb777114_3"
description: "shpc-registry automated BioContainers addition for artic-tools"
config: {"url": "https://biocontainers.pro/tools/artic-tools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for artic-tools", "latest": {"0.3.1--hb777114_3": "sha256:553bc3014cebef6e8ba240f7cd4cb246c91bd4fb36cc37d2f7ea46efd5c994fa"}, "tags": {"0.3.1--hb777114_3": "sha256:553bc3014cebef6e8ba240f7cd4cb246c91bd4fb36cc37d2f7ea46efd5c994fa"}, "docker": "quay.io/biocontainers/artic-tools", "aliases": {"artic-tools": "/usr/local/bin/artic-tools", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/artic-tools.
shpc-registry automated BioContainers addition for artic-tools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/artic-tools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/artic-tools:0.3.1--hb777114_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/artic-tools/0.3.1--hb777114_3
$ module help quay.io/biocontainers/artic-tools/0.3.1--hb777114_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### artic-tools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### artic-tools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### artic-tools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### artic-tools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### artic-tools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### artic-tools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### artic-tools

```bash
$ singularity exec <container> /usr/local/bin/artic-tools
$ podman run --it --rm --entrypoint /usr/local/bin/artic-tools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/artic-tools   -v ${PWD} -w ${PWD} <container> -c " $@"
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