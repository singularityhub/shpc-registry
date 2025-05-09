---
layout: container
name:  "quay.io/biocontainers/sdrf-pipelines"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sdrf-pipelines/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sdrf-pipelines/container.yaml"
updated_at: "2025-05-09 03:48:39.437431"
latest: "0.0.31--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/sdrf-pipelines"

versions:
 - "0.0.9--py_0"
 - "0.0.22--pyhdfd78af_0"
 - "0.0.24--pyhdfd78af_0"
 - "0.0.25--pyhdfd78af_0"
 - "0.0.26--pyhdfd78af_0"
 - "0.0.27--pyhdfd78af_0"
 - "0.0.29--pyhdfd78af_0"
 - "0.0.31--pyhdfd78af_0"
 - "0.0.31--pyhdfd78af_1"
description: "shpc-registry automated BioContainers addition for sdrf-pipelines"
config: {"url": "https://biocontainers.pro/tools/sdrf-pipelines", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sdrf-pipelines", "latest": {"0.0.31--pyhdfd78af_1": "sha256:3b8d4716c636e158bfa5ca939207c4827a6a2d20224185a6a52eb34b28d42a25"}, "tags": {"0.0.9--py_0": "sha256:bd38b5c004164b0d6e8492ca9d85cbc0d18b5b815720071ac50a889a960c4dc7", "0.0.22--pyhdfd78af_0": "sha256:3f8e2f54d5837991f04a8e4646f005fdf03ef0bfb7163adfa32fb33218c25660", "0.0.24--pyhdfd78af_0": "sha256:4338b0aa445b76b203567d6cb737971bcefc61829369344b8e91af09046e3ddc", "0.0.25--pyhdfd78af_0": "sha256:1a56235ae3fbb4c7ece99cb78b2161866db39412428d2ee9622e5f83d8eda5ea", "0.0.26--pyhdfd78af_0": "sha256:28878dffa7f7e9a2e5b0a2b9f3fb4d79c02a3bd35df0f7d8eb073a3c51526662", "0.0.27--pyhdfd78af_0": "sha256:a7c106f899d6a8ca1f1b47957e9fd2c7cdd994b43f1a8ce49cc535ce78579488", "0.0.29--pyhdfd78af_0": "sha256:c1a1568c293b6fb5a03415518027e497a7fa23c5899ff65cf54046ac0ac52625", "0.0.31--pyhdfd78af_0": "sha256:649cfbbd400643c78a26e73a59da4145c717ebffee9fcbc0a9959e3193eed906", "0.0.31--pyhdfd78af_1": "sha256:3b8d4716c636e158bfa5ca939207c4827a6a2d20224185a6a52eb34b28d42a25"}, "docker": "quay.io/biocontainers/sdrf-pipelines"}
---

This module is a singularity container wrapper for quay.io/biocontainers/sdrf-pipelines.
shpc-registry automated BioContainers addition for sdrf-pipelines
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sdrf-pipelines
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sdrf-pipelines:0.0.31--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sdrf-pipelines/0.0.31--pyhdfd78af_1
$ module help quay.io/biocontainers/sdrf-pipelines/0.0.31--pyhdfd78af_1
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