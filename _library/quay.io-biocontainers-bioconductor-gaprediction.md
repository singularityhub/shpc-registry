---
layout: container
name:  "quay.io/biocontainers/bioconductor-gaprediction"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gaprediction/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gaprediction/container.yaml"
updated_at: "2026-01-31 04:37:41.906371"
latest: "1.32.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gaprediction"
aliases:
 - "c89"
 - "c99"
versions:
 - "1.8.1--r351_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.12.0--r36_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.32.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gaprediction"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gaprediction", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gaprediction", "latest": {"1.32.0--r44hdfd78af_0": "sha256:33edbdfe63ae4e2af16c32451d8eec5ee3ccf88bf090e0cb679945fc7141cbfa"}, "tags": {"1.8.1--r351_0": "sha256:6f344251bf56a0d8373da1acccd33b0b946035dc0a32f1d54190f095ce4160d3", "1.20.0--r41hdfd78af_0": "sha256:dfa1834ae3f6d89bbd2b53035b793e9a36d81effdedf115dad448d17dbc73c7d", "1.18.0--r41hdfd78af_0": "sha256:d903582f03c7d607e2a2bc3a01b55499308ca2c80d57397afa2a333b8eb8d117", "1.16.0--r40hdfd78af_1": "sha256:106d5e28539f89b5614d6360c85d65f78b76d5d8b33685e700a45a76e6326200", "1.14.0--r40_0": "sha256:3bd97f8bbb653ce13049fe8ccf96e87037650c9d21aa1964943f4f5663056302", "1.12.0--r36_0": "sha256:86986d838bd780a273d2cb0b01810dd350f6cc565831e1821eda0bad58734572", "1.24.0--r42hdfd78af_0": "sha256:05bb05aaaf144608783c959e6f31ae6b939b17f4bfccd74b8055a00bd05cdd05", "1.26.0--r43hdfd78af_0": "sha256:3d769a428812bb1a148e99265ba46ba01d04c08a158e2cc3d1e1269044a1a806", "1.28.0--r43hdfd78af_0": "sha256:2145f1f16065c1342ba64c25e04ad4884b8890b3319a5bf2847c3a5b043a0143", "1.32.0--r44hdfd78af_0": "sha256:33edbdfe63ae4e2af16c32451d8eec5ee3ccf88bf090e0cb679945fc7141cbfa"}, "docker": "quay.io/biocontainers/bioconductor-gaprediction", "aliases": {"c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gaprediction.
shpc-registry automated BioContainers addition for bioconductor-gaprediction
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gaprediction
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gaprediction:1.32.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gaprediction/1.32.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gaprediction/1.32.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gaprediction-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gaprediction-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gaprediction-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gaprediction-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gaprediction-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gaprediction-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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