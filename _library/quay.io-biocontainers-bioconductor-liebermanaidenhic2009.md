---
layout: container
name:  "quay.io/biocontainers/bioconductor-liebermanaidenhic2009"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-liebermanaidenhic2009/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-liebermanaidenhic2009/container.yaml"
updated_at: "2024-08-18 02:51:42.663488"
latest: "0.40.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-liebermanaidenhic2009"

versions:
 - "0.32.0--r41hdfd78af_1"
 - "0.35.0--r42hdfd78af_0"
 - "0.38.0--r43hdfd78af_0"
 - "0.40.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-liebermanaidenhic2009"
config: {"url": "https://biocontainers.pro/tools/bioconductor-liebermanaidenhic2009", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-liebermanaidenhic2009", "latest": {"0.40.0--r43hdfd78af_0": "sha256:fa570b341c69ba4f389ae78e20621566f6c1c6d0718a2469d07c907fcd952c9e"}, "tags": {"0.32.0--r41hdfd78af_1": "sha256:4bafc704e45886e93f85f80f9f16fc3f7b338e9b6d1fe0dd75dd28a4e7dbdf6f", "0.35.0--r42hdfd78af_0": "sha256:e69af972e48da416a08cae1dae2b8ec575043e1883c81b2f3eba514300a19fa4", "0.38.0--r43hdfd78af_0": "sha256:35a6d5a33d167c0cd62ce9aa4fdf8a13d97616152a2369d7cefd558b4ebc97de", "0.40.0--r43hdfd78af_0": "sha256:fa570b341c69ba4f389ae78e20621566f6c1c6d0718a2469d07c907fcd952c9e"}, "docker": "quay.io/biocontainers/bioconductor-liebermanaidenhic2009"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-liebermanaidenhic2009.
shpc-registry automated BioContainers addition for bioconductor-liebermanaidenhic2009
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-liebermanaidenhic2009
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-liebermanaidenhic2009:0.40.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-liebermanaidenhic2009/0.40.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-liebermanaidenhic2009/0.40.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-liebermanaidenhic2009-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-liebermanaidenhic2009-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-liebermanaidenhic2009-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-liebermanaidenhic2009-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-liebermanaidenhic2009-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-liebermanaidenhic2009-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-liebermanaidenhic2009

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