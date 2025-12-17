---
layout: container
name:  "quay.io/biocontainers/bioconductor-pasillatranscriptexpr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pasillatranscriptexpr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pasillatranscriptexpr/container.yaml"
updated_at: "2025-12-17 16:20:56.590975"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pasillatranscriptexpr"

versions:
 - "1.22.0--r41hdfd78af_1"
 - "1.25.0--r42hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pasillatranscriptexpr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pasillatranscriptexpr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pasillatranscriptexpr", "latest": {"1.30.0--r43hdfd78af_0": "sha256:e7aa8a69532683edf59ec712f16479b6de6868f65bd3297b1b64aedf662b51a4"}, "tags": {"1.22.0--r41hdfd78af_1": "sha256:ad324b12d278d0a46e40c9926245986b3588ad167a8cc45f57edac96e82d9c21", "1.25.0--r42hdfd78af_0": "sha256:6b9d7f7ccfed02c4815ac29f42fd2f700c5630e03002a3c26b6dba0963382dd8", "1.28.0--r43hdfd78af_0": "sha256:48c288781059e7e13bfec7fca66d9a46e0088a1ab8d5f0cc75c325d35c1847d7", "1.30.0--r43hdfd78af_0": "sha256:e7aa8a69532683edf59ec712f16479b6de6868f65bd3297b1b64aedf662b51a4"}, "docker": "quay.io/biocontainers/bioconductor-pasillatranscriptexpr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pasillatranscriptexpr.
shpc-registry automated BioContainers addition for bioconductor-pasillatranscriptexpr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pasillatranscriptexpr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pasillatranscriptexpr:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pasillatranscriptexpr/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pasillatranscriptexpr/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pasillatranscriptexpr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pasillatranscriptexpr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pasillatranscriptexpr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pasillatranscriptexpr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pasillatranscriptexpr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pasillatranscriptexpr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-pasillatranscriptexpr

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