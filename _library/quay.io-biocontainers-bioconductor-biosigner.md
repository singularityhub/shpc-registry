---
layout: container
name:  "quay.io/biocontainers/bioconductor-biosigner"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biosigner/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biosigner/container.yaml"
updated_at: "2024-12-17 03:50:14.073489"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biosigner"

versions:
 - "1.8.0--r351_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.2--r40hdfd78af_0"
 - "1.16.0--r40_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-biosigner"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biosigner", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-biosigner", "latest": {"1.30.0--r43hdfd78af_0": "sha256:16a01d35176f8c8638a7f8e58d67952694e30325ed53919d1e6b83923bee7606"}, "tags": {"1.8.0--r351_0": "sha256:8ae7c24dce6623a452b307c7cba5515a554b241c87b2a470c226522295feaa51", "1.26.0--r42hdfd78af_0": "sha256:34789586eb17b1f4ab03c745c601493f8cb55bbae5802884b0f605b984ed4d17", "1.22.0--r41hdfd78af_0": "sha256:40eaa33d9d7d6a41f3f6c6fedc42d13f2809ad7314ac00307d3732f7c7c70ff0", "1.20.0--r41hdfd78af_0": "sha256:82eaa6d3ffc1802b00db3b8ab2d0357c41a783708cd1dde583b02ce12aa50b5a", "1.18.2--r40hdfd78af_0": "sha256:60574566c159916f6db0b1a5047ef48fa04e604ff99966534b26083629ab177a", "1.16.0--r40_0": "sha256:dc978028b01657fd249a13b1f8058307710b9bab27c8191daa553ff344961f21", "1.28.0--r43hdfd78af_0": "sha256:31e06f7bfa715727354d9ebec26ff83f5aadf3ecdd474064ea6bbf660bc7e323", "1.30.0--r43hdfd78af_0": "sha256:16a01d35176f8c8638a7f8e58d67952694e30325ed53919d1e6b83923bee7606"}, "docker": "quay.io/biocontainers/bioconductor-biosigner"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biosigner.
shpc-registry automated BioContainers addition for bioconductor-biosigner
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biosigner
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biosigner:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biosigner/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-biosigner/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biosigner-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biosigner-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biosigner-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biosigner-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biosigner-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biosigner-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-biosigner

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