---
layout: container
name:  "quay.io/biocontainers/bioconductor-operonhumanv3.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-operonhumanv3.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-operonhumanv3.db/container.yaml"
updated_at: "2024-05-10 02:54:50.000302"
latest: "3.2.3--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-operonhumanv3.db"

versions:
 - "3.2.3--r41hdfd78af_9"
 - "3.2.3--r42hdfd78af_10"
 - "3.2.3--r43hdfd78af_11"
 - "3.2.3--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-operonhumanv3.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-operonhumanv3.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-operonhumanv3.db", "latest": {"3.2.3--r43hdfd78af_12": "sha256:31ec9629089d93acfca08aa160a249615c28faec0faa4ab3d83aef1975c639bf"}, "tags": {"3.2.3--r41hdfd78af_9": "sha256:e986be3b5db610ea08be1d944f01ac793dd7120b1f6fbc03724f5a5b59820fdc", "3.2.3--r42hdfd78af_10": "sha256:1f2b1d73fd5c063d7976730fb83c7c35a4076d983e0cf13e384502d0638b297a", "3.2.3--r43hdfd78af_11": "sha256:c683d70dc1abcf278d35114cd78c2c71def77f5cab0061705574224550656967", "3.2.3--r43hdfd78af_12": "sha256:31ec9629089d93acfca08aa160a249615c28faec0faa4ab3d83aef1975c639bf"}, "docker": "quay.io/biocontainers/bioconductor-operonhumanv3.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-operonhumanv3.db.
shpc-registry automated BioContainers addition for bioconductor-operonhumanv3.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-operonhumanv3.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-operonhumanv3.db:3.2.3--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-operonhumanv3.db/3.2.3--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-operonhumanv3.db/3.2.3--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-operonhumanv3.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-operonhumanv3.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-operonhumanv3.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-operonhumanv3.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-operonhumanv3.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-operonhumanv3.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-operonhumanv3.db

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