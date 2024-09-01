---
layout: container
name:  "quay.io/biocontainers/bioconductor-gse62944"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gse62944/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gse62944/container.yaml"
updated_at: "2024-09-01 03:40:33.117703"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gse62944"

versions:
 - "1.22.0--r41hdfd78af_1"
 - "1.26.0--r42hdfd78af_0"
 - "1.28.1--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gse62944"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gse62944", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gse62944", "latest": {"1.30.0--r43hdfd78af_0": "sha256:a057c6f1523a089272982490dacec64440d6ed761d8815b3eba6631927fb2846"}, "tags": {"1.22.0--r41hdfd78af_1": "sha256:b87cfa9ce418b24a2ad996de28029eff283108a673a311cecd3b7508c830793a", "1.26.0--r42hdfd78af_0": "sha256:8be8849c43d3629668e5747359c0f8ec9460bb9dfaed87cf31e9898bda47c0fb", "1.28.1--r43hdfd78af_0": "sha256:fa1eadff65a80d1613531bc3d3c200f95ee0a76a4357f0060423d843a37c615b", "1.30.0--r43hdfd78af_0": "sha256:a057c6f1523a089272982490dacec64440d6ed761d8815b3eba6631927fb2846"}, "docker": "quay.io/biocontainers/bioconductor-gse62944"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gse62944.
shpc-registry automated BioContainers addition for bioconductor-gse62944
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gse62944
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gse62944:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gse62944/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gse62944/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gse62944-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gse62944-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gse62944-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gse62944-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gse62944-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gse62944-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gse62944

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