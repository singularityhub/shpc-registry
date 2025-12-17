---
layout: container
name:  "quay.io/biocontainers/hmftools-bwa-plus"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hmftools-bwa-plus/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hmftools-bwa-plus/container.yaml"
updated_at: "2025-12-17 15:37:11.728295"
latest: "1.0.0--h077b44d_0"
container_url: "https://biocontainers.pro/tools/hmftools-bwa-plus"
aliases:
 - "bwa-plus"
 - "bwa-plus.avx"
 - "bwa-plus.avx2"
 - "bwa-plus.avx512bw"
 - "bwa-plus.sse41"
 - "bwa-plus.sse42"
 - "sambamba"
versions:
 - "1.0.0--h077b44d_0"
description: "singularity registry hpc automated addition for hmftools-bwa-plus"
config: {"url": "https://biocontainers.pro/tools/hmftools-bwa-plus", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for hmftools-bwa-plus", "latest": {"1.0.0--h077b44d_0": "sha256:52f2858d7dc41038dac22756c31186541c0c4218287de16f41d013ff7452b273"}, "tags": {"1.0.0--h077b44d_0": "sha256:52f2858d7dc41038dac22756c31186541c0c4218287de16f41d013ff7452b273"}, "docker": "quay.io/biocontainers/hmftools-bwa-plus", "aliases": {"bwa-plus": "/usr/local/bin/bwa-plus", "bwa-plus.avx": "/usr/local/bin/bwa-plus.avx", "bwa-plus.avx2": "/usr/local/bin/bwa-plus.avx2", "bwa-plus.avx512bw": "/usr/local/bin/bwa-plus.avx512bw", "bwa-plus.sse41": "/usr/local/bin/bwa-plus.sse41", "bwa-plus.sse42": "/usr/local/bin/bwa-plus.sse42", "sambamba": "/usr/local/bin/sambamba"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hmftools-bwa-plus.
singularity registry hpc automated addition for hmftools-bwa-plus
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hmftools-bwa-plus
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hmftools-bwa-plus:1.0.0--h077b44d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hmftools-bwa-plus/1.0.0--h077b44d_0
$ module help quay.io/biocontainers/hmftools-bwa-plus/1.0.0--h077b44d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hmftools-bwa-plus-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hmftools-bwa-plus-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hmftools-bwa-plus-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hmftools-bwa-plus-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hmftools-bwa-plus-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hmftools-bwa-plus-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bwa-plus

```bash
$ singularity exec <container> /usr/local/bin/bwa-plus
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-plus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-plus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-plus.avx

```bash
$ singularity exec <container> /usr/local/bin/bwa-plus.avx
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-plus.avx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-plus.avx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-plus.avx2

```bash
$ singularity exec <container> /usr/local/bin/bwa-plus.avx2
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-plus.avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-plus.avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-plus.avx512bw

```bash
$ singularity exec <container> /usr/local/bin/bwa-plus.avx512bw
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-plus.avx512bw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-plus.avx512bw   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-plus.sse41

```bash
$ singularity exec <container> /usr/local/bin/bwa-plus.sse41
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-plus.sse41   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-plus.sse41   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-plus.sse42

```bash
$ singularity exec <container> /usr/local/bin/bwa-plus.sse42
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-plus.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-plus.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sambamba

```bash
$ singularity exec <container> /usr/local/bin/sambamba
$ podman run --it --rm --entrypoint /usr/local/bin/sambamba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sambamba   -v ${PWD} -w ${PWD} <container> -c " $@"
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