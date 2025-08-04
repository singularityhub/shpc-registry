---
layout: container
name:  "quay.io/biocontainers/bioconductor-pwmenrich.mmusculus.background"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pwmenrich.mmusculus.background/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pwmenrich.mmusculus.background/container.yaml"
updated_at: "2025-08-04 04:15:24.951701"
latest: "4.40.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pwmenrich.mmusculus.background"

versions:
 - "4.28.0--r41hdfd78af_1"
 - "4.32.0--r42hdfd78af_0"
 - "4.34.0--r43hdfd78af_0"
 - "4.36.0--r43hdfd78af_0"
 - "4.40.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pwmenrich.mmusculus.background"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pwmenrich.mmusculus.background", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pwmenrich.mmusculus.background", "latest": {"4.40.0--r44hdfd78af_0": "sha256:dfa2ba8f5ecb1599c38214d89e2aac46214d430199e6be836ef66a78640a0069"}, "tags": {"4.28.0--r41hdfd78af_1": "sha256:6e1c1d74f9cb2b4daedcdf66529325069306b60080e350683d84a55a758aab57", "4.32.0--r42hdfd78af_0": "sha256:b774c181620c2009fe37a04884a3b4b4d7ecabad7f122094b1207a8df1e3820f", "4.34.0--r43hdfd78af_0": "sha256:bd212b9874f833eccee01dc000e02d14e67d0cbab6531d22b175f900ae8e3888", "4.36.0--r43hdfd78af_0": "sha256:9ffbb7a764a8d85ace4a22d6c5cd67a1bc75ebae1ba9ef2b9dc259717b7f13f6", "4.40.0--r44hdfd78af_0": "sha256:dfa2ba8f5ecb1599c38214d89e2aac46214d430199e6be836ef66a78640a0069"}, "docker": "quay.io/biocontainers/bioconductor-pwmenrich.mmusculus.background"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pwmenrich.mmusculus.background.
shpc-registry automated BioContainers addition for bioconductor-pwmenrich.mmusculus.background
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pwmenrich.mmusculus.background
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pwmenrich.mmusculus.background:4.40.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pwmenrich.mmusculus.background/4.40.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pwmenrich.mmusculus.background/4.40.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pwmenrich.mmusculus.background-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pwmenrich.mmusculus.background-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pwmenrich.mmusculus.background-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pwmenrich.mmusculus.background-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pwmenrich.mmusculus.background-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pwmenrich.mmusculus.background-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-pwmenrich.mmusculus.background

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