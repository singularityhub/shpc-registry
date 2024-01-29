---
layout: container
name:  "quay.io/biocontainers/bioconductor-precisetadhub"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-precisetadhub/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-precisetadhub/container.yaml"
updated_at: "2024-01-29 02:39:56.223612"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-precisetadhub"

versions:
 - "1.2.0--r41hdfd78af_1"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-precisetadhub"
config: {"url": "https://biocontainers.pro/tools/bioconductor-precisetadhub", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-precisetadhub", "latest": {"1.10.0--r43hdfd78af_0": "sha256:3496b2ebc87b73681f25924185dda0609a91da6685431f39f2a7036869f40aa5"}, "tags": {"1.2.0--r41hdfd78af_1": "sha256:8c0355ed0fd22c142a09917f356971fa1e2aea4faa42be9e5af57e2de105cd4d", "1.6.0--r42hdfd78af_0": "sha256:3b60e31bd701c6b1bb14bce59016d09d904031df76c93d4951c4cab3a67efbeb", "1.8.0--r43hdfd78af_0": "sha256:022dc9cff0807f8a84ad9f7f10b1672a9f3879090ebf3a169b98d5dd75d684af", "1.10.0--r43hdfd78af_0": "sha256:3496b2ebc87b73681f25924185dda0609a91da6685431f39f2a7036869f40aa5"}, "docker": "quay.io/biocontainers/bioconductor-precisetadhub"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-precisetadhub.
shpc-registry automated BioContainers addition for bioconductor-precisetadhub
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-precisetadhub
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-precisetadhub:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-precisetadhub/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-precisetadhub/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-precisetadhub-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-precisetadhub-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-precisetadhub-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-precisetadhub-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-precisetadhub-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-precisetadhub-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-precisetadhub

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