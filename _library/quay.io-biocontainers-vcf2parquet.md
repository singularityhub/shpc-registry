---
layout: container
name:  "quay.io/biocontainers/vcf2parquet"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vcf2parquet/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vcf2parquet/container.yaml"
updated_at: "2023-02-27 03:20:09.465459"
latest: "0.3.1--hc308579_0"
container_url: "https://biocontainers.pro/tools/vcf2parquet"
aliases:
 - "vcf2parquet"
versions:
 - "0.3.1--hc308579_0"
description: "singularity registry hpc automated addition for vcf2parquet"
config: {"url": "https://biocontainers.pro/tools/vcf2parquet", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for vcf2parquet", "latest": {"0.3.1--hc308579_0": "sha256:81ac4b2a8ad072ef8a537e192e9c170c70b9e12212e28a33cb353e40427361d1"}, "tags": {"0.3.1--hc308579_0": "sha256:81ac4b2a8ad072ef8a537e192e9c170c70b9e12212e28a33cb353e40427361d1"}, "docker": "quay.io/biocontainers/vcf2parquet", "aliases": {"vcf2parquet": "/usr/local/bin/vcf2parquet"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vcf2parquet.
singularity registry hpc automated addition for vcf2parquet
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vcf2parquet
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vcf2parquet:0.3.1--hc308579_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vcf2parquet/0.3.1--hc308579_0
$ module help quay.io/biocontainers/vcf2parquet/0.3.1--hc308579_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vcf2parquet-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vcf2parquet-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vcf2parquet-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vcf2parquet-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vcf2parquet-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vcf2parquet-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### vcf2parquet

```bash
$ singularity exec <container> /usr/local/bin/vcf2parquet
$ podman run --it --rm --entrypoint /usr/local/bin/vcf2parquet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcf2parquet   -v ${PWD} -w ${PWD} <container> -c " $@"
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