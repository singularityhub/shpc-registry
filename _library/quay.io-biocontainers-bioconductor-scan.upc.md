---
layout: container
name:  "quay.io/biocontainers/bioconductor-scan.upc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scan.upc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scan.upc/container.yaml"
updated_at: "2023-09-09 02:47:12.863965"
latest: "2.42.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scan.upc"

versions:
 - "2.36.0--r41hdfd78af_0"
 - "2.40.0--r42hdfd78af_0"
 - "2.42.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scan.upc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scan.upc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scan.upc", "latest": {"2.42.0--r43hdfd78af_0": "sha256:7716b51dbe4103e78c9735412ec91ce404b8546fdc47db66508119d2c21dea10"}, "tags": {"2.36.0--r41hdfd78af_0": "sha256:8a08a64b9a385d2d67c6fb4a14244605331b03c31c4a438378ef2ecc677470af", "2.40.0--r42hdfd78af_0": "sha256:37b87841cd6e5c243a23cd473e1b19e66cab962622afde23fbb208e72d9fc403", "2.42.0--r43hdfd78af_0": "sha256:7716b51dbe4103e78c9735412ec91ce404b8546fdc47db66508119d2c21dea10"}, "docker": "quay.io/biocontainers/bioconductor-scan.upc"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scan.upc.
shpc-registry automated BioContainers addition for bioconductor-scan.upc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scan.upc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scan.upc:2.42.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scan.upc/2.42.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-scan.upc/2.42.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scan.upc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scan.upc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scan.upc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scan.upc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scan.upc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scan.upc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-scan.upc

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