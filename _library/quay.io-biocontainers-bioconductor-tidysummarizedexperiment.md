---
layout: container
name:  "quay.io/biocontainers/bioconductor-tidysummarizedexperiment"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tidysummarizedexperiment/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tidysummarizedexperiment/container.yaml"
updated_at: "2024-11-11 03:15:54.820720"
latest: "1.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tidysummarizedexperiment"

versions:
 - "1.4.1--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tidysummarizedexperiment"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tidysummarizedexperiment", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tidysummarizedexperiment", "latest": {"1.12.0--r43hdfd78af_0": "sha256:c5574cb506df0cfd0bce60d9269aa7b2a4c2088b4d2e11d8698cccf274427edc"}, "tags": {"1.4.1--r41hdfd78af_0": "sha256:67920e7a3bbb6094fdc5b095acaf9353f527937125c241b7072466438ecee38d", "1.8.0--r42hdfd78af_0": "sha256:1b811d73b37805b2816f0b403d0f3cc0ec65fce4d97e38e5c879d8c0e20fef23", "1.10.0--r43hdfd78af_0": "sha256:4536c5efa7d2343e63b06d6970095e549dd3a2aff3184a78047f80f43c482bba", "1.12.0--r43hdfd78af_0": "sha256:c5574cb506df0cfd0bce60d9269aa7b2a4c2088b4d2e11d8698cccf274427edc"}, "docker": "quay.io/biocontainers/bioconductor-tidysummarizedexperiment"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tidysummarizedexperiment.
shpc-registry automated BioContainers addition for bioconductor-tidysummarizedexperiment
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tidysummarizedexperiment
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tidysummarizedexperiment:1.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tidysummarizedexperiment/1.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tidysummarizedexperiment/1.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tidysummarizedexperiment-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tidysummarizedexperiment-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tidysummarizedexperiment-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tidysummarizedexperiment-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tidysummarizedexperiment-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tidysummarizedexperiment-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tidysummarizedexperiment

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