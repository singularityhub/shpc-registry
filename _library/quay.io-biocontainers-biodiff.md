---
layout: container
name:  "quay.io/biocontainers/biodiff"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biodiff/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/biodiff/container.yaml"
updated_at: "2023-03-07 03:42:22.837905"
latest: "0.2.2--hec16e2b_4"
container_url: "https://biocontainers.pro/tools/biodiff"
aliases:
 - "biodiff"
 - "udiff2vcf"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.2.2--hec16e2b_4"
description: "shpc-registry automated BioContainers addition for biodiff"
config: {"url": "https://biocontainers.pro/tools/biodiff", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for biodiff", "latest": {"0.2.2--hec16e2b_4": "sha256:4a7e24a29c6514cfa76032b92c7e9f3a41a05b323768419443c1f4ae5f65aef4"}, "tags": {"0.2.2--hec16e2b_4": "sha256:4a7e24a29c6514cfa76032b92c7e9f3a41a05b323768419443c1f4ae5f65aef4"}, "docker": "quay.io/biocontainers/biodiff", "aliases": {"biodiff": "/usr/local/bin/biodiff", "udiff2vcf": "/usr/local/bin/udiff2vcf", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/biodiff.
shpc-registry automated BioContainers addition for biodiff
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biodiff
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biodiff:0.2.2--hec16e2b_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biodiff/0.2.2--hec16e2b_4
$ module help quay.io/biocontainers/biodiff/0.2.2--hec16e2b_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### biodiff-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### biodiff-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### biodiff-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### biodiff-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### biodiff-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biodiff-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### biodiff

```bash
$ singularity exec <container> /usr/local/bin/biodiff
$ podman run --it --rm --entrypoint /usr/local/bin/biodiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/biodiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### udiff2vcf

```bash
$ singularity exec <container> /usr/local/bin/udiff2vcf
$ podman run --it --rm --entrypoint /usr/local/bin/udiff2vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/udiff2vcf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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