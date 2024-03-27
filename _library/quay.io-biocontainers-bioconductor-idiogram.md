---
layout: container
name:  "quay.io/biocontainers/bioconductor-idiogram"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-idiogram/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-idiogram/container.yaml"
updated_at: "2024-03-27 02:58:55.178390"
latest: "1.78.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-idiogram"

versions:
 - "1.70.0--r41hdfd78af_0"
 - "1.74.0--r42hdfd78af_0"
 - "1.76.0--r43hdfd78af_0"
 - "1.78.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-idiogram"
config: {"url": "https://biocontainers.pro/tools/bioconductor-idiogram", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-idiogram", "latest": {"1.78.0--r43hdfd78af_0": "sha256:05b449c1ce75ce9124541dfe30516e32d0a80a0eb8d0fde0efd962b2095341a0"}, "tags": {"1.70.0--r41hdfd78af_0": "sha256:318c07f4e2551224b9c54646a45c61680a2cdf15480efdc59e4f7134e7d66a16", "1.74.0--r42hdfd78af_0": "sha256:291af03a7a387fe07bc6c9d8131e3880293af592412c3e87068afac16b6651ba", "1.76.0--r43hdfd78af_0": "sha256:f5cbba662135dc3cfcc8c091e2feed202722dd78a9f8c231f68f048c61353167", "1.78.0--r43hdfd78af_0": "sha256:05b449c1ce75ce9124541dfe30516e32d0a80a0eb8d0fde0efd962b2095341a0"}, "docker": "quay.io/biocontainers/bioconductor-idiogram"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-idiogram.
shpc-registry automated BioContainers addition for bioconductor-idiogram
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-idiogram
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-idiogram:1.78.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-idiogram/1.78.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-idiogram/1.78.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-idiogram-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-idiogram-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-idiogram-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-idiogram-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-idiogram-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-idiogram-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-idiogram

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