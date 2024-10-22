---
layout: container
name:  "quay.io/biocontainers/bioconductor-human610quadv1bcrlmm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-human610quadv1bcrlmm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-human610quadv1bcrlmm/container.yaml"
updated_at: "2024-10-22 02:57:28.871897"
latest: "1.0.3--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-human610quadv1bcrlmm"

versions:
 - "1.0.3--r41hdfd78af_9"
 - "1.0.3--r42hdfd78af_10"
 - "1.0.3--r43hdfd78af_11"
 - "1.0.3--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-human610quadv1bcrlmm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-human610quadv1bcrlmm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-human610quadv1bcrlmm", "latest": {"1.0.3--r43hdfd78af_12": "sha256:014cae10f5a33ec9e625cd9ce3e49a2a16a955d86f0accc78548988c31f1eda6"}, "tags": {"1.0.3--r41hdfd78af_9": "sha256:62c103401e189a63caeb027c09f29e2c977ee6c6a79a9bc45e8ba4e9ce85210d", "1.0.3--r42hdfd78af_10": "sha256:9bb8f3567a1ec52a27fa104893d95568519c576574ee61af02ddc3354fd6e397", "1.0.3--r43hdfd78af_11": "sha256:e4add668a779fa2b7e5962bd2386161dd335268c1df951844c18dec255b3946b", "1.0.3--r43hdfd78af_12": "sha256:014cae10f5a33ec9e625cd9ce3e49a2a16a955d86f0accc78548988c31f1eda6"}, "docker": "quay.io/biocontainers/bioconductor-human610quadv1bcrlmm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-human610quadv1bcrlmm.
shpc-registry automated BioContainers addition for bioconductor-human610quadv1bcrlmm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-human610quadv1bcrlmm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-human610quadv1bcrlmm:1.0.3--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-human610quadv1bcrlmm/1.0.3--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-human610quadv1bcrlmm/1.0.3--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-human610quadv1bcrlmm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-human610quadv1bcrlmm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-human610quadv1bcrlmm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-human610quadv1bcrlmm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-human610quadv1bcrlmm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-human610quadv1bcrlmm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-human610quadv1bcrlmm

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