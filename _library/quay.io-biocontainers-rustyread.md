---
layout: container
name:  "quay.io/biocontainers/rustyread"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rustyread/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rustyread/container.yaml"
updated_at: "2023-08-08 03:00:24.093041"
latest: "0.4.1--h8bd2d3b_3"
container_url: "https://biocontainers.pro/tools/rustyread"
aliases:
 - "rustyread"
versions:
 - "0.4.1--hc308579_1"
 - "0.4.1--h8bd2d3b_3"
description: "shpc-registry automated BioContainers addition for rustyread"
config: {"url": "https://biocontainers.pro/tools/rustyread", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rustyread", "latest": {"0.4.1--h8bd2d3b_3": "sha256:d2b23892dc7514a81049308f667a296832aba673b1a65d19548b3dd3b8954c4d"}, "tags": {"0.4.1--hc308579_1": "sha256:2ef2e411f6a3972971444983dcc8474851104ddb200c2808b9386525c5ccda1a", "0.4.1--h8bd2d3b_3": "sha256:d2b23892dc7514a81049308f667a296832aba673b1a65d19548b3dd3b8954c4d"}, "docker": "quay.io/biocontainers/rustyread", "aliases": {"rustyread": "/usr/local/bin/rustyread"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rustyread.
shpc-registry automated BioContainers addition for rustyread
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rustyread
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rustyread:0.4.1--h8bd2d3b_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rustyread/0.4.1--h8bd2d3b_3
$ module help quay.io/biocontainers/rustyread/0.4.1--h8bd2d3b_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rustyread-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rustyread-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rustyread-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rustyread-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rustyread-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rustyread-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rustyread

```bash
$ singularity exec <container> /usr/local/bin/rustyread
$ podman run --it --rm --entrypoint /usr/local/bin/rustyread   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rustyread   -v ${PWD} -w ${PWD} <container> -c " $@"
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