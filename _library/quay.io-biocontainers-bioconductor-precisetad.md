---
layout: container
name:  "quay.io/biocontainers/bioconductor-precisetad"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-precisetad/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-precisetad/container.yaml"
updated_at: "2025-10-14 03:50:35.437985"
latest: "1.16.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-precisetad"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.16.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-precisetad"
config: {"url": "https://biocontainers.pro/tools/bioconductor-precisetad", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-precisetad", "latest": {"1.16.0--r44hdfd78af_0": "sha256:f30515737a7f2fd443921d8ff8e3d5b72197dc9873f78a4b8c0bf073edcc67cf"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:c1b7900391104f8333f72a58e7efd3162e8cf4943981c672bcd32bdfacf6828a", "1.8.0--r42hdfd78af_0": "sha256:2c27f5c895128d2177bf22e20119c3233e9f9dc2792658559e832c0fb35106cb", "1.10.0--r43hdfd78af_0": "sha256:4895d95e82739b7d8db61c3f9c102ff53b8948a819008db1135c62e2db4b8e66", "1.12.0--r43hdfd78af_0": "sha256:b4d4b911b5e3828cafb27d43b2566028e26bd9beffdfcc746fb9f38f525e0822", "1.16.0--r44hdfd78af_0": "sha256:f30515737a7f2fd443921d8ff8e3d5b72197dc9873f78a4b8c0bf073edcc67cf"}, "docker": "quay.io/biocontainers/bioconductor-precisetad"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-precisetad.
shpc-registry automated BioContainers addition for bioconductor-precisetad
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-precisetad
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-precisetad:1.16.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-precisetad/1.16.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-precisetad/1.16.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-precisetad-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-precisetad-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-precisetad-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-precisetad-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-precisetad-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-precisetad-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-precisetad

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