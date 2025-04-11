---
layout: container
name:  "quay.io/biocontainers/bioconductor-maskbad"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-maskbad/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-maskbad/container.yaml"
updated_at: "2025-04-11 03:06:29.564935"
latest: "1.50.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-maskbad"

versions:
 - "1.38.0--r41hdfd78af_0"
 - "1.42.0--r42hdfd78af_0"
 - "1.44.0--r43hdfd78af_0"
 - "1.46.0--r43hdfd78af_0"
 - "1.50.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-maskbad"
config: {"url": "https://biocontainers.pro/tools/bioconductor-maskbad", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-maskbad", "latest": {"1.50.0--r44hdfd78af_0": "sha256:81fbe81ba7b4bebbe95528cb672d7ef6c0d19b9a2327a4137b1409b4be4b8ead"}, "tags": {"1.38.0--r41hdfd78af_0": "sha256:a2b205867a53b6cb5be3e0a0cccb90dada97fc47c2f50c85f2cea5bf5e56a52e", "1.42.0--r42hdfd78af_0": "sha256:9d942009bf78fb0560845bcf48748b962353585c4bceaf1cd547a461cf31b158", "1.44.0--r43hdfd78af_0": "sha256:5e3465b78ccdba81056b1f5dd603bb69a82bf90ce969dc3de274cfdc28d107a4", "1.46.0--r43hdfd78af_0": "sha256:a793514244bbb0b647b93e4f5c55caa329739cbeb6630f3416a4d706d0a4ab4b", "1.50.0--r44hdfd78af_0": "sha256:81fbe81ba7b4bebbe95528cb672d7ef6c0d19b9a2327a4137b1409b4be4b8ead"}, "docker": "quay.io/biocontainers/bioconductor-maskbad"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-maskbad.
shpc-registry automated BioContainers addition for bioconductor-maskbad
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-maskbad
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-maskbad:1.50.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-maskbad/1.50.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-maskbad/1.50.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-maskbad-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-maskbad-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-maskbad-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-maskbad-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-maskbad-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-maskbad-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-maskbad

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