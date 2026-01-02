---
layout: container
name:  "quay.io/biocontainers/bioconductor-rgsea"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rgsea/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rgsea/container.yaml"
updated_at: "2026-01-02 03:51:40.191840"
latest: "1.40.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rgsea"

versions:
 - "1.28.0--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.40.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rgsea"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rgsea", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rgsea", "latest": {"1.40.0--r44hdfd78af_0": "sha256:f588d2c158bfb239add841469885b0be1493cf04d3a7d872955290c9703449c2"}, "tags": {"1.28.0--r41hdfd78af_0": "sha256:cc78820ace565665f92baa7ef969716b4f98158ae7ebb3c4e474ac35ad5dc70b", "1.32.0--r42hdfd78af_0": "sha256:a3bcf217e181bec38694fe8b9769f862ab465320d10251b0125ac5eaa9ab0058", "1.34.0--r43hdfd78af_0": "sha256:2c9135685b60c132927ab6e1189147547738174fd220a0307a4f5ba2f9e60248", "1.36.0--r43hdfd78af_0": "sha256:60dc21a6224bde7f023da5ea357e5f69d107206f7170f58dadffd751ae20290b", "1.40.0--r44hdfd78af_0": "sha256:f588d2c158bfb239add841469885b0be1493cf04d3a7d872955290c9703449c2"}, "docker": "quay.io/biocontainers/bioconductor-rgsea"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rgsea.
shpc-registry automated BioContainers addition for bioconductor-rgsea
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rgsea
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rgsea:1.40.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rgsea/1.40.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rgsea/1.40.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rgsea-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rgsea-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rgsea-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rgsea-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rgsea-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rgsea-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rgsea

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