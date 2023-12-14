---
layout: container
name:  "quay.io/biocontainers/bioconductor-icens"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-icens/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-icens/container.yaml"
updated_at: "2023-12-14 03:30:17.283906"
latest: "1.72.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-icens"

versions:
 - "1.66.0--r41hdfd78af_0"
 - "1.70.0--r42hdfd78af_0"
 - "1.72.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-icens"
config: {"url": "https://biocontainers.pro/tools/bioconductor-icens", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-icens", "latest": {"1.72.0--r43hdfd78af_0": "sha256:87e3ed0391f27581c516cdf59f305bc7f4576f5c9cf49a5208db3884d33b5bf1"}, "tags": {"1.66.0--r41hdfd78af_0": "sha256:2229bbad90473854767686694d3bb49f3e2dd24c6e58dc8f506b1f298512b68c", "1.70.0--r42hdfd78af_0": "sha256:c3153b6e4454a2bd443cb714cc3f0999977e2f6451691311921fcf5e7730158e", "1.72.0--r43hdfd78af_0": "sha256:87e3ed0391f27581c516cdf59f305bc7f4576f5c9cf49a5208db3884d33b5bf1"}, "docker": "quay.io/biocontainers/bioconductor-icens"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-icens.
shpc-registry automated BioContainers addition for bioconductor-icens
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-icens
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-icens:1.72.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-icens/1.72.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-icens/1.72.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-icens-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-icens-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-icens-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-icens-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-icens-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-icens-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-icens

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