---
layout: container
name:  "quay.io/biocontainers/cellsnp-lite"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cellsnp-lite/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cellsnp-lite/container.yaml"
updated_at: "2023-05-25 03:01:06.938583"
latest: "1.2.3--hc88714e_1"
container_url: "https://biocontainers.pro/tools/cellsnp-lite"
aliases:
 - "cellsnp-lite"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "1.2.2--hb0d9459_3"
 - "1.2.3--hb0d9459_0"
 - "1.2.3--hc88714e_1"
description: "shpc-registry automated BioContainers addition for cellsnp-lite"
config: {"url": "https://biocontainers.pro/tools/cellsnp-lite", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cellsnp-lite", "latest": {"1.2.3--hc88714e_1": "sha256:01234b19b7b4df91a5567e65bbd7d18e2ffc9985c43acc483587ed0590464f8d"}, "tags": {"1.2.2--hb0d9459_3": "sha256:9ad1b80f44fc8394cac6fbecaa0780d43a28fe329833785b495d1133d2736f73", "1.2.3--hb0d9459_0": "sha256:fe227191fa2ed87bfabcb54362ed46186fa33d0b0bd838ca8f89ac56316f136b", "1.2.3--hc88714e_1": "sha256:01234b19b7b4df91a5567e65bbd7d18e2ffc9985c43acc483587ed0590464f8d"}, "docker": "quay.io/biocontainers/cellsnp-lite", "aliases": {"cellsnp-lite": "/usr/local/bin/cellsnp-lite", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cellsnp-lite.
shpc-registry automated BioContainers addition for cellsnp-lite
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cellsnp-lite
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cellsnp-lite:1.2.3--hc88714e_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cellsnp-lite/1.2.3--hc88714e_1
$ module help quay.io/biocontainers/cellsnp-lite/1.2.3--hc88714e_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cellsnp-lite-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cellsnp-lite-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cellsnp-lite-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cellsnp-lite-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cellsnp-lite-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cellsnp-lite-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cellsnp-lite

```bash
$ singularity exec <container> /usr/local/bin/cellsnp-lite
$ podman run --it --rm --entrypoint /usr/local/bin/cellsnp-lite   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cellsnp-lite   -v ${PWD} -w ${PWD} <container> -c " $@"
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