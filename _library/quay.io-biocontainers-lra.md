---
layout: container
name:  "quay.io/biocontainers/lra"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lra/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/lra/container.yaml"
updated_at: "2022-11-09 23:38:26.437670"
latest: "1.3.4--hea94271_1"
container_url: "https://biocontainers.pro/tools/lra"
aliases:
 - "lra"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "1.3.4--hea94271_1"
description: "shpc-registry automated BioContainers addition for lra"
config: {"url": "https://biocontainers.pro/tools/lra", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for lra", "latest": {"1.3.4--hea94271_1": "sha256:daa1b6cc3ffdc267b73c5da2671b8907ffe3723281fd572964ba5ad3bb5927b3"}, "tags": {"1.3.4--hea94271_1": "sha256:daa1b6cc3ffdc267b73c5da2671b8907ffe3723281fd572964ba5ad3bb5927b3"}, "docker": "quay.io/biocontainers/lra", "aliases": {"lra": "/usr/local/bin/lra", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lra.
shpc-registry automated BioContainers addition for lra
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lra
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lra:1.3.4--hea94271_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lra/1.3.4--hea94271_1
$ module help quay.io/biocontainers/lra/1.3.4--hea94271_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lra-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lra-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lra-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lra-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lra-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lra-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### lra

```bash
$ singularity exec <container> /usr/local/bin/lra
$ podman run --it --rm --entrypoint /usr/local/bin/lra   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lra   -v ${PWD} -w ${PWD} <container> -c " $@"
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