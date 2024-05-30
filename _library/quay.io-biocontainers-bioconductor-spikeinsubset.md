---
layout: container
name:  "quay.io/biocontainers/bioconductor-spikeinsubset"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-spikeinsubset/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-spikeinsubset/container.yaml"
updated_at: "2024-05-30 04:05:08.513157"
latest: "1.42.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-spikeinsubset"

versions:
 - "1.34.0--r41hdfd78af_1"
 - "1.38.0--r42hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-spikeinsubset"
config: {"url": "https://biocontainers.pro/tools/bioconductor-spikeinsubset", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-spikeinsubset", "latest": {"1.42.0--r43hdfd78af_0": "sha256:c78f6d93e2d6069480cadc205ecc0aff7ccc381db4f6fa70c648d72fa80d38c2"}, "tags": {"1.34.0--r41hdfd78af_1": "sha256:44e1ce82d6e10e687621a6a71af3209af5397d1f9b7474c543647b5a788b8688", "1.38.0--r42hdfd78af_0": "sha256:5645d487eacd3924a41c9748e5f68d12c68fae42b8a4b5e67ba2eb3e7568a71f", "1.40.0--r43hdfd78af_0": "sha256:7961d2e36b5ba8b30772c4e0e1c63468995e76f7daebd1408cfb1fa8cd91ca33", "1.42.0--r43hdfd78af_0": "sha256:c78f6d93e2d6069480cadc205ecc0aff7ccc381db4f6fa70c648d72fa80d38c2"}, "docker": "quay.io/biocontainers/bioconductor-spikeinsubset"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-spikeinsubset.
shpc-registry automated BioContainers addition for bioconductor-spikeinsubset
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-spikeinsubset
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-spikeinsubset:1.42.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-spikeinsubset/1.42.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-spikeinsubset/1.42.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-spikeinsubset-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spikeinsubset-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spikeinsubset-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-spikeinsubset-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-spikeinsubset-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-spikeinsubset-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-spikeinsubset

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