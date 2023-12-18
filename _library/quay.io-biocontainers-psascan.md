---
layout: container
name:  "quay.io/biocontainers/psascan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/psascan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/psascan/container.yaml"
updated_at: "2023-12-18 03:06:01.907453"
latest: "0.1.0--h4ac6f70_4"
container_url: "https://biocontainers.pro/tools/psascan"
aliases:
 - "psascan"
versions:
 - "0.1.0--h9f5acd7_3"
 - "0.1.0--h4ac6f70_4"
description: "shpc-registry automated BioContainers addition for psascan"
config: {"url": "https://biocontainers.pro/tools/psascan", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for psascan", "latest": {"0.1.0--h4ac6f70_4": "sha256:c2a0f5595a448c37c36a4e977d16dbc7ec242b0e595d3fe07bbf50e9b8f7e22c"}, "tags": {"0.1.0--h9f5acd7_3": "sha256:944b5ed6b0d4327153537bbf9705ec789c85c87f7df6309db80abfbe5ca3658b", "0.1.0--h4ac6f70_4": "sha256:c2a0f5595a448c37c36a4e977d16dbc7ec242b0e595d3fe07bbf50e9b8f7e22c"}, "docker": "quay.io/biocontainers/psascan", "aliases": {"psascan": "/usr/local/bin/psascan"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/psascan.
shpc-registry automated BioContainers addition for psascan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/psascan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/psascan:0.1.0--h4ac6f70_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/psascan/0.1.0--h4ac6f70_4
$ module help quay.io/biocontainers/psascan/0.1.0--h4ac6f70_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### psascan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### psascan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### psascan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### psascan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### psascan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### psascan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### psascan

```bash
$ singularity exec <container> /usr/local/bin/psascan
$ podman run --it --rm --entrypoint /usr/local/bin/psascan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psascan   -v ${PWD} -w ${PWD} <container> -c " $@"
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