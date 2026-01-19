---
layout: container
name:  "quay.io/biocontainers/bioconductor-globaltest"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-globaltest/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-globaltest/container.yaml"
updated_at: "2026-01-19 04:02:39.183234"
latest: "5.60.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-globaltest"

versions:
 - "5.48.0--r41hdfd78af_0"
 - "5.52.0--r42hdfd78af_0"
 - "5.54.0--r43hdfd78af_0"
 - "5.56.0--r43hdfd78af_0"
 - "5.60.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-globaltest"
config: {"url": "https://biocontainers.pro/tools/bioconductor-globaltest", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-globaltest", "latest": {"5.60.0--r44hdfd78af_0": "sha256:bb5a2df77d6cfc84ffb995f8897c7b6da58c3dfd090d2dfad24b08c6800c0f57"}, "tags": {"5.48.0--r41hdfd78af_0": "sha256:a469741291e12972064393adafd2c398a805a996b3f1d15fee9f0beb4236fc8d", "5.52.0--r42hdfd78af_0": "sha256:e9fddefe78adfecff7e6e477f5953e9d3825c4c6e8c03f96f2339322ab0ec630", "5.54.0--r43hdfd78af_0": "sha256:9c99df0e77d33aad4e874c33fce780dd2ba43fe6adb3f4fd549bf45435eacba7", "5.56.0--r43hdfd78af_0": "sha256:a4aeaad0809c06ace55c441a17c4e925ede6698f392a2c913b35dc37197b947e", "5.60.0--r44hdfd78af_0": "sha256:bb5a2df77d6cfc84ffb995f8897c7b6da58c3dfd090d2dfad24b08c6800c0f57"}, "docker": "quay.io/biocontainers/bioconductor-globaltest"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-globaltest.
shpc-registry automated BioContainers addition for bioconductor-globaltest
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-globaltest
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-globaltest:5.60.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-globaltest/5.60.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-globaltest/5.60.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-globaltest-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-globaltest-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-globaltest-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-globaltest-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-globaltest-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-globaltest-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-globaltest

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