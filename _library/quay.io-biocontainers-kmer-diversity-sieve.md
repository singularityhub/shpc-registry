---
layout: container
name:  "quay.io/biocontainers/kmer-diversity-sieve"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kmer-diversity-sieve/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kmer-diversity-sieve/container.yaml"
updated_at: "2026-11-06 09:11:06.407754"
latest: "0.1.0--hab16a5f_0"
container_url: "https://biocontainers.pro/tools/kmer-diversity-sieve"
aliases:
 - "l1_pipeline_serial"
versions:
 - "0.1.0--hab16a5f_0"
description: "singularity registry hpc automated addition for kmer-diversity-sieve"
config: {"url": "https://biocontainers.pro/tools/kmer-diversity-sieve", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for kmer-diversity-sieve", "latest": {"0.1.0--hab16a5f_0": "sha256:fcb2d6c6b446e540264cb0027dc23a0d242d7b4873fc84b3f22187cad477a825"}, "tags": {"0.1.0--hab16a5f_0": "sha256:fcb2d6c6b446e540264cb0027dc23a0d242d7b4873fc84b3f22187cad477a825"}, "docker": "quay.io/biocontainers/kmer-diversity-sieve", "aliases": {"l1_pipeline_serial": "/usr/local/bin/l1_pipeline_serial"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kmer-diversity-sieve.
singularity registry hpc automated addition for kmer-diversity-sieve
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kmer-diversity-sieve
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kmer-diversity-sieve:0.1.0--hab16a5f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kmer-diversity-sieve/0.1.0--hab16a5f_0
$ module help quay.io/biocontainers/kmer-diversity-sieve/0.1.0--hab16a5f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kmer-diversity-sieve-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kmer-diversity-sieve-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kmer-diversity-sieve-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kmer-diversity-sieve-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kmer-diversity-sieve-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kmer-diversity-sieve-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### l1_pipeline_serial

```bash
$ singularity exec <container> /usr/local/bin/l1_pipeline_serial
$ podman run --it --rm --entrypoint /usr/local/bin/l1_pipeline_serial   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/l1_pipeline_serial   -v ${PWD} -w ${PWD} <container> -c " $@"
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