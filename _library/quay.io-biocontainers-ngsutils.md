---
layout: container
name:  "quay.io/biocontainers/ngsutils"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ngsutils/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ngsutils/container.yaml"
updated_at: "2022-10-27 01:05:52.865098"
latest: "0.5.9--py27h9801fc8_5"
container_url: "https://biocontainers.pro/tools/ngsutils"
aliases:
 - "bamutils"
 - "bedutils"
 - "fastqutils"
 - "gtfutils"
 - "ngsutils"
 - "swalign"
versions:
 - "0.5.9--py27h9801fc8_5"
description: "shpc-registry automated BioContainers addition for ngsutils"
config: {"url": "https://biocontainers.pro/tools/ngsutils", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ngsutils", "latest": {"0.5.9--py27h9801fc8_5": "sha256:82275edba78ee60556af60995bd56767cb4b54c3cd95d2cb4673362ca94b3376"}, "tags": {"0.5.9--py27h9801fc8_5": "sha256:82275edba78ee60556af60995bd56767cb4b54c3cd95d2cb4673362ca94b3376"}, "docker": "quay.io/biocontainers/ngsutils", "aliases": {"bamutils": "/usr/local/bin/bamutils", "bedutils": "/usr/local/bin/bedutils", "fastqutils": "/usr/local/bin/fastqutils", "gtfutils": "/usr/local/bin/gtfutils", "ngsutils": "/usr/local/bin/ngsutils", "swalign": "/usr/local/bin/swalign"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ngsutils.
shpc-registry automated BioContainers addition for ngsutils
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ngsutils
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ngsutils:0.5.9--py27h9801fc8_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ngsutils/0.5.9--py27h9801fc8_5
$ module help quay.io/biocontainers/ngsutils/0.5.9--py27h9801fc8_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ngsutils-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ngsutils-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ngsutils-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ngsutils-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ngsutils-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ngsutils-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bamutils

```bash
$ singularity exec <container> /usr/local/bin/bamutils
$ podman run --it --rm --entrypoint /usr/local/bin/bamutils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamutils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedutils

```bash
$ singularity exec <container> /usr/local/bin/bedutils
$ podman run --it --rm --entrypoint /usr/local/bin/bedutils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedutils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastqutils

```bash
$ singularity exec <container> /usr/local/bin/fastqutils
$ podman run --it --rm --entrypoint /usr/local/bin/fastqutils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastqutils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtfutils

```bash
$ singularity exec <container> /usr/local/bin/gtfutils
$ podman run --it --rm --entrypoint /usr/local/bin/gtfutils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtfutils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngsutils

```bash
$ singularity exec <container> /usr/local/bin/ngsutils
$ podman run --it --rm --entrypoint /usr/local/bin/ngsutils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngsutils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### swalign

```bash
$ singularity exec <container> /usr/local/bin/swalign
$ podman run --it --rm --entrypoint /usr/local/bin/swalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/swalign   -v ${PWD} -w ${PWD} <container> -c " $@"
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