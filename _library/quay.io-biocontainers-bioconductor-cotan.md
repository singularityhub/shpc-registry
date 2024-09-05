---
layout: container
name:  "quay.io/biocontainers/bioconductor-cotan"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cotan/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cotan/container.yaml"
updated_at: "2024-09-05 04:55:11.301051"
latest: "2.2.1--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cotan"

versions:
 - "1.2.0--r42hdfd78af_0"
 - "2.0.4--r43hdfd78af_0"
 - "2.2.1--r43hdfd78af_0"
description: "singularity registry hpc automated addition for bioconductor-cotan"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cotan", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-cotan", "latest": {"2.2.1--r43hdfd78af_0": "sha256:2b9909c13346db71326392827ff3e6fb795a2b22e5d56bb2621c011ac45e85ff"}, "tags": {"1.2.0--r42hdfd78af_0": "sha256:026c04608cc5d435ed3e53e8caac9e4d1ab838bb8f933fce7eed290d93e7e843", "2.0.4--r43hdfd78af_0": "sha256:f0aaad331665ee568d598f154cd326b88cd5fd77cb2ad48531ac82058011636f", "2.2.1--r43hdfd78af_0": "sha256:2b9909c13346db71326392827ff3e6fb795a2b22e5d56bb2621c011ac45e85ff"}, "docker": "quay.io/biocontainers/bioconductor-cotan"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cotan.
singularity registry hpc automated addition for bioconductor-cotan
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cotan
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cotan:2.2.1--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cotan/2.2.1--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cotan/2.2.1--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cotan-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cotan-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cotan-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cotan-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cotan-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cotan-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cotan

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