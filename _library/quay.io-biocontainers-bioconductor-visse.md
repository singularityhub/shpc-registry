---
layout: container
name:  "quay.io/biocontainers/bioconductor-visse"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-visse/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-visse/container.yaml"
updated_at: "2024-01-01 02:38:25.742669"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-visse"

versions:
 - "1.2.2--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-visse"
config: {"url": "https://biocontainers.pro/tools/bioconductor-visse", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-visse", "latest": {"1.10.0--r43hdfd78af_0": "sha256:a6e6ab084e0d77649d3fd0eb4d9c9906e2b0f41008217b5e01c5f6cea9dbc955"}, "tags": {"1.2.2--r41hdfd78af_0": "sha256:0b005632ff78fb32c52954ae2557f944e9ee474e9eeeb7826c6b621a74876193", "1.6.0--r42hdfd78af_0": "sha256:b9419359457d69adc7caf3eb549b1f04de45074c08d42988c2a77f7550486619", "1.8.0--r43hdfd78af_0": "sha256:90317f108a39073503c38c70538cc2a38b9bd1cd207cf9ab035085e822b7146f", "1.10.0--r43hdfd78af_0": "sha256:a6e6ab084e0d77649d3fd0eb4d9c9906e2b0f41008217b5e01c5f6cea9dbc955"}, "docker": "quay.io/biocontainers/bioconductor-visse"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-visse.
shpc-registry automated BioContainers addition for bioconductor-visse
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-visse
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-visse:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-visse/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-visse/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-visse-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-visse-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-visse-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-visse-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-visse-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-visse-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-visse

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