---
layout: container
name:  "quay.io/biocontainers/bioconductor-jaspar2018"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-jaspar2018/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-jaspar2018/container.yaml"
updated_at: "2025-12-13 04:02:30.236752"
latest: "1.1.1--r44hdfd78af_14"
container_url: "https://biocontainers.pro/tools/bioconductor-jaspar2018"

versions:
 - "1.1.1--r41hdfd78af_9"
 - "1.1.1--r41hdfd78af_10"
 - "1.1.1--r42hdfd78af_11"
 - "1.1.1--r43hdfd78af_12"
 - "1.1.1--r43hdfd78af_13"
 - "1.1.1--r44hdfd78af_14"
description: "shpc-registry automated BioContainers addition for bioconductor-jaspar2018"
config: {"url": "https://biocontainers.pro/tools/bioconductor-jaspar2018", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-jaspar2018", "latest": {"1.1.1--r44hdfd78af_14": "sha256:afa33bc6c1a5b973be6999c2264223be640bd9a815d5049809c5e03d2bb8a463"}, "tags": {"1.1.1--r41hdfd78af_9": "sha256:0c1156523c2fe1a0960597e2591ad3d6f612d991dee427d611169979d03ad147", "1.1.1--r41hdfd78af_10": "sha256:07564c3abd9023ce9bf6a65ac11b7bbb1ea359a337e9fdfff14c23627669cbee", "1.1.1--r42hdfd78af_11": "sha256:ff36bf60f5fd3906e7e069c8bb0b4e5512d2f1dccfc3c2bcbc6e92f9069e166a", "1.1.1--r43hdfd78af_12": "sha256:54bcdcc058f4a2bcea2ed432ee7fea1eaaf56205cfe2f25e877ec014b2125979", "1.1.1--r43hdfd78af_13": "sha256:c3253ef96228dd07bc42ddbe40f265d4096e99694cf7b6155255bbaf942a7e7c", "1.1.1--r44hdfd78af_14": "sha256:afa33bc6c1a5b973be6999c2264223be640bd9a815d5049809c5e03d2bb8a463"}, "docker": "quay.io/biocontainers/bioconductor-jaspar2018"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-jaspar2018.
shpc-registry automated BioContainers addition for bioconductor-jaspar2018
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-jaspar2018
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-jaspar2018:1.1.1--r44hdfd78af_14
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-jaspar2018/1.1.1--r44hdfd78af_14
$ module help quay.io/biocontainers/bioconductor-jaspar2018/1.1.1--r44hdfd78af_14
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-jaspar2018-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-jaspar2018-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-jaspar2018-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-jaspar2018-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-jaspar2018-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-jaspar2018-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-jaspar2018

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