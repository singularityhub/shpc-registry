---
layout: container
name:  "quay.io/biocontainers/bioconductor-dittoseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dittoseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dittoseq/container.yaml"
updated_at: "2023-03-29 00:22:08.012090"
latest: "1.10.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dittoseq"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dittoseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dittoseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dittoseq", "latest": {"1.10.0--r42hdfd78af_0": "sha256:45a3974b1cbd070565e9f0902e96848df4c210a44b38cd5436eee5510b71ba60"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:4496821416aef5cc939f99aaed99f50ef450f4355f8dbd0cae69a0a88929c7cf", "1.10.0--r42hdfd78af_0": "sha256:45a3974b1cbd070565e9f0902e96848df4c210a44b38cd5436eee5510b71ba60"}, "docker": "quay.io/biocontainers/bioconductor-dittoseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dittoseq.
shpc-registry automated BioContainers addition for bioconductor-dittoseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dittoseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dittoseq:1.10.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dittoseq/1.10.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-dittoseq/1.10.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dittoseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dittoseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dittoseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dittoseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dittoseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dittoseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-dittoseq

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