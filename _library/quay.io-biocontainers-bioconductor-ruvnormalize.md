---
layout: container
name:  "quay.io/biocontainers/bioconductor-ruvnormalize"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ruvnormalize/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ruvnormalize/container.yaml"
updated_at: "2025-03-16 03:27:52.040266"
latest: "1.40.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ruvnormalize"

versions:
 - "1.28.0--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.40.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ruvnormalize"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ruvnormalize", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ruvnormalize", "latest": {"1.40.0--r44hdfd78af_0": "sha256:102cce2adad89f87980ee275f59ff09c1a9302591810b7df89cd804d739b2c50"}, "tags": {"1.28.0--r41hdfd78af_0": "sha256:46e3c4291a2ce7c0736c24daf4273bc24dacf3fea335a91fc6ffa28eb1b85246", "1.32.0--r42hdfd78af_0": "sha256:c8bd6eae93938d29cf7fda479b827e7e05705433b3c843deb8dd2ab13806f3f6", "1.34.0--r43hdfd78af_0": "sha256:121724b8b70219a7a7638031d87f134e9a7441cae5ea398e5e28d049e64931c4", "1.36.0--r43hdfd78af_0": "sha256:9e487269d14a9d45178c6c565ef16468a2af6aadffaaa2a2fcdc33c136658abd", "1.40.0--r44hdfd78af_0": "sha256:102cce2adad89f87980ee275f59ff09c1a9302591810b7df89cd804d739b2c50"}, "docker": "quay.io/biocontainers/bioconductor-ruvnormalize"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ruvnormalize.
shpc-registry automated BioContainers addition for bioconductor-ruvnormalize
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ruvnormalize
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ruvnormalize:1.40.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ruvnormalize/1.40.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ruvnormalize/1.40.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ruvnormalize-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ruvnormalize-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ruvnormalize-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ruvnormalize-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ruvnormalize-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ruvnormalize-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ruvnormalize

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