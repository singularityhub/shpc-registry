---
layout: container
name:  "quay.io/biocontainers/rapmap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rapmap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rapmap/container.yaml"
updated_at: "2025-04-27 03:47:24.512084"
latest: "0.6.0--hd6d6fdc_6"
container_url: "https://biocontainers.pro/tools/rapmap"
aliases:
 - "rapmap"
versions:
 - "v0.2.1--hfc679d8_2"
 - "0.6.0--hf1761c0_3"
 - "0.5.0--hfc679d8_0"
 - "0.6.0--h6a68c12_5"
 - "0.6.0--hd6d6fdc_6"
description: "shpc-registry automated BioContainers addition for rapmap"
config: {"url": "https://biocontainers.pro/tools/rapmap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rapmap", "latest": {"0.6.0--hd6d6fdc_6": "sha256:5c21c13712300f3b39eb07cc6e7d614ff32d960e2cc2f42984cebd2e61238782"}, "tags": {"v0.2.1--hfc679d8_2": "sha256:c6846dba583697ed579b82108f9533e654ebdf9d23e6383d83eedb8a25fbe1cc", "0.6.0--hf1761c0_3": "sha256:863de1f30d00960140a1df9b7ee69672f1afef7e6346805dddb6d4e307d8e58f", "0.5.0--hfc679d8_0": "sha256:5364278a9257879a481402fd532b7ab92c8b92742d3120147a7293d1cd904b3f", "0.6.0--h6a68c12_5": "sha256:21023f8d6f723c403237be0812ec8f43cc223c3a00d557ec20e943634071d7d0", "0.6.0--hd6d6fdc_6": "sha256:5c21c13712300f3b39eb07cc6e7d614ff32d960e2cc2f42984cebd2e61238782"}, "docker": "quay.io/biocontainers/rapmap", "aliases": {"rapmap": "/usr/local/bin/rapmap"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rapmap.
shpc-registry automated BioContainers addition for rapmap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rapmap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rapmap:0.6.0--hd6d6fdc_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rapmap/0.6.0--hd6d6fdc_6
$ module help quay.io/biocontainers/rapmap/0.6.0--hd6d6fdc_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rapmap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rapmap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rapmap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rapmap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rapmap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rapmap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rapmap

```bash
$ singularity exec <container> /usr/local/bin/rapmap
$ podman run --it --rm --entrypoint /usr/local/bin/rapmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rapmap   -v ${PWD} -w ${PWD} <container> -c " $@"
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