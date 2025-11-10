---
layout: container
name:  "quay.io/biocontainers/bioconductor-a4"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-a4/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-a4/container.yaml"
updated_at: "2025-11-10 03:32:36.561269"
latest: "1.54.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-a4"

versions:
 - "1.42.0--r41hdfd78af_0"
 - "1.46.0--r42hdfd78af_0"
 - "1.48.0--r43hdfd78af_0"
 - "1.50.0--r43hdfd78af_0"
 - "1.54.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-a4"
config: {"url": "https://biocontainers.pro/tools/bioconductor-a4", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-a4", "latest": {"1.54.0--r44hdfd78af_0": "sha256:13ef60a586c7de7ff69dd6007e30c74792a1354b0763206109ab69e48beac178"}, "tags": {"1.42.0--r41hdfd78af_0": "sha256:c9c9eafd3a8d51ff88586547996dabf58c08c3783a2c47ced4b7e26db0d63bb6", "1.46.0--r42hdfd78af_0": "sha256:8b73e639dc754654c808ed8759865ac2e051874bc92e9b750e00cac04ff77de5", "1.48.0--r43hdfd78af_0": "sha256:613fd1a79f18dd4eedf0a4c2b379a08b6cbaf94d475e2ebe0fb25163bcc167bb", "1.50.0--r43hdfd78af_0": "sha256:0e55109d79edde4da1a1e94b6a45de0166a851255b26cf9d405f06a08a289109", "1.54.0--r44hdfd78af_0": "sha256:13ef60a586c7de7ff69dd6007e30c74792a1354b0763206109ab69e48beac178"}, "docker": "quay.io/biocontainers/bioconductor-a4"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-a4.
shpc-registry automated BioContainers addition for bioconductor-a4
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-a4
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-a4:1.54.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-a4/1.54.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-a4/1.54.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-a4-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-a4-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-a4-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-a4-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-a4-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-a4-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-a4

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