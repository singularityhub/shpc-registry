---
layout: container
name:  "quay.io/biocontainers/bioconductor-oncoscore"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-oncoscore/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-oncoscore/container.yaml"
updated_at: "2025-05-24 11:14:39.939531"
latest: "1.34.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-oncoscore"

versions:
 - "1.22.0--r41hdfd78af_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
 - "1.34.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-oncoscore"
config: {"url": "https://biocontainers.pro/tools/bioconductor-oncoscore", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-oncoscore", "latest": {"1.34.0--r44hdfd78af_0": "sha256:f7cee8a9a1c0e21e24b2b48e3876cbe36b6f4f381c7ae0f2fb8abf81b992a74c"}, "tags": {"1.22.0--r41hdfd78af_0": "sha256:dbcd92f5744f2af480a497d1b7cab31a6008d69d294d1c811ef185e5cf8deb54", "1.26.0--r42hdfd78af_0": "sha256:9194c0cab458ba32397cc40257e717f200ae5ffc1043d0214d217d161de0533e", "1.28.0--r43hdfd78af_0": "sha256:c154e3159462664a77729a181a11dc889f47266b1538d3c83ac6c64ba7485a11", "1.30.0--r43hdfd78af_0": "sha256:415a8dd648a7b78b6f06de3e7c98e91dbfbe6b1af083a47fe8d8efae127b698a", "1.34.0--r44hdfd78af_0": "sha256:f7cee8a9a1c0e21e24b2b48e3876cbe36b6f4f381c7ae0f2fb8abf81b992a74c"}, "docker": "quay.io/biocontainers/bioconductor-oncoscore"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-oncoscore.
shpc-registry automated BioContainers addition for bioconductor-oncoscore
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-oncoscore
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-oncoscore:1.34.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-oncoscore/1.34.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-oncoscore/1.34.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-oncoscore-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-oncoscore-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-oncoscore-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-oncoscore-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-oncoscore-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-oncoscore-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-oncoscore

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