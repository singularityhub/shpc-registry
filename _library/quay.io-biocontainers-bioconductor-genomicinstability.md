---
layout: container
name:  "quay.io/biocontainers/bioconductor-genomicinstability"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genomicinstability/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genomicinstability/container.yaml"
updated_at: "2024-11-27 03:16:04.093437"
latest: "1.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-genomicinstability"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-genomicinstability"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genomicinstability", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genomicinstability", "latest": {"1.8.0--r43hdfd78af_0": "sha256:fbd2a0aebec9c4b7080ef81c3063c4d5207a7b3344c2a3543328640e8d4bbf44"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:b2dfa52c92271683a44b6d4ce4e18cbc16ee3eb4b779474b45d9e327e0dfa54e", "1.4.0--r42hdfd78af_0": "sha256:7ae3e92a9241414c1446947ae77cdf81e66403bd51092639d219992cea2791da", "1.6.0--r43hdfd78af_0": "sha256:7468e3ced7b494900242a106d61d33877f874d9b93c36fce5d631f1581f61810", "1.8.0--r43hdfd78af_0": "sha256:fbd2a0aebec9c4b7080ef81c3063c4d5207a7b3344c2a3543328640e8d4bbf44"}, "docker": "quay.io/biocontainers/bioconductor-genomicinstability"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genomicinstability.
shpc-registry automated BioContainers addition for bioconductor-genomicinstability
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genomicinstability
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genomicinstability:1.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genomicinstability/1.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-genomicinstability/1.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genomicinstability-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genomicinstability-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genomicinstability-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genomicinstability-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genomicinstability-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genomicinstability-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-genomicinstability

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