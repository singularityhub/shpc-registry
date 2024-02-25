---
layout: container
name:  "quay.io/biocontainers/bioconductor-orthogene"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-orthogene/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-orthogene/container.yaml"
updated_at: "2024-02-25 02:58:22.420518"
latest: "1.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-orthogene"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-orthogene"
config: {"url": "https://biocontainers.pro/tools/bioconductor-orthogene", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-orthogene", "latest": {"1.8.0--r43hdfd78af_0": "sha256:58480c1380a779f21cd5660e842b3f5a1b35ed2fa3cc6dc1761d59f64f9a3cdd"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:77f45e481512165040cd650ae80b9ddb76bb32fc3d07cd9598f3fd866d699b34", "1.4.0--r42hdfd78af_0": "sha256:7753e61347fe292f90403d9d7204bd31ab166dade9151db468fd22c5b88c024f", "1.6.0--r43hdfd78af_0": "sha256:cb05d333226001d60c4556b7a162bc493c5be198b52e3171f3b36ca4ef869552", "1.8.0--r43hdfd78af_0": "sha256:58480c1380a779f21cd5660e842b3f5a1b35ed2fa3cc6dc1761d59f64f9a3cdd"}, "docker": "quay.io/biocontainers/bioconductor-orthogene"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-orthogene.
shpc-registry automated BioContainers addition for bioconductor-orthogene
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-orthogene
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-orthogene:1.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-orthogene/1.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-orthogene/1.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-orthogene-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-orthogene-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-orthogene-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-orthogene-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-orthogene-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-orthogene-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-orthogene

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