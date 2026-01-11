---
layout: container
name:  "quay.io/biocontainers/bioconductor-dfp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dfp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dfp/container.yaml"
updated_at: "2026-01-11 03:56:30.902768"
latest: "1.64.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dfp"

versions:
 - "1.52.0--r41hdfd78af_0"
 - "1.56.0--r42hdfd78af_0"
 - "1.58.0--r43hdfd78af_0"
 - "1.60.0--r43hdfd78af_0"
 - "1.64.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dfp"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dfp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dfp", "latest": {"1.64.0--r44hdfd78af_0": "sha256:c070f3b4bcae0491a8d679be354367926278d81f04da8edb2920d381ed97b10a"}, "tags": {"1.52.0--r41hdfd78af_0": "sha256:6ce737d366c1159e727827a638834e918b03712ba8fc47f796d7d77907123e0e", "1.56.0--r42hdfd78af_0": "sha256:29ab07f6cc4fe8dc003411716ab22489d6b27ae69538cadf6a8dceeb03519264", "1.58.0--r43hdfd78af_0": "sha256:f650b9a24a6c725931abeeb45322ef7bf9ed8e61c8183f5a569ba25e36205732", "1.60.0--r43hdfd78af_0": "sha256:cf0a06e72afe227a81dff501e58fcf1cf9a6c32a61ef722716bb7e811a64ed9f", "1.64.0--r44hdfd78af_0": "sha256:c070f3b4bcae0491a8d679be354367926278d81f04da8edb2920d381ed97b10a"}, "docker": "quay.io/biocontainers/bioconductor-dfp"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dfp.
shpc-registry automated BioContainers addition for bioconductor-dfp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dfp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dfp:1.64.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dfp/1.64.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-dfp/1.64.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dfp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dfp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dfp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dfp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dfp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dfp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-dfp

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