---
layout: container
name:  "quay.io/biocontainers/bioconductor-multimir"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-multimir/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-multimir/container.yaml"
updated_at: "2024-12-18 03:01:48.126208"
latest: "1.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-multimir"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.6.0--r36_1"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.0--r40hdfd78af_1"
 - "1.10.0--r40_0"
 - "1.20.0--r42hdfd78af_0"
 - "1.22.0--r43hdfd78af_0"
 - "1.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-multimir"
config: {"url": "https://biocontainers.pro/tools/bioconductor-multimir", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-multimir", "latest": {"1.24.0--r43hdfd78af_0": "sha256:a7809034218c0418b93772a80418cf391a06b2d33966a83ace91ad7b2e93a6cf"}, "tags": {"1.6.0--r36_1": "sha256:9f517d9bf37c5c28ed52230b71075e475059b6269245b5f7f410425c8b678daf", "1.16.0--r41hdfd78af_0": "sha256:a1a23ea8dd61b2bd47501be8252f05c1dd3589a96520c0ecd62f1e9835f33123", "1.14.0--r41hdfd78af_0": "sha256:a24e216e5a3e1f55b72fadc7fb3b1365003bfb2b455daf49c4a9ea6b3fc382c7", "1.12.0--r40hdfd78af_1": "sha256:ea8af6016eea8461a2dff76e2a744ceda7c4b940b7dbfdf9ce542def696b3d01", "1.10.0--r40_0": "sha256:bdf2247f66717b9ffc8d37ce9d58ae4199cca4d2c8f64781f40d19b5699fd6a5", "1.20.0--r42hdfd78af_0": "sha256:9cf79b19cf95bc9e2b1fc82f4cbabc5291d2102d1fcff3b2ff3b81456432672d", "1.22.0--r43hdfd78af_0": "sha256:73a8d0f48bdd2e5612d5b250900016cba4f58bd196dabbfc48c6b8f001ef09e2", "1.24.0--r43hdfd78af_0": "sha256:a7809034218c0418b93772a80418cf391a06b2d33966a83ace91ad7b2e93a6cf"}, "docker": "quay.io/biocontainers/bioconductor-multimir", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-multimir.
shpc-registry automated BioContainers addition for bioconductor-multimir
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-multimir
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-multimir:1.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-multimir/1.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-multimir/1.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-multimir-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-multimir-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-multimir-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-multimir-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-multimir-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-multimir-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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