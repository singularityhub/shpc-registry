---
layout: container
name:  "quay.io/biocontainers/bioconductor-parody"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-parody/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-parody/container.yaml"
updated_at: "2024-04-11 02:58:26.925522"
latest: "1.60.0--r43hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-parody"

versions:
 - "1.52.0--r41hdfd78af_0"
 - "1.56.0--r42hdfd78af_0"
 - "1.58.0--r43hdfd78af_0"
 - "1.60.0--r43hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-parody"
config: {"url": "https://biocontainers.pro/tools/bioconductor-parody", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-parody", "latest": {"1.60.0--r43hdfd78af_1": "sha256:150bd0b893dcca9de7dedd97c9066b9af98d95b88d4b9ca95dd2f94c08519673"}, "tags": {"1.52.0--r41hdfd78af_0": "sha256:1f29ce1f53bd61ed5039b1f535ee7e6b3ddd86df52427cf9e52e0e99ce134a04", "1.56.0--r42hdfd78af_0": "sha256:3d50cd206ee3d14a23b44245a5d0acc374a35baddf7a57a5276c474ed641f120", "1.58.0--r43hdfd78af_0": "sha256:43bd3dcf256b440b1248bdf1a22c5c5a9f89e45e16f9b97d31718e6f8ce37b0a", "1.60.0--r43hdfd78af_1": "sha256:150bd0b893dcca9de7dedd97c9066b9af98d95b88d4b9ca95dd2f94c08519673"}, "docker": "quay.io/biocontainers/bioconductor-parody"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-parody.
shpc-registry automated BioContainers addition for bioconductor-parody
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-parody
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-parody:1.60.0--r43hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-parody/1.60.0--r43hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-parody/1.60.0--r43hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-parody-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-parody-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-parody-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-parody-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-parody-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-parody-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-parody

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