---
layout: container
name:  "quay.io/biocontainers/bioconductor-rbiopaxparser"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rbiopaxparser/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rbiopaxparser/container.yaml"
updated_at: "2025-05-14 03:25:20.809374"
latest: "2.46.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rbiopaxparser"

versions:
 - "2.34.0--r41hdfd78af_0"
 - "2.38.0--r42hdfd78af_0"
 - "2.40.0--r43hdfd78af_0"
 - "2.42.0--r43hdfd78af_0"
 - "2.46.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rbiopaxparser"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rbiopaxparser", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rbiopaxparser", "latest": {"2.46.0--r44hdfd78af_0": "sha256:139322350b085f145803ad4d377edc749fcff81853f23cb45fb8d4f522caf47d"}, "tags": {"2.34.0--r41hdfd78af_0": "sha256:26d4caad7dad9b5cf8686b7e425ac58b8591f64a4d860b17bf4acf22aea137cf", "2.38.0--r42hdfd78af_0": "sha256:2ebcfbcb6d66f90a3bdffd7f0b0ac6e72f5ee576a626d03a990dafc2f7cc8e68", "2.40.0--r43hdfd78af_0": "sha256:93d56c5fb8025ea413d0c8f90fb93effe6dc1d0104b4ca18d3b0c06769f2e055", "2.42.0--r43hdfd78af_0": "sha256:196a37cc4cbc4a7112bffc9ab1f04777d387db149e345dfdc35833faae18b2f7", "2.46.0--r44hdfd78af_0": "sha256:139322350b085f145803ad4d377edc749fcff81853f23cb45fb8d4f522caf47d"}, "docker": "quay.io/biocontainers/bioconductor-rbiopaxparser"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rbiopaxparser.
shpc-registry automated BioContainers addition for bioconductor-rbiopaxparser
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rbiopaxparser
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rbiopaxparser:2.46.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rbiopaxparser/2.46.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rbiopaxparser/2.46.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rbiopaxparser-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rbiopaxparser-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rbiopaxparser-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rbiopaxparser-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rbiopaxparser-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rbiopaxparser-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rbiopaxparser

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