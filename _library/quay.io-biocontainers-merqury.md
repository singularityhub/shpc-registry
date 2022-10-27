---
layout: container
name:  "quay.io/biocontainers/merqury"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/merqury/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/merqury/container.yaml"
updated_at: "2022-10-27 00:51:13.577316"
latest: "v1.0--0"
container_url: "https://biocontainers.pro/tools/merqury"
aliases:
 - ".merqury-post-link.sh"
 - "igvtools"
 - "merqury.sh"
 - "meryl-import"
 - "meryl-lookup"
 - "sequence"
versions:
 - "v1.0--0"
description: "shpc-registry automated BioContainers addition for merqury"
config: {"url": "https://biocontainers.pro/tools/merqury", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for merqury", "latest": {"v1.0--0": "sha256:9a83df64687dcbd1b03a23882503669b0620ee63f8febe734eeb56d7ddf23210"}, "tags": {"v1.0--0": "sha256:9a83df64687dcbd1b03a23882503669b0620ee63f8febe734eeb56d7ddf23210"}, "docker": "quay.io/biocontainers/merqury", "aliases": {".merqury-post-link.sh": "/usr/local/bin/.merqury-post-link.sh", "igvtools": "/usr/local/bin/igvtools", "merqury.sh": "/usr/local/bin/merqury.sh", "meryl-import": "/usr/local/bin/meryl-import", "meryl-lookup": "/usr/local/bin/meryl-lookup", "sequence": "/usr/local/bin/sequence"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/merqury.
shpc-registry automated BioContainers addition for merqury
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/merqury
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/merqury:v1.0--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/merqury/v1.0--0
$ module help quay.io/biocontainers/merqury/v1.0--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### merqury-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### merqury-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### merqury-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### merqury-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### merqury-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### merqury-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .merqury-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.merqury-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.merqury-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.merqury-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### igvtools

```bash
$ singularity exec <container> /usr/local/bin/igvtools
$ podman run --it --rm --entrypoint /usr/local/bin/igvtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igvtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merqury.sh

```bash
$ singularity exec <container> /usr/local/bin/merqury.sh
$ podman run --it --rm --entrypoint /usr/local/bin/merqury.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merqury.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### sequence

```bash
$ singularity exec <container> /usr/local/bin/sequence
$ podman run --it --rm --entrypoint /usr/local/bin/sequence   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sequence   -v ${PWD} -w ${PWD} <container> -c " $@"
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