---
layout: container
name:  "quay.io/biocontainers/bioconductor-mirlab"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mirlab/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mirlab/container.yaml"
updated_at: "2024-12-30 03:29:32.588785"
latest: "1.32.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mirlab"

versions:
 - "1.24.0--r41hdfd78af_0"
 - "1.28.0--r42hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mirlab"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mirlab", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mirlab", "latest": {"1.32.0--r43hdfd78af_0": "sha256:bbbd368d0a3a9f0e645ddb719e135375b816ebc536970056bf52c92b7e28eb97"}, "tags": {"1.24.0--r41hdfd78af_0": "sha256:75de825544468d8930ecef5cf10d8eede54f4c4fd8cd59c1218329675b152aae", "1.28.0--r42hdfd78af_0": "sha256:88064235d65d78c2035493e2f8c3e08242bb37af660a8ef437ddd70b1ee57e50", "1.30.0--r43hdfd78af_0": "sha256:0ff7f513cf8f790ff00ceb4e2e8188752f7faf7c21b33757f02967427852668f", "1.32.0--r43hdfd78af_0": "sha256:bbbd368d0a3a9f0e645ddb719e135375b816ebc536970056bf52c92b7e28eb97"}, "docker": "quay.io/biocontainers/bioconductor-mirlab"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mirlab.
shpc-registry automated BioContainers addition for bioconductor-mirlab
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mirlab
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mirlab:1.32.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mirlab/1.32.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mirlab/1.32.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mirlab-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mirlab-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mirlab-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mirlab-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mirlab-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mirlab-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mirlab

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