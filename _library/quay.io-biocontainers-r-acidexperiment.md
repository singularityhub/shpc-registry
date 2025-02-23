---
layout: container
name:  "quay.io/biocontainers/r-acidexperiment"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-acidexperiment/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-acidexperiment/container.yaml"
updated_at: "2025-02-23 03:34:41.763062"
latest: "0.5.4--r44hdfd78af_1"
container_url: "https://biocontainers.pro/tools/r-acidexperiment"

versions:
 - "0.3.0--r41hdfd78af_0"
 - "0.4.4--r42hdfd78af_0"
 - "0.4.4--r42hdfd78af_1"
 - "0.4.5--r42hdfd78af_0"
 - "0.4.5--r42hdfd78af_1"
 - "0.4.7--r42hdfd78af_1"
 - "0.4.7--r43hdfd78af_2"
 - "0.5.2--r43hdfd78af_0"
 - "0.5.3--r43hdfd78af_0"
 - "0.5.4--r43hdfd78af_0"
 - "0.5.4--r44hdfd78af_1"
description: "shpc-registry automated BioContainers addition for r-acidexperiment"
config: {"url": "https://biocontainers.pro/tools/r-acidexperiment", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-acidexperiment", "latest": {"0.5.4--r44hdfd78af_1": "sha256:527ac0006de4cc78aaae75431fd67fa024a7762f688f695268d9b617ef76a19e"}, "tags": {"0.3.0--r41hdfd78af_0": "sha256:7f190b21233e13ed428108eed86005c9896f03d82fad42d5c45a5c81252b12a3", "0.4.4--r42hdfd78af_0": "sha256:9ce87bf63b684343a8b113ef9f829b60c53c8064805dce7746ebd1ee9cac6871", "0.4.4--r42hdfd78af_1": "sha256:565b32ae3b62788a82bf497ed2f5b1f948a7586c6ec242a62d410fe95a248de2", "0.4.5--r42hdfd78af_0": "sha256:b80b37a52a231b6fb0f0572ca94db8c2a5491aa811c9625affd6863acbbd5d73", "0.4.5--r42hdfd78af_1": "sha256:53f87b72022e263f79853356f645faff833ff307148a1b235b97288080758b3c", "0.4.7--r42hdfd78af_1": "sha256:24b73ceddfc19f03d640001872d4815ed5567b88aba91edc9d7fde7bac8301d5", "0.4.7--r43hdfd78af_2": "sha256:b7b27dbad41c787f08da962ad2fcbb39c45b803dc96bf0c266dde0358bbd4f4d", "0.5.2--r43hdfd78af_0": "sha256:9193eee4f3c29231af03ba9058a87984e50ea02b2757c8c9907f40fc38035dbb", "0.5.3--r43hdfd78af_0": "sha256:ee3f7d19cf39c4f866a65c441a742cf8b75fdc96b8db3807f9929d28aa46c1ed", "0.5.4--r43hdfd78af_0": "sha256:5715e4570c91c4d85a9b0f1722ee3de455c3013f22378fa4a88cec6743716c83", "0.5.4--r44hdfd78af_1": "sha256:527ac0006de4cc78aaae75431fd67fa024a7762f688f695268d9b617ef76a19e"}, "docker": "quay.io/biocontainers/r-acidexperiment"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-acidexperiment.
shpc-registry automated BioContainers addition for r-acidexperiment
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-acidexperiment
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-acidexperiment:0.5.4--r44hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-acidexperiment/0.5.4--r44hdfd78af_1
$ module help quay.io/biocontainers/r-acidexperiment/0.5.4--r44hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-acidexperiment-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-acidexperiment-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-acidexperiment-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-acidexperiment-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-acidexperiment-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-acidexperiment-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-acidexperiment

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