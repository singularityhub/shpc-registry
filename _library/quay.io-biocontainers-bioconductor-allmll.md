---
layout: container
name:  "quay.io/biocontainers/bioconductor-allmll"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-allmll/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-allmll/container.yaml"
updated_at: "2025-09-15 03:54:31.803774"
latest: "1.46.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-allmll"

versions:
 - "1.34.0--r41hdfd78af_1"
 - "1.38.0--r42hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
 - "1.46.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-allmll"
config: {"url": "https://biocontainers.pro/tools/bioconductor-allmll", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-allmll", "latest": {"1.46.0--r44hdfd78af_0": "sha256:fa26f23436131dd017b7ab236ed57ec76138d84dd1fd0e5bb4da988d602bad75"}, "tags": {"1.34.0--r41hdfd78af_1": "sha256:ffa43501763ae5711438af0bc857067d8e903ac38257faf6ed966f1c32f459cb", "1.38.0--r42hdfd78af_0": "sha256:e49931c23d4167c04f48b35eec1953585e1daadc79f456621bed9bcc2d36a22f", "1.40.0--r43hdfd78af_0": "sha256:78fad54b728a0bb4080507fc27381cd05b7b2876eb710a82ac6748607ea529e3", "1.42.0--r43hdfd78af_0": "sha256:bc5d498f1c379efc500387df70d6775138e405e7c43fe8857203bb3c740397d4", "1.46.0--r44hdfd78af_0": "sha256:fa26f23436131dd017b7ab236ed57ec76138d84dd1fd0e5bb4da988d602bad75"}, "docker": "quay.io/biocontainers/bioconductor-allmll"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-allmll.
shpc-registry automated BioContainers addition for bioconductor-allmll
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-allmll
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-allmll:1.46.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-allmll/1.46.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-allmll/1.46.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-allmll-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-allmll-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-allmll-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-allmll-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-allmll-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-allmll-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-allmll

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