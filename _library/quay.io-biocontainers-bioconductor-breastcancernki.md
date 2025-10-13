---
layout: container
name:  "quay.io/biocontainers/bioconductor-breastcancernki"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-breastcancernki/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-breastcancernki/container.yaml"
updated_at: "2025-10-13 03:39:46.564819"
latest: "1.44.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-breastcancernki"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.35.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.44.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-breastcancernki"
config: {"url": "https://biocontainers.pro/tools/bioconductor-breastcancernki", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-breastcancernki", "latest": {"1.44.0--r44hdfd78af_0": "sha256:ff13dfaec4d1967e26f4de7953af5e5c2723eb492cb1ff24438d0d2eb6f83200"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:e6eeecf794b2f285d720c10f50f3c8ecef56401cf7b43dc338a59b279f6a1057", "1.35.0--r42hdfd78af_0": "sha256:22dc66ede4c966d38474dd1febb75170d8d4824b0deda97d514de75e71fab49d", "1.38.0--r43hdfd78af_0": "sha256:1147ea5277fc9ac39c2e7aa5409c7685d65ff9d8087ba5b794c24523b80fca70", "1.40.0--r43hdfd78af_0": "sha256:302d3b9a2531ccd00558fc429e27ae743dff95bad7f601b9178fcdc7ffcca153", "1.44.0--r44hdfd78af_0": "sha256:ff13dfaec4d1967e26f4de7953af5e5c2723eb492cb1ff24438d0d2eb6f83200"}, "docker": "quay.io/biocontainers/bioconductor-breastcancernki"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-breastcancernki.
shpc-registry automated BioContainers addition for bioconductor-breastcancernki
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-breastcancernki
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-breastcancernki:1.44.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-breastcancernki/1.44.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-breastcancernki/1.44.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-breastcancernki-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-breastcancernki-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-breastcancernki-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-breastcancernki-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-breastcancernki-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-breastcancernki-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-breastcancernki

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