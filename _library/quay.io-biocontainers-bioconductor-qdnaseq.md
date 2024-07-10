---
layout: container
name:  "quay.io/biocontainers/bioconductor-qdnaseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-qdnaseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-qdnaseq/container.yaml"
updated_at: "2024-07-10 03:05:21.432539"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-qdnaseq"

versions:
 - "1.8.0--0"
 - "1.34.0--r42hdfd78af_0"
 - "1.30.0--r41hdfd78af_0"
 - "1.28.0--r41hdfd78af_0"
 - "1.26.0--r40hdfd78af_1"
 - "1.24.0--r40_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-qdnaseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-qdnaseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-qdnaseq", "latest": {"1.38.0--r43hdfd78af_0": "sha256:750f3c24c364f57f3bbf3ceca5ba850fb40d710ab0b09a87bccb7e0708c5b72f"}, "tags": {"1.8.0--0": "sha256:8926eae5e345b21ffe765bc5fed8e544af3a7eff99482a0803175129b62dc851", "1.34.0--r42hdfd78af_0": "sha256:68c42f27d6bc6d588b33dc1390ac457aec436ce05ba693cfcb502083e334fa8f", "1.30.0--r41hdfd78af_0": "sha256:0fbc4f62bd0b4a7cfb749baf536880560571074177e604b587f7918436977f92", "1.28.0--r41hdfd78af_0": "sha256:8ab6a456d9ae28305e7d5ffc6d5a27d038d527dcd3e1f62fbe03dc56ee1fbe49", "1.26.0--r40hdfd78af_1": "sha256:7fa8bcbe9270beca7ea11612dd911e4784296fb33cb702cda88abf5993bbe8b6", "1.24.0--r40_0": "sha256:5ef1b66ccbcdad2650935147f642020563f1f19c4a7666e26ff14d701cc21213", "1.36.0--r43hdfd78af_0": "sha256:630ccb8847d74e94e24e9e73b335dd1e713ad0584c9967f6c245bfd04d589585", "1.38.0--r43hdfd78af_0": "sha256:750f3c24c364f57f3bbf3ceca5ba850fb40d710ab0b09a87bccb7e0708c5b72f"}, "docker": "quay.io/biocontainers/bioconductor-qdnaseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-qdnaseq.
shpc-registry automated BioContainers addition for bioconductor-qdnaseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-qdnaseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-qdnaseq:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-qdnaseq/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-qdnaseq/1.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-qdnaseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-qdnaseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-qdnaseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-qdnaseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-qdnaseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-qdnaseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-qdnaseq

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