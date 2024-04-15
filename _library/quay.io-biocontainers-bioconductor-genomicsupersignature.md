---
layout: container
name:  "quay.io/biocontainers/bioconductor-genomicsupersignature"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-genomicsupersignature/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-genomicsupersignature/container.yaml"
updated_at: "2024-04-15 06:34:51.641531"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-genomicsupersignature"
aliases:
 - "pandoc"
versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-genomicsupersignature"
config: {"url": "https://biocontainers.pro/tools/bioconductor-genomicsupersignature", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-genomicsupersignature", "latest": {"1.10.0--r43hdfd78af_0": "sha256:b4fb4f3635f54bdd46fd93ac97ccb3ee41542db7bade68dd20656470b95d5fbe"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:96a5cd7a3ba792eca18635401fe51f454376752408fea6b329c0890813860a49", "1.6.0--r42hdfd78af_0": "sha256:a9e356680040702a658e15623a4456070c2d07b23d24a1c60eaf06466093cd0c", "1.8.0--r43hdfd78af_0": "sha256:c4672884b27b7c3e3df3e4ac033b338c7fd269392143db9fe621d4591d9b7ab1", "1.10.0--r43hdfd78af_0": "sha256:b4fb4f3635f54bdd46fd93ac97ccb3ee41542db7bade68dd20656470b95d5fbe"}, "docker": "quay.io/biocontainers/bioconductor-genomicsupersignature", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-genomicsupersignature.
shpc-registry automated BioContainers addition for bioconductor-genomicsupersignature
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-genomicsupersignature
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-genomicsupersignature:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-genomicsupersignature/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-genomicsupersignature/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-genomicsupersignature-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genomicsupersignature-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-genomicsupersignature-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-genomicsupersignature-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-genomicsupersignature-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-genomicsupersignature-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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