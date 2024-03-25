---
layout: container
name:  "quay.io/biocontainers/gsearch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gsearch/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gsearch/container.yaml"
updated_at: "2024-03-25 03:20:19.870992"
latest: "0.1.9--hdbdd923_0"
container_url: "https://biocontainers.pro/tools/gsearch"
aliases:
 - "request"
 - "tohnsw"
versions:
 - "0.0.12--h87f3376_0"
 - "0.1.2--h43eeafb_6"
 - "0.1.4--hdbdd923_0"
 - "0.1.6--hdbdd923_0"
 - "0.1.7--hdbdd923_0"
 - "0.1.9--hdbdd923_0"
description: "singularity registry hpc automated addition for gsearch"
config: {"url": "https://biocontainers.pro/tools/gsearch", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for gsearch", "latest": {"0.1.9--hdbdd923_0": "sha256:444caee3f2707119b03f2bcfdf12e5a7c231d063bd519d1f0ad8d0892fa6aa1c"}, "tags": {"0.0.12--h87f3376_0": "sha256:f84d5cb4c00788fe4166ae40cc5caf9bc23550ea9cd655a0e830ba23583fec43", "0.1.2--h43eeafb_6": "sha256:dd9e7d11197dc1519906f745c7bd520c9d3302832113eab879deba0a3ae553fd", "0.1.4--hdbdd923_0": "sha256:eaf550307c5090808e7628310a5a23670e15bf2d633e758fb02964c2bc04504e", "0.1.6--hdbdd923_0": "sha256:3ea1e9ed7d25baf83df39cd3de67d086337f7e5915f5b2e24a1b71f9b9528233", "0.1.7--hdbdd923_0": "sha256:815df99ef963dfbfaf59bd715f701a8d77e22b601177720fba697813590bff5a", "0.1.9--hdbdd923_0": "sha256:444caee3f2707119b03f2bcfdf12e5a7c231d063bd519d1f0ad8d0892fa6aa1c"}, "docker": "quay.io/biocontainers/gsearch", "aliases": {"request": "/usr/local/bin/request", "tohnsw": "/usr/local/bin/tohnsw"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gsearch.
singularity registry hpc automated addition for gsearch
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gsearch
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gsearch:0.1.9--hdbdd923_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gsearch/0.1.9--hdbdd923_0
$ module help quay.io/biocontainers/gsearch/0.1.9--hdbdd923_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gsearch-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gsearch-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gsearch-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gsearch-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gsearch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gsearch-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### request

```bash
$ singularity exec <container> /usr/local/bin/request
$ podman run --it --rm --entrypoint /usr/local/bin/request   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/request   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tohnsw

```bash
$ singularity exec <container> /usr/local/bin/tohnsw
$ podman run --it --rm --entrypoint /usr/local/bin/tohnsw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tohnsw   -v ${PWD} -w ${PWD} <container> -c " $@"
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