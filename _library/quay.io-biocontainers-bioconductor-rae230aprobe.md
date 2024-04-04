---
layout: container
name:  "quay.io/biocontainers/bioconductor-rae230aprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rae230aprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rae230aprobe/container.yaml"
updated_at: "2024-04-04 03:51:38.303391"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-rae230aprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-rae230aprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rae230aprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rae230aprobe", "latest": {"2.18.0--r43hdfd78af_12": "sha256:7c5f578d9576f7a6c22a2248e2e7580f37a19a3ed40f0880f6c5a926b9f2216a"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:1784247cf1725a4ea0cbe799f8030fcbde677d53eae0428ff62b80f05fe6eee5", "2.18.0--r42hdfd78af_10": "sha256:4dcddbd03af0e59613800c9c9efcf95303ea722b7c08d53ac31de1aa13f469be", "2.18.0--r43hdfd78af_11": "sha256:f1bd3bb0af6f8ea236daf0a578dd60b9620d6194f9b094643c0e94c142189aa5", "2.18.0--r43hdfd78af_12": "sha256:7c5f578d9576f7a6c22a2248e2e7580f37a19a3ed40f0880f6c5a926b9f2216a"}, "docker": "quay.io/biocontainers/bioconductor-rae230aprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rae230aprobe.
shpc-registry automated BioContainers addition for bioconductor-rae230aprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rae230aprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rae230aprobe:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rae230aprobe/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-rae230aprobe/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rae230aprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rae230aprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rae230aprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rae230aprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rae230aprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rae230aprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rae230aprobe

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