---
layout: container
name:  "quay.io/biocontainers/r-deseqanalysis"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-deseqanalysis/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-deseqanalysis/container.yaml"
updated_at: "2025-03-02 03:01:04.368040"
latest: "0.7.1--r44hdfd78af_1"
container_url: "https://biocontainers.pro/tools/r-deseqanalysis"

versions:
 - "0.5.0--r41hdfd78af_0"
 - "0.6.6--r42hdfd78af_1"
 - "0.5.0--r41hdfd78af_1"
 - "0.6.7--r42hdfd78af_0"
 - "0.6.7--r42hdfd78af_1"
 - "0.6.8--r42hdfd78af_1"
 - "0.6.8--r43hdfd78af_2"
 - "0.6.12--r43hdfd78af_0"
 - "0.7.0--r43hdfd78af_0"
 - "0.7.1--r43hdfd78af_0"
 - "0.7.1--r44hdfd78af_1"
description: "shpc-registry automated BioContainers addition for r-deseqanalysis"
config: {"url": "https://biocontainers.pro/tools/r-deseqanalysis", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-deseqanalysis", "latest": {"0.7.1--r44hdfd78af_1": "sha256:6d03af857d4bc27e2382ea16c9a37442af5a30eb6da0e61e8e5f4d7631df6ecb"}, "tags": {"0.5.0--r41hdfd78af_0": "sha256:5d4a998f8c2cdcc71d51436356f20e386df2b4f87c60f29e266a0725cd07519e", "0.6.6--r42hdfd78af_1": "sha256:e31d7686bc8e0a038101f0ba1e9a98eeb7f6d9cc2249f569f90fd6753c8945a5", "0.5.0--r41hdfd78af_1": "sha256:53be90e5cd4502199d649e8488dc743f7cb739307873edf86d1bd5e6f54683d3", "0.6.7--r42hdfd78af_0": "sha256:c32b1cdfb87a23488db9132a121d13bef1aa47cbcfea8b82e8c7e8813335f136", "0.6.7--r42hdfd78af_1": "sha256:be3af40c79026058518b751e471a3ac474eefa68cd488d1924b1e16d1c75f7f2", "0.6.8--r42hdfd78af_1": "sha256:572507c7c110f01065f9ff8e9e3a560ac16c2a5120f4cac1b0954e3cc1bb27f0", "0.6.8--r43hdfd78af_2": "sha256:50dc9c2c1cd8f8ca2edf0e9c65c10fb0d6dcb7d183d0b0b142ced4f4a5617a49", "0.6.12--r43hdfd78af_0": "sha256:eaa02a66a1ef6cd81424ca42bf60ae3f7fac0196e7138aa0ab559a61b96e7e0b", "0.7.0--r43hdfd78af_0": "sha256:2f97992897a9a331f45851643275d5ecadff5caba4c7a34d1aa2227c9c989aa1", "0.7.1--r43hdfd78af_0": "sha256:d8cb350b2b9d0e675e6c303b0dce8039762dbc2d09306b23e93bc4ccc6f5ba4f", "0.7.1--r44hdfd78af_1": "sha256:6d03af857d4bc27e2382ea16c9a37442af5a30eb6da0e61e8e5f4d7631df6ecb"}, "docker": "quay.io/biocontainers/r-deseqanalysis"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-deseqanalysis.
shpc-registry automated BioContainers addition for r-deseqanalysis
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-deseqanalysis
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-deseqanalysis:0.7.1--r44hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-deseqanalysis/0.7.1--r44hdfd78af_1
$ module help quay.io/biocontainers/r-deseqanalysis/0.7.1--r44hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-deseqanalysis-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-deseqanalysis-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-deseqanalysis-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-deseqanalysis-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-deseqanalysis-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-deseqanalysis-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-deseqanalysis

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