---
layout: container
name:  "quay.io/biocontainers/bioconductor-gviz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gviz/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gviz/container.yaml"
updated_at: "2025-02-27 03:34:31.063603"
latest: "1.50.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gviz"

versions:
 - "1.38.0--r41hdfd78af_0"
 - "1.42.0--r42hdfd78af_0"
 - "1.44.0--r43hdfd78af_0"
 - "1.46.1--r43hdfd78af_0"
 - "1.50.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gviz"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gviz", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gviz", "latest": {"1.50.0--r44hdfd78af_0": "sha256:78a151f26d0de42b4fc239862a17afe0e5b93c715619b02da5f63943c43dcbf9"}, "tags": {"1.38.0--r41hdfd78af_0": "sha256:15f3042268d5ef5068c8dd9d58dd7da7aa39c530337a0463ea06973d5d584239", "1.42.0--r42hdfd78af_0": "sha256:656a7e8af331f506ba18cafd773c4cd1611df2121319acd23525ffa519415d45", "1.44.0--r43hdfd78af_0": "sha256:b251901830cbd27bd6276117499e0c48d685de48dd66ffd0eea660bb078cc7fe", "1.46.1--r43hdfd78af_0": "sha256:4c07a57613dc453d69792e1e873ec9c1791016d7707b0aa26e58eb997d16e7c9", "1.50.0--r44hdfd78af_0": "sha256:78a151f26d0de42b4fc239862a17afe0e5b93c715619b02da5f63943c43dcbf9"}, "docker": "quay.io/biocontainers/bioconductor-gviz"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gviz.
shpc-registry automated BioContainers addition for bioconductor-gviz
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gviz
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gviz:1.50.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gviz/1.50.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gviz/1.50.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gviz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gviz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gviz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gviz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gviz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gviz-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gviz

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