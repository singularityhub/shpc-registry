---
layout: container
name:  "quay.io/biocontainers/bioconductor-test2cdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-test2cdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-test2cdf/container.yaml"
updated_at: "2024-01-29 02:33:32.127391"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-test2cdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-test2cdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-test2cdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-test2cdf", "latest": {"2.18.0--r43hdfd78af_12": "sha256:9e50e5b77db166f746d355377394bf164146ae823ce223d0e76e5ba763c0eece"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:a4e3aacef7bd5551b5bfb622d53ca0d27742a82fe6b8e7c256061b15e0ff2f03", "2.18.0--r42hdfd78af_10": "sha256:100776379785f0b1a2ea1652c37191275df27a187da35a229a3d4b55ef62e2ba", "2.18.0--r43hdfd78af_11": "sha256:d459688e40aaae3c2571f091c65ca815420b1eb36239b94e2f3daafc68b7adf6", "2.18.0--r43hdfd78af_12": "sha256:9e50e5b77db166f746d355377394bf164146ae823ce223d0e76e5ba763c0eece"}, "docker": "quay.io/biocontainers/bioconductor-test2cdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-test2cdf.
shpc-registry automated BioContainers addition for bioconductor-test2cdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-test2cdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-test2cdf:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-test2cdf/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-test2cdf/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-test2cdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-test2cdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-test2cdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-test2cdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-test2cdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-test2cdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-test2cdf

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