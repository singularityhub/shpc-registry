---
layout: container
name:  "quay.io/biocontainers/bioconductor-ath1121501probe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ath1121501probe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ath1121501probe/container.yaml"
updated_at: "2024-03-23 02:42:08.770017"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-ath1121501probe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-ath1121501probe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ath1121501probe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ath1121501probe", "latest": {"2.18.0--r43hdfd78af_12": "sha256:ac33651b18798b8fc5f05d20c974854642a3e9c33a19fda527f52183ddb36737"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:91f6c22bfcbcc303087aec4c9d9b2439d7239187b8d9d7430dd7ad1442a0d100", "2.18.0--r42hdfd78af_10": "sha256:6f1117575c69e1d4e787e131fb325e70da8a579baa0e30f94bdb62a49604c97a", "2.18.0--r43hdfd78af_11": "sha256:9548f8b18a615dbbec8485d05a502e41287472be303bfc9619c1e5912a7f8ffe", "2.18.0--r43hdfd78af_12": "sha256:ac33651b18798b8fc5f05d20c974854642a3e9c33a19fda527f52183ddb36737"}, "docker": "quay.io/biocontainers/bioconductor-ath1121501probe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ath1121501probe.
shpc-registry automated BioContainers addition for bioconductor-ath1121501probe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ath1121501probe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ath1121501probe:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ath1121501probe/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-ath1121501probe/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ath1121501probe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ath1121501probe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ath1121501probe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ath1121501probe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ath1121501probe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ath1121501probe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ath1121501probe

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