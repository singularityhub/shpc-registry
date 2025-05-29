---
layout: container
name:  "quay.io/biocontainers/bioconductor-flowbin"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-flowbin/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-flowbin/container.yaml"
updated_at: "2025-05-29 03:58:41.638292"
latest: "1.42.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-flowbin"

versions:
 - "1.30.0--r41hdfd78af_0"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.42.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-flowbin"
config: {"url": "https://biocontainers.pro/tools/bioconductor-flowbin", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-flowbin", "latest": {"1.42.0--r44hdfd78af_0": "sha256:95e0683dcea878d672cce09a9445f90eb4aad348d1f96f0e9957325c8f88caa8"}, "tags": {"1.30.0--r41hdfd78af_0": "sha256:3316e80ce542d4bbe4caab107ba87f80874235c63d3bf4a8b201a388c854a3f1", "1.34.0--r42hdfd78af_0": "sha256:181f4dd3fc48bfd209d0a511804ef3bdf258f833b929ecf96f858cb4450c9bd7", "1.36.0--r43hdfd78af_0": "sha256:4c32547cf5253e02b40cecd6521d5799f133140717550e84c31a26939bf3cfe0", "1.38.0--r43hdfd78af_0": "sha256:43fe617eddcab7c8fc0c955c298a9f239bff98f7769fc3189454cfa5c0cfe36b", "1.42.0--r44hdfd78af_0": "sha256:95e0683dcea878d672cce09a9445f90eb4aad348d1f96f0e9957325c8f88caa8"}, "docker": "quay.io/biocontainers/bioconductor-flowbin"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-flowbin.
shpc-registry automated BioContainers addition for bioconductor-flowbin
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-flowbin
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-flowbin:1.42.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-flowbin/1.42.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-flowbin/1.42.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-flowbin-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowbin-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowbin-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-flowbin-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-flowbin-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-flowbin-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-flowbin

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