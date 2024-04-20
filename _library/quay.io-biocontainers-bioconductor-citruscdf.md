---
layout: container
name:  "quay.io/biocontainers/bioconductor-citruscdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-citruscdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-citruscdf/container.yaml"
updated_at: "2024-04-20 02:44:31.892855"
latest: "2.18.0--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-citruscdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-citruscdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-citruscdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-citruscdf", "latest": {"2.18.0--r43hdfd78af_11": "sha256:3da69ad29d851e3900f4c70026efcb633e4702dfeb411d68a5dcce85416e95f9"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:0e95b90ef0917f2fc185f6f36a8a792ff3dc8cad7d95fd7c9013a067715eb403", "2.18.0--r42hdfd78af_10": "sha256:213996596dd0ae8c52eb07ea5152cf883d67b5d22881a525f2b0a67672a4fe8e", "2.18.0--r43hdfd78af_11": "sha256:3da69ad29d851e3900f4c70026efcb633e4702dfeb411d68a5dcce85416e95f9"}, "docker": "quay.io/biocontainers/bioconductor-citruscdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-citruscdf.
shpc-registry automated BioContainers addition for bioconductor-citruscdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-citruscdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-citruscdf:2.18.0--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-citruscdf/2.18.0--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-citruscdf/2.18.0--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-citruscdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-citruscdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-citruscdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-citruscdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-citruscdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-citruscdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-citruscdf

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