---
layout: container
name:  "quay.io/biocontainers/gsearch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gsearch/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gsearch/container.yaml"
updated_at: "2025-11-02 03:38:26.723852"
latest: "0.3.1--hafc0c1d_1"
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
 - "0.2.0--hdbdd923_0"
 - "0.2.1--hdbdd923_0"
 - "0.2.2--hdbdd923_0"
 - "0.2.4--h3ab6199_0"
 - "0.2.5--h3ab6199_0"
 - "0.2.8--hafc0c1d_0"
 - "0.3.1--hafc0c1d_0"
 - "0.2.9--hafc0c1d_0"
 - "0.3.1--hafc0c1d_1"
description: "singularity registry hpc automated addition for gsearch"
config: {"url": "https://biocontainers.pro/tools/gsearch", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for gsearch", "latest": {"0.3.1--hafc0c1d_1": "sha256:d42a27761527bdd6b645df54f03c123cb5a3beb44bece8fedbbc40c765dcd0b0"}, "tags": {"0.0.12--h87f3376_0": "sha256:f84d5cb4c00788fe4166ae40cc5caf9bc23550ea9cd655a0e830ba23583fec43", "0.1.2--h43eeafb_6": "sha256:dd9e7d11197dc1519906f745c7bd520c9d3302832113eab879deba0a3ae553fd", "0.1.4--hdbdd923_0": "sha256:eaf550307c5090808e7628310a5a23670e15bf2d633e758fb02964c2bc04504e", "0.1.6--hdbdd923_0": "sha256:d670a0da215b8be14705823bc137540e7489f55d80f6071097414f3842b8d3d8", "0.1.7--hdbdd923_0": "sha256:815df99ef963dfbfaf59bd715f701a8d77e22b601177720fba697813590bff5a", "0.1.9--hdbdd923_0": "sha256:444caee3f2707119b03f2bcfdf12e5a7c231d063bd519d1f0ad8d0892fa6aa1c", "0.2.0--hdbdd923_0": "sha256:0090bfc05c60d257c595710dd5724ba6bc19aa2efbb8d16390d89742dd6a05ed", "0.2.1--hdbdd923_0": "sha256:eb32bfc4c272ab6ce8415ae1f5e893e2950b675e8bb6d1a1619cb3f06903c8db", "0.2.2--hdbdd923_0": "sha256:5b3c48c8e0ec9935a37efaadb1b6860cc18e74b9d028fbd15f23feae1917389d", "0.2.4--h3ab6199_0": "sha256:2dba4df0a67d47b0215ef314e33dda1140472edccea76e92e4e2613bd8044aec", "0.2.5--h3ab6199_0": "sha256:7e5ccbdcafbe217d8e766b5baec1806ce8a9e31afcaa3faee8e794aa69906798", "0.2.8--hafc0c1d_0": "sha256:ec897d6609b21a55f4e71aa6cc73c980c3463d8b72b4f441eb1bfed16b9e339b", "0.3.1--hafc0c1d_0": "sha256:2d8496b596b8c538bf9549248f91510c1918aaf356973678fcf07840790fc71a", "0.2.9--hafc0c1d_0": "sha256:c3598fd6956a0f9fda1c05e6128525336468f2075db5510fbf9d151d46fd41c7", "0.3.1--hafc0c1d_1": "sha256:d42a27761527bdd6b645df54f03c123cb5a3beb44bece8fedbbc40c765dcd0b0"}, "docker": "quay.io/biocontainers/gsearch", "aliases": {"request": "/usr/local/bin/request", "tohnsw": "/usr/local/bin/tohnsw"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gsearch.
singularity registry hpc automated addition for gsearch
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gsearch
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gsearch:0.3.1--hafc0c1d_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gsearch/0.3.1--hafc0c1d_1
$ module help quay.io/biocontainers/gsearch/0.3.1--hafc0c1d_1
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