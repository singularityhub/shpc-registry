---
layout: container
name:  "quay.io/biocontainers/bioconductor-polyester"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-polyester/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-polyester/container.yaml"
updated_at: "2025-12-17 04:09:24.503054"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-polyester"

versions:
 - "1.30.0--r41hdfd78af_0"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-polyester"
config: {"url": "https://biocontainers.pro/tools/bioconductor-polyester", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-polyester", "latest": {"1.38.0--r43hdfd78af_0": "sha256:b83aa57d41726b3d380849a274ae7664b677532755fb182b5f1f12b2d26a895b"}, "tags": {"1.30.0--r41hdfd78af_0": "sha256:1680fe0290d01b1c9b26ab26792625dd4780e9d0e7c62762d0858dc20617ce0c", "1.34.0--r42hdfd78af_0": "sha256:731c182db21204246464c54eeb4b4bbe4a474d70c31be76f969739336d892087", "1.36.0--r43hdfd78af_0": "sha256:bcf7612cc330c8fe57d45168f8a174161c990bdee01914566a7a1927f2fa2b12", "1.38.0--r43hdfd78af_0": "sha256:b83aa57d41726b3d380849a274ae7664b677532755fb182b5f1f12b2d26a895b"}, "docker": "quay.io/biocontainers/bioconductor-polyester"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-polyester.
shpc-registry automated BioContainers addition for bioconductor-polyester
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-polyester
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-polyester:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-polyester/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-polyester/1.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-polyester-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-polyester-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-polyester-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-polyester-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-polyester-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-polyester-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-polyester

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