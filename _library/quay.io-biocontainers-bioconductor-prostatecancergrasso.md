---
layout: container
name:  "quay.io/biocontainers/bioconductor-prostatecancergrasso"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-prostatecancergrasso/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-prostatecancergrasso/container.yaml"
updated_at: "2025-05-19 03:35:19.861455"
latest: "1.34.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-prostatecancergrasso"

versions:
 - "1.22.0--r41hdfd78af_1"
 - "1.26.0--r42hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
 - "1.34.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-prostatecancergrasso"
config: {"url": "https://biocontainers.pro/tools/bioconductor-prostatecancergrasso", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-prostatecancergrasso", "latest": {"1.34.0--r44hdfd78af_0": "sha256:0e99741d91edeacd659c19df5a598144e74200d8d44d12075695c737601724b3"}, "tags": {"1.22.0--r41hdfd78af_1": "sha256:4fa20e2828c1d9a258d48b43f37410501e61785940c173506e04fa8fec856521", "1.26.0--r42hdfd78af_0": "sha256:3ebd31ef7e47df394b2b0220ab2d12723d0c8563fbfec761ff0a3abfa2a1fcfe", "1.28.0--r43hdfd78af_0": "sha256:ac727333b02759be69bd8e370adf00d8f96203113e3f8873a3a3462fa9fa446a", "1.30.0--r43hdfd78af_0": "sha256:d82f66dcd6dc70f664ad18e7772b5836fe00d56e06446b12adf5f2aedd97ece0", "1.34.0--r44hdfd78af_0": "sha256:0e99741d91edeacd659c19df5a598144e74200d8d44d12075695c737601724b3"}, "docker": "quay.io/biocontainers/bioconductor-prostatecancergrasso"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-prostatecancergrasso.
shpc-registry automated BioContainers addition for bioconductor-prostatecancergrasso
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-prostatecancergrasso
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-prostatecancergrasso:1.34.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-prostatecancergrasso/1.34.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-prostatecancergrasso/1.34.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-prostatecancergrasso-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-prostatecancergrasso-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-prostatecancergrasso-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-prostatecancergrasso-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-prostatecancergrasso-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-prostatecancergrasso-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-prostatecancergrasso

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