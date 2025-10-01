---
layout: container
name:  "quay.io/biocontainers/bioconductor-sparrow"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sparrow/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sparrow/container.yaml"
updated_at: "2025-10-01 03:23:21.412103"
latest: "1.12.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sparrow"

versions:
 - "1.0.1--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.12.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sparrow"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sparrow", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sparrow", "latest": {"1.12.0--r44hdfd78af_0": "sha256:bd14560fbfc750dfdc54b3680b81e5924fff67301e44b3a3c4e6d548717a4075"}, "tags": {"1.0.1--r41hdfd78af_0": "sha256:f58daa0faeccdeabaff45413439414c42edf545648d3db1da1374dd1c152eb4e", "1.4.0--r42hdfd78af_0": "sha256:ff23e0f82e5c6393f08c3bd4a3dfc18f30325ab5a2939714dbda0b9c55ed3988", "1.6.0--r43hdfd78af_0": "sha256:485c58c00884e5245f26f9388e658c324db238cce159bbc614c5a0b8390a4210", "1.8.0--r43hdfd78af_0": "sha256:a3a87cdfdd2f31da8e0685e38a88171652a498ce394abbeb6ffc591450714d07", "1.12.0--r44hdfd78af_0": "sha256:bd14560fbfc750dfdc54b3680b81e5924fff67301e44b3a3c4e6d548717a4075"}, "docker": "quay.io/biocontainers/bioconductor-sparrow"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sparrow.
shpc-registry automated BioContainers addition for bioconductor-sparrow
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sparrow
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sparrow:1.12.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sparrow/1.12.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-sparrow/1.12.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sparrow-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sparrow-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sparrow-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sparrow-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sparrow-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sparrow-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-sparrow

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