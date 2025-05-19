---
layout: container
name:  "quay.io/biocontainers/bioconductor-bayesknockdown"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bayesknockdown/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bayesknockdown/container.yaml"
updated_at: "2025-05-19 04:02:11.124123"
latest: "1.32.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bayesknockdown"
aliases:
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.32.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bayesknockdown"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bayesknockdown", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bayesknockdown", "latest": {"1.32.0--r44hdfd78af_0": "sha256:6b3497b99678b0376c778b89605832f06068a74e0cd7196b4dd8bd1ff3d05303"}, "tags": {"1.8.0--r351_0": "sha256:5f4a55061ccf1fc43f93dbc34bbf886dd9d4fd6cef7e35159e4fb32cf9c993ab", "1.24.0--r42hdfd78af_0": "sha256:a7a263fd970fa05bdd2bb8e816c9887a60ee8dd05e69c2c2731e2f88c5c09594", "1.20.0--r41hdfd78af_0": "sha256:65b079f28689dc0908108120a5e469fd10ce5793df3b7b7b6b92e6e15d86b1b4", "1.18.0--r41hdfd78af_0": "sha256:1c4f857fe4255a75ddfbf28366db154436d3890c36a6661bdab137048974e679", "1.16.0--r40hdfd78af_1": "sha256:83749b8d89359b704dd06d6b0ad0cb0b5c6b1add6b1e892619bf62a20a43b448", "1.14.0--r40_0": "sha256:06232ee75e4e345c3d2ee79f135d8bfd1cba85a3fc6e193e2e6bb0f248f4f824", "1.26.0--r43hdfd78af_0": "sha256:f540c86cc98b563f82c978e46735f9fc59ffc7bfff46e09e0b9b5908c4d6b12f", "1.28.0--r43hdfd78af_0": "sha256:c62b584f28fbc450525ccd13f3d77213d6c8bcd3153826fcdda0f01aedcb52d0", "1.32.0--r44hdfd78af_0": "sha256:6b3497b99678b0376c778b89605832f06068a74e0cd7196b4dd8bd1ff3d05303"}, "docker": "quay.io/biocontainers/bioconductor-bayesknockdown", "aliases": {"c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bayesknockdown.
shpc-registry automated BioContainers addition for bioconductor-bayesknockdown
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bayesknockdown
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bayesknockdown:1.32.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bayesknockdown/1.32.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-bayesknockdown/1.32.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bayesknockdown-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bayesknockdown-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bayesknockdown-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bayesknockdown-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bayesknockdown-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bayesknockdown-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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