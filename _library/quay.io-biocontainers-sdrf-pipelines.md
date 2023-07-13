---
layout: container
name:  "quay.io/biocontainers/sdrf-pipelines"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sdrf-pipelines/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sdrf-pipelines/container.yaml"
updated_at: "2023-07-13 03:34:06.523963"
latest: "0.0.22--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/sdrf-pipelines"

versions:
 - "0.0.9--py_0"
 - "0.0.22--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for sdrf-pipelines"
config: {"url": "https://biocontainers.pro/tools/sdrf-pipelines", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sdrf-pipelines", "latest": {"0.0.22--pyhdfd78af_0": "sha256:3f8e2f54d5837991f04a8e4646f005fdf03ef0bfb7163adfa32fb33218c25660"}, "tags": {"0.0.9--py_0": "sha256:bd38b5c004164b0d6e8492ca9d85cbc0d18b5b815720071ac50a889a960c4dc7", "0.0.22--pyhdfd78af_0": "sha256:3f8e2f54d5837991f04a8e4646f005fdf03ef0bfb7163adfa32fb33218c25660"}, "docker": "quay.io/biocontainers/sdrf-pipelines"}
---

This module is a singularity container wrapper for quay.io/biocontainers/sdrf-pipelines.
shpc-registry automated BioContainers addition for sdrf-pipelines
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sdrf-pipelines
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sdrf-pipelines:0.0.22--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sdrf-pipelines/0.0.22--pyhdfd78af_0
$ module help quay.io/biocontainers/sdrf-pipelines/0.0.22--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sdrf-pipelines-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sdrf-pipelines-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sdrf-pipelines-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sdrf-pipelines-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sdrf-pipelines-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sdrf-pipelines-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### sdrf-pipelines

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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