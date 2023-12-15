---
layout: container
name:  "quay.io/biocontainers/bioconductor-mircompdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mircompdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mircompdata/container.yaml"
updated_at: "2023-12-15 02:51:50.852751"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mircompdata"

versions:
 - "1.24.0--r41hdfd78af_1"
 - "1.28.0--r42hdfd78af_0"
 - "1.27.0--r42hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mircompdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mircompdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mircompdata", "latest": {"1.30.0--r43hdfd78af_0": "sha256:96948737167db6e595e157c61c704324f10e4c68c4249aabb1f03d23b06cf6eb"}, "tags": {"1.24.0--r41hdfd78af_1": "sha256:eabcd08fa8d7ebbe98e80dbba2b412d1a90af00f1baebc63635dd41cd5323d2c", "1.28.0--r42hdfd78af_0": "sha256:d9e0ddc2b414f9b4943a1d22052b4aff3d06d93b1a7a5a720f069412334f4966", "1.27.0--r42hdfd78af_0": "sha256:440451d920163e217be7fec549afd3d60c54230fc6f1e72a637e0817a756a182", "1.30.0--r43hdfd78af_0": "sha256:96948737167db6e595e157c61c704324f10e4c68c4249aabb1f03d23b06cf6eb"}, "docker": "quay.io/biocontainers/bioconductor-mircompdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mircompdata.
shpc-registry automated BioContainers addition for bioconductor-mircompdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mircompdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mircompdata:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mircompdata/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mircompdata/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mircompdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mircompdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mircompdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mircompdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mircompdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mircompdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mircompdata

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