---
layout: container
name:  "quay.io/biocontainers/bioconductor-roseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-roseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-roseq/container.yaml"
updated_at: "2024-01-24 02:41:31.115745"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-roseq"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-roseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-roseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-roseq", "latest": {"1.14.0--r43hdfd78af_0": "sha256:38886fbe8160d10bd30014974d1813f782b7c4e0e3f9c3698b08fb8dfb1f138b"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:2b7f302cda9030ec922b640794b5329e9d91f68a6d26749f2a195e36ac296429", "1.10.0--r42hdfd78af_0": "sha256:19a82e5b05d0ee69244076dc56588ee7f37c19b1969470ab94c0ae7d5a2f3443", "1.12.0--r43hdfd78af_0": "sha256:367ded239fd94b03762970d1e3f0b7c4f662b9b1fbaa3a348559be2740630885", "1.14.0--r43hdfd78af_0": "sha256:38886fbe8160d10bd30014974d1813f782b7c4e0e3f9c3698b08fb8dfb1f138b"}, "docker": "quay.io/biocontainers/bioconductor-roseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-roseq.
shpc-registry automated BioContainers addition for bioconductor-roseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-roseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-roseq:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-roseq/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-roseq/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-roseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-roseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-roseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-roseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-roseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-roseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-roseq

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