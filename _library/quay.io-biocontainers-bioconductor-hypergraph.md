---
layout: container
name:  "quay.io/biocontainers/bioconductor-hypergraph"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hypergraph/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hypergraph/container.yaml"
updated_at: "2025-10-28 03:42:18.993348"
latest: "1.78.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-hypergraph"

versions:
 - "1.66.0--r41hdfd78af_0"
 - "1.70.0--r42hdfd78af_0"
 - "1.72.0--r43hdfd78af_0"
 - "1.74.0--r43hdfd78af_0"
 - "1.78.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-hypergraph"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hypergraph", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hypergraph", "latest": {"1.78.0--r44hdfd78af_0": "sha256:7f5bb442a92d46c189853e460479f6fd1012cb261ef74d368a0301d32e3fc64f"}, "tags": {"1.66.0--r41hdfd78af_0": "sha256:ca22484df39003f70ead7a514a4869a995c258c2c023eaab4eea46cea7829dde", "1.70.0--r42hdfd78af_0": "sha256:250cbb57628320ea24ccb3902e6941924e6349e9576667988c821ee927cd01f0", "1.72.0--r43hdfd78af_0": "sha256:c1181a57fffe7ce09918ec4c6c704768985453444d4d1425eed16931e9ef51e8", "1.74.0--r43hdfd78af_0": "sha256:d040dfc036ba5536759b1eeb430270cbe522025679e7c343c884e9ec67810938", "1.78.0--r44hdfd78af_0": "sha256:7f5bb442a92d46c189853e460479f6fd1012cb261ef74d368a0301d32e3fc64f"}, "docker": "quay.io/biocontainers/bioconductor-hypergraph"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hypergraph.
shpc-registry automated BioContainers addition for bioconductor-hypergraph
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hypergraph
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hypergraph:1.78.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hypergraph/1.78.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-hypergraph/1.78.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hypergraph-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hypergraph-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hypergraph-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hypergraph-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hypergraph-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hypergraph-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hypergraph

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