---
layout: container
name:  "quay.io/biocontainers/bioconductor-genomewidesnp5crlmm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genomewidesnp5crlmm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genomewidesnp5crlmm/container.yaml"
updated_at: "2024-08-08 03:21:54.309617"
latest: "1.0.6--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-genomewidesnp5crlmm"

versions:
 - "1.0.6--r41hdfd78af_9"
 - "1.0.6--r42hdfd78af_10"
 - "1.0.6--r43hdfd78af_11"
 - "1.0.6--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-genomewidesnp5crlmm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genomewidesnp5crlmm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genomewidesnp5crlmm", "latest": {"1.0.6--r43hdfd78af_12": "sha256:418c1272085ac89342033938872d1d6d9d42234e72a265247d109a6b46528da7"}, "tags": {"1.0.6--r41hdfd78af_9": "sha256:64197ea76e2bdc3aa423156060bce48aab93bad6c04e839a48a00425db80a0e3", "1.0.6--r42hdfd78af_10": "sha256:6ed1a73155e4ef721b99483310540306f6fc71db3726e51792dc62096d59130a", "1.0.6--r43hdfd78af_11": "sha256:24f3363a1947c15ea75263a01c83eb642b722e1395740a741220f866e62df48b", "1.0.6--r43hdfd78af_12": "sha256:418c1272085ac89342033938872d1d6d9d42234e72a265247d109a6b46528da7"}, "docker": "quay.io/biocontainers/bioconductor-genomewidesnp5crlmm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genomewidesnp5crlmm.
shpc-registry automated BioContainers addition for bioconductor-genomewidesnp5crlmm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genomewidesnp5crlmm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genomewidesnp5crlmm:1.0.6--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genomewidesnp5crlmm/1.0.6--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-genomewidesnp5crlmm/1.0.6--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genomewidesnp5crlmm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genomewidesnp5crlmm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genomewidesnp5crlmm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genomewidesnp5crlmm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genomewidesnp5crlmm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genomewidesnp5crlmm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-genomewidesnp5crlmm

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