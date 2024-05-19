---
layout: container
name:  "quay.io/biocontainers/bioconductor-scpdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scpdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scpdata/container.yaml"
updated_at: "2024-05-19 02:46:39.704167"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scpdata"
aliases:
 - "glpsol"
versions:
 - "1.2.0--r41hdfd78af_1"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scpdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scpdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scpdata", "latest": {"1.10.0--r43hdfd78af_0": "sha256:0e27aa2ef90bde5749658f1f8496f59fb56a97da7d7cbf7233bb1d8adad21926"}, "tags": {"1.2.0--r41hdfd78af_1": "sha256:97c24d199ce9fbe9602b03ad0d658c9b98382377b01eadae5822aeaa476d6ccc", "1.6.0--r42hdfd78af_0": "sha256:0db19fb3bc401c252e1e5d9bbcfebead0f4239aa10d7673609f278edfb384afb", "1.8.0--r43hdfd78af_0": "sha256:9110e3c332539edfa67405da202e420b2ff7fb3faba5a9cf59c0f64d7632e934", "1.10.0--r43hdfd78af_0": "sha256:0e27aa2ef90bde5749658f1f8496f59fb56a97da7d7cbf7233bb1d8adad21926"}, "docker": "quay.io/biocontainers/bioconductor-scpdata", "aliases": {"glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scpdata.
shpc-registry automated BioContainers addition for bioconductor-scpdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scpdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scpdata:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scpdata/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-scpdata/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scpdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scpdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scpdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scpdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scpdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scpdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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