---
layout: container
name:  "quay.io/biocontainers/multiqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/multiqc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/multiqc/container.yaml"
updated_at: "2025-05-27 12:03:51.745298"
latest: "1.29--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/multiqc"
aliases:
 - "multiqc"
versions:
 - "1.9--py_1"
 - "1.10.1--pyhdfd78af_1"
 - "1.11--pyhdfd78af_0"
 - "1.12--pyhdfd78af_0"
 - "1.21--pyhdfd78af_0"
 - "1.20--pyhdfd78af_2"
 - "1.19--pyhdfd78af_0"
 - "1.18--pyhdfd78af_0"
 - "1.17--pyhdfd78af_1"
 - "1.22.1--pyhdfd78af_0"
 - "1.22.3--pyhdfd78af_0"
 - "1.23--pyhdfd78af_0"
 - "1.24.1--pyhdfd78af_0"
 - "1.25--pyhdfd78af_0"
 - "1.25.1--pyhdfd78af_0"
 - "1.25.2--pyhdfd78af_0"
 - "1.26--pyhdfd78af_0"
 - "1.27--pyhdfd78af_0"
 - "1.27.1--pyhdfd78af_0"
 - "1.28--pyhdfd78af_0"
 - "1.29--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for multiqc"
config: {"url": "https://biocontainers.pro/tools/multiqc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for multiqc", "latest": {"1.29--pyhdfd78af_0": "sha256:f4ebfe78e45dd96f04a9c883e1882e77ac357988a10a7c980df6d500bfc46de6"}, "tags": {"1.9--py_1": "sha256:67cc651cb350b1ee2fc0929bd6bcd5189ec8c17f09566a3cd54cde7479e48a09", "1.10.1--pyhdfd78af_1": "sha256:c64ea8fcaf49dfc4b0594bc7349e6d1a662eb4484f5aac3252f4eea86cad164c", "1.11--pyhdfd78af_0": "sha256:88df23fac5b9eecda9943d922f81b68e30188eb4dd7cbfe9554e952ff5a3b0ee", "1.12--pyhdfd78af_0": "sha256:82dae6463e1b19fafb6022401186300b66decf5ce319a725271700fe4e32e12a", "1.21--pyhdfd78af_0": "sha256:ecafca93ba3346775b773bbfd6ff920ecfc259f554777576c15d3139c678311b", "1.20--pyhdfd78af_2": "sha256:e32ae95da678783635b36be6f0a93c1e45b6af8b6b650019a930b87733d87bdb", "1.19--pyhdfd78af_0": "sha256:6487aad25c1d232abb98e7b23236606205ce39882a3de22b20e6d12b3d3e69af", "1.18--pyhdfd78af_0": "sha256:91e7d3e4673d8c617ce3c41123949daf63f84e84d48aed22157abd1be0f2e925", "1.17--pyhdfd78af_1": "sha256:fb7d6625fb5adaed43ced8bd051a875038714180bcfcd7c8e467204f72882de9", "1.22.1--pyhdfd78af_0": "sha256:0d41f422dfdd35636c02b8efb4162cb44a9652a6dbdd65f81219b88386b31c93", "1.22.3--pyhdfd78af_0": "sha256:691899b5899eb7777b5e689029c8f9fc3a2838378cbda01fe41ff0198af0cc7d", "1.23--pyhdfd78af_0": "sha256:3c4f30008244f191ed5268703ad5318a2e6aa697e3e8480fe98492da40a50340", "1.24.1--pyhdfd78af_0": "sha256:0e80f2cbbfece8a52c7ad645a751b1d34465a4053904c5130b3a7a81ac5e02f6", "1.25--pyhdfd78af_0": "sha256:2c529689826c39931deea64d3a810fccacd7814e196c2867800d767423abdf77", "1.25.1--pyhdfd78af_0": "sha256:64fa8caa046020780a7df765cdd27b459f20665578e6f1f240a12d415527adaa", "1.25.2--pyhdfd78af_0": "sha256:d939a5fc6c5b505f7bb148ce3527fb9850c6e8f3f4eab7cc5a4be180f0533f46", "1.26--pyhdfd78af_0": "sha256:a05cc0922e1d620f428954a12a659dc9dcb57528a4f1c71811ae1f8b8d3ed9ce", "1.27--pyhdfd78af_0": "sha256:a024b23be16fa3f3919ef018741478a7a3bfaaed0222369dff59abaf28316149", "1.27.1--pyhdfd78af_0": "sha256:e8821df086710ff4fe535814e70eb6390d4685dd6e962fc743bff58b35b0e603", "1.28--pyhdfd78af_0": "sha256:9cf4fcfb2df9c4ebc017983c6c6918ff7c9258553076b0aa7a23a626e48dd201", "1.29--pyhdfd78af_0": "sha256:f4ebfe78e45dd96f04a9c883e1882e77ac357988a10a7c980df6d500bfc46de6"}, "docker": "quay.io/biocontainers/multiqc", "aliases": {"multiqc": "/usr/local/bin/multiqc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/multiqc.
shpc-registry automated BioContainers addition for multiqc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/multiqc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/multiqc:1.29--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/multiqc/1.29--pyhdfd78af_0
$ module help quay.io/biocontainers/multiqc/1.29--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### multiqc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### multiqc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### multiqc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### multiqc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### multiqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### multiqc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### multiqc

```bash
$ singularity exec <container> /usr/local/bin/multiqc
$ podman run --it --rm --entrypoint /usr/local/bin/multiqc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/multiqc   -v ${PWD} -w ${PWD} <container> -c " $@"
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