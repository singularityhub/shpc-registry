---
layout: container
name:  "quay.io/biocontainers/bioconductor-tinesath1probe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tinesath1probe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tinesath1probe/container.yaml"
updated_at: "2024-08-02 02:39:18.344444"
latest: "1.40.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tinesath1probe"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tinesath1probe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tinesath1probe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tinesath1probe", "latest": {"1.40.0--r43hdfd78af_0": "sha256:01fbea5841647744ef4ff46c50e19a5269ef2cbaf4394458d183142547bd13d7"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:f38bebb82fe6e946e02669d466cde40afe8d4969c7bf0671e0f09f2cd2120e21", "1.36.0--r42hdfd78af_0": "sha256:c3a81b13aed95256ed338975056d3d5b67c5249cdaee74b0ad04fda09a66f677", "1.38.0--r43hdfd78af_0": "sha256:fcc32d822fa09156352a115a70c801218473159819355b1170c9ca1e164e4d1f", "1.40.0--r43hdfd78af_0": "sha256:01fbea5841647744ef4ff46c50e19a5269ef2cbaf4394458d183142547bd13d7"}, "docker": "quay.io/biocontainers/bioconductor-tinesath1probe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tinesath1probe.
shpc-registry automated BioContainers addition for bioconductor-tinesath1probe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tinesath1probe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tinesath1probe:1.40.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tinesath1probe/1.40.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tinesath1probe/1.40.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tinesath1probe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tinesath1probe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tinesath1probe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tinesath1probe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tinesath1probe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tinesath1probe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tinesath1probe

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