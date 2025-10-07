---
layout: container
name:  "quay.io/biocontainers/bioconductor-ideoviz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ideoviz/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ideoviz/container.yaml"
updated_at: "2025-10-07 03:49:59.759716"
latest: "1.42.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ideoviz"

versions:
 - "1.30.0--r41hdfd78af_0"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.37.0--r43hdfd78af_0"
 - "1.42.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ideoviz"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ideoviz", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ideoviz", "latest": {"1.42.0--r44hdfd78af_0": "sha256:2459756c5548b377cd9b52ac056af0a2172004e66d04ea3fea4d4a6ef1f217e6"}, "tags": {"1.30.0--r41hdfd78af_0": "sha256:8a4191e209e9599e085f7628e226eaa9f045fdf7b80ecb1882de5c23cf3dd77b", "1.34.0--r42hdfd78af_0": "sha256:1e55116f1adffc033c304bb209c3ae1f63b9492f1eaf102562adfdf6ceb62c9a", "1.36.0--r43hdfd78af_0": "sha256:5de7deca6ed256ea32bf433449628c4db1f4e3f4458b28f5ef23252507ae9849", "1.37.0--r43hdfd78af_0": "sha256:16b5f776ed72fe4193e1e495c7a1669b48753fc1d1e2dc83d65b96f03472dc55", "1.42.0--r44hdfd78af_0": "sha256:2459756c5548b377cd9b52ac056af0a2172004e66d04ea3fea4d4a6ef1f217e6"}, "docker": "quay.io/biocontainers/bioconductor-ideoviz"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ideoviz.
shpc-registry automated BioContainers addition for bioconductor-ideoviz
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ideoviz
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ideoviz:1.42.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ideoviz/1.42.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ideoviz/1.42.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ideoviz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ideoviz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ideoviz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ideoviz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ideoviz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ideoviz-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ideoviz

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