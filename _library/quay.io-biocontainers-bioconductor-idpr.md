---
layout: container
name:  "quay.io/biocontainers/bioconductor-idpr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-idpr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-idpr/container.yaml"
updated_at: "2024-03-28 02:29:20.936833"
latest: "1.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-idpr"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-idpr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-idpr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-idpr", "latest": {"1.12.0--r43hdfd78af_0": "sha256:a9615907e24c53015205a978af100bcef28661026d17ae192887d5e601453d07"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:1494c418e3969e247c479f7762d351d129dce498ed614182bb2f94034565f657", "1.8.0--r42hdfd78af_0": "sha256:957ddc2449f66af5a19630ab51105873cae7457b203ae49792c6b5da7571f267", "1.10.0--r43hdfd78af_0": "sha256:b23ff9a1a97eb67781313e164d0a4af1330f6470a391a8ccec16dfcbe3bd25fc", "1.12.0--r43hdfd78af_0": "sha256:a9615907e24c53015205a978af100bcef28661026d17ae192887d5e601453d07"}, "docker": "quay.io/biocontainers/bioconductor-idpr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-idpr.
shpc-registry automated BioContainers addition for bioconductor-idpr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-idpr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-idpr:1.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-idpr/1.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-idpr/1.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-idpr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-idpr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-idpr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-idpr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-idpr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-idpr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-idpr

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