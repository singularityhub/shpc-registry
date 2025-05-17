---
layout: container
name:  "quay.io/biocontainers/bioconductor-consensus"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-consensus/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-consensus/container.yaml"
updated_at: "2025-05-17 03:34:51.032406"
latest: "1.24.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-consensus"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_1"
 - "1.24.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-consensus"
config: {"url": "https://biocontainers.pro/tools/bioconductor-consensus", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-consensus", "latest": {"1.24.0--r44hdfd78af_0": "sha256:1147c9cabc0f6519b0d11676a5906d9098b9587df3b7c8ef25cc3e98118dd8fb"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:cf7a2d20740da9fda17c945dc8bbf2cd305f1f208da68c3ef6bbc5333790ab4d", "1.16.0--r42hdfd78af_0": "sha256:c451fd4135fe9977e31eff4698f2b21cbbb6faa03dd4d943e0e9c0e1bfa9254f", "1.12.0--r41hdfd78af_0": "sha256:1b6eb65276b6a2cb564c7c87eceec672a7423a38ba40ab42942b2476c272da0f", "1.10.0--r41hdfd78af_0": "sha256:86066264379cd9ff827680bdaef15b028a6f47d6470d1b1f46c2892f8ca10861", "1.18.0--r43hdfd78af_0": "sha256:f652977c3560c3679abfb6c27c33041d76d361f385f419c8d0c11dcf814b5790", "1.20.0--r43hdfd78af_1": "sha256:6f31631dd653854b18c65069d4070a8d4b1ca9dd15d097577052c0edd22ffef4", "1.24.0--r44hdfd78af_0": "sha256:1147c9cabc0f6519b0d11676a5906d9098b9587df3b7c8ef25cc3e98118dd8fb"}, "docker": "quay.io/biocontainers/bioconductor-consensus", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-consensus.
shpc-registry automated BioContainers addition for bioconductor-consensus
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-consensus
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-consensus:1.24.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-consensus/1.24.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-consensus/1.24.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-consensus-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-consensus-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-consensus-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-consensus-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-consensus-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-consensus-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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