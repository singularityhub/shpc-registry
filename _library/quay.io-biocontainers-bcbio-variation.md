---
layout: container
name:  "quay.io/biocontainers/bcbio-variation"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bcbio-variation/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bcbio-variation/container.yaml"
updated_at: "2022-10-27 00:56:41.447853"
latest: "0.2.6--hdfd78af_4"
container_url: "https://biocontainers.pro/tools/bcbio-variation"
aliases:
 - "bcbio-variation"
versions:
 - "0.2.6--hdfd78af_4"
description: "shpc-registry automated BioContainers addition for bcbio-variation"
config: {"url": "https://biocontainers.pro/tools/bcbio-variation", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bcbio-variation", "latest": {"0.2.6--hdfd78af_4": "sha256:a7c6ed07ddb4fee0f3dc5e4f70724c1fa2a8de7a321381a1af272eb7a1c57389"}, "tags": {"0.2.6--hdfd78af_4": "sha256:a7c6ed07ddb4fee0f3dc5e4f70724c1fa2a8de7a321381a1af272eb7a1c57389"}, "docker": "quay.io/biocontainers/bcbio-variation", "aliases": {"bcbio-variation": "/usr/local/bin/bcbio-variation"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bcbio-variation.
shpc-registry automated BioContainers addition for bcbio-variation
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bcbio-variation
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bcbio-variation:0.2.6--hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bcbio-variation/0.2.6--hdfd78af_4
$ module help quay.io/biocontainers/bcbio-variation/0.2.6--hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bcbio-variation-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bcbio-variation-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bcbio-variation-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bcbio-variation-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bcbio-variation-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bcbio-variation-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bcbio-variation

```bash
$ singularity exec <container> /usr/local/bin/bcbio-variation
$ podman run --it --rm --entrypoint /usr/local/bin/bcbio-variation   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcbio-variation   -v ${PWD} -w ${PWD} <container> -c " $@"
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