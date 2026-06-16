---
layout: container
name:  "quay.io/biocontainers/fastq-dupaway"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastq-dupaway/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastq-dupaway/container.yaml"
updated_at: "2026-06-16 08:04:46.218943"
latest: "1.5.1--hd63eeec_0"
container_url: "https://biocontainers.pro/tools/fastq-dupaway"
aliases:
 - "fastq-dupaway"
versions:
 - "1.5.1--hd63eeec_0"
description: "singularity registry hpc automated addition for fastq-dupaway"
config: {"url": "https://biocontainers.pro/tools/fastq-dupaway", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for fastq-dupaway", "latest": {"1.5.1--hd63eeec_0": "sha256:a18f069bf72e6a6e9c375224c740d1a0aa8e21b5a5f81384a91ba7d6dcf88dd4"}, "tags": {"1.5.1--hd63eeec_0": "sha256:a18f069bf72e6a6e9c375224c740d1a0aa8e21b5a5f81384a91ba7d6dcf88dd4"}, "docker": "quay.io/biocontainers/fastq-dupaway", "aliases": {"fastq-dupaway": "/usr/local/bin/fastq-dupaway"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastq-dupaway.
singularity registry hpc automated addition for fastq-dupaway
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastq-dupaway
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastq-dupaway:1.5.1--hd63eeec_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastq-dupaway/1.5.1--hd63eeec_0
$ module help quay.io/biocontainers/fastq-dupaway/1.5.1--hd63eeec_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastq-dupaway-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastq-dupaway-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastq-dupaway-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastq-dupaway-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastq-dupaway-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastq-dupaway-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fastq-dupaway

```bash
$ singularity exec <container> /usr/local/bin/fastq-dupaway
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-dupaway   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-dupaway   -v ${PWD} -w ${PWD} <container> -c " $@"
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