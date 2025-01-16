---
layout: container
name:  "quay.io/biocontainers/bioconductor-apcomplex"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-apcomplex/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-apcomplex/container.yaml"
updated_at: "2025-01-16 03:24:30.340676"
latest: "2.68.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-apcomplex"

versions:
 - "2.60.0--r41hdfd78af_0"
 - "2.64.0--r42hdfd78af_0"
 - "2.66.0--r43hdfd78af_0"
 - "2.68.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-apcomplex"
config: {"url": "https://biocontainers.pro/tools/bioconductor-apcomplex", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-apcomplex", "latest": {"2.68.0--r43hdfd78af_0": "sha256:2d46e331edfdabf44dc43595ef678be4c52f42e14f53d5558a525d6b5be9e631"}, "tags": {"2.60.0--r41hdfd78af_0": "sha256:901e78551a7eefc599920daa63fba64f9c10376e71cbeee57043da8ca635ca66", "2.64.0--r42hdfd78af_0": "sha256:6dfaa8e8b62df3fb9a19f2a333c748ec3fbf8185672537b3c721573445ff3de2", "2.66.0--r43hdfd78af_0": "sha256:a06afd6004fb572f46c7112674bca9627ef5db35a8a663fbe0d1973e8f5794c7", "2.68.0--r43hdfd78af_0": "sha256:2d46e331edfdabf44dc43595ef678be4c52f42e14f53d5558a525d6b5be9e631"}, "docker": "quay.io/biocontainers/bioconductor-apcomplex"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-apcomplex.
shpc-registry automated BioContainers addition for bioconductor-apcomplex
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-apcomplex
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-apcomplex:2.68.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-apcomplex/2.68.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-apcomplex/2.68.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-apcomplex-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-apcomplex-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-apcomplex-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-apcomplex-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-apcomplex-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-apcomplex-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-apcomplex

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