---
layout: container
name:  "quay.io/biocontainers/bioconductor-moex10stprobeset.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-moex10stprobeset.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-moex10stprobeset.db/container.yaml"
updated_at: "2025-03-06 03:29:12.109888"
latest: "8.8.0--r44hdfd78af_5"
container_url: "https://biocontainers.pro/tools/bioconductor-moex10stprobeset.db"

versions:
 - "8.8.0--r41hdfd78af_1"
 - "8.8.0--r42hdfd78af_2"
 - "8.8.0--r43hdfd78af_3"
 - "8.8.0--r43hdfd78af_4"
 - "8.8.0--r44hdfd78af_5"
description: "shpc-registry automated BioContainers addition for bioconductor-moex10stprobeset.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-moex10stprobeset.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-moex10stprobeset.db", "latest": {"8.8.0--r44hdfd78af_5": "sha256:8f858cd32d0d472671123aaa3de61ff13cda1a78a4235f810220d817ec227407"}, "tags": {"8.8.0--r41hdfd78af_1": "sha256:3037451726ea8ed7ead3c3726a1fb6937b8fb420bce5b19b5e8309b195f28542", "8.8.0--r42hdfd78af_2": "sha256:1f965abb6c323bd053731c8596c22dab8b663114849b864d95b96f9b7500d174", "8.8.0--r43hdfd78af_3": "sha256:9f64094ea3aa5cbe7478a44c2b2f4da8bea66f1bf51bef29bf2d5e3902dcbf66", "8.8.0--r43hdfd78af_4": "sha256:a2e672a38a183660d2f72232c16ec88e869284355c3f0c87a949a06f1240d98f", "8.8.0--r44hdfd78af_5": "sha256:8f858cd32d0d472671123aaa3de61ff13cda1a78a4235f810220d817ec227407"}, "docker": "quay.io/biocontainers/bioconductor-moex10stprobeset.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-moex10stprobeset.db.
shpc-registry automated BioContainers addition for bioconductor-moex10stprobeset.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-moex10stprobeset.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-moex10stprobeset.db:8.8.0--r44hdfd78af_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-moex10stprobeset.db/8.8.0--r44hdfd78af_5
$ module help quay.io/biocontainers/bioconductor-moex10stprobeset.db/8.8.0--r44hdfd78af_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-moex10stprobeset.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-moex10stprobeset.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-moex10stprobeset.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-moex10stprobeset.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-moex10stprobeset.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-moex10stprobeset.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-moex10stprobeset.db

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