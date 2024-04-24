---
layout: container
name:  "quay.io/biocontainers/mosaicatcher"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mosaicatcher/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mosaicatcher/container.yaml"
updated_at: "2024-04-24 02:27:26.696676"
latest: "0.3.1--h5642b88_3"
container_url: "https://biocontainers.pro/tools/mosaicatcher"
aliases:
 - "mosaicatcher"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.3.1--hefd527f_1"
 - "0.3.1--h66ab1b6_2"
 - "0.3.1--h5642b88_3"
description: "singularity registry hpc automated addition for mosaicatcher"
config: {"url": "https://biocontainers.pro/tools/mosaicatcher", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mosaicatcher", "latest": {"0.3.1--h5642b88_3": "sha256:f35e3def9960e98fc7a3f0fd07b285cd38f098cc841e5f80d5af8aeedbf7b3ce"}, "tags": {"0.3.1--hefd527f_1": "sha256:4c02db963230108b295b36c2cb220cf8b17336c4ae803aeb91c0a33109046f51", "0.3.1--h66ab1b6_2": "sha256:249f4ec44e4bef980fef9d67218ea0511f2e565a6c2c788fc0a8a9905c30a5ad", "0.3.1--h5642b88_3": "sha256:f35e3def9960e98fc7a3f0fd07b285cd38f098cc841e5f80d5af8aeedbf7b3ce"}, "docker": "quay.io/biocontainers/mosaicatcher", "aliases": {"mosaicatcher": "/usr/local/bin/mosaicatcher", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mosaicatcher.
singularity registry hpc automated addition for mosaicatcher
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mosaicatcher
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mosaicatcher:0.3.1--h5642b88_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mosaicatcher/0.3.1--h5642b88_3
$ module help quay.io/biocontainers/mosaicatcher/0.3.1--h5642b88_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mosaicatcher-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mosaicatcher-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mosaicatcher-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mosaicatcher-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mosaicatcher-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mosaicatcher-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mosaicatcher

```bash
$ singularity exec <container> /usr/local/bin/mosaicatcher
$ podman run --it --rm --entrypoint /usr/local/bin/mosaicatcher   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mosaicatcher   -v ${PWD} -w ${PWD} <container> -c " $@"
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