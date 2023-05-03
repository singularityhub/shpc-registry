---
layout: container
name:  "quay.io/biocontainers/bioconductor-hsagilentdesign026652.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hsagilentdesign026652.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hsagilentdesign026652.db/container.yaml"
updated_at: "2023-05-03 03:00:13.564207"
latest: "3.2.3--r42hdfd78af_10"
container_url: "https://biocontainers.pro/tools/bioconductor-hsagilentdesign026652.db"

versions:
 - "3.2.3--r41hdfd78af_9"
 - "3.2.3--r42hdfd78af_10"
description: "shpc-registry automated BioContainers addition for bioconductor-hsagilentdesign026652.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hsagilentdesign026652.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hsagilentdesign026652.db", "latest": {"3.2.3--r42hdfd78af_10": "sha256:4dc1b69fd9a19c4bdd56f508fe61ea1abf04c9c67ea13d7ab601005238ed9045"}, "tags": {"3.2.3--r41hdfd78af_9": "sha256:fb9f7d352404ca27d3cba76f2ccb535d135adf4d200690efe4ca4108b39391a0", "3.2.3--r42hdfd78af_10": "sha256:4dc1b69fd9a19c4bdd56f508fe61ea1abf04c9c67ea13d7ab601005238ed9045"}, "docker": "quay.io/biocontainers/bioconductor-hsagilentdesign026652.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hsagilentdesign026652.db.
shpc-registry automated BioContainers addition for bioconductor-hsagilentdesign026652.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hsagilentdesign026652.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hsagilentdesign026652.db:3.2.3--r42hdfd78af_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hsagilentdesign026652.db/3.2.3--r42hdfd78af_10
$ module help quay.io/biocontainers/bioconductor-hsagilentdesign026652.db/3.2.3--r42hdfd78af_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hsagilentdesign026652.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hsagilentdesign026652.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hsagilentdesign026652.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hsagilentdesign026652.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hsagilentdesign026652.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hsagilentdesign026652.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hsagilentdesign026652.db

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