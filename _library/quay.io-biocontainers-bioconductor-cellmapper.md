---
layout: container
name:  "quay.io/biocontainers/bioconductor-cellmapper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cellmapper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cellmapper/container.yaml"
updated_at: "2025-12-17 03:27:08.930274"
latest: "1.32.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cellmapper"

versions:
 - "1.8.0--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40_0"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.32.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cellmapper"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cellmapper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cellmapper", "latest": {"1.32.0--r44hdfd78af_0": "sha256:4b89f667b132dcd7575325a7b1f11b9abc7e771f4e88251ab079fca29c6cc6c1"}, "tags": {"1.8.0--r351_0": "sha256:e9ec50d1cdad961b058b4b2a994789c80df26f7c3221466f4629bc560cdcaf97", "1.24.0--r42hdfd78af_0": "sha256:2e4078371fb3c499c49a4782128b408d2d178d9a50fcbe029275bedb69f945d3", "1.20.0--r41hdfd78af_0": "sha256:75445244376a00c71453a27eef5b855292a67274559acdfcbe8df7bbe57de814", "1.18.0--r41hdfd78af_0": "sha256:04b8ecc8aff22afb7464dfbd74849d4f7432e6dedba435d1473d7aad1ca9923d", "1.16.0--r40_0": "sha256:9227920889848aefb0cdf9d6579b4043ca4bf8128df58a80abeb17eec040d0d4", "1.14.0--r40_0": "sha256:095b05d5438657d81569e53b2e843658ab401073378973981d69ad61d168746d", "1.26.0--r43hdfd78af_0": "sha256:46859a1c898f39416c48476bf98ec1e4fd26bbb98c9e0558b1261aa724e4e680", "1.28.0--r43hdfd78af_0": "sha256:44a6e61541fbca2de61f22785ef919d9450e1f7824266a5d46f896cd626ef6f4", "1.32.0--r44hdfd78af_0": "sha256:4b89f667b132dcd7575325a7b1f11b9abc7e771f4e88251ab079fca29c6cc6c1"}, "docker": "quay.io/biocontainers/bioconductor-cellmapper"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cellmapper.
shpc-registry automated BioContainers addition for bioconductor-cellmapper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cellmapper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cellmapper:1.32.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cellmapper/1.32.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cellmapper/1.32.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cellmapper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cellmapper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cellmapper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cellmapper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cellmapper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cellmapper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cellmapper

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