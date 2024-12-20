---
layout: container
name:  "quay.io/biocontainers/bioconductor-ragene11stprobeset.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ragene11stprobeset.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ragene11stprobeset.db/container.yaml"
updated_at: "2024-12-20 03:30:57.405941"
latest: "8.8.0--r43hdfd78af_4"
container_url: "https://biocontainers.pro/tools/bioconductor-ragene11stprobeset.db"

versions:
 - "8.8.0--r41hdfd78af_1"
 - "8.8.0--r42hdfd78af_2"
 - "8.8.0--r43hdfd78af_3"
 - "8.8.0--r43hdfd78af_4"
description: "shpc-registry automated BioContainers addition for bioconductor-ragene11stprobeset.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ragene11stprobeset.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ragene11stprobeset.db", "latest": {"8.8.0--r43hdfd78af_4": "sha256:0bd136f4c23fa28ae0f1e6ed095b1191bcd7eae0a463bd40b2ccb924375636f4"}, "tags": {"8.8.0--r41hdfd78af_1": "sha256:faadddb19dfe396e53ca089a08cec8158e6a2b3a8c7885279f120e813fc61776", "8.8.0--r42hdfd78af_2": "sha256:e20bb988edb8d6fea1325c382a24d9928315b0ff48d4f854a00da556fa0186d7", "8.8.0--r43hdfd78af_3": "sha256:dc39710edf95b96d1d2e7fe2039003081ec15926ee3549723ff116fa92b1b5e8", "8.8.0--r43hdfd78af_4": "sha256:0bd136f4c23fa28ae0f1e6ed095b1191bcd7eae0a463bd40b2ccb924375636f4"}, "docker": "quay.io/biocontainers/bioconductor-ragene11stprobeset.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ragene11stprobeset.db.
shpc-registry automated BioContainers addition for bioconductor-ragene11stprobeset.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ragene11stprobeset.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ragene11stprobeset.db:8.8.0--r43hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ragene11stprobeset.db/8.8.0--r43hdfd78af_4
$ module help quay.io/biocontainers/bioconductor-ragene11stprobeset.db/8.8.0--r43hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ragene11stprobeset.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ragene11stprobeset.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ragene11stprobeset.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ragene11stprobeset.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ragene11stprobeset.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ragene11stprobeset.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ragene11stprobeset.db

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