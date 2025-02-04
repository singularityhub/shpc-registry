---
layout: container
name:  "quay.io/biocontainers/bioconductor-biodbkegg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biodbkegg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biodbkegg/container.yaml"
updated_at: "2025-02-04 02:55:31.557471"
latest: "1.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biodbkegg"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-biodbkegg"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biodbkegg", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-biodbkegg", "latest": {"1.8.0--r43hdfd78af_0": "sha256:5d0556d35c73b2e60c0e7292584e4f5dc1823382a2428e7a3b19f40c85e11f5e"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:d899a0fc4deb089b4ee56d0a85b5d2045c4c7440b75d258f9bd789d13b60b819", "1.4.0--r42hdfd78af_0": "sha256:50b16766ab0dfd3b45f68d636e7bc3d89ed688677687389c8ef67c5bf6769c62", "1.6.0--r43hdfd78af_0": "sha256:ed291df848c0fbef0e296e50eef99c1726beb749f534992c330bdc908c39c641", "1.8.0--r43hdfd78af_0": "sha256:5d0556d35c73b2e60c0e7292584e4f5dc1823382a2428e7a3b19f40c85e11f5e"}, "docker": "quay.io/biocontainers/bioconductor-biodbkegg"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biodbkegg.
shpc-registry automated BioContainers addition for bioconductor-biodbkegg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biodbkegg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biodbkegg:1.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biodbkegg/1.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-biodbkegg/1.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biodbkegg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biodbkegg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biodbkegg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biodbkegg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biodbkegg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biodbkegg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-biodbkegg

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