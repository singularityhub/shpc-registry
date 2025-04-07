---
layout: container
name:  "quay.io/biocontainers/phynder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/phynder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/phynder/container.yaml"
updated_at: "2025-04-07 03:35:45.261957"
latest: "1.0--h566b1c6_4"
container_url: "https://biocontainers.pro/tools/phynder"
aliases:
 - "annot-tsv"
 - "phynder"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "1.0--h81da01d_0"
 - "1.0--h566b1c6_4"
description: "singularity registry hpc automated addition for phynder"
config: {"url": "https://biocontainers.pro/tools/phynder", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for phynder", "latest": {"1.0--h566b1c6_4": "sha256:874592a924e89a7ac96d853e631e1824d07d41d7c216529de8645b3b01e2bb28"}, "tags": {"1.0--h81da01d_0": "sha256:7a6262a21b793ad11c3012a6139b7bf978e2331fff4b7a6a7ee40abb7740533e", "1.0--h566b1c6_4": "sha256:874592a924e89a7ac96d853e631e1824d07d41d7c216529de8645b3b01e2bb28"}, "docker": "quay.io/biocontainers/phynder", "aliases": {"annot-tsv": "/usr/local/bin/annot-tsv", "phynder": "/usr/local/bin/phynder", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/phynder.
singularity registry hpc automated addition for phynder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/phynder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/phynder:1.0--h566b1c6_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/phynder/1.0--h566b1c6_4
$ module help quay.io/biocontainers/phynder/1.0--h566b1c6_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### phynder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### phynder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### phynder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### phynder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### phynder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### phynder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phynder

```bash
$ singularity exec <container> /usr/local/bin/phynder
$ podman run --it --rm --entrypoint /usr/local/bin/phynder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phynder   -v ${PWD} -w ${PWD} <container> -c " $@"
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