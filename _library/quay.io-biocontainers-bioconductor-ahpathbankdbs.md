---
layout: container
name:  "quay.io/biocontainers/bioconductor-ahpathbankdbs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ahpathbankdbs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ahpathbankdbs/container.yaml"
updated_at: "2024-09-30 04:15:06.770727"
latest: "0.99.5--r43hdfd78af_5"
container_url: "https://biocontainers.pro/tools/bioconductor-ahpathbankdbs"

versions:
 - "0.99.5--r41hdfd78af_2"
 - "0.99.5--r42hdfd78af_3"
 - "0.99.5--r43hdfd78af_4"
 - "0.99.5--r43hdfd78af_5"
description: "shpc-registry automated BioContainers addition for bioconductor-ahpathbankdbs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ahpathbankdbs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ahpathbankdbs", "latest": {"0.99.5--r43hdfd78af_5": "sha256:b0be4625d6ac683b650419d5aebd0fd950ff4936dd4c3ce0b604b861c4ce5532"}, "tags": {"0.99.5--r41hdfd78af_2": "sha256:567ecb8989f79ce36d7cce929135cee42fc9289e1bcf7df406cd9caec8696069", "0.99.5--r42hdfd78af_3": "sha256:93e11561c0a63f098edcf79713b48b3feb8ff32eb22315601f40298268dc77b5", "0.99.5--r43hdfd78af_4": "sha256:d0a6ed567d1d4f127acd6503640f6b6557a50cd81a5a216add859ebbaf6d2af2", "0.99.5--r43hdfd78af_5": "sha256:b0be4625d6ac683b650419d5aebd0fd950ff4936dd4c3ce0b604b861c4ce5532"}, "docker": "quay.io/biocontainers/bioconductor-ahpathbankdbs"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ahpathbankdbs.
shpc-registry automated BioContainers addition for bioconductor-ahpathbankdbs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ahpathbankdbs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ahpathbankdbs:0.99.5--r43hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ahpathbankdbs/0.99.5--r43hdfd78af_5
$ module help quay.io/biocontainers/bioconductor-ahpathbankdbs/0.99.5--r43hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ahpathbankdbs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ahpathbankdbs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ahpathbankdbs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ahpathbankdbs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ahpathbankdbs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ahpathbankdbs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ahpathbankdbs

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