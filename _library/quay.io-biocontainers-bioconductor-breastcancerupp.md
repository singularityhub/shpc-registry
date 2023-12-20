---
layout: container
name:  "quay.io/biocontainers/bioconductor-breastcancerupp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-breastcancerupp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-breastcancerupp/container.yaml"
updated_at: "2023-12-20 02:30:32.076722"
latest: "1.40.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-breastcancerupp"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.35.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-breastcancerupp"
config: {"url": "https://biocontainers.pro/tools/bioconductor-breastcancerupp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-breastcancerupp", "latest": {"1.40.0--r43hdfd78af_0": "sha256:143861953e50e3f648a761912824168d3fb396edf2760a70df5fc19960e895b0"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:444b5a400fbc2a2ebf9ba42ea9c82caae95b12a532c49d7462e4f825c41e9ab8", "1.35.0--r42hdfd78af_0": "sha256:0d303e5e666120a97598e027a7b50f976ca32325d7349fa4ed1b463dba52929a", "1.38.0--r43hdfd78af_0": "sha256:b2d53ff5f06ace91dae30bfe9e101297821d9852417ed34984fde37f06b863da", "1.40.0--r43hdfd78af_0": "sha256:143861953e50e3f648a761912824168d3fb396edf2760a70df5fc19960e895b0"}, "docker": "quay.io/biocontainers/bioconductor-breastcancerupp"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-breastcancerupp.
shpc-registry automated BioContainers addition for bioconductor-breastcancerupp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-breastcancerupp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-breastcancerupp:1.40.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-breastcancerupp/1.40.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-breastcancerupp/1.40.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-breastcancerupp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-breastcancerupp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-breastcancerupp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-breastcancerupp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-breastcancerupp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-breastcancerupp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-breastcancerupp

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