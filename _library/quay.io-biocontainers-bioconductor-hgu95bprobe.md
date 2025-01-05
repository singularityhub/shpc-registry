---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgu95bprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgu95bprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgu95bprobe/container.yaml"
updated_at: "2025-01-05 03:28:13.502797"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-hgu95bprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-hgu95bprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgu95bprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgu95bprobe", "latest": {"2.18.0--r44hdfd78af_13": "sha256:0b20bb5d91a843b5a015e3d24a9e48f46ef77b5936a53df7422f9df4059801e8"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:f20db16efdd57116b14abd72701e3ac1d35a411a795e35c9b9c3117cb7f1e410", "2.18.0--r42hdfd78af_10": "sha256:7f108043047b10bdad6817ab420da2726822f1435c54e6a74fd2ee5556364212", "2.18.0--r43hdfd78af_11": "sha256:a14b9f60a6f744cd0e33187ff61f750d4c6bfd15485c1a267d6b794a950a028c", "2.18.0--r43hdfd78af_12": "sha256:6bf956a3f9c1b6c787c56dbfdb63f0861969b3dc963edadb0525c55cff3c333f", "2.18.0--r44hdfd78af_13": "sha256:0b20bb5d91a843b5a015e3d24a9e48f46ef77b5936a53df7422f9df4059801e8"}, "docker": "quay.io/biocontainers/bioconductor-hgu95bprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgu95bprobe.
shpc-registry automated BioContainers addition for bioconductor-hgu95bprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu95bprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu95bprobe:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgu95bprobe/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-hgu95bprobe/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgu95bprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu95bprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu95bprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgu95bprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgu95bprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgu95bprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hgu95bprobe

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