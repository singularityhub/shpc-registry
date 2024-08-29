---
layout: container
name:  "quay.io/biocontainers/bioconductor-txcutr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-txcutr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-txcutr/container.yaml"
updated_at: "2024-08-29 03:15:47.186218"
latest: "1.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-txcutr"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-txcutr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-txcutr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-txcutr", "latest": {"1.8.0--r43hdfd78af_0": "sha256:94a503757229f5a87297c526e9ddb6332b917c352dd3a2034a413a083e37724b"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:27b345fa493c9c9f8952b0a66506d5df258503f951d03f35f778d2b704dc25bf", "1.4.0--r42hdfd78af_0": "sha256:74cf4c3f8b4ff172ecfd0e98aaf82edd9b19020ba7a54e894a797eb07aab9f8a", "1.6.0--r43hdfd78af_0": "sha256:361efa175386f3896ca5e70709bdf4cd2d068725036a23c84b9e9d3896094177", "1.8.0--r43hdfd78af_0": "sha256:94a503757229f5a87297c526e9ddb6332b917c352dd3a2034a413a083e37724b"}, "docker": "quay.io/biocontainers/bioconductor-txcutr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-txcutr.
shpc-registry automated BioContainers addition for bioconductor-txcutr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-txcutr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-txcutr:1.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-txcutr/1.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-txcutr/1.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-txcutr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txcutr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-txcutr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-txcutr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-txcutr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-txcutr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-txcutr

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