---
layout: container
name:  "quay.io/biocontainers/genomemanagement"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/genomemanagement/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/genomemanagement/container.yaml"
updated_at: "2026-03-15 04:52:06.988839"
latest: "2.0.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/genomemanagement"
aliases:
 - "get-genome-statistic"
 - "meme-xml2bed"
 - "plantpan2"
 - "plantpan3"
 - "promoter-retrieve"
 - "proteins-retrieve"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
versions:
 - "2.0.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for genomemanagement"
config: {"url": "https://biocontainers.pro/tools/genomemanagement", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for genomemanagement", "latest": {"2.0.0--pyhdfd78af_0": "sha256:ac8b7214722022d0c102ded6e7a224d855ea3b850f3c4ad414b0026f4e002a14"}, "tags": {"2.0.0--pyhdfd78af_0": "sha256:ac8b7214722022d0c102ded6e7a224d855ea3b850f3c4ad414b0026f4e002a14"}, "docker": "quay.io/biocontainers/genomemanagement", "aliases": {"get-genome-statistic": "/usr/local/bin/get-genome-statistic", "meme-xml2bed": "/usr/local/bin/meme-xml2bed", "plantpan2": "/usr/local/bin/plantpan2", "plantpan3": "/usr/local/bin/plantpan3", "promoter-retrieve": "/usr/local/bin/promoter-retrieve", "proteins-retrieve": "/usr/local/bin/proteins-retrieve", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/genomemanagement.
singularity registry hpc automated addition for genomemanagement
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/genomemanagement
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/genomemanagement:2.0.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/genomemanagement/2.0.0--pyhdfd78af_0
$ module help quay.io/biocontainers/genomemanagement/2.0.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### genomemanagement-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### genomemanagement-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### genomemanagement-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### genomemanagement-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### genomemanagement-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### genomemanagement-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### get-genome-statistic

```bash
$ singularity exec <container> /usr/local/bin/get-genome-statistic
$ podman run --it --rm --entrypoint /usr/local/bin/get-genome-statistic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/get-genome-statistic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### meme-xml2bed

```bash
$ singularity exec <container> /usr/local/bin/meme-xml2bed
$ podman run --it --rm --entrypoint /usr/local/bin/meme-xml2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/meme-xml2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plantpan2

```bash
$ singularity exec <container> /usr/local/bin/plantpan2
$ podman run --it --rm --entrypoint /usr/local/bin/plantpan2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plantpan2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plantpan3

```bash
$ singularity exec <container> /usr/local/bin/plantpan3
$ podman run --it --rm --entrypoint /usr/local/bin/plantpan3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plantpan3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### promoter-retrieve

```bash
$ singularity exec <container> /usr/local/bin/promoter-retrieve
$ podman run --it --rm --entrypoint /usr/local/bin/promoter-retrieve   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/promoter-retrieve   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proteins-retrieve

```bash
$ singularity exec <container> /usr/local/bin/proteins-retrieve
$ podman run --it --rm --entrypoint /usr/local/bin/proteins-retrieve   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proteins-retrieve   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.14

```bash
$ singularity exec <container> /usr/local/bin/idle3.14
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.14

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.14
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14

```bash
$ singularity exec <container> /usr/local/bin/python3.14
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14-config

```bash
$ singularity exec <container> /usr/local/bin/python3.14-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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