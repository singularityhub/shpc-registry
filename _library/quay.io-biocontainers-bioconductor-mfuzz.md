---
layout: container
name:  "quay.io/biocontainers/bioconductor-mfuzz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mfuzz/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mfuzz/container.yaml"
updated_at: "2024-12-18 03:09:58.987502"
latest: "2.62.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mfuzz"

versions:
 - "2.54.0--r41hdfd78af_0"
 - "2.58.0--r42hdfd78af_0"
 - "2.60.0--r43hdfd78af_0"
 - "2.62.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mfuzz"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mfuzz", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mfuzz", "latest": {"2.62.0--r43hdfd78af_0": "sha256:1fd3c728924b1f232ec084b2f2f1c1e761815dc60ed26a5b9823c94f4cde90dd"}, "tags": {"2.54.0--r41hdfd78af_0": "sha256:da2dc92176c554afefc934b7fe77c224ab4508d8334987a08b42bbbaeaaa9ff1", "2.58.0--r42hdfd78af_0": "sha256:0bf399b689bb2521fff01fd5a5dfe7376d70d85b9e7790dfc56652fad2c17c32", "2.60.0--r43hdfd78af_0": "sha256:96313a439260d5035db84a83cc9e0e03aabe637efd8ca2f682a66a61949cfeac", "2.62.0--r43hdfd78af_0": "sha256:1fd3c728924b1f232ec084b2f2f1c1e761815dc60ed26a5b9823c94f4cde90dd"}, "docker": "quay.io/biocontainers/bioconductor-mfuzz"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mfuzz.
shpc-registry automated BioContainers addition for bioconductor-mfuzz
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mfuzz
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mfuzz:2.62.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mfuzz/2.62.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mfuzz/2.62.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mfuzz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mfuzz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mfuzz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mfuzz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mfuzz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mfuzz-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mfuzz

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