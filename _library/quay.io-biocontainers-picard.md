---
layout: container
name:  "quay.io/biocontainers/picard"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/picard/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/picard/container.yaml"
updated_at: "2024-12-07 01:35:11.432984"
latest: "3.3.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/picard"
aliases:
 - "picard"
versions:
 - "2.9.2--py36_1"
 - "2.18.23--0"
 - "2.17.11--py36_0"
 - "2.16.0--py36_0"
 - "2.15.0--py35_0"
 - "2.14.1--py35_0"
 - "3.1.1--hdfd78af_0"
 - "3.0.0--hdfd78af_1"
 - "2.27.5--hdfd78af_0"
 - "2.26.11--hdfd78af_0"
 - "2.25.7--hdfd78af_0"
 - "3.2.0--hdfd78af_0"
 - "3.3.0--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for picard"
config: {"url": "https://biocontainers.pro/tools/picard", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for picard", "latest": {"3.3.0--hdfd78af_0": "sha256:8b95c2742d74ccc04ce56af3ca051b9a418a246be48c9af5239f0274409e495d"}, "tags": {"2.9.2--py36_1": "sha256:2aeca0a7a8985abd6e45e97db6f9cc84f1c3b3439573dc484fa7f86e9e443be5", "2.18.23--0": "sha256:ae8e2821c8687a78606f17fafb417eea0de1ac75142ef94d428897f5d6b90876", "2.17.11--py36_0": "sha256:d1ae699f57390dbf2b28dc0a6eacf8d1ec4c962990fd0c703695ad7b934e82f0", "2.16.0--py36_0": "sha256:44ebf986e50ee71196f26eb022adbb260df067d53718d9857aeea2e6731cdbc7", "2.15.0--py35_0": "sha256:51858bc89b7ef0b3a9c6e15f2000c1c6052ec697aaa4d38dc16e4d2ee654142e", "2.14.1--py35_0": "sha256:b77b00ab69f55a842b67b9380881305130229ceb2daeeece710b3013dfa62b6c", "3.1.1--hdfd78af_0": "sha256:6ed9979090434fd3ee3f197c990f04e64279fdb0ca9d9897ed88450da8fe2658", "3.0.0--hdfd78af_1": "sha256:1807618ee8ac1af18a2a4656dd8b4d4a0a6f679b6a1e554a6603ac7a6d732d95", "2.27.5--hdfd78af_0": "sha256:573ec3f38ab84c12a619eb31cf15cc1e5d709e50c083486cce04faf14ede91d4", "2.26.11--hdfd78af_0": "sha256:229d61d04965e797b9f77dbb56d46a14646abb52c7bcdf0c9586c8382f06f851", "2.25.7--hdfd78af_0": "sha256:cdd60185fdc3a479ed6cc918e739fefcf28f3f6853c8ec3f0f5cfce09f8258c9", "3.2.0--hdfd78af_0": "sha256:0ba3a90a242cfa06362da145df868e92401c1cc8cd85cc08e85c4a5c9e55ed23", "3.3.0--hdfd78af_0": "sha256:8b95c2742d74ccc04ce56af3ca051b9a418a246be48c9af5239f0274409e495d"}, "docker": "quay.io/biocontainers/picard", "aliases": {"picard": "/usr/local/bin/picard"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/picard.
shpc-registry automated BioContainers addition for picard
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/picard
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/picard:3.3.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/picard/3.3.0--hdfd78af_0
$ module help quay.io/biocontainers/picard/3.3.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### picard-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### picard-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### picard-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### picard-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### picard-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### picard-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### picard

```bash
$ singularity exec <container> /usr/local/bin/picard
$ podman run --it --rm --entrypoint /usr/local/bin/picard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/picard   -v ${PWD} -w ${PWD} <container> -c " $@"
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