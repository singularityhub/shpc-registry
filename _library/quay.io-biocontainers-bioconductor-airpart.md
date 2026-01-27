---
layout: container
name:  "quay.io/biocontainers/bioconductor-airpart"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-airpart/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-airpart/container.yaml"
updated_at: "2026-01-27 04:03:06.104029"
latest: "1.14.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-airpart"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.14.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-airpart"
config: {"url": "https://biocontainers.pro/tools/bioconductor-airpart", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-airpart", "latest": {"1.14.0--r44hdfd78af_0": "sha256:227ba8a4f17549eecc21986459f61f2cd6bb507c1ae005e553f9791fba3483eb"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:3115dbcd8ed70620d9a51f3092def1d1b14842f0b030540fa886aded2ec2995f", "1.6.0--r42hdfd78af_0": "sha256:21466c9445e509f4e51db6804b7bafe826f00e09569573fe736125859f826644", "1.8.0--r43hdfd78af_0": "sha256:d3e9d23f922d17aa2c90505f6009b02280b403ec22c0400e8fcef7d8a49ae75e", "1.10.0--r43hdfd78af_0": "sha256:9dbc11e1be146104562795c6d2776b3769009a8a73e870d8771acc8a71d9721a", "1.14.0--r44hdfd78af_0": "sha256:227ba8a4f17549eecc21986459f61f2cd6bb507c1ae005e553f9791fba3483eb"}, "docker": "quay.io/biocontainers/bioconductor-airpart"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-airpart.
shpc-registry automated BioContainers addition for bioconductor-airpart
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-airpart
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-airpart:1.14.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-airpart/1.14.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-airpart/1.14.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-airpart-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-airpart-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-airpart-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-airpart-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-airpart-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-airpart-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-airpart

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