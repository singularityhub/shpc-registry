---
layout: container
name:  "quay.io/biocontainers/bioconductor-graphite"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-graphite/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-graphite/container.yaml"
updated_at: "2025-10-28 03:22:54.396289"
latest: "1.52.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-graphite"

versions:
 - "1.40.0--r41hdfd78af_0"
 - "1.44.0--r42hdfd78af_0"
 - "1.46.0--r43hdfd78af_0"
 - "1.48.0--r43hdfd78af_0"
 - "1.52.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-graphite"
config: {"url": "https://biocontainers.pro/tools/bioconductor-graphite", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-graphite", "latest": {"1.52.0--r44hdfd78af_0": "sha256:d769fba7d5371a5a55376918cf7c5dc20c85f9e86c734dd8770b4d1385ac9f89"}, "tags": {"1.40.0--r41hdfd78af_0": "sha256:2b3a965bf006074d7d28fe494fa91e311cc02cc043f33427d40ad245bb570b17", "1.44.0--r42hdfd78af_0": "sha256:fd1cfedb55bc64e1ea4ef38f6e12bf5829d889d6b473bc2a8d51d0d3be1f30cc", "1.46.0--r43hdfd78af_0": "sha256:da72cf06d21912b4e3c9b4f1c0abd4c62284484d7815afaafa4ed6f0bd9dd397", "1.48.0--r43hdfd78af_0": "sha256:de155c8fa546bc1532766897deeec026ee86aaade6675b526639113c46b6cf50", "1.52.0--r44hdfd78af_0": "sha256:d769fba7d5371a5a55376918cf7c5dc20c85f9e86c734dd8770b4d1385ac9f89"}, "docker": "quay.io/biocontainers/bioconductor-graphite"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-graphite.
shpc-registry automated BioContainers addition for bioconductor-graphite
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-graphite
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-graphite:1.52.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-graphite/1.52.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-graphite/1.52.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-graphite-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-graphite-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-graphite-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-graphite-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-graphite-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-graphite-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-graphite

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