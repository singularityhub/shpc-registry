---
layout: container
name:  "quay.io/biocontainers/bioconductor-gsgalgor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gsgalgor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gsgalgor/container.yaml"
updated_at: "2023-08-04 03:02:48.621218"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gsgalgor"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gsgalgor"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gsgalgor", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gsgalgor", "latest": {"1.10.0--r43hdfd78af_0": "sha256:3f8336d336d9be559f07846ef2cf346dce395d8e48941de3644f3f2190f6deba"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:e6607565cf328cb3501616df3c7b2065dd3ab4cb65c0aef41c7854262eaa515a", "1.8.0--r42hdfd78af_0": "sha256:35aeb1e32f03235a8242c8fdafe8ff42961027e640ac74263baf6fd9a3305c6c", "1.10.0--r43hdfd78af_0": "sha256:3f8336d336d9be559f07846ef2cf346dce395d8e48941de3644f3f2190f6deba"}, "docker": "quay.io/biocontainers/bioconductor-gsgalgor"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gsgalgor.
shpc-registry automated BioContainers addition for bioconductor-gsgalgor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gsgalgor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gsgalgor:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gsgalgor/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gsgalgor/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gsgalgor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gsgalgor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gsgalgor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gsgalgor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gsgalgor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gsgalgor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gsgalgor

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